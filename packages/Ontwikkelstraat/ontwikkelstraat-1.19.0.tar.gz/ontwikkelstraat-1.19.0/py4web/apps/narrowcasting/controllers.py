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
import pathlib
import uuid

import qrcode
import qrcode.image.styledpil
from edwh.core.backend import NotFoundException
from edwh.core.data_model import (
    DEFAULT_EXCLUDED_VISIBILITY,
    DEFAULT_INCLUDED_VISIBILITY,
    Visibility,
)
from py4web_debug import dd, is_debug, tools

from py4web import action, request, response

from .backend_support import OrganisationWithItems, backend
from .common import db, session
from .fixtures import BaseTemplateSettings, TilesHelpers
from .settings import STATIC_FOLDER

if IS_DEBUG := is_debug():
    tools.enable(db, enabled=True, debugbar_enabled=False)


@action("index")
def index():
    return "This app has the routes `/qr/&lt;gid&gt;` and `/lef`."


@action("qr/<gid>", method=["GET"])
@action.uses(BaseTemplateSettings)
def qr(gid):
    # delen.meteddie.nl/item/<gid>
    href = (
        request.settings["item_uri_template"].format(gid)
        + "?utm_source=narrowcasting-lef"
    )
    # Nu met embedded PNG:
    code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    code.add_data(href)
    icon_path = pathlib.Path(STATIC_FOLDER) / "images/icon.png"
    img = code.make_image(
        image_factory=qrcode.image.styledpil.StyledPilImage,
        embeded_image_path=icon_path,
    )
    from io import BytesIO

    image_buffer = BytesIO()
    img.save(image_buffer)
    image_buffer.seek(0)
    response.headers["Content-Type"] = "image/png"
    return image_buffer.read()


@action("lef", method=["GET"])
@action.uses("narrowcasting.html", session, backend, TilesHelpers, BaseTemplateSettings)
def narrowcasting(org_gid=None, **internal_settings):
    """
    :param org_gid:
    :param internal_settings: bedoeld om een remote request te kunnen simuleren tbv school_praktijkoverzicht
    :return:
    """

    settings = internal_settings or request.settings
    limit = 0
    offset = limit * (settings.get("page", 1) - 1)
    tags = ["1274163a-be86-4395-8eef-4af66d9b81ec"]

    org: OrganisationWithItems = None
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

    if org_gid and org and hasattr(org, "items"):
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
        "anonymous": backend.is_anonymous,
        "thumbnail": backend.thumbnail_url,
    }
