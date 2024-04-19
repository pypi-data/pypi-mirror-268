import json
import os
import typing
import uuid
from datetime import datetime
from urllib import parse as urlparse

import user_agents
import yatl
from pydal.objects import Row
from pydal.tools.tags import Tags
from pydal.validators import IS_EMAIL, ValidationError
from yatl import XML

from py4web import HTTP, URL, action, redirect, request, response
from py4web.core import Fixture
from py4web.utils.grid import Grid

from .backend_support import backend
from .common import auth, cache
from .fixtures import LTSBaseTemplateSettings
from .markdown_template import MarkdownTemplate
from .models import _set_header
from .models_lts import (
    POSSIBLE_GROUPS,
    get_my_groups,
    groups,
    is_admin,
    lts_assets_db,
    lts_users_db,
    table_email_registration,
)
from .settings import APP_FOLDER

##### LTS SPECIFIC #####


def _to_bool(something: str | typing.Any, default: bool = False) -> bool:
    """
    Convert y/1/True etc. to True and false-ish values (n/0/False) to False.
    Useful for parsing user input.

    default: if the value does not look like either, which should it pick?
    """
    if isinstance(something, str) and something.isnumeric():
        # e.g. 1 and 0 -> True, False
        return bool(int(something))
    elif isinstance(something, str):
        # e.g. Yes, True, on -> True
        # Strings such as No, False, off -> False
        _lower = something.lower()
        # yes or true
        if default is False:
            return (
                _lower.startswith("y")  # yes
                or _lower.startswith("t")  # true
                or _lower == "on"  # html checkbox
            )
        elif default is True:
            return not (
                not _lower
                or _lower.startswith("n")  # no
                or _lower.startswith("f")  # false
                or _lower == "off"  # html checkbox
            )
        else:
            raise NotImplementedError("`default` can be either True or False.")
    else:
        # e.g. int 0 or simply bool false
        return bool(something)


def parse_query(url: str) -> dict[str, list[str] | str]:
    """
    Parse a query string like 'a=b&c=d' into a dictionary {'a': 'b', 'c': 'd'},
    ?a=b&a=c&d=e becomes {'a': ['b', 'c'], 'd': 'e'}
    """
    # parse entire URL
    parsed_url = urlparse.urlparse(url)
    # keep only the query (url search string) and parse that:
    parsed = urlparse.parse_qs(parsed_url.query)
    # parsed is now a dict with lists as values, e.g. {'a': ['b', 'c'], 'd': ['e']}
    # convert lists to strings if they only have one item, e.g. {'a': 'b', 'd': 'e'}:
    return {k: (v[0] if len(v) == 1 else v) for k, v in parsed.items()}


class LTSSettings(typing.TypedDict, total=False):
    # used in template:
    do_paginate: bool
    q: str
    page: int
    limit: int
    likes: str
    change_url: bool
    base_tags: str | XML  # converted from csv on input to JSON in template
    tags: str
    quickfilter: bool | str | dict
    searchbar: bool
    filters: bool | str
    menu_style: typing.Literal["modal", "default"] | str

    # can be passed but not used in template:
    search: str


@action("external_tiles/<version>", method=["POST"])
@action("simple_tiles", method=["POST"])
@action.uses("external_tiles.html")
def external_tiles(version=None):
    """
     demo van minimale versie van tiles (incl scoped design) voor externe partijen
    (zie cmsx/extern voor een demo van de html die de klant dan moet toevoegen)
    normaal is het een beetje ingewikkeld hoe je welke variabele moet meesturen aan POST tiles.
    Deze functie genereert die code op basis van de hx-vals en <input>'s die de klant invult

    Quickfilter kan verschillende soorten values krijgen:
    - disabled
    - default (zelfde balk als delen.meteddie
    - <str>: de naam van een quickfilter (zie de quickfilters functie (`def quick_filter`)
    - <obj>: een (JSON) object met key = label en value = gid (van de tag)
    """
    data: LTSSettings = {**request.forms}

    data["q"] = data.get("search", "") or data.get("q", "")
    data["page"] = data.get("page", 1)
    data["limit"] = data.get("limit", 3)
    data["likes"] = data.get("likes", "disabled")
    data["change_url"] = _to_bool(data.get("change_url", 1))
    # avoid name collision with helper:
    data["do_paginate"] = (
        _to_bool(data.pop("paginate")) if "paginate" in data else False
    )
    data["searchbar"] = _to_bool(data.get("searchbar", False))

    _filters = data.get("filters", "false")
    data["filters"] = (
        "with-active" if "active" in _filters else _to_bool(_filters, default=True)
    )

    data["menu_style"] = "modal" if "modal" in _filters else "default"

    # base tags in: "abc,def"
    # base tags out: ["abc", "def"]
    base_tags = [f"'{t}'" for t in data.get("base_tags", "").split(",") if t]
    data["base_tags"] = XML("[" + ",".join(base_tags) + "]")

    data["tags"] = data.get("tags", "")

    data["quickfilter"] = data.get("quickfilter", False)

    if (_qf := str(data["quickfilter"]).lower()) in ("yes", "true", "1", "enabled"):
        # quickfilter = True - show default
        data["quickfilter"] = True
    elif _qf in ("no", "false", "0", "disabled"):
        # quickfilter = False - hide
        data["quickfilter"] = False
    elif _qf.strip().startswith(("{", "[")):
        # object -> custom quickfilter buttons
        # let op: _qf is nu welicht [object Object] omdat htmx het zo opstuurt bij een application/x-www-form-urlencoded
        # Dit komt wel weer goed bij de echte requests (/quick-filter, /tiles), omdat die application/json krijgen.
        # Ik heb geprobeerd in de htmx pre-request code dit Object te JSON-encoden, maar dat gaat mis bij andere
        # requests, omdat op dit punt de content-type niet (reliably) te checken is. Voor nu werkt dit dus goed genoeg,
        # maar houd er rekening mee dat de quick-filter informatie binnen deze functie dus niet te achterhalen valt!
        data["quickfilter"] = "custom"
    # else: specific quickfilter chosen by name

    return data


@action("docs")
@action("documentatie")
@action("documentation")
@action.uses(MarkdownTemplate("documentatie.md"))
def documentatie():
    """
    Show the markdown with custom css
    """
    css = """
    h1 {border: 0; margin-bottom: 0}
    h2 {margin-top: 0}
    """
    return dict(css=css)


@action("email_registration_form")
@action.uses("email_registration_form.html")
def email_registration_form():
    """
    Show the form
    """
    return {**request.query}


def notify_eddie(email, event):
    """
    Send an email to the shared inbox
    """
    auth.sender.send(
        to=[os.environ.get("LTS_EMAIL_NOTIFICATION_RECEIVER")],
        subject="LTS subscribers",
        body=f"{email} {event}",
        sender=os.environ.get("LTS_EMAIL_NOTIFICATION_SENDER"),
    )


def _subscribe(form):
    """ """
    db = lts_users_db

    email = form.email
    pagina = form.pagina
    versievoorkeur = form.versievoorkeur

    if not email:
        return False, "Geen emailadres ingevuld"

    if not versievoorkeur:
        return False, "Geen versie voorkeur gekozen"

    try:
        IS_EMAIL().validate(email)
    except ValidationError:
        return False, "Geen geldig emailadres ingevuld"

    if db(db.email_registration.email == email).count():
        return False, "Emailadres is al geregistreerd"

    db.email_registration.insert(
        email=email,
        pagina=pagina,
        voorkeur=versievoorkeur,
        subscribed_at=datetime.now(),
        unsubscribe_code=str(uuid.uuid4()),
    )

    try:
        notify_eddie(email, "registered")
    except Exception:
        # kan gebeuren, zou niet motten.
        pass

    return True, "Emailadres succesvol geregistreerd"


@action("email_subscribe", method=["POST"])
@action.uses(lts_users_db)
def subscribe():
    """
    Endpoint to add user to maillist
    """
    back = request.environ["HTTP_REFERER"].split("?")[0]

    success, message = _subscribe(request.forms)
    success = "1" if success else ""
    back += f"?success={success}&msg={message}"
    back += "#email-form"

    return redirect(back)


@action("email_unsubscribe")
@action.uses(lts_users_db)
def unsubscribe():
    """
    Endpoint to remove user from maillist
    """
    db = lts_users_db

    email = request.query.get("email")
    code = request.query.get("code")

    query = (db.email_registration.email == email) & (
        db.email_registration.unsubscribe_code == code
    )
    registration = db(query).select().first()

    if not registration:
        # raise HTTP(404, "Combinatie email en beveiligingscode niet gevonden.")
        response.status = 404
        return "Combinatie email en beveiligingscode niet gevonden."

    db(query).delete()

    notify_eddie(email, "unsubscribed")

    return "Registratie verwijderd"


# @action("dev_debug")
# @action.uses(db)
# def dev_debug():
#     before = str(
#         db(db.email_registration.id > 0).select().as_list()
#     )
#
#     # db.email_registration.truncate()
#
#     return before


@cache.memoize(expiration=999999999)
def _cache_cdn(filetype: str, version: str) -> Row:
    """
    Retrieves the specified type of static file from the assets database

    Arguments:
        filetype: js or css
        version: major.minor.patch
    """
    db = lts_assets_db

    # css - 3.0 -> bundled-3.0.1.css
    # https://fragments.robin.edwh.nl/lts/cdn/3.0/js/bundle.min.js
    table = db.bundle_version

    query = table.filetype == filetype

    version_triplet = version.split(".")

    if version_triplet:
        query &= table.major == version_triplet.pop(0)
    if version_triplet:
        query &= table.minor == version_triplet.pop(0)
    if version_triplet:
        query &= table.patch == version_triplet.pop(0)

    file = db(query).select(orderby=[~table.major, ~table.minor, ~table.patch]).first()

    if not file:
        raise HTTP(404, "File Version not Found")

    return file


@action("cdn/<versie>/<filetype>/<filename>")
@action.uses(lts_assets_db)
def cdn(versie, filetype, filename):
    """
    Since headers can't be cached, DON'T use @cache.memoize on this action
    """
    file = _cache_cdn(filetype, versie)

    file_name_base = (
        "-".join(file.filename.split("-")[:-1]) if file.filename else filename
    )
    _set_header(
        "Content-Disposition", f'attachment; filename="{file_name_base}.{filetype}"'
    )
    _set_header("Content-Type", f"text/{filetype}")
    return file.contents


class DenyBotsFixture(Fixture):
    """
    Using the user_agents library,
    block (self-identified) scraping bots from the route.
    """

    def on_request(self, context):
        headers = {**request.headers}
        ua = user_agents.parse(headers["User-Agent"])
        # print("catch |", headers["User-Agent"])
        if ua.is_bot:
            raise HTTP(403, "User Agent indicates this client is a bot.")


deny_bots = DenyBotsFixture()


class GridActionButton:
    """
    Custom action button for in the Grid
    """

    # https://py4web.com/_documentation/static/en/chapter-14.html#sample-action-button-class
    def __init__(
        self,
        url,
        text=None,
        icon=None,
        onclick=None,
        additional_classes: list = None,
        message="",
        append_id=False,
        ignore_attribute_plugin=False,
        **attrs,
    ):
        self.url = url
        self.text = text
        self.icon = icon
        self.onclick = onclick
        self.additional_classes = additional_classes
        self.message = message
        self.append_id = append_id
        self.ignore_attribute_plugin = ignore_attribute_plugin
        self.attrs = attrs


@action("changelog")
@action.uses(MarkdownTemplate("changelog.md"))
def changelog():
    """
    Show the static changelog page
    (actual changelogs are loaded in with htmx)
    """
    return {}


@action("changelog/<filetype>")
@action.uses(lts_assets_db, deny_bots)
def changelog_per_type(filetype: str):
    """
    Load the changelog for a specific file type (js or css)
    """
    db = lts_assets_db

    table = db.bundle_version
    query = db(table.filetype == filetype).select(
        orderby=[~table.major, ~table.minor, ~table.patch]
    )
    log = ""

    for row in query:
        log += f"<h3>{row.version}</h3><p>{row.changelog or '-'}</p>"

    return log


@action("manage")
@action.uses("lts/manage.html")
@action.uses(auth.user, deny_bots)
def manage():
    """
    Show the (static) manage overview,
    containing two buttons
    """
    my_groups = get_my_groups()
    return {"is_admin": "admin" in my_groups}


@action("manage_maillist")
@action("manage_maillist/<path:path>", method=["GET", "POST"])
@action.uses("lts/manage_grid.html")
@action.uses(auth.user, lts_users_db, deny_bots, is_admin)
def manage_maillist(path=""):
    """
    Show the grid to manage maillist users
    """
    grid = Grid(path, query=(table_email_registration.id > 0))

    return {"grid": grid.render(), "missing": []}


@action("manage_versions")
@action("manage_versions/<path:path>", method=["GET", "POST", "DELETE"])
@action.uses("lts/manage_grid.html")
@action.uses(auth.user, lts_assets_db, deny_bots, is_admin)
def manage_versions(path=""):
    """
    Show the grid to manage static file versions
    """
    db = lts_assets_db
    table = db.bundle_version

    # https://github.com/web2py/py4web/blob/master/py4web/core.py#L769
    # lijkt niet meer nodig omdat het nu gewoon een app is ipv eigen docker met traefik routing
    # request.environ['SCRIPT_NAME'] = '/lts'

    if not path:
        # only show on home page, not on edit/new screen
        missing_changelog = db(
            (table.changelog == None) | (table.changelog == "")
        ).select()
    else:
        missing_changelog = []

    grid = Grid(
        path,
        query=(table.id > 0),
        orderby=[~table.major, ~table.minor, ~table.patch],
        details=False,
        post_action_buttons=[
            lambda row: GridActionButton(
                lambda row: URL(
                    "cdn", row.version, row.filetype, row.filename, scheme="https"
                ),
                text=f"Download {row.version}",
                _target="blank",
            ),
            lambda row: GridActionButton(
                lambda row: URL(
                    "demo", row.version, row.filetype, row.filename, scheme="https"
                ),
                text=f"Demo v{row.version}",
                additional_classes=["btn-secondary"],
                _target="blank",
            ),
        ],
    )

    grid.endpoint = grid.endpoint.rstrip("/")

    return dict(grid=grid.render(), missing=missing_changelog)


@action("manage_users")
@action("manage_users/<path:path>", method=["GET", "POST", "DELETE"])
@action.uses("lts/manage_grid.html")
@action.uses(auth.user, lts_users_db, deny_bots, is_admin)
def manage_users(path=""):
    db = lts_users_db

    db.auth_user.password.readable = False
    db.auth_user.password.writable = True

    grid = Grid(
        path,
        query=db.auth_user.id > 0,
        post_action_buttons=[
            lambda row: GridActionButton(
                lambda row: URL("manage_groups", row.id),
                text=f"Manage groups",
            ),
        ],
    )
    return dict(grid=grid)


@action("manage_groups/<user_id:int>", method=["GET", "POST"])
@action.uses("lts/manage_groups.html")
@action.uses(auth.user, lts_users_db, deny_bots, is_admin)
def manage_groups(user_id):
    db = lts_users_db
    user = db.auth_user(id=user_id)
    if not user:
        raise HTTP(404, "User Not Found")

    message = None
    if request.method == "POST":
        data = {**request.forms}
        for group in POSSIBLE_GROUPS:
            if data.get(group) == "on":
                groups.add(user_id, group)
            else:
                groups.remove(user_id, group)
        message = "Groepen aangepast!"

    their_groups = groups.get(user_id)
    return dict(
        user=user, their=set(their_groups), possible=POSSIBLE_GROUPS, message=message
    )


@action("versions")
@action("versions/<path:path>", method=["GET"])
@action.uses("lts/manage_grid.html", lts_assets_db)
@action.uses(lts_assets_db, deny_bots)
def see_versions(path=""):
    """
    read-only versie van manage_versions,
    wel voor publiek, met button naar demo page per versie
    """
    db = lts_assets_db
    table = db.bundle_version

    grid = Grid(
        path,
        query=(table.id > 0),
        orderby=[~table.major, ~table.minor, ~table.patch],
        details=False,
        create=False,
        deletable=False,
        editable=False,
        post_action_buttons=[
            lambda row: GridActionButton(
                lambda row: URL(
                    "cdn", row.version, row.filetype, row.filename, scheme="https"
                ),
                text=f"Download {row.version}",
                _target="blank",
            ),
            lambda row: GridActionButton(
                lambda row: URL(
                    "demo", row.version, row.filetype, row.filename, scheme="https"
                ),
                text=f"Demo v{row.version}",
                additional_classes=["btn-secondary"],
                _target="blank",
            ),
        ],
    )

    grid.endpoint = grid.endpoint.rstrip("/")

    return dict(grid=grid.render(), missing=[])


@action("builder")
@action("builder/1")
@action.uses("lts/builder_1.html", deny_bots, auth.user)
def lts_builder_step1():
    return {"version": 1}


@action("builder/2", method=["POST", "GET"])
@action.uses("lts/builder_2.html", deny_bots, auth.user)
def lts_builder_step2():
    # e.g.
    # https://delen.meteddie.nl/?qf=3ce22256-df83-42f1-a8f8-34621066693e&page=1&tags=%5B%224cc54bf2-b7c8-415d-8938-7a47d9207439%22%2C%226925fc99-1dfb-47d1-99f5-6c4c3484103b%22%2C%223ce22256-df83-42f1-a8f8-34621066693e%22%5D&q=search
    prefill = {
        "paginate": True,
        "limit": 3,
        "likes": "disabled",
        "quickfilter": False,
        "change_url": False,
    }
    if url := request.forms.get("URL"):
        query = parse_query(url)

        tags = query.get("tags", [])
        if isinstance(tags, str):
            try:
                tags = json.loads(tags)
            except json.JSONDecodeError:
                # not json, try csv
                tags = tags.split(",")

        prefill["base_tags"] = tags

        prefill["search"] = query.get("q", None)

    return dict(prefill=prefill, version="1")


HOSTINGDOMAIN = os.getenv("HOSTINGDOMAIN")


@action("builder/3", method=["POST"])
@action.uses("lts/builder_3.html", deny_bots, auth.user)
def lts_builder_step3():
    data = {**request.forms}

    # html checkboxes sturen helemaal niks op als hij niet checked is, dus voegt dat nog toe:
    if not data.get("paginate"):
        data["paginate"] = "off"

    if not data.get("change_url"):
        data["change_url"] = "off"

    if qf := data.get("quickfilter"):
        try:
            obj = json.loads(qf)
            data["quickfilter"] = obj
        except json.JSONDecodeError:
            # don't alter qf
            pass

    lts_base_url = f"https://fragments.{HOSTINGDOMAIN}/lts/"

    ctx = {
        "data": XML(json.dumps(data, indent=16)),
        "FRONT_END_BASE": lts_base_url,
        "CDN_URL": f"{lts_base_url}cdn/1",
        "URL": URL,
    }

    with open(f"{APP_FOLDER}/templates/lts/demo_template.html") as f:
        code = yatl.render(stream=f, context=ctx, delimiters="[[ ]]")

    return {"code": code, "version": 1}


@action("tag_finder")
@action.uses("lts/builder_tags.html", backend, LTSBaseTemplateSettings, auth.user)
def tag_finder():
    default_tags = ["8b78e33d-c4ab-442e-aaf6-411fda089b03"]  # default
    tags = backend.filter_tags(default_tags, {})[0]

    tags = {
        parent["id"]: {
            "name": parent["name"],
            # only include two levels!
            "children": {child["id"]: child["name"] for child in parent["children"]},
        }
        for parent in tags
    }

    return {
        "tags": tags,
        "style": request.query.get("output_style"),
        # output_target?
    }


@action("demo/<path:path>")
@action.uses("lts/demo.html")
@action.uses(deny_bots)
def demo(path):
    """
    Demo page voor een specifieke versie van de static files.
    """
    version, *_ = path.split("/")

    return dict(version=version)


# invoke bundle.build -> only generate bundled files
# invoke bundle.publish -v <versie>
# invoke bundle.publish --patch
# invoke bundle.publish -> prompt versie
