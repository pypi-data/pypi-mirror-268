# -*- coding: utf-8 -*-
import base64
import functools
import json  # noqa
import os
import re
import textwrap
import typing
from uuid import uuid4

import gluon.cache
import httpx
import tabulate
from pydal.objects import Row, Query

from edwh.core.backend.engine import (
    DuplicateSlugException,
    User,
    Visibility,
    new_password,
)
from edwh.core.tags import Tag
from edwh.core.backend.tasks import work_auto_tags_magic
from edwh.core.web2py_tools import HTMXAutocompleteWidget

if typing.TYPE_CHECKING:
    from gluon import (
        HTTP,
        URL,
        auth,
        cache,
        redirect,
        request,
        response,
        service,
        session,
    )
    from gluon.html import BUTTON, DIV, IMG, LI, PRE, SPAN, TABLE, TD, TR, XML, A, I
    from gluon.sqlhtml import SQLFORM, SQLTABLE
    from pydal import DAL, Field
    from pydal.validators import (
        IS_EMAIL,
        IS_EMPTY_OR,
        IS_IN_DB,
        IS_IN_SET,
        IS_LIST_OF,
        IS_NOT_EMPTY,
    )

    from ..models.db import (
        add_attachment_to_item,
        database,
        db,
        get_sticker_collections,
        hash_password,
        is_admin,
        last_opened_warning,
        may_remove_stickers,
    )
    from ..models.db_z_backend import backend
    from ..models.processes import restart_py4web
    from ..models.tags import bind_attachment_and_sticker, unbind_sticker

EDDIE_GID = "c8831058-34a3-42f1-ad83-eaf84aef2a30"

EW_PASSWORD_SALT = b"$2a$10$UFkhEG5ZjcRS57cXAmg9CO"


def index():
    if not auth.user:
        raise redirect("user/login?_next=/init/default/index")

    if auth.has_membership(role="education_warehouse"):
        redirect(URL(f="items"))
    elif auth.has_membership(role="minion"):
        response.headers["log"] = "minon redirect"
        redirect(URL(c="organisations", f="index"))
    elif auth.has_membership(role="ioldb"):
        response.headers["log"] = "ioldb redirect"
        redirect(URL(a="ioldb", f="index"))
    else:
        return "No roles defined for this user."


# for user in database(~database.user.password.like("$2a%")).select():
#     # user.update_record(password=bcrypt.hashpw(user.password, b'$2a$10$UFkhEG5ZjcRS57cXAmg9CO'))
#     pass
# # return database(database.user.email.startswith('faked') & database.user.platform.contains('debug')).#delete()
# database.commit()
# database.user.email.represent = lambda x: x
# return dict(
#     form=database(database.user.platform.contains("SvS")).select(
#         orderby=~database.user.id
#     )
# )
# # return dict(form=database(~database.user.password.like("$2a%")).select())


@auth.requires_membership("education_warehouse")
def email_footer():
    form = SQLFORM.factory(
        Field("fullname", default=f"{auth.user.first_name} {auth.user.last_name}"),
        Field("title"),
        Field("phone", default="+31(0)6-"),
        Field("extra", "list:string", default=[], requires=IS_LIST_OF()),
        Field("email_disclaimer", "boolean"),
    )

    if form.process().accepted:
        return dict(
            fullname=form.vars.fullname,
            title=form.vars.title,
            phone=form.vars.phone,
            extra_contact_lines=form.vars.extra,
            email_disclaimer=form.vars.email_disclaimer,
        )
    else:
        return response.render("default/email_footer_form.html", dict(form=form))


@cache(request.env.path_info, cache_model="ram", time_expire=3600)
def word_freq():  # NO_TEST_REDIRECT_ON
    "Handig voor automatisch en load testen. Levert een lijst van gebruikte woorden op uit onze database."
    from collections import Counter

    freqs = Counter()
    for row in database(database.item.author != None).select(
        database.item.short_description
    ):
        text = row.short_description.lower()
        woorden = [woord.strip("-") for woord in re.findall(r"[\w-]+", text)]
        freqs.update(woorden)
    return response.json(dict(freqs.most_common()))


@auth.requires_membership("education_warehouse")
def clean_redis():
    import redis

    backend.applog.clean_redis(email=auth.user.email)

    r = redis.Redis(os.environ["REDIS_MASTER_HOST"])
    killed = copied = skipped = 0
    try:
        traffic_db = redis.Redis(os.environ["REDIS_MASTER_HOST"], db=1)
        keys = r.keys()
        for key in keys:
            if b"-keys" in key:
                # requests-keys and # response-keys cannot be moved this way as they aren't regular values but sets
                skipped += 1
                continue
            if b"request-" in key or b"response-" in key:
                # copy the value to the specific traffic redis database
                traffic_db[key] = r[key]
                copied += 1
            del r[key]
            killed += 1
    except Exception as e:
        session.flash = f"Probleem met het opschonen van redis: {str(e)}"
    else:
        session.flash = (
            f"Redis cleansing: Killed {killed}, copied: {copied}, skipped:{skipped}."
        )
    redirect(URL(f="items"))


@auth.requires_membership("education_warehouse")
def uncache():
    from edwh.core.pgcache.clean import clean

    rows = database.executesql(
        """
    select pg_size_pretty(pg_relation_size('cache')) as table_only, pg_size_pretty(pg_total_relation_size('cache')) as total;
    """
    )
    html = tabulate.tabulate(
        rows, headers=["just the tables", "total size"], tablefmt="html"
    )

    clean()
    session.flash = f"Cache geschoond!"
    return html
    # redirect(URL(f="items"))


@auth.requires_membership("education_warehouse")
def herstart():
    backend.applog.server_event(
        what="restart py4web",
        who=auth.user.email,
        why="unknown",
    )
    restart_py4web()
    redirect(URL("default", "items"))


def toggle_sticker(item_ids, tag_gid, state):
    for item_id in item_ids:
        item = database.item(id=item_id)

        tags_before = tags_after = item.tags

        if not item:
            session.flash = "item not found for id:" + str(item_id)
            continue
        if state == "on":
            if tag_gid not in item.tags or []:
                tags_after = (item.tags or []) + [tag_gid]
                item.update_record(tags=tags_after)
        elif state == "off":
            if tag_gid in item.tags or []:
                tags_after = [_ for _ in item.tags or [] if _ != tag_gid]
                item.update_record(tags=tags_after)

        backend.applog.update_item(
            item.gid,
            by_eddie_email=auth.user.email,
            fields_before={"tags": tags_before},
            fields_after={"tags": tags_after},
        )
    database.commit()


@auth.requires_membership("education_warehouse")
def sticker_beheer():
    TStickers = Tag(database, "67ba8cd8-b564-4cb4-b1bc-10364c5edf16")
    if "unbind" in request.vars:
        if may_remove_stickers:
            unbind_sticker(database, request.vars.unbind)
            TStickers.remove_child(database, Tag(database, request.vars.unbind))

        return redirect(URL())

    (
        stickers_by_tag_gid,
        stickers_by_name,
        image_uri_by_tag_gid,
    ) = get_sticker_collections()
    ordered_names = list(stickers_by_name.values())
    ordered_names.sort(key=lambda name: name.lower())
    memdb = DAL("sqlite:memory")
    memdb.define_table(
        "form",
        Field(
            "tag_gid",
        ),
        Field(
            "image",
            "upload",
            uploadfield="image_file",
            required=True,
            requires=IS_NOT_EMPTY(error_message="Geef een plaatje op."),
        ),
        Field("image_file", "blob"),
    )
    if "new_gid" in request.vars:
        # stel in dat dit vanaf de ?new_gid=<gid> value komt en er niets meer geslecteerd hoeft te worden
        memdb.form.tag_gid.requires = True
        memdb.form.tag_gid.default = request.vars.new_gid
        memdb.form.tag_gid.writable = False
        memdb.form.tag_gid.comment = "Voorgeselecteerd vanuit vorige scherm"
        memdb.form.tag_gid.represent = lambda tag_gid, row: PRE(tag_gid)
    else:
        memdb.form.tag_gid.comment = "Zoek en selecteer een tag via de drop-down list; of laat leeg voor een nieuwe naam"
        memdb.form.tag_gid.requires = IS_EMPTY_OR(
            IS_IN_DB(database, "tag.gid", "%(name)s")
        )

    memdb.form.tag_gid.widget = HTMXAutocompleteWidget(
        request,
        database.tag.name,
        database.tag.gid,
        query=database.tag.deprecated == False,
    )

    form = SQLFORM(memdb.form)

    def form_validation(form):
        if not form.vars.tag_gid and not memdb.form.tag_gid.default:
            form.errors.tag_gid = (
                "Geef een nieuwe naam op, of selecteer een bestaande tag."
            )

    if form.process(onvalidation=form_validation).accepted:
        upload_complete = _handle_sticker_upload(memdb, TStickers)
    else:
        upload_complete = False

    def img_for_gid(gid):
        return (
            IMG(_src=image_uri_by_tag_gid[gid], _width="100")
            if image_uri_by_tag_gid.get(gid)
            else SPAN(XML(I("upload onderweg.")), _style="color:red;font:bold;")
        )

    sticker_gids = list(stickers_by_tag_gid.keys())
    sticker_gids.sort(key=lambda gid: stickers_by_tag_gid.get(gid).lower())

    def table_row(idx: int, gid: str):
        columns = [
            TD(img_for_gid(gid), _style="padding:5px"),
            TD(stickers_by_tag_gid.get(gid), _style="padding:5px"),
            TD(PRE(gid), _style="padding:5px"),
            TD(
                A(
                    "Vervang sticker",
                    _href=URL(vars=dict(new_gid=gid)),
                    _class="button btn btn-info",
                ),
            ),
        ]

        if may_remove_stickers:
            columns.append(
                TD(
                    A(
                        "Verwijder sticker",
                        _href=URL(vars=dict(unbind=gid)),
                        _class="button btn btn-warning",
                        _onclick="return confirm('Weet je zeker dat je deze sticker wil verwijderen?')",
                    ),
                )
            )

        columns.append(
            TD(
                A(
                    "OPEN tag",
                    _href=URL(c="workbench", f="tag", vars=dict(gid=gid)),
                    _class="button btn btn-info",
                ),
            )
        )

        return TR(
            *columns,
            _style="background-color:rgb(240,240,240);" if idx % 2 == 0 else "",
        )

    table = TABLE(
        [table_row(idx, gid) for idx, gid in enumerate(sticker_gids)],
        _border=0,
    )
    return dict(
        table=table,
        form=form,
        upload_complete=upload_complete,
    )


def _handle_sticker_upload(memdb: DAL, TStickers: Tag):
    # nieuwe upload
    uploaded_record = memdb.form[1]
    # gebruik de ingevoerde of de default value
    tag = Tag(database, uploaded_record.tag_gid or memdb.form.tag_gid.default)
    # add_parent kan gewoon gedaan worden, die zoekt zelf al uit dat een child niet dubbel gekoppeld wordt.
    tag.add_parent(database, TStickers)
    file_ext = uploaded_record.image.split(".")[-1]
    # binary_file_contents should be bytes. image_file is a blob.
    # blobs can be , well. anything. since they're blobs.
    # svg's are text, so they are received as text. while pngs are binary.
    # test for conversion possibility to binary: if so , convert
    # to binary and go from there.
    binary_file_contents = (
        uploaded_record.image_file.encode("utf-8")
        if hasattr(uploaded_record.image_file, "encode")
        else uploaded_record.image_file
    )
    attachment = backend.upload_attachment(
        me=User.load(database, EDDIE_GID),
        filecontent=base64.b64encode(binary_file_contents).decode("utf-8"),
        filename=f"{tag.gid}.{file_ext}",
        purpose="attachment",
        ts=request.now,
    )
    # hang de bijlage aan dit specifieke ROC item van Remco
    add_attachment_to_item(
        "0da1c5e9-4572-4da6-af4f-14c277c90c97", str(attachment.id)
    )
    # knoop de attachment ook aan de sticker zelf via de koppeltabel.
    bind_attachment_and_sticker(database, tag.gid, str(attachment.id))
    backend.invalidate("tag", tag.gid)
    backend.invalidate("attachment", attachment.id)
    database.commit()
    return True


@auth.requires_membership("education_warehouse")
def taggem():
    stickers_by_gid, stickers_by_name, image_uri_by_tag_gid = get_sticker_collections()
    platform = request.vars.platform or "SvS"
    all_items = {
        row.gid: row
        for row in database(database.item.id > 0).select(
            database.item.gid, database.item.tags
        )
    }

    # print('stickers by gid:', stickers_by_gid)

    def stickers_for_item(item_gid):
        # print('sticker_for_item', item_gid, 'tags:', all_items[item_gid].tags, end='')
        stickers = [stickers_by_gid.get(str(tag)) for tag in all_items[item_gid].tags]
        result = ", ".join([_ for _ in stickers if _])
        # print('stickers:', repr(stickers), 'result:', repr(result))
        return result

    base_query = database.item.platform == platform
    fields = [
        database.item.gid,
        database.item.name,
        database.user.email,
        database.user.name,
        database.item.short_description,
    ]
    links = [
        dict(
            header="Bewerk",
            body=lambda row: A("Bewerk", _href=URL(f="quick_edit", args=[row.gid])),
        ),
        dict(header="Stickers", body=lambda row: stickers_for_item(row.gid)),
    ]
    selectable = []
    # database.item.gid.represent = lambda value,row:A(value,_href='https://delen.meteddie.nl/Item/'+row.gid,_target='_blank')
    database.item.name.represent = lambda value, row: A(
        value, _href="https://delen.meteddie.nl/Item/" + row.gid, _target="_blank"
    )
    for name, gid in stickers_by_name.items():
        selectable.append(
            ("+" + name, functools.partial(toggle_sticker, tag_gid=gid, state="on"))
        )
        selectable.append(
            ("-" + name, functools.partial(toggle_sticker, tag_gid=gid, state="off"))
        )
    left = database.user.on(database.item.author == database.user.gid)

    def short_but_searchable(short_description, row):
        sd_len = 100
        if not short_description:
            short = "&mdash;"
        elif len(short_description) < sd_len:
            short = short_description
        else:
            short = short_description[:sd_len] + "..."
        return SPAN(short, SPAN(short_description, _style="display:none"))

    database.item.short_description.represent = short_but_searchable
    form = SQLFORM.grid(
        base_query,
        fields=fields,
        searchable=False,
        paginate=None,
        orderby=(~database.item.ts_changed),
        maxtextlength=200,
        maxtextlengths={"item.name": 150, "item.short_description": 100000},
        editable=False,
        details=False,
        deletable=False,
        create=False,
        csv=False,
        selectable=selectable,
        links=links,
    )
    return dict(form=form)


@auth.requires_membership("education_warehouse")
def new_tag():
    platform = request.vars.platform or "SvS"
    # vraag sticker naam, plaatje
    # upload bijlage
    # maak sticker aan als tag en plaats onder stickers
    form = SQLFORM.factory(
        Field("name", "string", required=True, requires=[IS_NOT_EMPTY()]),
        Field("description", "string", required=True, requires=[IS_NOT_EMPTY()]),
        # Field("image", "upload", required=True), # sticker functionaliteit toevoegen
    )

    def validate(form):
        try:
            Tag.new(database, name=form.vars.name, description=form.vars.description)
            # deze rollback is nodig zodat hij straks na de validation een insert kan doen,
            # zonder dat deze al toegevoegd is.
            database.rollback()
        except AssertionError as e:
            form.errors.name = str(e)

    if form.process(onvalidation=validate).accepted:
        new = Tag.new(
            database,
            name=form.vars.name,
            description=form.vars.description,
            meta_tags=[Tag(database, "fc8a7d36-e23e-4aba-8ee9-f5269ecc8dfc")],
            parents=[Tag(database, "38f7b956-6315-4676-8076-8aeef258563e")],
        )
        database.commit()
        return redirect(URL(c="workbench", f="tag.html", vars={"gid": new.gid}))
    return dict(form=form)


@auth.requires_membership("education_warehouse")
def overdragen():
    item = database(database.item.gid == request.args[0]).select().first()
    author = database(database.user.gid == item.author).select().first()
    welkom = None
    # autocomplete widget instellen
    new_author = SQLFORM.widgets.autocomplete(
        request,
        database.user.name,
        id_field=database.user.gid,
        at_beginning=False,
        help_fields=[database.user.name, database.user.email],
        help_string=f"%(name)s (%(email)s)",
    )
    select_form = SQLFORM.factory(
        Field("gid", widget=new_author, label="Naam"),
    )
    if select_form.process(formname="select_form").accepted:
        # get the new ID for the new owner
        new_gid = select_form.vars.gid
        # save the old gid, for later invalidation
        old_author_gid = item.author
        # update the owner to the new gid
        item.update_record(author=new_gid)
        # before anything else, commit to database
        database.commit()
        backend.applog.update_item(
            item.gid,
            by_eddie_email=auth.user.email,
            fields_before={"author": old_author_gid},
            fields_after={"author": new_gid},
        )
        # call the triggers of changed user records
        backend.invalidate("user", new_gid)
        backend.invalidate("user", old_author_gid)
        response.flash = "Praktijk heeft een nieuwe eigenaar. Geen emails verstuurd, ververs de pagina. "
    elif select_form.errors:
        response.flash = "select_form has errors"

    new_user_form = SQLFORM.factory(
        Field("firstname", required=True),
        Field("lastname", required=True),
        Field(
            "email",
            requires=IS_EMAIL(),
            required=True,
            comment="E-mail van de gebruiker. Alleen @educationwarehouse.nl adressen mogen dubbel gebruikt worden.",
        ),
    )

    def check_new_user_form(form):
        if not form.vars.email.strip():
            form.errors.email = "Invalid email address"
        if not form.vars.firstname.strip():
            form.errors.firstname = "Invalid name"
        if not form.vars.lastname.strip():
            form.errors.lastname = "Invalid name"
        if (
            not form.vars.email.strip().lower().endswith("@educationwarehouse.nl")
        ) and (
            database(
                database.user.email.lower() == form.vars.email.strip().lower()
            ).count()
            > 0
        ):
            form.errors.email = "Er is al een gebruiker voor dit email adres, zoek de gebruiker in het veld hierboven."

    if new_user_form.process(
        onvalidation=check_new_user_form, formname="new_user_form"
    ).accepted:
        password = new_password()
        author = backend.create_user(
            new_user_form.vars.email,
            password,
            new_user_form.vars.firstname,
            new_user_form.vars.lastname,
            "",
            "",
            "",
            None,
        )
        old_author_gid = item.author
        item.update_record(author=author.id)
        database.commit()
        backend.applog.update_item(
            item.gid,
            by_eddie_email=auth.user.email,
            fields_before={"author": old_author_gid},
            fields_after={"author": author.id},
        )
        backend.applog.accept_adoption(item.gid, author.id)
        # nodig voor de welkom mail
        welkom = dict(user_gid=str(author.id), password=password)
    elif new_user_form.errors:
        response.flash = "new_user_form has errors"

    return dict(
        select_form=select_form,
        new_user_form=new_user_form,
        item=item,
        author=author,
        welkom=welkom,
        domain=os.getenv("APPLICATION_NAME") + "." + os.getenv("HOSTINGDOMAIN"),
    )


@auth.requires_membership("education_warehouse")
def remove_attachment():
    item_gid, field, attachment_gid = request.args
    item = database.item(gid=item_gid)
    gids = item[field]
    gids.remove(attachment_gid)
    update_args = {field: gids}
    item.update_record(**update_args)
    session.flash = "Attachment ontkoppeld."
    return redirect(URL(f="quick_edit", args=[item_gid]))


@auth.requires_membership("education_warehouse")
def move_background_gid_to_head():
    item_gid, attachment_gid = request.args
    item: Row = database.item(gid=item_gid)
    background_gids: list = item.backgrounds
    if attachment_gid in background_gids:
        background_gids.remove(attachment_gid)
    background_gids.insert(0, attachment_gid)

    old_thumbnail = item.thumbnail
    old_backgrounds = item.backgrounds
    item.update_record(thumbnail=background_gids[0], backgrounds=background_gids)
    session.flash = "Omslagfoto ingesteld."
    database.commit()
    backend.applog.update_item(
        item.gid,
        by_eddie_email=auth.user.email,
        fields_before={"thumbnail": old_thumbnail, "backgrounds": old_backgrounds},
        fields_after={"thumbnail": background_gids[0], "backgrounds": background_gids},
    )
    return redirect(URL(f="quick_edit", args=[item_gid]))


class MutableString(str):
    ...


@auth.requires_membership("education_warehouse")
def quick_create():
    name_field = Field(
        "name",
        "string",
        label="Naam",
        comment="De naam van jouw ontwikkelpraktijk.",
        default=request.vars.name or "",  # fill in old in case of error
        requires=IS_NOT_EMPTY(),
    )

    form = SQLFORM.factory(name_field)

    if form.process().accepted:
        name = form.vars.name
        # dit is meer een placeholder, omdat het fijn is als er altijd een short description is.
        short_description = "Begin hier met het schrijven van een ontwikkelpraktijk..."

        # maak een nieuw item aan via de backend.
        try:
            item = backend.create_item(
                author=EDDIE_GID,
                name=name,
                short_description=short_description,
                by_eddie_email=auth.user.email,
            )
            # maak een nieuwe, lege property bag aan voor het nieuwe item.
            database.property_bag.insert(
                gid=uuid4(), belongs_to_gid=str(item.id), properties={}
            )
            return redirect(URL("quick_edit", args=[str(item.id)]))
        except DuplicateSlugException as e:
            form.errors.name = str(e)
            response.flash = "Er is iets misgegaan."

    return dict(form=form)


@auth.requires_membership("education_warehouse")
def toggle_visibility():
    item_gid = request.args[0]
    visibility = Visibility(request.args[1])
    item = database.item(gid=item_gid)
    # before = f"{item.visibility}"
    old_visibilities = list(set(item.visibility))

    if visibility.value in item.visibility:
        item.visibility.remove(visibility.value)
    else:
        item.visibility.append(visibility.value)

    current_visibilities = list(set(item.visibility))
    item.update_record(visibility=current_visibilities)
    database.commit()

    if "deleted" in current_visibilities and "deleted" not in old_visibilities:
        backend.applog.remove_item(item_gid, auth.user.email)
    else:
        backend.applog.update_item(
            item_gid,
            by_eddie_email=auth.user.email,
            fields_before={"visibility": old_visibilities},
            fields_after={"visibility": current_visibilities},
        )

    backend.invalidate_search_results()
    # after = f"{item.visibility}"
    # return f'before: {before} <br/>after: {after} <br/> visiblity: {visibility} <br/> {visibility in item.visibility}'
    return redirect(request.env.http_referer)


def is_graphic_filename(filename: str):
    return filename.strip().endswith(
        (".jpg", ".png", ".tiff", ".bmp", ".jpeg", ".gif", ".svg")
    )


@auth.requires_membership("education_warehouse")
def quick_edit():
    warning = last_opened_warning("item")
    item_gid = request.args[0]
    item = database.item(gid=item_gid)
    database.item.id.readable = False
    database.item.platform.readable = False
    database.item.platform.writable = False
    database.item.author.writable = False
    database.item.gid.writable = False
    database.item.gid.represent = lambda v: PRE(v)
    database.item.thumbnail.writable = False
    database.item.thumbnail.readable = False
    database.item.ts_changed.writable = False
    database.item.ts_changed.represent = lambda v: PRE(v)
    database.item.alternatives.writable = False
    database.item.alternatives.readable = False

    #  deze 2 zijn wel writable, maar via eigen form en functies
    database.item.attachments.writable = False
    database.item.backgrounds.writable = False
    database.item.onderbouwing_bronnen.writable = False

    database.item.slug.writable = auth.has_membership(role="admin")
    database.item.slug.represent = lambda v: PRE(v)
    database.item.tags.readable = False
    database.item.tags.writable = False
    database.item.short_description.comment = (
        "Klik op ESC om de Fullscreen-editor te verlaten."
    )

    database.item.visibility.writable = False
    database.item.visibility.comment = (
        "Stel de zichtbaarheid in middels de bovenste knoppen."
    )

    # database.item.short_description.length = 2**16

    def represent_attachments(gids, field):
        items = []
        nbsp = XML("&nbsp;")
        span_20px = DIV(nbsp, _class="width:20px;")
        for gid in gids or []:
            att = database.attachment(gid=gid)
            remove_link = A(
                I(_class="fa fa-trash", _title="Attachment ontkoppelen"),
                _href=URL(f="remove_attachment", args=[item.gid, field, att.gid]),
            )
            if att.b2_uri:
                li = LI(
                    SPAN(
                        A(
                            I(_class="fa fa-image", _title="Maak omslag foto"),
                            _href=URL(
                                f="move_background_gid_to_head",
                                args=[item.gid, att.gid],
                            ),
                        ),
                        nbsp,
                    )
                    if field == "backgrounds"
                    else DIV(span_20px, nbsp),
                    remove_link,
                    nbsp,
                    A(
                        IMG(_src=att.b2_uri, _width="50", _title=gid)
                        if (field == "backgrounds" or is_graphic_filename(att.filename))
                        else att.filename,
                        _href=att.b2_uri,
                        _target="blank",
                    ),
                )
            else:
                li = LI(
                    remove_link,
                    nbsp,
                    nbsp,
                    SPAN(att.filename, " is pending upload...", _title=gid),
                )
            items.append(li)
        return DIV(*items, _style="list-style-type: none;")

    database.item.backgrounds.represent = lambda gids: represent_attachments(
        gids, "backgrounds"
    )
    database.item.attachments.represent = lambda gids: represent_attachments(
        gids, "attachments"
    )
    database.item.onderbouwing_bronnen.represent = lambda gids: represent_attachments(
        gids, "onderbouwing_bronnen"
    )
    database.item.author.comment = XML(
        A("Overdragen", _href=URL("overdragen", args=[item_gid]), _target="blank")
    )

    attachment_form = SQLFORM.factory(
        Field(
            "purpose",
            "string",
            requires=IS_IN_SET(["BACKGROUND", "ATTACHMENT", "ONDERBOUWING"]),
            comment="BACKGROUND voor (extra) achtergronden die bij het artikel getoond worden; ATTACHMENT voor bijlagen die in het bijlagen veld ter download aangeboden worden. ",
        ),
        Field(
            "published_filename",
            "string",
            requires=IS_NOT_EMPTY(),
            comment="De naam die gebruikt wordt voor het gepubliceerde bestand.",
        ),
        Field("attachment", "upload", label="Attachment uploaden"),
    )
    attachment_form.element(_type="submit")["_value"] = "Bijlagen en media opslaan"
    if attachment_form.process().accepted:
        handle_attachment_form(attachment_form, item)

    form = SQLFORM(database.item, item)
    form.element(_type="submit")["_value"] = "Eigenschappen opslaan"
    if form.process().accepted:
        return handle_item_form(form, item, item_gid)

    domain = os.getenv("APPLICATION_NAME") + "." + os.getenv("HOSTINGDOMAIN")
    return dict(
        form=form,
        item_id=item.id,
        item=item,
        property_bag=json.loads(
            getattr(database.property_bag(belongs_to_gid=item_gid), "properties", "{}")
        ),
        attachments=attachment_form,
        warning=warning,
        item_url=f"https://{domain}/item/{item.gid}",
    )


def handle_item_form(form, item: Row, item_gid: str):
    # reflect changes in the propertybag.
    # load the appropriate bag
    pb = database.property_bag(belongs_to_gid=item_gid)
    # load string into json
    properties = json.loads(pb.properties) if pb else {}
    # update fieldSummary field
    properties["fieldSummary"] = form.vars.short_description
    # update pb record so changes are written in database
    if pb:
        pb.update_record(properties=properties)
    # reflect a record change in the item record
    database.item(gid=item_gid).update_record(ts_changed=request.now)
    database.commit()

    data_after = dict(form.vars)
    data_before = {
        key: value for key, value in item.as_dict().items() if key in data_after
    }

    backend.applog.update_item(
        item_gid,
        by_eddie_email=auth.user.email,
        fields_before=data_before,
        fields_after=data_after,
    )
    # invalidate from cache
    # force reload of the page, display the datetime updates correct
    backend.invalidate("item", item_gid)
    session.flash = "Success, item cache is geïnvalideerd."
    # if visibility changed, invalidate search results so this item will
    # show up in the search results, that until now haven't seen this item.
    if item.visibility != form.vars.visibility:
        session.flash += " Zoekresultaten zijn geïnvalideerd."
        backend.invalidate_search_results()
    return redirect(URL(args=request.args))


def handle_attachment_form(attachment_form, item):
    # bij het verwerken van nieuwe attachments:

    # bedenk het volledig pad naar het zojuist geuploade bestand, wat een tijdelijke naam kan hebben
    # maar wel de juiste extensie
    uploaded_filename = os.path.join(
        request.folder, "uploads", attachment_form.vars.attachment
    )
    # onthoud de extensie van de upload
    att_extension = os.path.splitext(attachment_form.vars.attachment)[-1]
    if att_extension not in attachment_form.vars.published_filename:
        # als de extensie niet voorkomt in de bestandsnaam, voeg deze dan toe voor
        # gebruikersgemak op het platform (dat bla.pdf met een naam 'rapport' wordt dan rapport.pdf)
        attachment_form.vars.published_filename += att_extension
    # upload het bestand, update het record met het gekozen veld, en verleng de lijst met attachment_gids
    with open(uploaded_filename, "rb") as uploaded_file:
        # update de attachment, maar wel onder de eddie_token. Want de normale mag niet uploaden
        attachment = backend.upload_attachment(
            me=User.load(database, EDDIE_GID),
            filename=attachment_form.vars.published_filename,
            filecontent=base64.b64encode(uploaded_file.read()).decode("utf-8"),
            purpose=attachment_form.vars.purpose.lower(),
            ts=request.now,
        )

    # update_kwargs is variabel ivm het kiezen van backgrounds of attachments veld
    update_kwargs = {}
    field_name = {
        "BACKGROUND": "backgrounds",
        "ONDERBOUWING": "onderbouwing_bronnen",
        "ATTACHMENT": "attachments",
    }[attachment_form.vars.purpose]

    # haal de huidige lijst op van het record
    old_list_of_gids = item[field_name]
    current_list_of_gids = old_list_of_gids.copy()
    # voeg nieuwe element toe
    if current_list_of_gids:
        current_list_of_gids.append(str(attachment.id))
    else:
        current_list_of_gids = [str(attachment.id)]
    # stel de nieuwe lijst van items in als de nieuwe waarheid
    update_kwargs[field_name] = current_list_of_gids
    # en sla op in de database
    item.update_record(**update_kwargs)
    database.commit()
    backend.applog.update_item(
        item.gid,
        by_eddie_email=auth.user.email,
        fields_before={field_name: old_list_of_gids},
        fields_after={field_name: current_list_of_gids},
    )
    # verwijder het bestand uit de 'uploads' folder. deze hebben we namelijk niet meer nodig, omdat deze
    # alleen dient als buffer tussen de cloudopslag en web2py.
    os.unlink(uploaded_filename)


@auth.requires_membership("education_warehouse")
def prev_items():
    item = database.item
    base_query = item.platform == (request.vars.platform or "SvS")
    base_query &= item.author != None
    fields = [
        item.name,
        item.short_description,
        item.author,
        item.ts_changed,
        item.gid,
        item.gid,
        item.gid,
        item.gid,
    ]
    short_description_idx = 1
    delen_link_idx = 5
    edit_item_idx = 6
    overdragen_idx = 4
    if "tech" in request.vars:
        fields.extend(
            [
                item.gid,
                item.author,
                item.tags,
            ]
        )
    rows = database(base_query).select(*fields, orderby=(~item.ts_changed))
    form = SQLTABLE(rows, truncate=50000)
    # hide the short_description, but it's in there, so search works based on that
    for idx, row in enumerate(form.elements("tr")):
        row[short_description_idx][0] = SPAN(
            row[short_description_idx][0], _style="display:None"
        )
        if idx == 0:
            row[delen_link_idx][0] = "Delen link"
            row[edit_item_idx][0] = "Bewerk item"
            row[overdragen_idx][0] = "Overdragen"
        else:
            row[delen_link_idx][0] = A(
                row[delen_link_idx][0],
                _href="https://delen.meteddie.nl/item/" + row[delen_link_idx][0],
                _target="_blank",
            )
            row[edit_item_idx][0] = A(
                "Bewerk", _href=URL(f="quick_edit", args=[row[edit_item_idx][0]])
            )
            row[overdragen_idx][0] = A(
                "Overdragen", _href=URL(f="overdragen", args=[row[overdragen_idx][0]])
            )
    return dict(form=form)


re_markdown_link = re.compile(r"(?:__|[*#])|\[(.*?)\]\((.*?)\)")


def link_check(item_row):
    @gluon.cache.lazy_cache(
        key="link-checker" + str(item_row.gid), time_expire=180, cache_model=cache.ram
    )
    def do_check():
        item = item_row
        status = True
        errors = []
        okay_link_count = 0
        links = []
        # find all matchs
        matches = [
            match.groups()[-2:]
            for match in re_markdown_link.finditer(item_row.short_description)
        ]
        # drop link is None and strip() the link in result
        matches = [(label, link.strip()) for label, link in matches if link]
        for label, link in matches:
            if link in links:
                continue
            links += [link]
            try:
                headers = {
                    "user-agent": "Mozilla/5.0 (Linux x86_64; educationwarehouse-link-checker/2022.05.04 +https://www.educationwarehouse.nl)"
                }
                code = httpx.options(link, headers=headers).status_code
                valid = 200 <= code < 400
                if not valid:
                    code = httpx.head(link, headers=headers).status_code
                    valid = 200 <= code < 400
                    if not valid:
                        code = httpx.get(link, headers=headers).status_code
                        valid = 200 <= code < 400
                        if not valid:
                            errors.append(link + ":" + str(code))
                else:
                    okay_link_count += 1
            except Exception as e:
                valid = False
                code = -1
                errors.append(str(e))
            status &= valid
        return DIV(
            XML(
                " ".join(
                    [
                        f"&check;&nbsp;({okay_link_count})" if okay_link_count else "",
                        f"&cross;&nbsp;({len(errors)})" if errors else "",
                    ]
                )
            ),
            _title=str(errors),
        )

    return do_check()


def advanced_search_widget(_, url):
    keywords = request.vars.get("keywords")

    help_text = """
    Tip: 
    Gebruik <code>#</code> voor tags (bijv. #iol-rapportage). 
    Gebruik quotes (<code>'</code>, <code>"</code>) om exact te zoeken. 
    Gebruik <code>-</code> om termen uit te sluiten (bijv. -"begin hier met").
    """

    return CAT(
        STYLE(
            """
    .web2py_console {
        display: flex;
    }
    """
        ),
        DIV(
            FORM(
                INPUT(
                    _name="keywords",
                    _value=keywords,
                    _id="w2p_keywords",
                    _class="form-control",
                    _style="width: 100%",
                ),
                INPUT(
                    _type="submit",
                    _value=T("Search"),
                    _class="btn btn-default btn-secondary",
                ),
                INPUT(
                    _type="submit",
                    _value=T("Clear"),
                    _class="btn btn-default btn-secondary",
                ),
                _method="GET",
                _action=url,
                _style="display: flex",
            ),
            TAG.SMALL(XML(help_text), _style="margin: 10px;"),
            _style="flex: 1; padding-bottom: 10px",
        ),
    )


def advanced_item_search_handling(search_in: list[str, Field], keywords: str) -> Query:
    search_in = ["tags", "name", "description", "author"]

    select_kwargs = {}
    query = backend._apply_search(
        database.item.id > 0, keywords, search_in, select_kwargs
    )

    # create subquery here to take select_kwargs into account (e.g. required left joins):
    results = database(query)._select(database.item.id, **select_kwargs)

    # final subquery:
    return database.item.id.belongs(results)


@auth.requires_membership("education_warehouse")
def items():
    item = database.item
    database.item.name.label = "Titel"
    database.item.short_description.label = "Artikel"
    database.item.author.label = "Auteur"
    database.item.ts_changed.label = "Laatst gewijzigd"

    if is_admin:
        # link to 'applog/<gid>'
        database.item.ts_changed.represent = lambda value, row: A(
            XML(str(value or "?").replace(" ", "<br/>")),
            _style="white-space: nowrap",
            _href=URL("applog", "item", row.gid),
        )
    else:
        database.item.ts_changed.represent = lambda value, row: SPAN(
            XML(str(value).replace(" ", "<br/>")), _style="white-space: nowrap"
        )

    database.item.gid.readable = False
    database.item.tags.represent = lambda tag_gids, row: SPAN(
        *(
            SPAN(
                database.tag(gid=tag_gid).name,
                _class="badge",
            )
            for tag_gid in tag_gids
        )
    )
    base_query = item.platform == (request.vars.platform or "SvS")
    if not is_admin:
        base_query &= ~item.visibility.contains("deleted")

    base_query &= item.author != None

    if request.vars.get("order") == "~item.ts_changed":
        # prevent None (when you use no order, None is at the top)
        base_query &= item.ts_changed != None

    fields = [
        item.name,
        item.short_description,
        item.author,
        item.ts_changed,
        item.tags,
        item.gid,
    ]
    links = [
        dict(
            header="Bekijk",
            body=lambda row: A(
                XML("Bekijk op website"),
                _href=f"https://{os.getenv('APPLICATION_NAME')}.{os.getenv('HOSTINGDOMAIN')}/item/"
                      + row.gid,
                _target="_blank",
                _class="btn btn-primary",
            ),
        ),
        dict(
            header="Bewerk",
            body=lambda row: A(
                "Bewerk",
                _href=URL(f="quick_edit", args=[row.gid]),
                _target="_blank",
                _class="btn btn-default",
            ),
        ),
        dict(
            header="Overdragen",
            body=lambda row: A(
                "Overdragen",
                _href=URL(f="overdragen", args=[row.gid]),
                _target="_blank",
                _class="btn btn-warning",
            ),
        ),
    ]
    met_linkchecker = "lc" in request.vars
    if met_linkchecker:
        links.append(
            dict(
                header="Link check",
                body=lambda row: link_check(row),
            )
        )

    form = SQLFORM.grid(
        base_query,
        fields=fields,
        orderby=~item.ts_changed,
        create=False,
        deletable=False,
        editable=False,
        # searchable=True,
        searchable=advanced_item_search_handling,
        search_widget=advanced_search_widget,
        advanced_search=False,
        details=False,
        maxtextlength=100,
        paginate=10 if met_linkchecker else 25,
        links_in_grid=True,
        buttons_placement="left",
        links_placement="left",
        csv=False,
        links=links,
    )
    return dict(form=form)


@auth.requires_membership("education_warehouse")
def users():  # NO_TEST_REDIRECT_ON
    user = database.user
    query = database.user
    fields = [user.platform, user.name, user.email, user.has_validated_email, user.gid]
    if "tech" in request.vars:
        fields.extend([user.property_bag, user.platform])
    else:
        database.user.gid.readable = False
        query = database.user.platform == "SvS"
    password_reset_link = dict(
        header="Herstel wachtwoord",
        body=lambda row: A(
            "Herstel wachtwoord",
            _class="btn btn-default",
            _href=URL(f="password_reset_are_you_sure", args=row.id),
        ),
    )
    find_items = dict(
        header="Praktijken",
        body=lambda row: A(
            f"Bekijk {database(database.item.author == row.gid).count()} praktijken",
            _class="btn btn-default",
            _href=URL(f="items", vars={"keywords": row.gid}),
        ),
    )

    def hash_possible_password(form):
        if not form.vars.password.startswith("$sa"):
            form.vars.password = hash_password(form.vars.password)
        print(form.vars)

    form = SQLFORM.grid(
        query,
        fields=fields,
        searchable=True,
        advanced_search=False,
        paginate=20,
        orderby=(~user.id),
        maxtextlength=200,
        links=[password_reset_link, find_items],
        buttons_placement="left",
        links_placement="left",
        onvalidation=hash_possible_password,
    )
    return dict(form=form)


@auth.requires_membership("education_warehouse")
def domeinen():
    t = database.email_domain
    t.platform.readable = True
    form = SQLFORM.grid(
        t,
        fields=(t.platform, t.domain, t.is_new_user_allowed),
        searchable=False,
        paginate=250,
        orderby=(t.domain),
    )
    return dict(form=form)


@auth.requires_membership("education_warehouse")
def check_domeinen():
    domains = gevonden = None
    bekend = []
    onbekend = []
    form = SQLFORM.factory(
        Field(
            "lap_text",
            "text",
            requires=IS_NOT_EMPTY(),
            label="Tekst met email adressen",
            comment="Knip en plak hier text uit excel of vanuit je mailpakket, email adressen worden opgezocht.",
        )
    )
    processed = form.process()
    if processed.accepted:
        import re

        text = form.vars.lap_text.replace("<", "").replace(">", "")
        emails = [t[0] for t in re.findall(r"(\w+@[\w]+\.(.[\w]+)+)", text)]
        if not emails:
            domains = [l.strip() for l in text.split("\n")]
        else:
            domains = [email.split("@")[1] for email in emails]
        # print(domains)
        domains = list(set(domains))
        domains.sort()
        for domain in domains:
            if (
                database(database.email_domain.domain.lower() == domain.lower()).count()
                > 0
            ):
                bekend.append(domain)
            else:
                onbekend.append(domain)
        # print(bekend, onbekend)
    elif form.errors:
        response.flash = "Help! Niet goed!"
    return dict(form=form, gevonden=domains, bekend=bekend, onbekend=onbekend)


@auth.requires_membership("education_warehouse")
def insert():
    allowed = bool(int(request.vars.allowed)) if request.vars.allowed else False
    print(allowed, request.vars)
    # insert alle domains die als args zijn toegevoegd
    for domain in request.args:
        database.email_domain.insert(domain=domain, is_new_user_allowed=allowed)
    redirect(URL(f="index"))


@auth.requires_membership("education_warehouse")
def password_reset_are_you_sure():
    # als er geen argument in de URL word meegegeven,
    # raise een HTTP 400 error
    if not request.args:
        raise HTTP(400, "No ID specified.")
    for field in database.user.fields:
        database.user[field].writable = False
        database.user[field].readable = False
    for field in ["email", "name"]:
        database.user[field].readable = True

        # form = SQLFORM.factory(
    #     Field('gebruiker', requires=IS_IN_DB(db, 'gebruiker.email', '%(email)s -> %(gebruikersnaam)s'))
    # )
    form = SQLFORM(
        database.user,
        # record meegegeven in de URL
        record=request.args[0],
        # geeft de form een button 'Reset wachtwoord' die naar de functie form_process gaat
        # met als argument de request.args die hiervoor meegegeven was.
        buttons=[
            BUTTON(
                "Reset wachtwoord",
                _type="button",
                _onClick="parent.location='%s'"
                         % URL(f="password_reset_confirmed", args=request.args[0]),
            )
        ],
    )
    return dict(form=form)


@auth.requires_membership("education_warehouse")
def password_reset_confirmed():
    user_id = request.args[0]
    user = database.user[user_id]
    backend.recover(user.email)
    session.flash = "Mail verstuurd!\n"
    redirect(URL(f="users"))


#
# @auth.requires_membership("education_warehouse")
# def password_reset_confirmed():
#     """ " Set the password reset key and send an invitation email."""
#     reset_key = generate_reset_key()
#     user_id = request.args[0]
#     user = database.user[user_id]
#
#     # sla de reset key op bij de gebruiker
#     user.update_record(reset_key=reset_key)
#     database.commit()
#
#     # stel het url samen waarmee de gebruiker het wachtwoord kan wijzigen, zodat we deze url gaan mailen
#     web_url = str(
#         URL(
#             f="change_password",
#             scheme="https",
#             host=myconf.get("host.name_in_email"),
#             args=[reset_key],
#         )
#     )
#
#     # stuur op basis van de pwreset template de uitnodiging naar de eindgebruiker
#     #  LET OP: dit gaat naar de HUIDIGE APPLICATIE ...
#     # todo: dit moet naar een mooier url :)
#     mg_message = send_mail(
#         "pwreset", user.email, {"naam": user.name, "url": web_url}
#     ).json()["message"]
#     session.flash = "Mail verstuurd!\n" + mg_message
#     redirect(URL(f="users"))
#
#
# def change_password():
#     # controleer eerst of er wel een reset_key is meegegeven
#     if not request.args:
#         return dict(
#             form=None,
#             error=XML(
#                 "Helaas, deze link werkt niet.<br/>"
#                 "Probeer een wachtwoord herstel vanaf <br/> "
#                 '<a href="https://delen.meteddie.nl">delen.meteddie.nl</a>'
#             ),
#         )
#     # lees deze dan uit
#     reset_key = request.args[0]
#     # vind het gebruiker record dat hoort bij deze key.
#     # deze shorthand functie gebruikt altijd het eerste resultaat, en voorkomt een .first()
#     user = database.user(reset_key=reset_key)
#
#     if not user:
#         return dict(
#             form=None,
#             error=XML(
#                 "Helaas. <code>'%s'</code> is vermoedelijk al eens gebruikt.<br/>"
#                 "Probeer nogmaals een wachtwoord herstel vanaf "
#                 '<a href="https://delen.meteddie.nl">delen.meteddie.nl</a>' % reset_key
#             ),
#         )
#
#     not_strong_error = "Niet complex genoeg. Zie hieronder voor een toelichting."
#     not_equal_error = "Wachtwoorden komen niet overeen."
#
#     form = SQLFORM.factory(
#         Field(
#             "new_password",
#             "password",
#             requires=[
#                 IS_NOT_EMPTY(error_message="Mag niet leeg zijn."),
#                 IS_STRONG(min=8, special=1, upper=1, error_message=not_strong_error),
#             ],
#             label="Nieuw wachtwoord",
#         ),
#         Field(
#             "confirm_password",
#             "password",
#             requires=[
#                 IS_NOT_EMPTY(error_message="Mag niet leeg zijn."),
#                 # LET OP: magie van Kevin hier aan het werk....
#                 # dit is NIET de normale web2py manier van doen.
#                 #  maar het werkt wel... kudos...
#                 # moet gelijk zijn aan het eerst opgegeven wachtwoord
#                 IS_EQUAL_TO(request.vars.new_password, error_message=not_equal_error),
#             ],
#             label="Bevestig nieuw wachtwoord",
#         ),
#         formstyle="bootstrap4_stacked",
#     )
#
#     if form.process().accepted:
#         # bedenk een nieuwe hash op basis van het wachtwoord, zoals de front-end dat ook zou doen.
#         new_pass = hash_password(form.vars.new_password)
#
#         # update het gebruikers record met het nieuwe wachtwoord, en vergeet de reset_key
#         user.update_record(password=new_pass, reset_key=None)
#
#         invalidate("user", user.gid)
#
#         database.commit()
#         # stuur de gebruiker door naar delen.meteddie.nl want die kan niks op onze FAB omgeving
#         redirect("http://delen.meteddie.nl")
#
#     return dict(form=form, error=None)


@auth.requires_membership("education_warehouse")
def tag_search():
    show_search = request.vars.get("search", "yes") != "no"
    database.define_table(
        "tag_search_result",
        Field("name", "string", comment="Waar wil je op zoeken", label="Naam"),
        Field(
            "similarity",
            "float",
            represent=lambda value, row: PRE(round(value, 2)),
            label="Vergelijkbaar",
        ),
        Field(
            "name2",
            "string",
            comment="Similarity search",
            label="Similarty",
            writable=False,
        ),
        Field("item", "integer", represent=lambda items, row: PRE(items)),
        Field(
            "btn",
            "str",
            length=36,
            represent=lambda value, row: A(
                "Open",
                _href=URL(
                    c="workbench", f="tag", extension="html", vars={"gid": value}
                ),
                _class="btn button btn-default",
            ),
        ),
        Field("gid", "string", represent=lambda gid, row: PRE(gid)),
        migrate=False,
        primarykey=["gid"],
    )
    if show_search:
        # als er een search getoond mag worden, mag je hier op doorzoeken.
        # anders is doorzoeken niet de bedoeling. Dan is het geload als component
        database.tag_search_result.name2.represent = lambda value, row: A(
            "Zoek", _href=URL(args=[value]), _class="btn button btn-secondary"
        )
    table = database.tag_search_result
    form = SQLFORM.factory(
        table.name,
    )
    if request.vars.q:
        form.vars.name = request.vars.q
    # process the form if applicable
    if form.process(keepvalues=True).accepted:
        gezochte_tag = form.vars.name
        redirect(URL(vars=dict(q=gezochte_tag)))
    else:
        # if form unused, check for args or parameters
        gezochte_tag = request.vars.get("q", request.args[0] if request.args else None)

    form.vars.name = gezochte_tag

    if gezochte_tag:
        result_set = database.executesql(
            """
            select 
                tag.name as name,
                similarity(%(tag)s, tag.name) * 5 + 
                    coalesce(similarity(%(tag)s, tag.akas),0) * 5  + 
                    coalesce(similarity(%(tag)s, tag.description),0) + 
                    coalesce(similarity(%(tag)s, tag.search_hints),0) + 
                    coalesce(similarity(%(tag)s, tag.definition),0) + 
                    coalesce(similarity(%(tag)s, tag.instructions),0) + 
                    coalesce(similarity(%(tag)s, tag.remarks),0)
                    as similarity, 
                tag.name as name2,
                count(item.id) as aantal,
                tag.gid as btn, 
                tag.gid as gid
              from tag 
              left outer join item on item.tags like '%%|'|| tag.gid ||'|%%'
             where (
                    similarity(%(tag)s, tag.name)>0.1 
                    or tag.gid = %(tag)s 
                    or similarity(%(tag)s, tag.akas)>0.1
                    or similarity(%(tag)s, tag.description)>0.1
                    or similarity(%(tag)s, tag.search_hints)>0.1
                    or similarity(%(tag)s, tag.definition)>0.1
                    or similarity(%(tag)s, tag.instructions)>0.1
                    or similarity(%(tag)s, tag.remarks)>0.1
                    )
               and deprecated='F'
             group by tag.name, tag.gid, tag.akas, tag.description, tag.search_hints, tag.definition, tag.instructions, tag.remarks
             order by 2 desc
             limit 50
        """,
            placeholders={"tag": gezochte_tag},
            fields=table,
        )

        if not result_set:
            return dict(
                form=form,
                table="Niets gevonden dat leek op {}".format(gezochte_tag),
                show_search=show_search,
            )

        return dict(
            form=form,
            table=SQLTABLE(
                result_set,
                truncate=60,
                renderstyle=True,
                headers="labels",
                # columns={
                #     # result_set.colnames[0]: False,
                #     result_set.colnames[1]: True,
                #     result_set.colnames[2]: True,
                # },
            ),
            show_search=show_search,
        )
    return dict(form=form, table=None, show_search=show_search)


@auth.requires_membership("education_warehouse")
def auto_tags():
    """
    This method `auto_tags` performs automated tagging based on certain criteria.

    @return: a dictionary containing the generated grid for display

    The method uses a database connection and a table named 'auto_tag' in a SQLite in-memory database. The table has the following fields:

    - `needle` : type string (description: Search criteria)
    - `visibilities` : type list of strings (description: List of visibilities to include)
    - `tag_gid` : type string (description: Tag GUID)
    - `tagged_in_db` : type list of strings (description: List of item GUIDs currently tagged with the destination tag)
    - `search_results` : type list of strings (description: List of item GUIDs matching the search criteria)

    Here is the process flow of the method:

    1. Create the database connection.
    2. Define the table 'auto_tag' with the specified fields.
    3. Insert a sample record into the 'auto_tag' table.
    4. Retrieve all records from the 'auto_tag' table.
    5. For each record, perform the following steps:
       - Get the tagged items with the destination tag from the 'mv__item_tags' table.
       - Perform a search based on the search criteria and included visibilities.
       - Update the record in the 'auto_tag' table with the tagged items and search results.
       - Calculate the items to untag and the items to tag.
       - For items to untag, remove the tag from the item record.
       - For items to tag, add the tag to the item record.
    6. If there are items to untag or items to tag, commit the changes and refresh the materialized view 'mv__item_tags' in the database.
    7. Generate a grid for displaying the 'auto_tag' table with specific configuration.
    8. Return a dictionary containing the generated grid.

    Note: This method requires membership authorization with the role "education_warehouse".

    """
    auto_tag = database.auto_tag
    ITEM_GID = "fc8a7d36-e23e-4aba-8ee9-f5269ecc8dfc"
    auto_tag.tag_gid.widget = HTMXAutocompleteWidget(
        request,
        database.tag.name,
        database.tag.gid,
        query=database.tag.meta_tags.contains(ITEM_GID),
    )
    full_table = database(auto_tag).select()
    from functools import reduce

    # reduce(lambda sublist, accumulator: set(accumulator) | set(sublist), nested_list, set())

    all_used_gids = reduce(
        lambda accumulator, sublist: accumulator | set(sublist or []),
        full_table.column("tagged_in_db"),
        set(),
    ) | reduce(
        lambda accumulator, sublist: accumulator | set(sublist or []),
        full_table.column("search_results"),
        set(),
    )

    item_gid_map = {
        _.gid: _.name
        for _ in database(database.item.gid.belongs(list(all_used_gids))).select(
            database.item.gid, database.item.name
        )
    }

    auto_tag.tagged_in_db.writable = False
    auto_tag.search_results.writable = False

    def item_gid_as_link(gid, record, with_untag_button=False):
        full_name = item_gid_map.get(gid, "?")
        short_name = XML(
            textwrap.shorten(full_name, width=30, placeholder="&mldr;")  # …
        )

        untag_button = (
            A(
                XML("&#10060;"),  # ❌
                _href=URL(
                    f="untag",
                    args=[gid, record.tag_gid],
                ),
                _style="font-size:0.8rem;",
                _title="Verwijder deze tag.",
                _onclick="return confirm('"
                         "Weet je zeker dat je deze tag wilt ontkoppelen? "
                         "Het zou kunnen dat het automatisch weer wordt toegevoegd indien de zoektag matcht."
                         "')",
            )
            if with_untag_button
            else ""
        )

        return SPAN(
            A(short_name, _title=full_name, _href=URL("quick_edit", args=[gid])),
            untag_button,
            _title=full_name,
        )

    def item_gids_as_links(gids, record, with_untag_button=False):
        if not gids:
            return SPAN()

        links = sorted(
            [
                item_gid_as_link(gid, record, with_untag_button=with_untag_button)
                for gid in gids
            ],
            key=lambda a: a.attributes.get("_title"),
        )
        links = [str(_) for _ in links]
        return SPAN(XML(" | ".join(links)))

    if "edit" not in request.args:
        auto_tag.tagged_in_db.represent = functools.partial(
            item_gids_as_links,
            with_untag_button=True,
        )
        auto_tag.search_results.represent = functools.partial(
            item_gids_as_links,
            with_untag_button=False,
        )
    else:
        auto_tag.tagged_in_db.readable = False
        auto_tag.search_results.readable = False

    def represent_auto_tag(gid: str, _record) -> A:
        row = database.tag(gid=gid)

        return A(
            row.name if row else "(verwijderde tag)",
            _href=URL(c="workbench", f='tag', args=[gid]),
            _target="_blank"
        )

    auto_tag.tag_gid.represent = represent_auto_tag
    grid = SQLFORM.grid(
        auto_tag,
        searchable=True,
        advanced_search=False,
        paginate=None,
        maxtextlength=20000,
        editable=True,
        details=False,
        deletable=True,
        create=True,
        csv=False,
    )
    return dict(
        grid=grid,
    )


@auth.requires_membership("education_warehouse")
def untag():
    """
    Removes a specific tag from an item.

    Requires the user to have the membership "education_warehouse" in order to access this method.

    Args:
        None.

    Raises:
        HTTP(400): If the method is called without providing both an item gid and a tag gid.
        HTTP(404): If the provided item gid is not found in the database.
        HTTP(404): If the provided tag gid is not found on the item.

    Returns:
        None.
    """
    if len(request.args) != 2:
        raise HTTP(400, "Untag requires an item gid and a tag gid.")

    item_gid, tag_gid = request.args

    record = database.item(gid=item_gid)
    if not record:
        raise HTTP(404, "Item gid not found")

    tags = record.tags

    if tag_gid not in tags:
        raise HTTP(404, "Tag not found on item.")

    record.update_record(tags=list(set(tags) - {tag_gid}))
    database.commit()
    work_auto_tags_magic.delay()
    session.flash = (
        f'Removed tag from "{record.name}", auto_tag is scheduled for update.'
    )
    redirect(request.env.http_referer)


@auth.requires_membership("education_warehouse")
def update_mv__item_tags():
    work_auto_tags_magic.delay()
    session.flash = "Achtergrond update aangevraagd, dit kan even duren."
    redirect(request.env.http_referer or URL(f="auto_tags"))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@auth.requires_membership("education_warehouse")
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():  # NO_TEST_REDIRECT_ON
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
