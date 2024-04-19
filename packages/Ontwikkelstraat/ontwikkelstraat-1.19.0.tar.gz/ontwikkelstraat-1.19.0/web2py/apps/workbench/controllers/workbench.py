import typing

from gluon.tools import prettydate

if typing.TYPE_CHECKING:
    from dataclasses import dataclass

    from edwh.core.tags import Tag
    from gluon import (
        HTTP,
        IS_URL,
        SQLFORM,
        URL,
        A,
        Field,
        auth,
        redirect,
        request,
        response,
        service,
        session,
    )
    from pydal import DAL
    from pydal.objects import Row, Rows
    from slugify import slugify
    from yatl import *

    from ..models.aaa_500_checkbox_widget import TagTree
    from ..models.article_importers import ArticleImporterError, import_article_by_url
    from ..models.db import db, hash_password, may_edit_tag_structure
    from ..models.db_workbench import markdown_preview_widget, workbench_db
    from ..models.db_z_backend import backend, is_authorized_to_edit
    from ..models.plugin_comments import add_comment
    from ..models.scheduler import scheduler

    database: DAL


@auth.requires_membership("education_warehouse")
def index():
    sync_status = scheduler.task_status(db.scheduler_task.task_name == "sync_eddie")
    failed = {"TIMEOUT", "FAILED"}
    if sync_status:
        if sync_status.status in failed:
            response.flash = (
                f"{sync_status.status}: Laatste synchronisatie niet gelukt."
            )
        last_synced = (
            prettydate(sync_status.last_run_time) if sync_status.last_run_time else None
        )
    else:
        last_synced = None

    workbench_db.item.klad.readable = False
    workbench_db.item.id.readable = False
    workbench_db.item.ctime.readable = False
    workbench_db.item.mtime.readable = False
    workbench_db.item.live_gid.readable = False
    workbench_db.item.ori_uri.readable = False
    workbench_db.item.property_bag.readable = False

    grid = SQLFORM.grid(
        workbench_db.item,
        maxtextlength=60,
        csv=False,
        paginate=1000,
        advanced_search=False,
        create=False,
        editable=False,
        deletable=False,
        orderby=~workbench_db.item.mtime,
        links=[
            dict(
                header="Edit",
                body=lambda row: A(
                    "Edit", _class="btn btn-default", _href=URL(f="edit", args=[row.id])
                ),
            ),
            dict(
                header="Metadateren",
                body=lambda row: A(
                    "Metadateren",
                    _class="btn btn-primary",
                    _href=URL("metadateren", args=row.id),
                ),
            ),
        ],
    )

    import_form = SQLFORM.factory(
        Field("import_url", requires=IS_URL(error_message="Dit is geen URL."))
    ).process()
    if import_form.accepted:
        return redirect(URL("import_item", vars={"url": import_form.vars.import_url}))

    return dict(
        grid=grid,
        import_form=import_form,
        sync_status=sync_status,
        last_synced=last_synced,
    )


@auth.requires_membership("education_warehouse")
def import_item():
    url = request.vars["url"]
    try:
        new_article_id = import_article_by_url(url)
    except ArticleImporterError as e:
        session.flash = str(e)
        redirect(URL("index"))
    session.flash = "Item succesvol geïmporteerd."
    return redirect(URL("edit", args=[new_article_id]))


@auth.requires_membership("admin")
def eddie_sync():
    """Controller voor het starten van de synchronisatie via GraphQL."""
    # TODO: synchronisatie werkt momenteel één kant op, moet dit ook andersom?
    # annuleer het proces als de task een van onderstaande statussen heeft.
    cancel_on = {"QUEUED", "RUNNING", "ASSIGNED"}
    task = scheduler.task_status(db.scheduler_task.task_name == "sync_eddie")

    if task:
        if task.status in cancel_on:
            # de gebruiker mag niet nog een keer de task uit laten voeren als deze al bezig is,
            # daarom redirecten we terug naar de index.
            session.flash = "ERROR: Er is al een synchronisatie gestart."
            return redirect(URL("index"))

    # task in de wachtrij zetten, herhaalt zich 1 keer als het proces gefaald is.
    scheduler.queue_task("sync_eddie", repeats=1, immediate=True, timeout=600)
    session.flash = "Synchronisatie gestart.. (Dit kan even duren)"
    return redirect(URL("index"))


@auth.requires_membership("education_warehouse")
def new():
    # TODO: reduceren tot alleen een titel en een contact id.
    item_form = SQLFORM(workbench_db.item)
    if item_form.process().accepted:
        new_record_id = item_form.vars.id
        add_comment(
            "item",
            new_record_id,
            f"Ik heb dit item aangemaakt als {item_form.vars.name}.",
        )
        redirect(URL(f="edit", args=[new_record_id]))
    return dict(item_form=item_form)


@auth.requires_membership("education_warehouse")
def metadateren():
    """Bedoeld om alleen de metadata van een item te editen"""
    if not request.args:
        return "requires item id"
    item_id = request.args[0]
    item = workbench_db.item[item_id]
    if not item:
        return "item doesn't exist."

    workbench_db.item.id.readable = False
    workbench_db.item.contact_id.writable = False
    workbench_db.item.title.writable = False
    workbench_db.item.ori_uri.writable = False
    if item.raw_text:
        workbench_db.item.raw_text.widget = markdown_preview_widget
    if item.klad:
        workbench_db.item.klad.widget = markdown_preview_widget
    else:
        workbench_db.item.klad.writable = False

    item_form = SQLFORM(
        workbench_db.item,
        item_id,
        fields=["contact_id", "title", "raw_text", "klad", "ori_uri"],
    )

    return dict(item_form=item_form, item=item)


@auth.requires_membership("education_warehouse")
def edit():
    """Bedoeld om een item aan te passen."""
    if not request.args:
        return "requires item_id"
    item = workbench_db.item[request.args[0]]
    if item.live_gid:
        workbench_db.item.live_gid.writable = False
    if item.raw_frozen:
        workbench_db.item.raw_text.widget = markdown_preview_widget
    item_form = SQLFORM(workbench_db.item, item.id)
    if item_form.vars.raw_text is None:
        # waarschijnlijk ondertussen overbodig, maar voor de zekerheid staat
        # het er nog.
        item_form.vars.raw_text = item.raw_text
    item_form.process(formname="item_name", keepvalues=True, detect_record_change=True)
    # submit knop van het formulier van het item verbergen. dit doen we om uiteindelijk via 1 centrale
    # submit knop alles in 1x te submitten.
    item_form.element(_type="submit")["_class"] = "hide submit_item"

    if item_form.record_changed:
        session.flash = "LET OP: wijzigingen zijn niet opgeslagen, omdat iemand anders net deze tekst heeft gewijzigd. "
        redirect(URL(args=[item.id]))
    elif item_form.accepted:
        import difflib

        old = (item.raw_text or "").splitlines(True)
        if item_form.vars.raw_text:
            new = item_form.vars.raw_text.splitlines(True)
            if old != new:
                diff = difflib.unified_diff(old, new)
                diff = "".join(diff)
                diff = f"""``` diff\n{diff}\n```"""
                add_comment("item", item.id, f"Wijziging in Ruwe tekst:\n\n{diff}")
        old = (item.klad or "").splitlines(True)
        if item_form.vars.klad:
            new = item_form.vars.klad.splitlines(True)
            if old != new:
                diff = difflib.unified_diff(old, new)
                diff = "".join(diff)
                diff = f"""``` diff\n{diff}\n```"""
                add_comment("item", item.id, f"Wijziging in klad tekst:\n\n{diff}")
        redirect(URL(args=[item.id]))
    workbench_db.source_file.item_id.default = item.id

    login_form = SQLFORM.factory(Field("email"), Field("password", "password"))
    if login_form.process().accepted:
        validated = backend.login(
            email=login_form.vars.email,
            password_hash=hash_password(login_form.vars.password),
            hardware="{}",
        )
        if not validated.ok:
            response.flash = validated.feedback
        else:
            response.flash = f"Ingelogd als {validated.user.name}"

    return dict(item_form=item_form, item=item, tags=tag_tree, login_form=login_form)


@auth.requires_membership("education_warehouse")
def create_or_update_item():
    """Bedoeld om een item te maken of updaten."""
    if not request.args:
        return redirect(URL("edit"))
    item_id = request.args[0]
    item = workbench_db.item[item_id]

    if not item:
        session.flash = "Item bestaat niet"
        return redirect(URL("index"))

    # we willen expliciet de rows meegeven, omdat we zo ook de juiste filename mee kunnen geven bij het uploaden
    # van een attachment.
    attachment_rows = workbench_db(workbench_db.source_file.item_id == item_id).select()
    item_tags = workbench_db(workbench_db.item_tag.item_id == item_id).select()
    # hier hebben we alleen de gids nodig van de tags.
    tags = [_.tag_gid for _ in item_tags] if item_tags else []

    status = request.vars.get("status")
    if status not in {"published", "unpublished", "draft"}:
        session.flash = "ERROR: Ongeldige status."
        return redirect(URL("edit", args=item_id))

    elif status == "published":
        # als het item al gepubliceerd is, dan gaan we het item updaten.
        if not is_authorized_to_edit(item_gid=item.live_gid, me=backend.me):
            # als een gebruiker niet de huidige auteur van het item is, dan mag hij/zij
            # deze ook niet aanpassen.
            session.flash = "Niet bevoegd om dit item aan te passen."
            return redirect(URL("edit", args=item_id))

        resp = backend.update_item(
            id=item.live_gid,
            name=item.title,
            short_description=item.klad,
            attachments=attachment_rows,
            tags=tags,
            thumbnail=None,
        )
        session.flash = (
            resp["errors"][0]["message"]
            if resp.get("errors")
            else "Item updates gepubliceerd!"
        )
        return redirect(URL("edit", args=item_id))

    else:
        # als het item niet eerder gepubliceerd is, dan gaan we nu dus een item aanmaken
        # via de backend.
        live_gid = backend.create_item(
            name=item.title,
            # item.klad, omdat we item.raw_text niet naar de productieomgeving willen hebben.
            short_description=item.klad,
            attachments=attachment_rows,
            tags=tags,
            thumbnail=None,
        )
        # update het item in de workbench met de nieuwe live_gid van delen.meteddie.nl
        item.update(live_gid=live_gid)
        # item record opslaan, voor de zekerheid.
        item.update_record()
        session.flash = "Item gepubliceerd!"
        return redirect(URL("edit", args=[item_id]))


@auth.requires_membership("education_warehouse")
def source_grid():
    """Bedoeld om een grid te laden van de bijlagen van een item.

    :returns dict met een grid van de bijlagen van een item.
    """
    item_id = request.args[0]
    workbench_db.source_file.item_id.writable = False
    workbench_db.source_file.item_id.readable = False
    workbench_db.source_file.id.readable = False
    workbench_db.source_file.item_id.default = item_id

    grid = SQLFORM.grid(
        workbench_db.source_file.item_id == item_id,
        formname="source_grid",
        args=request.args[:1],
        paginate=100,
        maxtextlength=60,
        searchable=False,
        csv=False,
    )
    return dict(source_grid=grid)


def flatten(list_of_lists):
    return sum(list_of_lists, [])


@auth.requires_membership("education_warehouse")
def tag_tree():
    """Bedoeld als component om een tree van tags te laten zien."""
    target_database = request.args[0]
    item_id = request.args[1]
    # lees de huidige tags, doe dit op basis van de doel database
    if target_database == "workbench":
        _tags = workbench_db(workbench_db.item_tag.item_id == item_id).select(
            workbench_db.item_tag.tag_gid, workbench_db.item_tag.parent
        )

        tag_gids = set(tag.gid for tag in _tags)
    elif target_database == "backend":
        # haal de tags op die voor dit item gebruikt zijn
        item_tags = (
            database(database.item.id == item_id)
            .select(database.item.tags)
            .first()
            .tags
        )
        # voor elke tag wordt nu een lijst gemaakt van de koppeling met de parent. deze lijst wordt platgeslagen en
        # uniek gemaakt.
        _tags = database(
            database.tag.gid.belongs(item_tags) & (database.tag.deprecated == False)
        ).select(database.tag.gid, database.tag.parents)

        tag_gids = set(tag.gid for tag in _tags)
    else:
        raise ValueError(f"{target_database} is onbekend en niet ondersteund.")

    # haal alle tag records waarvan de gid overeenkomt met een gid uit de lijst.
    tag_rows = database(database.tag.gid.belongs(tag_gids)).select(distinct=True)

    tree = TagTree(selected_tag_gids=tag_gids)
    api_target_updater_function = {
        "backend": "backend_item_tag",
        "workbench": "workbench_item_tag",  # fixme: strip prefix ...: bij saven
    }[target_database]

    return dict(
        tags=tag_rows,
        item_id=item_id,
        widget=tree,
        api_tag_updater_function=api_target_updater_function,
    )


@auth.requires_membership("education_warehouse")
def tag_beheer():
    tree = TagTree(
        checkbox=False,
        drag_n_drop=True,
        save_url=URL("api", "update_tags"),
    ).tree()

    return dict(tags_tree=tree)


@auth.requires_membership("education_warehouse")
def tag_items():
    tag_gid = request.vars.gid
    item = database.item
    query = item.tags.contains(tag_gid)
    query &= item.platform == "SvS"

    item.gid.represent = lambda value, row: A(
        row.gid, _target="blank", _href=URL(c="default", f="quick_edit", args=[row.gid])
    )

    item.name.represent = lambda value, row: A(
        row.name, _target="blank", _href="https://delen.meteddie.nl/item/" + row.gid
    )
    # items = database(query).select(item.name, item.short_description)
    return SQLFORM.grid(
        query,
        (item.gid, item.name, item.short_description),
        formname="tagitems",
        maxtextlength=60,
        searchable=True,
        advanced_search=False,
        csv=False,
        create=False,
        details=False,
        deletable=False,
        editable=False,
    )


@auth.requires_membership("education_warehouse")
def tag_questions():
    tag_gid = request.vars.gid
    query = workbench_db.tag_question.tag_gid == tag_gid
    workbench_db.tag_question.tag_gid.default = tag_gid
    workbench_db.tag_question.tag_gid.writable = False
    workbench_db.tag_question.tag_gid.readable = False
    return SQLFORM.smartgrid(
        workbench_db.tag_question,
        formname="tag_questions",
        constraints={"tag_question": query},
        linked_tables=["question"],
        maxtextlength=60,
        csv=False,
    )


def sortable_tags(field: str = None, target_gid: str = None, method: str = "CALL"):
    if field not in {"children", "parents", "meta_tags", "related"}:
        raise HTTP(400, "field not allowed")

    target = Tag(database, target_gid)

    if method == "POST":
        if not may_edit_tag_structure:
            raise HTTP(403, "not allowed to edit tag structure")
        # when used to update tags, the gid is posted as a list
        # process the list and update the target row
        # when the result of a move is an empty list, no payload will be posted
        # and request.vars.gid is None.
        posted_gids = request.vars.gid or []
        if not isinstance(posted_gids, list):
            posted_gids = [posted_gids]
        # make sure the gids are unique
        posted_gids = list(dict({gid: gid for gid in posted_gids}).keys())
        old_gids = getattr(target, field)
        # find the delta between the old and new gids
        removed_gids = set(old_gids or []) - set(posted_gids)
        added_gids = set(posted_gids) - set(old_gids or [])
        print("Removed:", [Tag(database, gid).name for gid in removed_gids])
        print("Added:", [Tag(database, gid).name for gid in added_gids])
        # Updating the children means updates of the parents is required as well and vice versa.
        # A mere database update is not enough.
        print("Updating", field, "for", target.name)
        if field == "children":
            for removed_child in removed_gids:
                target.remove_child(database, Tag(database, removed_child))
            for added_child in added_gids:
                target.add_child(database, Tag(database, added_child))
        elif field == "parents":
            for removed_parent in removed_gids:
                target.remove_parent(database, Tag(database, removed_parent))
            for added_parent in added_gids:
                target.add_parent(database, Tag(database, added_parent))
        elif field == "meta_tags":
            for removed_meta_tag in removed_gids:
                target.remove_metatag(database, Tag(database, removed_meta_tag))
            for added_meta_tag in added_gids:
                target.add_metatag(database, Tag(database, added_meta_tag))
        elif field == "related":
            for removed_related in removed_gids:
                target.remove_related(database, Tag(database, removed_related))
            for added_related in added_gids:
                target.add_related(database, Tag(database, added_related))
        else:
            raise ValueError(f"Unsupported field {field}")
        if not removed_gids:
            # only reorder, save the new order. This happens for every add
            # as well as every update (sort) action.
            # HOLY!! first we add a new child/metatag/... and save to database
            # and then we update the record AGAIN! to save the new order.
            target.save_reordered(database, field, posted_gids)

        shown_tag_gids = posted_gids
        database.commit()
        # for idx, (query, timing) in enumerate(database._timings):
        #     print(idx, query, timing)

    else:
        # when used with a GET it's for loading the list
        # just get the ids from the Tags field.
        shown_tag_gids = getattr(target, field)
    print("SORTABLE_TAGS: ", method, field, target_gid, len(shown_tag_gids))
    return sortable_divs(shown_tag_gids, currently_opened_tag=target, property=field)


@auth.requires(may_edit_tag_structure)
def unlink():
    tag = Tag(database, request.args(0))
    property = request.args(1)
    other = Tag(database, request.args(2))
    if property == "children":
        success = tag.remove_child(database, other)
    elif property == "parents":
        success = tag.remove_parent(database, other)
    elif property == "meta_tags":
        success = tag.remove_metatag(database, other)
    elif property == "related":
        success = tag.remove_related(database, other)
    else:
        raise ValueError(f"Unsupported property {property}")
    database.commit()
    return ""


def sortable_divs(
    tag_gids, *, currently_opened_tag: Tag | str = None, property: str = None
):
    def hxattrs(gid):
        return {
            "_hx-post": URL(
                f="unlink",
                args=[
                    getattr(currently_opened_tag, "gid", currently_opened_tag),
                    property,
                    gid,
                ],
            ),
            "_hx-trigger": "click",
            "_hx-target": f"#{property}-{gid}",
            "_hx-swap": "outerHTML",
        }

    sortable_divs = [
        DIV(
            INPUT(_type="hidden", _name="gid", _value=gid),
            A(
                "[X]",
                **hxattrs(gid),
            )
            if property and may_edit_tag_structure
            else "",
            XML("&nbsp;"),
            Tag(database, gid).name,
            XML("&nbsp;"),
            A("Open", _href=URL(f="tag", vars=dict(gid=gid))),
            _class="btn btn-link",
            _id=f"{property}-{gid}",
        )
        for gid in tag_gids
    ]
    output = [str(div) for div in sortable_divs]
    return XML("\n".join(output))


@auth.requires_membership("education_warehouse")
def hxpost_tags():
    "Post new tag gids as children|parents|... of target tag."
    field, target_gid = request.args
    return sortable_tags(field, target_gid, request.method)


@auth.requires_membership("education_warehouse")
def hxsearch():
    if request.vars.q is None or len(request.vars.q.strip()) < 3:
        return "Geef minimaal 3 tekens op om op te zoeken"
    return sortable_divs(Tag.search(database, request.vars.q))


@auth.requires_membership("admin")
def recover_stickers():
    TSticker = Tag(database, "67ba8cd8-b564-4cb4-b1bc-10364c5edf16")
    stickers = database().select(database.sticker.tag_gid)
    TSticker.save_reordered(database, "children", [row.tag_gid for row in stickers])
    redirect(URL(f="tag", vars={"gid": TSticker.gid}))


@auth.requires_membership("education_warehouse")
def tag():
    if request.vars.gid:
        tag_gid = request.vars.gid
    elif request.args:
        tag_gid = request.args[0]
    else:
        tag_gid = None

    tag = database.tag(gid=tag_gid)
    if tag is None:
        raise HTTP(404, f"Tag met gid {tag_gid} niet gevonden.")

    database.tag.id.readable = False
    database.tag.platform.readable = False
    database.tag.platform.writable = False
    database.tag.gid.writable = False
    database.tag.gid.readable = True
    database.tag.gid.represent = lambda gid, row: PRE(gid)
    database.tag.slug.writable = False
    database.tag.slug.represent = lambda gid, row: PRE(gid)
    database.tag.parents.comment = "Tags boven de tag"
    database.tag.children.comment = "Tags onder de tag"
    database.tag.description.comment = "Wanneer is deze tag van toepassing?"
    database.tag.meta_tags.comment = "Wat voor soort tag is dit?"

    # def represent_tag_list(tags, row):
    #     return (
    #         DIV(
    #             DIV(
    #                 UL(
    #                     *[
    #                         LI(A(Tag(tag).name, _href=URL(vars=dict(gid=tag))))
    #                         for tag in tags
    #                     ]
    #                 )
    #             ),
    #         )
    #         if tags
    #         else "geen."
    #     )

    database.tag.parents.readable = False
    database.tag.meta_tags.readable = False
    database.tag.children.readable = False
    database.tag.related.readable = False

    database.tag.parents.writable = False
    database.tag.meta_tags.writable = False
    database.tag.children.writable = False
    database.tag.related.writable = False

    # database.tag.parents.represent = represent_tag_list
    # database.tag.meta_tags.represent = represent_tag_list
    # database.tag.children.represent = represent_tag_list
    details_form = SQLFORM(database.tag, tag.id)

    def validate_slug_is_unique(form):
        new_slug = slugify.slugify(form.vars.name)
        form.vars.slug = new_slug
        if (
            database(
                (database.tag.slug == new_slug) & (database.tag.id != tag.id)
            ).count()
            > 0
        ):
            form.errors.name = "Conflicteert met een bestaande slug."

    if details_form.process(onvalidation=validate_slug_is_unique).accepted:
        database.commit()
        redirect(URL(vars=dict(gid=tag_gid)))
    return dict(
        tag=tag,
        parents=database(database.tag.gid.belongs(tag.parents or [])).select(),
        children=database(database.tag.gid.belongs(tag.children or [])).select(),
        meta_tags=database(database.tag.gid.belongs(tag.meta_tags or [])).select(),
        related=database(database.tag.gid.belongs(tag.related or [])).select(),
        details_form=details_form,
        sortable_tags=sortable_tags,
    )


@auth.requires_membership("education_warehouse")
def questions():
    workbench_db.tag_question.question_id.writable = False
    return dict(
        grid=SQLFORM.smartgrid(
            workbench_db.question, linked_tables=["tag_question"], maxtextlength=60
        )
    )


@auth.requires_membership("education_warehouse")
def dod_rules():
    workbench_db.tag_dod_rule.dod_rule_id.writable = False
    return dict(
        grid=SQLFORM.smartgrid(
            workbench_db.dod_rule, linked_tables=["tag_dod_rule"], maxtextlength=60
        )
    )


@auth.requires_membership("education_warehouse")
def update_item_dod_rule():
    item_dod_rule_id = request.args[0]
    ticked = request.vars.ticked == "on"
    note = request.vars.note
    rec = workbench_db.item_dod_rule[item_dod_rule_id]
    rec.update_record(ticked=ticked, note=note)
    # return BEAUTIFY(request.vars)
    redirect(URL(f="edit", args=[rec.item_id]))


@auth.requires_membership("education_warehouse")
def item_dod_rules():
    item_id = request.args[0]
    idr = workbench_db.item_dod_rule
    query = idr.item_id == item_id
    query &= idr.deleted == False
    if not workbench_db(query).count():
        return "Geen. Koppel tags met regels."
    # idr.id.readable=False
    # idr.item_id.readable=False
    # idr.item_id.writable=False
    # idr.dod_rule_id.writable=False
    # idr.deleted.writable=False
    # idr.deleted.readable=False
    # grid = SQLFORM.grid(query,
    #                     fields=(idr.dod_rule_id, idr.ticked, idr.note, idr.last_changed_by, idr.mtime),
    #                     formname='itemdodrules',
    #                     args=request.args[:1],
    #                     searchable=False,
    #                     csv=False,
    #                     details=False,
    #                     deletable=False,
    #                     create=False,
    #                     maxtextlength=60
    #                     )
    # return dict(grid=grid)
    grid = None
    query &= idr.dod_rule_id == workbench_db.dod_rule.id
    rows = workbench_db(query).select()
    return locals()


@auth.requires_membership("education_warehouse")
def item_questions():
    item_id = request.args[0]
    q = workbench_db.question
    iq = workbench_db.item_question
    query = iq.item_id == item_id
    query &= iq.deleted == False
    query &= iq.question_id == q.id
    iq.question_id.writable = False
    iq.question_id.readable = False
    iq.item_id.readable = False
    iq.item_id.writable = False
    iq.id.readable = False
    iq.mtime.readable = False
    iq.last_changed_by.readable = False

    if workbench_db(query).count() == 0:
        return "Geen. Koppel tags met vragen."
    # grid = SQLFORM.grid(query,
    #                     fields=(q.name, q.question, iq.note, iq.last_changed_by , iq.mtime,),
    #                     formname='itemquestions',
    #                     field_id=iq.id,
    #                     args=request.args[:1],
    #                     searchable=False,
    #                     csv=False,
    #                     details=False,
    #                     deletable=False,
    #                     create=False,
    #                     maxtextlength=60
    #                     )
    # return dict(grid=grid)
    grid = None
    rows = workbench_db(query).select()

    @dataclass
    class form_and_details:
        form: SQLFORM
        question: Row
        item_question: Row
        rows: Rows

    question_details = []
    for row in rows.render():
        if row.question.answer_type == "short":
            workbench_db.item_question.note.widget = SQLFORM.widgets.string.widget
        else:
            workbench_db.item_question.note.widget = SQLFORM.widgets.text.widget
        form = SQLFORM(
            workbench_db.item_question,
            row.item_question.id,
            formname=f"iq-{row.item_question.id}",
            deletable=False,
        ).process()
        # voor de zekerheid committen, als we dit niet doen dan blijkt het dat de antwoorden op de vragen
        # niet goed opgeslagen worden.
        db.commit()
        # we willen alle submit knoppen verbergen om er als laatst één over te houden.
        form.element(_type="submit")["_class"] = "hide_submit"
        question_detail = form_and_details(form, row.question, row.item_question, row)
        question_details.append(question_detail)

    return locals()


@auth.requires_membership("education_warehouse")
def gen_template():
    item_id = request.args[0]
    item = workbench_db.item[item_id]
    q = workbench_db.question
    iq = workbench_db.item_question
    rows = workbench_db(
        (iq.item_id == item_id) & (q.id == iq.question_id) & (iq.deleted == False)
    ).select()
    answer_per_question = {
        row.question.name.strip().strip("?"): row.item_question.note for row in rows
    }
    # return BEAUTIFY(answer_per_question)
    import textwrap

    md = [
        f"# {item.title}",
        f"Bij {item.contact_id.org} in {item.contact_id.location} wordt sinds {answer_per_question.get('Sinds wanneer')} "
        f"gewerkt met {answer_per_question.get('Kern van de praktijk')} om {answer_per_question.get('Aanleiding')}. ",
    ]
    for row in rows:
        def nice_paragraph(note):
            return textwrap.indent(textwrap.dedent(note or ""), "> ")

        md.append(f"## {row.question.question}")
        md.append(f"{nice_paragraph(row.item_question.note)}")
        md.append("")
        md.append("")
    return HTML(PRE("\n".join(md)))


@auth.requires_membership("education_warehouse")
def contacts():
    grid = SQLFORM.smartgrid(workbench_db.contact, csv=False, advanced_search=False)
    return dict(grid=grid)


@auth.requires_membership("education_warehouse")
def apply_to_all():
    workbench_db.apply_to_all_items.id.readable = False
    form = SQLFORM(
        workbench_db.apply_to_all_items,
        workbench_db.apply_to_all_items[1],
        create=False,
        deleteable=False,
    ).process()
    return dict(form=form)


auth.settings.allow_basic_login = True


@service.xmlrpc
def test(a, b, c):
    seen = "Gezien {a},{b} an {c}".format(a=a, b=b, c=c)
    return locals()


@service.xmlrpc
def list_contacts():  # NO_TEST_REDIRECT_ON
    # somehow this still returns empty bytes, even though it's a xmlrpc request... quite odd.
    return workbench_db(workbench_db.contact).select().as_list()


@service.xmlrpc
def list_items(*columns):
    if columns:
        columns = [workbench_db.item[c] for c in columns]
    return workbench_db(workbench_db.item).select(*columns).as_list()


@service.xmlrpc
def delete_item(id):
    removed_record = workbench_db.item[id].as_dict()
    del workbench_db.item[id]
    workbench_db.commit()
    return removed_record


@service.xmlrpc
def create_source_file(item_id, name, binary, original_uri):
    # binary must be  type xmlrpc.client.Binary()
    import io

    source_file = workbench_db.source_file  # table
    attachment = source_file.attachment  # field
    result = source_file.validate_and_insert(
        item_id=item_id,
        name=name,
        original_uri=original_uri,
        added_by=auth.user_id,
        attachment=attachment.store(io.BytesIO(binary.data), name),
    )
    if result.errors:
        return result
    d = source_file[result.id].as_dict()
    del d["attachment"]
    return d


@service.xmlrpc
def read_item(id):
    item = workbench_db.item[id]
    d = item.as_dict()
    d["source_files"] = item.source_file.select(
        workbench_db.source_file.id, workbench_db.source_file.name
    ).as_list()
    d["tags"] = item.item_tag.select(workbench_db.item_tag.tag_gid).as_list()
    return d


@service.xmlrpc
def update_contact(id, name=None, email=None, org=None, location=None):
    # verwerk alle argumenten in een dictionary met waarden die geupdate
    # moeten worden. Verwerk None als 'geen update', en "None" als string
    # als teken om None toe te kennen. Elk andre waarde wordt letterlijk overgenomen
    update_with = {}
    for argument in ("name", "email", "org", "location"):
        value = locals()[argument]
        if value is not None:
            update_with[argument] = None if value == "None" else value

    workbench_db.contact[id].update_record(**update_with)
    workbench_db.commit()
    return workbench_db.contact[id].as_dict()


@service.xmlrpc
def create_contact(name, email, org, location):
    return dict(
        id=workbench_db.contact.validate_and_insert(
            email=email, name=name, org=org, location=location
        )
    )


@service.xmlrpc
def create_item(contact_id, title, raw, klad, ori_uri, usability, live_gid=None):
    result = workbench_db.item.validate_and_insert(
        contact_id=contact_id,
        title=title,
        raw_text=raw,
        klad=klad,
        ori_uri=ori_uri,
        live_gid=live_gid,
        usability=usability,
    )
    if result.errors:
        return result
    add_comment("item", result.id, f"Import.")
    workbench_db.commit()
    return workbench_db.item[result.id].as_dict()


@auth.requires_membership("education_warehouse")
def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

# def demo():
#     # return response.json(asdict(backend.pratices(search=request.vars.q)))
#     return response.json(
#         asdict(
#             backend.pratices(search=request.vars.q),
#             value_serializer=serialize_backend_types,
#             filter=filter_backend_types,
#         ),
#         indent=2,
#     )
