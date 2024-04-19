"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""
import datetime
import json
import os
import typing
import uuid
import warnings
from typing import Callable

import attr
import edwh.core.backend
import yatl
from edwh.core.backend import NotFoundException, ValidationCode, edwh_asdict
from edwh.core.backend.ntfy_sh import warning
from edwh.core.data_model import (
    DEFAULT_EXCLUDED_VISIBILITY,
    DEFAULT_INCLUDED_VISIBILITY,
    Visibility,
)
from edwh.core.pgcache import Magic
from py4web_debug import is_debug, tools
from pydal.objects import Query
from yatl import SPAN
from ycecream import y

from py4web import HTTP, URL, redirect, request, response

from .backend_support import (
    BACKEND_ME,
    Item,
    OrganisationWithItems,
    SecurityException,
    backend,
)
from .common import auth, db, flash, leidendb, session
from .common_lts import action  # DIFFERENT ACTION !!!
from .fixtures import LTSBaseTemplateSettings as BaseTemplateSettings
from .fixtures import TilesHelpers
from .handlebars import Handlebars, handlebars_helpers
from .helpers import DotMap, b64decode
from .hotspots import get_hotspots
from .models import _calculate_star_average, plaatsen, redirect_temporary
from .settings import APP_FOLDER
from .tasks import log_once

if IS_DEBUG := is_debug():
    tools.enable(db, enabled=True, debugbar_enabled=False)

y.configure(
    enabled=os.getenv("ENABLE_ICECREAM"),
)


# component
@action("tiles", method=["GET", "POST"])
# @action("tiles/", method=["GET", "POST"])
@action("tiles/org/<org_gid>", method=["GET", "POST"])
@action.uses(
    "tiles.html",
    session,
    backend,
    TilesHelpers,
    BaseTemplateSettings,
)
def tiles(org_gid=None, **internal_settings):
    """
    :param org_gid:
    :param internal_settings: bedoeld om een remote request te kunnen simuleren tbv school_praktijkoverzicht
    :return:
    """

    settings = internal_settings or request.settings
    limit = settings.get("limit")
    offset = limit * (settings.get("page", 1) - 1)

    tags = settings.get("tags") or []
    if org_gid:
        if isinstance(org_gid, (str, uuid.UUID)):
            org = backend.organisation(org_gid)
        elif isinstance(org_gid, OrganisationWithItems):
            org = org_gid
        else:
            raise ValueError(f"Uknown type {type(org_gid)} for tiles, value: {org_gid}")
        if org and org.item_tag:
            tags.append(org.item_tag.id)
        else:
            raise NotFoundException("Organisation not found.")
    if org_gid and hasattr(org, "items"):
        tiles = backend.search_result_from_gid_list(
            org.items.found, available=org.items.available
        )
    else:
        include = request.settings.get("include", DEFAULT_INCLUDED_VISIBILITY)
        exclude = request.settings.get("exclude", DEFAULT_EXCLUDED_VISIBILITY)
        tiles = backend.tiles(
            search=settings.get("q") or "",
            tags=tags,
            order=settings.get("order") or "RECENT_DESC",
            limit=limit,
            offset=offset,
            author=settings.get("author") or None,
            include=include,
            exclude=exclude,
        )
        backend.applog.search(
            search=settings.get("q") or "",
            tags=tags,
            author=settings.get("author", None) or None,
            found_tiles_cnt=tiles.available,
            found_tiles_gids=[tile.id for tile in tiles.found],
            limit=tiles.first,
            offset=tiles.offset,
            order=settings.get("order") or "RECENT_DESC",
            loggedIn=backend.is_registered_user,
            include=include,
            exclude=exclude,
        )
    if internal_settings and internal_settings.get("return_none_when_no_tiles"):
        print("test tiles found:", tiles.available, bool(tiles.available))
        if not tiles.available:
            return None

    return {
        "tiles": tiles,
        "thumbnail": backend.thumbnail_url,
        "anonymous": backend.is_anonymous,
    }


@action("index")
@action.uses(session, flash, backend)
def component_loader():
    # LTS specific
    if auth.get_user():
        return redirect_temporary("/lts/manage")
    else:
        return redirect_temporary("/lts/docs")


@action("eat_cookies")
@action.uses(session)
def eat_cookies():
    # wipe cookie and start over
    session.clear()
    redirect(URL("index"))


@attr.define
class QuickFilter:
    label: str
    tag: typing.Optional[str | list[str]]

    def __attrs_post_init__(self):
        if isinstance(self.tag, list):
            # convert list of UUIDs to a semicolon-separated string
            self.tag = ";".join(self.tag)


@action("quick-filter", method=["GET", "POST"])
@action("quick-filter/<groupname>", method=["GET", "POST"])
@action.uses(
    "quick_filter.html",
    session,
    backend,
    TilesHelpers,
    BaseTemplateSettings,
)
def quick_filter(groupname="default"):
    filter_group = DotMap(
        default=[
            QuickFilter(label=tag.name, tag=str(tag.id))
            for tag in backend.quick_filter_tags()
        ],
        iol=[
            QuickFilter(
                label="Voor Gebruikers", tag=["3f72ffb6-f180-4add-abb3-b1277b4e636a"]
            ),
            QuickFilter(
                label="Voor Makers",
                tag=[
                    "955448e0-d013-4a8b-81c0-c1c691fd61ea",
                    "330cadce-c040-4c33-b4b1-9b49ab3d3b9c",
                ],
            ),
            QuickFilter(
                label="Voor Scholen",
                tag=[
                    "cecac4fe-a868-49c7-8620-17d6cd01c3af",
                    "52f1e6b8-0c49-4d5b-8374-9a14baa6f508",
                ],
            ),
        ],
        zoetermeer=[
            QuickFilter(
                label="Burgerschap en Toekomst",
                tag=[
                    "df8c43bc-2a9a-4122-a13b-d939b26fa4cd",
                    "b421596a-3da9-48ff-b541-224cb3173b9f",
                    "39e0afe2-37d7-4bee-a655-c9b1e5b85e9c",
                ],
            ),
            QuickFilter(
                label="Diversiteit en Inclusie",
                tag=[
                    "f8c62e24-bbe4-44bd-bc02-ae12db371a03",
                    "ed11c63a-48ab-4fef-b9c9-42bf5b972612",
                ],
            ),
            QuickFilter(
                label="Taal en rekenen",
                tag=[
                    "5df7e34c-2ad6-4b78-8538-d1d3932e6d28",
                    "b696b4da-1e46-4bdc-be46-292d205e9a6a",
                    "b94ee984-5e80-4097-b357-752f2ea7b282",
                    "2411b353-d5f9-42c3-9f74-2635296207fd",
                    "82a1dff7-8850-4207-8f50-335929229a03",
                    "fefba7ec-e347-4062-9795-b5f8cd2c47ed",
                    "94ad5f15-8358-48c1-8c3f-bfbb93b98c3f",
                    "66dbb90c-3e98-44e2-9c9d-a4d0f19697c8",
                    "88d57db3-070d-480f-8eaf-9f625265f66e",
                ],
            ),
            QuickFilter(
                label="Kunst en cultuur",
                tag=[
                    "c7930f0f-f61b-49bc-bd0b-8ff74cfd0c79",
                    "5de752ac-04a5-46fd-b624-8b373720b8e2",
                ],
            ),
            QuickFilter(
                label="Wetenschap en techniek",
                tag=[
                    "09c2d825-c600-40f1-8296-09a86168290e",
                    "3479b7bf-97e7-450f-bf97-2047eb550f1d",
                    "2236f08f-e5a0-4c0b-9a5e-f73dfcf71c4c",
                    "4210c000-d376-4adf-9aae-99976c84717d",
                    "55300815-a697-4d17-afe7-500d520db3a8",
                    "e54bde1c-f19e-4bc5-97d7-c8112102675e",
                    "07df9e97-2c9d-457d-bd35-65a107dbc66d",
                    "15e62476-23d4-404e-aa8a-a6386d0c6ec8",
                    "4b3cbe42-422a-4d83-aa99-e34794c518e6",
                ],
            ),
            QuickFilter(
                label="Sport en gezondheid",
                tag=[
                    "d9c62794-f8e9-41fa-86d2-89709c17b4cb",
                    "5a2fbf9a-cdcc-4302-b798-e8d2c2548159",
                    "471a920d-7a44-4524-bfd0-46d45b00350b",
                    "8f750d7d-887b-4cde-9598-f046aac70e41",
                    "906f763a-c563-4f0f-8bd9-77db5691ceec",
                    "b9f65f79-9363-4f12-8987-496e5b7c97d3",
                ],
            ),
            QuickFilter(
                label="Natuur en duurzaamheid",
                tag=[
                    "a89f45b8-61d2-44f0-bdca-0d2fa3313569",
                    "07f7c1b5-ac52-4c87-92a5-edcbb102a8af",
                    "6c16ad99-056c-4b6b-8be9-322579c67ce4",
                ],
            ),
            QuickFilter(
                label="21e eeuwse vaardigheden",
                tag=["539632c3-4601-4479-8349-2ba527bbe817"],
            ),
            QuickFilter(
                label="Anders organiseren en samenwerken",
                tag=[
                    "bf2f7ada-b750-4d0b-880a-80cc27c650fc",
                    "7afe35b0-881b-41bf-88ec-7e1d3fc774e3",
                    "0fadb1b8-16a4-4580-b1d7-b0822bd842f0",
                    "909c5cdc-2284-4fdf-a253-755a3565bb70",
                    "01f5ed8c-907b-4f35-b3b9-b2b387e2e2c4",
                    "0b2e65d8-89bd-4f93-830e-04c552d148eb",
                    "334747a3-987b-4272-a18f-0ba07a7c8baa",
                    "15120f72-db0c-483f-bc48-5f933a650a6d",
                    "01f5ed8c-907b-4f35-b3b9-b2b387e2e2c4",
                    "0c5008d0-86fb-4c42-bd7a-ff81c8e96bd9",
                    "bce22921-67fb-4739-959e-bc5919c05965",
                    "4af68055-55d5-42ee-9ca0-1e9d6368e097",
                    "aac593a5-95a4-4c2e-b150-7405b7411221",
                    "a3c9d25b-7b5f-4edf-8dbe-c79aa1655f8d",
                    "54b0f0ca-5edc-4e6c-ae55-6be94316ab3a",
                ],
            ),
            QuickFilter(
                label="Professionalisering",
                tag=[
                    "bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7",
                    "54b0f0ca-5edc-4e6c-ae55-6be94316ab3a",
                ],
            ),
            QuickFilter(
                label="Ouderbetrokkenheid en opvoeding",
                tag=[
                    "c914f8b6-fefd-4358-a15e-7e561af3ebf9",
                    "aac86a8c-ebf6-452f-b213-283e2bf3cf91",
                    "d9525a90-9ad6-416b-bd90-3cbceaef7e93",
                ],
            ),
        ],
        gelijkekansenindeklas=[
            QuickFilter(
                label="Kansengelijkheid", tag="36ee028a-6bbe-4e92-85b7-f3fffc512cdd"
            ),
            QuickFilter(
                label="burgerschap", tag="39e0afe2-37d7-4bee-a655-c9b1e5b85e9c"
            ),
            QuickFilter(
                label="ouderbetrokkenheid", tag="c914f8b6-fefd-4358-a15e-7e561af3ebf9"
            ),
            QuickFilter(
                label="taalvaardigheid", tag="2411b353-d5f9-42c3-9f74-2635296207fd"
            ),
            QuickFilter(label="identiteit", tag="bcecf476-9787-4897-a656-5d6b1a45ac96"),
            QuickFilter(label="Armoede", tag="186e7169-47d0-46ef-b1bc-62d8dd6afb8b"),
            QuickFilter(
                label="Cultureel en sociaal kapitaal",
                tag="43130c0c-ff6e-4c8d-b826-dfaca33d2f00",
            ),
            QuickFilter(
                label="Verwachtingen", tag="89742fec-0a7b-4705-9db5-5c4098a2ba2d"
            ),
            QuickFilter(
                label="Prestatiedruk", tag="8a10dd37-d780-4b08-9030-e5653daee092"
            ),
        ],
        slimfit=[
            QuickFilter(
                label="Algemene visie en organisatie",
                tag="c85461ed-d24e-4a0c-912d-8eca4f68293e",
            ),
            QuickFilter(label="Personeel", tag="146214d3-6091-4aff-bfdf-3f50d41d2e8a"),
            QuickFilter(
                label="Leeromgeving", tag="684af7bc-9db2-4f1d-b66f-04e307f39809"
            ),
            QuickFilter(label="Leerinhoud", tag="4225d914-d4c8-4f89-85c5-11e26f853afa"),
            QuickFilter(
                label="ICT ontwikkeling", tag="cfebbbba-61ce-41de-b8a8-536e84143363"
            ),
            QuickFilter(
                label="Het volgen van leerlingen",
                tag="3ce22256-df83-42f1-a8f8-34621066693e",
            ),
            QuickFilter(
                label="Differentiatie", tag="82c567e7-0ee5-442b-b9c6-289447f5ec4d"
            ),
            QuickFilter(
                label="Professionele leergemeenschap / leiderschap / cultuur",
                tag="03cfa524-c04b-478e-845c-ce29ac009612",
            ),
            QuickFilter(
                label="School en samenleving",
                tag="e70d6a29-b026-4664-9ae0-7673c94af664",
            ),
        ],
        sterkmetschoolkracht=[
            QuickFilter(
                label="Onderwijskwaliteit", tag="ec3cf551-3e5c-4ba2-9518-171c39ff3776"
            ),
            # QuickFilter(label="Lerarentekort",tag="ea1b9d7e-3763-4f0c-8afb-649a391a01f3"),
            # QuickFilter(label="Schoolleiderstekort",tag="0d968ee8-a67d-4cc0-9912-286a45edbc03"),
            QuickFilter(
                label="Kansen(on)gelijkheid", tag="36ee028a-6bbe-4e92-85b7-f3fffc512cdd"
            ),
            QuickFilter(
                label="Digitalisering", tag="07df9e97-2c9d-457d-bd35-65a107dbc66d"
            ),
        ],
        testing=[
            QuickFilter(
                label="niet bestaand 1", tag="0fc58d00-d187-4fd5-adbd-3980f901f2a9"
            ),
            QuickFilter(
                label="niet bestaand 2", tag="60107ed0-50ad-451b-971c-6d583832471a"
            ),
        ],
        leiden_en_omgeving=[
            QuickFilter(
                label="Duurzaamheid", tag="6c16ad99-056c-4b6b-8be9-322579c67ce4"
            ),
            QuickFilter(
                label="Rijke Leeromgeving", tag="c899b309-72c3-40e1-a691-682a99e584cb"
            ),
            QuickFilter(
                label="Talentontwikkeling", tag="e34d60fd-61f1-4e2a-8a6d-8391a7f0cbb8"
            ),
            QuickFilter(
                label="Digitale Geletterdheid",
                tag="4b3cbe42-422a-4d83-aa99-e34794c518e6",
            ),
            QuickFilter(
                label="Onderzoeken", tag="2236f08f-e5a0-4c0b-9a5e-f73dfcf71c4c"
            ),
        ],
        oekraine=[
            QuickFilter(
                label="Vluchtelingen", tag="bbada696-fae5-48d0-9147-218412bdf81e"
            ),
            QuickFilter(
                label="Vluchtelingen", tag="bbada696-fae5-48d0-9147-218412bdf81e"
            ),
            QuickFilter(
                label="Kansengelijkheid", tag="36ee028a-6bbe-4e92-85b7-f3fffc512cdd"
            ),
            QuickFilter(
                label="School en samenleving",
                tag="e70d6a29-b026-4664-9ae0-7673c94af664",
            ),
        ],
    )

    qf: list[QuickFilter]

    if groupname == "custom" and (qfs := request.json["quickfilter"]):
        if isinstance(qfs, str):
            # probably json
            qfs = json.loads(qfs)

        qf = [QuickFilter(label=label, tag=tag) for tag, label in qfs.items()]
    else:
        qf = filter_group[groupname] or filter_group["default"]
        qf.insert(0, QuickFilter(label="Alles Tonen", tag=None))

    return {"filters": qf}


def _filter_partials() -> dict[str, str]:
    """
    Er zijn verschillende combinaties van filter componenten mogelijk (met/zonder active tags, normaal filter menu, modal filter menu).
    Deze functie geeft op bassi van de menu_style setting de juiste modal file paths terug die gebruikt worden in het template.
    """
    menu_style = request.settings["menu_style"]
    MENU_STYLES = {
        "modal": "filtermenu-modal.html",
        "default": "filtermenu.html",
    }

    filtermenu = MENU_STYLES.get(menu_style, MENU_STYLES["default"])

    return {"filtermenu": filtermenu, "filterbuttons": "filterbuttons.html"}


def _filter(tags: list[str]):
    """
    Return the available filters, optionally having some tags (currently ignored, I think),
    and other info required by the filter component (e.g. start_open from settings and the right icons)
    """
    state = {**(request.json or request.params or {})}

    tag_tree, tag_gids = backend.filter_tags(tags, request.settings)
    order_options = {
        "RECENT_DESC": "van Nieuw naar Oud",
        # "RECENT_ASC": "van Oud naar Niew",
        "POPULARITY_DESC": "Populariteit Aflopend",
        # "RANDOM": "Willekeurig",
        # "THUMBS_DESC": "Duimpjes Aflopend",
        # "THUMBS_ASC": "Duimpjes Oplopend",
        # "VIEWS_DESC": "Bekeken Aflopend",
        # "VIEWS_ASC": "Bekeken Oplopend",
    }

    order_options = [DotMap({"code": k, "label": v}) for k, v in order_options.items()]

    start_open = str(state.get("_start_open", "false")).lower() == "true"

    return {
        "filters": [
            DotMap(_) for _ in tag_tree
        ],  # fixme: Remco kan tag_tree ook niet een dict geven??
        "tag_gids": list(tag_gids),
        "order_options": order_options,
        "start_open": start_open,
        "icon_before": "fa-angle-up" if start_open else "fa-angle-down",
        "icon_after": "fa-angle-down" if start_open else "fa-angle-up",
        "partials": _filter_partials(),
        "menu_style": request.settings.get("menu_style", "default"),
    }


@action("filter", method=["GET", "POST"])
@action("filter/<tags:path>", method=["GET", "POST"])
@action.uses(
    "filter.html",
    session,
    backend,
    TilesHelpers,
    BaseTemplateSettings,
)
def filter(tags=["8b78e33d-c4ab-442e-aaf6-411fda089b03"]):
    return _filter(tags)


def _active_filters():
    """
    Get info (from the backend) about the selected tags (from settings);

    When the quick-filter is used with multiple gid per menu-item, the gids are separated by a semicolon in the received
    settings. Explodes these into a flat list of gids.
    """
    tag_gids = []
    for tag_input in request.settings.get("tags", []):
        if not tag_input:
            # ignore empty tags
            continue
        elif isinstance(tag_input, str):
            # explode on ;
            tag_gids.extend(tag_input.split(";"))
        else:
            # assume it's a list: explode each element in the list if possible
            for tag in tag_input:
                if ";" in tag:
                    tag_gids.extend(tag.split(";"))
                else:
                    tag_gids.append(tag)
    return {
        "tags": backend.get_tags(tag_gids),
        # 'tag_gids': tag_gids,
    }


@action("active-filters", method=["GET", "POST"])
@action.uses(
    "active_filters.html",
    session,
    backend,
    BaseTemplateSettings,
)
def active_filters():
    """
    Component met een buttonslijst van actieve filters
    """
    return _active_filters()


@action("filter-with-active", method=["GET", "POST"])
@action("filter-with-active/<tags:path>", method=["GET", "POST"])
@action.uses(
    "filter-with-active.html",
    session,
    backend,
    TilesHelpers,
    BaseTemplateSettings,
)
def filter_with_active(tags=("8b78e33d-c4ab-442e-aaf6-411fda089b03",)):
    """
    Component die active-filters en filters combineert tot 1 component
    """
    if isinstance(tags, str):
        tags = tags.split(";")
    elif isinstance(tags, tuple):
        tags = list(tags)

    filter_data = _filter(tags)
    active_data = _active_filters()

    return {**filter_data, **active_data}


# shared code between /item and /og_item
def _item(id):
    """
    Haal de info voor een itempagina op
    """
    try:
        item = Item.unpermalink(db, id) or backend.item(id)
    except Exception:
        raise HTTP(404, "Item niet gevonden.")

    backend.applog.read_item(
        item.id, backend.token.token, request.me.id if request.me else None
    )

    if not item.is_visible(
        include=None,  # allow all
        exclude={Visibility.DELETED},  # except deleted items
    ):
        raise HTTP(404, "Item niet gevonden.")

    return {
        "item": item,
        "anonymous": backend.is_anonymous,
        "thumbnail": backend.thumbnail_url,
        "db": db,
        "my_email": request.me.email if request.me else None,
    }


@action("item/<id>", method=["GET", "POST"])
@action.uses(
    "item.html",
    session,
    backend,
    BaseTemplateSettings,
    TilesHelpers,
)
def item_by_id(id):
    """LETOP: dit wordt standaard niet gebruikt vanuit de reguliere front-end!, dat is def item() hieronder."""
    return _item(id)


@action("item", method=["GET"])
@action.uses(
    "item.html",
    session,
    backend,
    BaseTemplateSettings,
    TilesHelpers,
)
def item():
    """Let op: de javascript in de 'normale frontend' stuurt deze settings door, via een get ipv een post."""
    id = request.query.item_id
    return _item(id)


def _user(id):
    """
    Haal de info voor de userpagina op
    """
    user_obj = backend.user(id=id)
    # backend.applog.read_user(user_gid=id) # TODO: applog
    me = request.me
    isme = me and uuid.UUID(id) == me.id
    backend.applog.read_user(id)

    return {
        "user": user_obj,
        "isme": isme,
        "me": me if isme else {},
    }


@action("user/<id>", method=["GET", "POST"])
@action.uses(
    "user.html",
    session,
    backend,
    # TilesHelpers,
    BaseTemplateSettings,
)
def user_by_id(id):
    return _user(id)


@action("user", method=["POST"])
@action.uses(
    "user.html",
    session,
    backend,
    BaseTemplateSettings,
)
def user():
    id = request.json.get("user_id")
    return _user(id)


@action("list_plaatsen", method=["GET"])
@action.uses(
    "component/datalist_plaatsen.html",
    BaseTemplateSettings,
)
def list_plaatsen():
    items = plaatsen.find_plaatsen(request.query.locatie)

    return dict(items=items)


@action("list_scholen", method=["GET"])
@action.uses(
    "component/datalist_scholen.html",
    BaseTemplateSettings,
)
def list_scholen():
    LIMIT = 10

    items = backend.list_schools_for_register(
        location=request.query.locatie, search=request.query.school, limit=LIMIT
    )

    return dict(items=items)

    # query = request.query.locatie + " " + request.query.school
    # found_scholen, state = scholen.find_scholen(query)
    # items = dict(list(found_scholen.items())[:LIMIT])
    #
    # return dict(items=items)


@action("menu", method=["GET", "POST"])
@action.uses(
    "menu.html",
    session,
    backend,
    BaseTemplateSettings,
)
def menu():
    return dict(backend=backend, me=request.me)


@action("modals", method=["GET", "POST"])
@action.uses("modals.html", session, backend, BaseTemplateSettings)
def menu_modals():
    return dict(backend=backend, me=request.me)


@action("notifications", method=["GET", "POST"])
@action.uses(
    "notification.html",
    session,
    backend,
    BaseTemplateSettings,
)
def notifications():
    # TODO:  notification functionaliteit toevoegen
    notifications = []
    for notif in backend.notifications()["data"]["auth"]["notifications"]:
        notifications.append(
            {
                "id": notif["id"],
                "title": notif["title"],
                "message": notif["message"]
                if notif["message"] != notif["title"]
                else "",
                "read": notif["readTimestamp"],
                "type": notif["concerningType"],
                "when": backend.timeago(notif["when"]),
            }
        )
    return {"notifications": notifications}


@action("notification_seen", method=["POST"])
@action.uses(
    session,
    backend,
)
def notification_seen():
    # TODO: later toevoegen
    return backend.notification_seen(request.json.get("notification"))


@action("debug")
@action.uses(session, backend)
def debug():
    http_cookie = request.environ.get("HTTP_COOKIE", "")
    c = request.cookies
    is_registered_user = backend.is_registered_user
    return dict(
        session=dict(session),
        cookie=c,
        http_cookie=http_cookie,
        is_registered_user=is_registered_user,
        me=request.me,
        is_anonymous=backend.is_anonymous,
    )


@action("login", method=["POST"])
@action.uses(
    session,
    backend,
)
def login():
    js = request.json

    if js:
        username = js.get("username")
        password = js.get("password")
        hardware = b64decode(js.get("hardware"))

        validated = backend.login(email=username, hardware=hardware, password=password)
        if validated.code == ValidationCode.INVALID_CREDENTIALS:
            return DANGER(
                "Gebruikersnaam of wachtwoord onbekend, probeer een andere combinatie.",
            )

        elif validated.code == ValidationCode.REQUIRES_EMAIL_VALIDATION:
            return WARNING(
                "Inloggen gelukt! Valideer nu je email.",
                _=f'on load send ew:load_form(form: "email_validate", name: "{validated.user.name}", id: "{str(validated.user.id)}", email: "{validated.user.email}") to closest .edwh-messagebus',
            )

        elif validated.code == ValidationCode.OK:
            return SUCCESS("Inloggen gelukt!")
        else:
            return DANGER(validated.feedback)

    else:
        return DANGER("Niet alle vereiste parameters zijn opgegeven.")


@action("logout", method=["POST"])
@action.uses(session)
def logout():
    # clear cookie:
    response.set_cookie(
        request.app_name + "_session",
        "",  # lege cookie om de session weg te gooien
        path="/",
        secure=True,
        same_site=None,  # anders werkt het alleen op hetzelfde domein
    )
    try:
        del session[BACKEND_ME]
    except KeyError:
        pass
    try:
        del session["token"]
    except KeyError:
        pass
    session.save()
    return SUCCESS("Uitgelogd!")


def form_or_json_input(key, default=None):
    data, altdata = request.forms, request.json
    if data and key in data:
        return data[key]
    if altdata and key in altdata:
        return altdata[key]
    return default


@action("contact", method=["POST"])
@action.uses(session, backend, db)
def contact():
    item = Item.load(db, form_or_json_input("item"))
    question = form_or_json_input("question")
    succes, message = backend.contact(item, question, request.me)

    if succes:
        return SUCCESS(message)
    else:
        return DANGER(message)


@action("claim_ownership", method=["POST"])
@action.uses(session, backend, db)
def claim_ownership():
    item = Item.load(db, form_or_json_input("item"))
    tel = form_or_json_input("phone")
    message = form_or_json_input("message")
    if request.me:
        succes, message = backend.claim_ownership_authenticated(
            item, request.me, tel, message
        )
    else:
        email = form_or_json_input("email")
        succes, message = backend.claim_ownership_unauthenticated(
            item, email, tel, message
        )

    if succes:
        return SUCCESS(message)
    else:
        return DANGER(message)


@action("like", method=["POST"])
@action.uses(session, backend)
def like():
    gid = form_or_json_input("subject")
    backend.like(
        gid,
        int(form_or_json_input("toggle")),
        form_or_json_input("action"),
    )
    return ""  # has to be empty, otherwise text will be added after the count on tiles and items.


@action("signup", method=["POST"])
@action.uses(
    session,
    backend,
)
def signup():
    js = request.json
    if request.method == "POST" and js:
        email = js.get("username")
        password = js.get("password")
        fields = session.get("register1")  # sent through session from previuos form

        fields["propertyBag"]: json.dumps({"kvk": fields.pop("kvk")})
        try:
            user = backend.signup(
                email=email,
                password=password,
                firstname=fields["firstname"],
                lastname=fields["lastname"],
                organisation=fields["location"],
                location=fields["location"],
                primary_organisational_role=fields["primary_organisational_role"],
                kvk=fields["kvk"],
            )
        except edwh.core.backend.SecurityException as e:
            warning(
                f'Poging to maken gebruikersaccount voor {email} mislukt vanwege "{str(e)}". Details:\n {fields}'
            )
            backend.applog.new_user_failed(email=email, details=fields)
            return DANGER(str(e))
        except ValueError as e:
            warning(
                f'Poging to maken gebruikersaccount voor {email} mislukt vanwege "{str(e)}". Details:\n {fields}'
            )
            backend.applog.new_user_failed(email=email, details=fields)
            return DANGER(str(e))

        return SUCCESS("Geregistreerd! Je kunt nu inloggen.")
    else:
        return DANGER("Niet alle vereiste parameters zijn opgegeven.")


@action("updateme", method=["POST"])
@action.uses(
    session,
    backend,
)
def updateme():
    js = request.json

    if request.method == "POST" and js:
        avatar = None
        if js["avatar"]:
            avatar = backend.upload_avatar(
                me=request.me,
                filename=js["avatar"],
                filecontent=js["avatarcontent"],
                ts=datetime.datetime.now(),
            )
        property_bag = {}

        if kvk := js.get("kvk"):
            property_bag["kvk"] = kvk

        if bio := js.get("bio"):
            property_bag["bio"] = bio

        user = backend.update_user(
            request.me,
            request.me,
            email=js.get("email"),
            password=js.get("password"),
            firstname=js.get("voornaam"),
            lastname=js.get("achternaam"),
            location=js.get("location"),
            organisation=js.get("organisation"),
            primary_organisational_role=js.get("rol"),
            property_bag=property_bag or None,
            avatar=avatar,
        )
        session[BACKEND_ME] = edwh_asdict(user)
        return SUCCESS("Aangepast")


def _hyperscript_xml(self):
    """
    TAGGER.xml modified to allow quotes (required for hyperscript)

    e.g. _="send event(some: 'data')" will be escaped normally:
    > <span ="on="" load="" send="" event(form:="" &amp;#x27;some="" form&amp;#x27;)"="" class="help is-warningmy_txt  btn"></span>
    but will become:
    """

    # self = SPAN or other element
    from yatl.helpers import _vk, is_helper, xmlescape

    def _escape(value):
        # custom: don't HTML-escape but replace ' -> \' and " -> '
        value = xmlescape(str(value), quote=False)
        value = value.replace("'", r"\'")
        value = value.replace('"', "'")
        return value

    name = self.name
    parts = []
    for key in sorted(self.attributes):
        value = self.attributes.get(key)
        if key.startswith("_") and not (value is False or value is None):
            if value is True:
                value = _vk(key[1:])
            else:
                value = _escape(value)  # <- custom
            if key == "_":
                # hyperscript:
                k = key
            else:
                # strip prefixing _ (e.g. _class=...)
                k = key[1:]
            parts.append('%s="%s"' % (_vk(k), value))
    joined = " ".join(parts)
    if joined:
        joined = " " + joined
    if name.endswith("/"):
        return "<%s%s/>" % (name[0:-1], joined)
    else:
        content = "".join(
            s.xml() if is_helper(s) else _escape(s) for s in self.children  # <- custom
        )
        return "<%s%s>%s</%s>" % (name, joined, content, name)


def _span_component(name: str, text: str, *classes, **other_attrs):
    """
    Helper om een feedback span (inline tekst) te maken met bulma alert classes.
    Usage:
    > return _span_component("danger", "Er is iets misgegaan", "extra", "css-classes", "hier", _="log 'en met _hyperscript'")
    of gebruik de SUCCESS, DANGER, WARNING classes van hieronder om het eerste argument te skippen:
    > return DANGER("Er is iets misgegaan", ...)

    bijv. components/danger.html
    <span _="on load send ew:danger"></span>
    <span class="help is-danger [[=classes]]" [[=attrs]]">
        [[=text]]
    </span>

    ->
    <span _="on load send ew:danger"></span>
    <span class="help is-danger extra css-classes hier" _="log 'en met _hyperscript'">
        [[=text]]
    </span>

    """

    """<span _="on load send ew:warning"></span>"""
    event_span = SPAN(**dict(_=f"on load send ew:{name}"))

    """
    <span class="help is-warning [[=classes]]" [[=XML(attrs)]]>
        [[=text]]
    </span>
    """

    visual_span = SPAN(
        text, _class=f"help is-{name}" + "  ".join(classes), **other_attrs
    )

    return _hyperscript_xml(event_span) + _hyperscript_xml(visual_span)


SUCCESS = lambda text, *c, **a: _span_component("success", text, *c, **a)
DANGER = lambda text, *c, **a: _span_component("danger", text, *c, **a)
WARNING = lambda text, *c, **a: _span_component("warning", text, *c, **a)


@action("recover", method=["POST"])
@action.uses(
    session,
    backend,
)
def recover():
    # backend.recover
    response = backend.recover(request.json.get("email"))
    if response:
        return SUCCESS("Nieuw wachtwoord aangevraagd, je kunt hier nu mee inloggen!")
    else:
        return DANGER("Geen account gevonden met dit emailadres.")


def _render(fname: str, ctx: dict):
    """
    Helper om yatl makkelijk te renderen van een file
    """
    with open(f"{APP_FOLDER}/templates/{fname}", encoding="UTF-8") as stream:
        return yatl.render(
            stream=stream,
            context=ctx,
            delimiters="[[ ]]",
        )


def _auth(path: str, data: dict = None, old: dict = None):
    """
    Helper om een auth component makkelijk te renderen
    """
    return _render(
        f"auth/{path}.html", dict(data=DotMap(data or {}), old=DotMap(old or {}))
    )


# HTMX auth router
@action("auth", method=["GET"])
@action.uses(
    session,
    backend,
)
def auth_form():
    path = request.query.get("ewform")
    data = b64decode(request.query.details)
    old = session.get(path, {})

    return _auth(path, data, old)


@action("register-step-1", method=["POST"])
@action.uses("auth/register2.html", session)
def register_step_1():
    form1 = request.json

    session["register1"] = {
        "firstname": form1.get("voornaam"),
        "lastname": form1.get("achternaam"),
        "location": form1.get("locatie"),
        "organisation": form1.get("school"),
        "primary_organisational_role": form1.get("rol"),
        "kvk": form1.get("kvk"),
    }

    return {}


@action("validate", method=["POST"])
@action.uses(
    session,
    backend,
)
def validate():
    try:
        # preauth is set in backend.login
        backend.validate_email_address(request.json.get("code"))
        return SUCCESS("Email geverifieerd!")
    except SecurityException as e:
        return DANGER("Ongeldige code")


@action("validate_for_claim", method=["GET"])
@action.uses(
    session,
    backend,
)
def validate_for_claim():
    try:
        succes, msg = backend.validate_ownership_claim(request.query.token)
        if succes:
            return SUCCESS("Geverifieerd, u kunt dit venster sluiten.")
        else:
            return WARNING(msg)
    except SecurityException as e:
        return DANGER("Ongeldige code")


def _school(id):
    """
    Haal de info voor de schoolpagina op
    """
    school_info = backend.organisation(id=id)
    if "," in str(school_info.lonlat):
        school_info.lon, school_info.lat = school_info.lonlat.strip("()").split(",")
    else:
        school_info.lon = school_info.lat = ""

    return {"school": school_info}


@action("school/<id>", method=["POST"])
@action.uses(
    "school.html",
    session,
    backend,
    BaseTemplateSettings,
)
def school_by_id(id):
    return _school(id)


@action("school", method=["POST"])
@action.uses(
    "school.html",
    session,
    backend,
    BaseTemplateSettings,
)
def school():
    id = request.json.get("school_id")
    return _school(id)


# LEIDEN PRIKBORD:


# @action(leidendb, "ratings/clear", method=["GET"])
# def clear_ratings():
#     from filelock import FileLock
#
#     with FileLock(os.path.join(APP_FOLDER, "databases/storage.lock")):
#         _platform_and_post = (leidendb.ratings.platform == request.params["platform"]) & (
#                 leidendb.ratings.post_id == request.params["postid"]
#         )
#         try:
#             leidendb(_platform_and_post).delete()
#             # we committen binnen de lock, opdat de hele transactie klaar is
#             leidendb.commit()
#         except:
#             # als er iets misgaat dan maken we de transactie ongedaan en
#             # gooien we dezelfde error
#             leidendb.rollback()
#             raise
#     return "Done"


@action("find_related/<gid>", method=["GET"])
@action.uses(session, backend)
def find_related(gid):
    item = backend.item(id=gid)
    return item.find_related(backend.db, n=5, extra_fields=["item_name"])


@action("calculate_similarity/<gid1>/<gid2>", method=["GET"])
@action.uses(session, backend)
def calculate_similarity(gid1, gid2):
    # bereken de hoeveelheid tags (%) die gelijk is tussen de twee items
    item1 = backend.item(id=gid1)
    item2 = backend.item(id=gid2)

    return str(
        item1.calculate_similarity(
            backend.db,
            item1,
            item2,
        )
    )


@action("ratings", method=["POST"])
@action.uses(leidendb, Handlebars("rating_results.hbs", helpers=handlebars_helpers))
def ratings():
    """
    Rate een ghost post van 1 tot 5 sterren

    request form data moet de volgende velden bevatten:
    - postid: de GHOST post id
    - stars: hoeveelheid sterren gegeven (1 t/m 5)
    - platform: het platform waar de stemmende user zich op bevindt
    """

    data = request.forms

    # noinspection PyTypeChecker
    # is wel een query!
    _platform_and_post: Query = leidendb.ratings.platform == data["platform"]
    _platform_and_post &= leidendb.ratings.post_id == data["postid"]

    if "stars" in data:
        score = int(data["stars"])

        if not 1 <= score <= 5:
            # invalide score mag niet, ouwe hackert!
            raise ValueError("Score should be in range of 1 - 5")

        _vote(_platform_and_post, data, score)

    else:
        score = None

    average, count, details = _get_votes(_platform_and_post)
    return {
        "count": count,
        "average": round(average, 1),
        "details": details[::-1],  # reverse list to have 5 stars at the top
        "postid": data["postid"],
        "chosen_stars": score,
    }


def _get_votes(_platform_and_post: Query) -> (int, int, list[dict]):
    """
    Voor Leiden

    we halen het aantal ratings per aantal sterren op, dus bijv.
    1 ster: 5x, 2 sterren: 10x etc.

    Details bevat (per score 1-5):
        "fraction": int,
        "stars": int,
        "count": int,
        "singular": bool,
    """
    count = leidendb.ratings.id.count()
    _results = leidendb(_platform_and_post).select(
        leidendb.ratings.rating, count, groupby=leidendb.ratings.rating
    )
    results = [0] * 5  # fill list with 5 zeroes
    for result in _results:
        results[result["ratings"]["rating"] - 1] = result[count]
    # hier worden de getoonde getallen berekend en vervolgens aan de handlebars
    # template opgestuurd
    count, average, details = _calculate_star_average(results)
    return average, count, details


def _vote(_platform_and_post, data, score):
    """
    Voor Leiden:
    Geef een rating 1-5 op een prikbord item
    """
    from filelock import FileLock

    # omdat py4web niet chill samengaat met sqlite door multi-threading, maken we
    # een filelock aan. Dan weten we zeker dat de db niet gelocked wordt.
    # Als er nog een lock op zit, dan wacht een tweede request tot de lock vrij is.
    with FileLock(os.path.join(APP_FOLDER, "databases/storage.lock")):
        try:
            leidendb.ratings.update_or_insert(
                # if the post id + session combi exists, create. otherwise update
                (leidendb.ratings.session_id == data["rating_client_id"])
                & _platform_and_post,
                post_id=data["postid"],
                session_id=data["rating_client_id"],
                rating=score,
                platform=data["platform"],
            )
            # we committen binnen de lock, opdat de hele transactie klaar is
            leidendb.commit()
        except:
            # als er iets misgaat dan maken we de transactie ongedaan en
            # gooien we dezelfde error
            leidendb.rollback()
            raise


@action("rating_form")
@action.uses(leidendb, Handlebars("rating_form.hbs", helpers=handlebars_helpers))
def rating_form():
    data = request.params

    if data.rating_client_id == "undefined":
        data.rating_client_id = None

    session_id = data.rating_client_id or uuid.uuid4()
    query = (
        (leidendb.ratings.platform == data["platform"])
        & (leidendb.ratings.post_id == data["postid"])
        & (leidendb.ratings.session_id == session_id)
    )
    row = leidendb(query).select(leidendb.ratings.rating).first()
    stars = row.rating if row else 0

    checked = [""] * 6  # ignore 0
    checked[stars] = "checked"

    # stars-{{postid}}
    # rating_client_id should NOT be used to determine result show,
    # stars-{id} should.
    stars = data.get(f"stars_{data['postid']}", "undefined")
    show_results = bool("" if stars == "undefined" else stars)

    return {
        "show_results": show_results,
        "rating_client_id": session_id,
        "checked": checked,
        "server": data.server,
    }


@action("school_praktijkoverzicht/leidenenomgeving")
@action.uses(
    "school_praktijkoverzicht.html",
    session,
    backend,
    BaseTemplateSettings,
)
# @cached(db, 'controllers-schoolpraktijkoverzicht')
def school_praktijkoverzicht(track: Callable = Magic):
    scholen_gids = [
        "8058c99c-e493-4c18-95c6-f7e8ddde2fd3",
        "d21784d7-37df-4371-986b-9de320605575",
        # "1dcd7e6e-2548-4dda-81e5-c2d7a56f1b5c",
        # "4abba417-7fb0-457e-819a-5c4d2d54f861",
        # "81c09b76-033f-45e1-87a2-535618128d78",
        # "85e87397-4b88-42b6-b70e-c504624cd6e6",
        # "2f3e617c-40fb-4b71-8a5b-0fa74faa9f62",
        # "4c25bb4e-cb6e-4f71-a576-7c4ca65be9d8",
        # "994c695e-39e3-4d7f-b872-b87eb54538e0",
        # "251193bd-1620-49d9-a40e-0060218e017b",
        # "d6afb8c6-b596-4a84-bf15-b862f2e57c95",
        # "d8456b54-a674-45df-8fa6-a3ccb186aab4",
        # "187b272d-13ad-4249-9a87-0e9e5204e3e6",
        # "3ce1024f-6474-43b5-97f2-2063a53fc84e",
        # "0808b3c9-7cab-47b8-bf7a-e385a81ed723",
        # "5e19f5ec-84d8-4c93-bfcc-fd4700b151c5",
        # "9984d2e2-6e7c-4ad8-ba53-fea48026c2ff",
        # "8c6e8f48-5103-4945-ab7e-e094d845293d",
        # "c806a917-c766-41f6-ad69-485dd460bbe4",
        # "a27c4c94-6473-417b-ad4f-cdfb2768c15e",
        # "438d28e5-e68b-49a6-9b4a-d2b7bd992c1c",
        # "f3ff0897-109e-4aff-9293-60c4dfaa737c",
        # "3ef0ff87-4cb7-4c6b-893f-8b76349736a6",
        # "054f9362-440b-4bd6-a5c2-a8ff7283ecc2",
        # "dd4e8bbd-4cc3-4332-8950-d4574f38afeb",
        # "4be60b42-0926-4856-80fc-9c0fc7487c92",
        # "b5d1eea7-58db-497a-9fad-84a883672925",
        # "3b12a5ff-962a-435c-8489-26d6c8ec6401",
        # "4631d4d3-9c05-438f-8fc3-481ef643b443",
        # "61be9407-2e23-468b-8804-0a1ef042d041",
        # "8601f02c-5120-43b6-8a2d-bbbdaf402ee2",
        # "c7bf00b7-0c03-40c7-8e92-0556a187b226",
        # "a730f11d-5533-4785-a657-d312650af44d",
        # "0c02ba61-51c6-4884-aa61-b5a191996451",
        # "bedf1827-0a34-4250-9976-ee085967e661",
        # "4829ca3d-f641-4230-95e0-537ef38f5ff3",
        # "c77615c4-2c85-4b1a-ae31-98c3b5f70edc",
        # "09a32fe6-9f1a-4f83-bb6f-e5fdf4faf85c",
        # "d306abfd-3c01-4454-8fa1-57c8264b9f5e",
        # "dccbdc1c-a419-4e90-9214-1263a6f2f6c3",
        # "0509b690-2341-499d-8c46-2f1cc6165608",
        # "8fef1f19-e89b-4a11-a511-b908aa6e586c",
        # "14dc660b-b0de-4e66-a8fa-b16641ae3bbe",
        # "e2b363b6-c23e-4bdd-bbaa-597494df47e9",
        # "1b715efe-b897-4eb7-a6c6-bb352cc8a346",
        # "0d138643-c0b6-413f-a031-2f7b0f3d84e6",
        # "560c2182-b60d-4700-a042-cd686b5dfc20",
        # "c5bd77ee-7c01-4e4e-9f86-1a4a81a5b7ca",
        # "40e0a26c-5e0c-4384-b4ad-9438b83e8eab",
        # "636c5127-a770-4506-b407-22e2467dd15e",
        # "c375a6a8-e836-4afe-9668-b18b415cdd12",
        # "97256c2f-d1a7-4cb1-ba20-7a488e7c5bdb",
        # "256441ad-3698-4c56-b22c-5fc6e382ec66",
        # "0404eab2-45aa-4a28-a328-487186d8964f",
        # "0c563434-a025-415a-b5cc-39144e713edf",
        # "a5d18e65-6603-4455-af18-2c01a17103f7",
        # "14965ee5-1329-40dd-aad6-6e023fd96dce",
        # "10975f41-c82e-4f44-8377-6680ab3f8864",
        # "618f9e03-6855-4109-ac38-24ec9064c12c",
        # "6bafd631-a597-4edc-8cfc-5ad714367e85",
        # "aaef3c95-aed1-47b3-8b51-17b903d81cdb",
        # "07755415-d27c-4edc-93a6-76be7d33b1d2",
        # "899fa809-d5ba-4046-acf6-8c875a412c88",
        # "c3a2cbb9-9140-47a9-a934-24c42b5df808",
        # "56855cb9-c8bc-455b-8dc7-6a00aed32539",
        # "361f528f-bfb8-44dd-9a2a-b0dbde9215ac",
        # "f617f5d3-7bd5-4941-bc6a-37bc109eb8c3",
        # "a96aa9d1-2982-43b1-af1e-1be7d8ad35ed",
        # "515f139b-5453-4c3e-9e58-13f9ead79607",
        # "d5f1f5da-b981-44fd-86bf-4b0293679393",
        # "ab34ed18-704c-492d-a564-85db9dc55293",
        # "e10cb3fc-39d5-4e95-b8fc-a4fff9a1ba70",
        # "438e6999-63e6-42cd-8dcc-689dba7bd82a",
        # "645d8ddb-b210-4d3f-a72b-696b5b58fa34",
        # "b0e64f94-a077-4810-81b3-4b55091a47af",
        # "dace78c5-ca40-45a6-8859-bf0d05eaca15",
        # "d8735d2b-25b3-4579-88d3-910a22b4fbda",
        # "547011fb-c221-44fa-8a7a-f1b15815b692",
        # "9904b8c9-ac67-4d14-a431-aa116c2541de",
        # "9f8a59c1-5531-4597-8675-744537ed6c22",
        # "788c711d-797c-4f2b-9be9-c5f3160a61aa",
        # "2481cd39-c4b5-4a8f-b854-9717ffd44a6a",
        # "b43acb45-6644-4b2b-82be-3771de4b0137",
        # "b1a9f4c3-8c7c-4ba3-bbe9-d5ceaa697be4",
        # "9c03e49e-f40f-489f-bbc9-10b5d6012d34",
        # "4d6874eb-38b3-4ba3-923a-dfb56d99868c",
        # "d625375a-ebc3-4a3f-ba58-ce33ad123da8",
        # "5c02a1d4-2198-4924-9412-42c8672c0cda",
        # "169a50fd-16c9-4fa0-96a2-1c7f6435d1e7",
        # "739da2e7-1fbe-44d5-92c3-70e95b665586",
        # "8cd35384-ce10-4f34-8bb9-c65ce482803d",
        # "a6bce9f1-8fe2-44a6-9166-6a1a5cd407f4",
        # "4c34f93b-f7c8-44c8-aeee-d5edb4a66a36",
        # "20a9e740-4cdc-48ca-85f5-88946f4afbf2",
        # "1508963f-3b1e-452b-b16c-b5dfbc8be0c1",
        # "ebff206c-2fb6-4fb4-b367-320be4698e0a",
        # "4af5d00b-05da-4cb1-a5c9-bc37b1f7443c",
        # "b2e06d84-466c-4229-b1e8-51254c2db0a9",
        # "a44eda9a-2a9d-42ea-ba9b-812441444d93",
        # "a5dec13d-069a-43c5-a2c8-c6d1069e23cb",
        # "c1a9baa0-2689-479d-a8ee-ea99c1217d4b",
        # "ad54c2d4-39ed-45c6-9da6-195e5dfbd1f1",
        # "d04a0de8-0004-4375-9316-d3baf63e25fa",
        # "78b77378-c7e2-4d1c-a92f-96a75f67263d",
        # "b51a6837-348c-4e9b-a501-0f97c6e4200c",
        # "da1ce1dd-5999-44a2-95b8-48039dfe63a5",
        # "a17b508e-5222-4153-96ee-d4537d252034",
        # "d10aa5bb-88eb-4e37-bf22-092d08ee0a18",
        # "22ad522d-918f-4468-9d54-280e7af3fa6a",
        # "b2616aa2-1dd2-4d10-80af-f2fa64d092c9",
        # "0c4aaaed-0448-40ff-ab11-2ca17026be20",
        # "7e7d2fe1-ff21-469e-b333-f49e62e686c4",
        # "5e73c9e4-a68f-49c0-af43-76aff01bb5a6",
        # "868e0c87-e084-481e-97e0-22f314cc78e1",
        # "b161586d-3e93-467a-afd4-7f8ebfa41a5a",
        # "c2d90af6-07d5-4e22-b0ec-f8177a7a080b",
        "ff7af6ce-d05d-4248-b52b-084863682ad8",
        "bb394920-c643-4a75-b291-2ea377f959d5",
        "b67d36a1-bae8-48b8-a243-999753f068fe",
        "e6ae9b3e-d980-4030-94cc-51db20bfd413",
        "3088cb13-eb83-4fe7-97e5-adf77804eb14",
        "c6e68a99-8206-4133-81fd-f01ea2d65175",
        "e235c919-189b-4150-a21d-89f9f19236db",
        "3c2dc59e-11ab-4d42-8b11-f6fb7a463224",
        "5abb4a68-3f6b-4e27-aa91-e035dac2724e",
        "56d07d65-0121-4ca3-b87c-5abe25cca0b6",
        "bffb4db9-6be4-43fd-a461-62bed089a8e9",
        "a8ca20ee-5e58-4884-b292-384b0a3b0ba0",
        "d5e38c55-06ba-442d-a548-d0d623648307",
        "d9d32718-7a14-4f19-b656-819a0afd08df",
        "6078eea0-f54b-4028-bd05-f5016fe23027",
    ]
    organisations = []
    for gid in scholen_gids:
        try:
            organisations.append(backend.organisation(gid, track=track))
        except NotFoundException:
            warnings.warn(f"Geen school gevonden voor gid: {gid}")
    # return repr(orgs)
    tiles_per_org = []

    settings = {"paginate": False, "limit": 3, "return_none_when_no_tiles": True}

    for org in organisations:
        try:
            org_tiles = tiles(org.id, **settings)
            if org_tiles:
                tiles_per_org.append(
                    DotMap(
                        org_gid=org.id,
                        org_name=org.name,
                        tiles=org_tiles,
                    )  # org.tiles?
                )
        except NotFoundException:
            warnings.warn(f"Org {gid}")
    db.commit()
    print("######################### COMMITTED #############################")
    return {"tiles": tiles_per_org}


###  demo functies:


@action("hotspots")
@action.uses("hotspots.html")
def hotspots():
    endpoint = request.params.get("api_endpoint", "https://robin.farm.edwh.nl")
    image = request.params.get("image", "https://placehold.co/500x500")
    content_api = request.params.get(
        "api_key", "50b422ec8c5f7f124610dc2170"
    )  # enter ghost content (public) API key

    HOTSPOTS = get_hotspots(endpoint, content_api)

    return {
        "edit_mode": False,
        "hotspots": HOTSPOTS,
        "image": image,
    }


@action("clicked", method=["GET", "POST"])
def clicked():
    longjson = json.dumps(dict(request.forms), indent=4)
    compactjson = json.dumps(dict(request.forms))
    return """
    <pre>
    {longjson}
    </pre>
    <script type="text/hyperscript">
       on load set @hx-vals of {state_id} to '{compactjson}'
    </script>
    """.format(
        longjson=longjson,
        compactjson=compactjson,
        state_id=request.forms.get("state_id", "#state"),
    )


@action("celery")
@action("celery/<who>")
def test_celery(who=None):
    result = log_once.delay(who)
    return f"zie logs; {result}"


@action("stats")
def stats():
    import tabulate

    return tabulate.tabulate(
        db.executesql("select * from pg_stat_activity"), headers="keys", tablefmt="html"
    )
