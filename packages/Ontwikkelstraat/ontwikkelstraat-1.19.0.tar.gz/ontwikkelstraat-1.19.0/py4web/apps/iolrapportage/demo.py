from py4web import URL, Flash, abort, action, redirect, request

from .handlebars import Handlebars, handlebars_helpers

__all__ = ["demo", "demo_component", "demo_template", "demo_nieuw"]

flash = Flash()


@action("demo_people")
@action.uses(
    Handlebars(
        "demo.hbs",
        helpers=handlebars_helpers,
    )
)
def demo():
    return dict(
        context={
            "people": [
                {"firstName": "Pietje", "lastName": "Katz"},
                {"firstName": "Carl", "lastName": "Lerche"},
                {"firstName": "Alan", "lastName": "Johnson"},
            ]
        },
        # helpers=helpers
        # partials=partials,
    )


@action("demo/component")
@action("demo/component/<path:path>")
@action.uses(Handlebars("demo_component.hbs"))
def demo_component(path=None):
    return dict(context={"path": path})


@action("demo/template")
@action.uses(flash)
@action.uses(Handlebars("demo_template.hbs", helpers=handlebars_helpers))
def demo_template():
    flash.set("dit is m")
    return {"title": "niet leeg"}


@action("demo/nieuw")
def demo_nieuw():
    return "hoi"
