import sys

from py4web import URL, abort, action, redirect, request, response
from py4web.core import HTTP, Fixture

from .demo import *
from .fixtures import opengraph_metadata_from_id
from .handlebars import Handlebars, handlebars_helpers
from .opengraph import get_and_format_metadata, get_metadata

# sys.stdout.reconfigure(encoding="utf-8")
# sys.stderr.reconfigure(encoding="utf-8")


class CacheHeaders(Fixture):
    def __init__(self, max_age) -> None:
        self.max_age = max_age

    def on_request(self, ctx):
        pass

    def on_error(self, ctx):
        pass

    def on_success(self, status):
        response.headers["Cache-Control"] = f"max-age={self.max_age}, must-revalidate"

    def transform(self, output, shared_data=None):
        return output


cacheheaders = CacheHeaders(60)


def _redirect_permanent(to):
    # redirect() is 303, we want 301 for permanent
    response.set_header("Location", to)
    raise HTTP(301)


@action("component")
@action("component/<path:path>")
@action.uses(cacheheaders, Handlebars("component.hbs"))
def component(path=None):
    return dict(context={"path": path})


# let op: (nep)ghost routes mogen geen context hebben, omdat (echte) ghost templates static zijn!


@action("item")
@action("item/<id>")
@action("Item/<id>")
@action("Item/<id>/<name>")
@action("item/<id>/<name>")
# fixme: handlebars er uit bonjouren,
@action.uses("item.html", cacheheaders, opengraph_metadata_from_id)
def item(id=None, name=None):
    # for ghost cms, see https://ghost.org/docs/tutorials/creating-content-collections/ for advanced routing

    # item id from URL via JS
    return dict()


@action("index")
@action.uses(cacheheaders, Handlebars("index.hbs", helpers=handlebars_helpers))
def index():
    return dict(
        page_title="index",
        context={},
    )


@action("profile/<id>")
@action("Profile/<id>")
@action("user/<id>")
@action("user")
@action.uses("user.html", cacheheaders, opengraph_metadata_from_id)
def user(id=None):
    # user id from URL via JS
    return dict()


@action("demo")
@action.uses(cacheheaders, Handlebars("demo.hbs", helpers=handlebars_helpers))
def demo():
    # test 3 groepjes tiles
    return {}


@action("attribution")
@action.uses(cacheheaders, Handlebars("attribution.hbs", helpers=handlebars_helpers))
def attribution():
    return {}


@action("school/<id>")
@action("school")
@action.uses("school.html", cacheheaders, opengraph_metadata_from_id)
def school(id=None):
    # school id from URL via JS
    return dict()


@action("ratings")
@action.uses(cacheheaders, Handlebars("ratings.hbs", helpers=handlebars_helpers))
def ratings():
    return {}


@action("activiteiten")
@action.uses(cacheheaders, Handlebars("activiteiten.hbs", helpers=handlebars_helpers))
def activiteiten():
    return {}


@action("school_praktijkoverzicht")
@action.uses(Handlebars("school_praktijkoverzicht.hbs", helpers=handlebars_helpers))
def school_praktijkoverzicht():
    return {}


@action("leiden")
@action.uses(Handlebars("leiden.hbs", helpers=handlebars_helpers))
def leiden():
    return {"tag": "1274163a-be86-4395-8eef-4af66d9b81ec"}


@action("hotspots")
@action.uses(Handlebars("hotspots.hbs", helpers=handlebars_helpers))
def hotspots():
    return {}


@action("extern")
@action.uses(Handlebars("extern.hbs", helpers=handlebars_helpers))
def extern():
    # 3rd party usage of tiles
    return {}
