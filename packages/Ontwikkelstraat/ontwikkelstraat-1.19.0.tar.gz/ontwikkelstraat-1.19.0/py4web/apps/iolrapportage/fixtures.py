from py4web.core import Fixture, request

from .opengraph import get_and_format_metadata


def get_path_arg_dynamically(arg: str, default=None):
    """
    Normally, you can define dynamic routes for controllers as:
    e.g. /user/<id:str>
    def user(id): ...

    However, when you're in a fixture or deep inside a function/method, you may not have access to this id (anymore).
    But you do have access to the 'request', which also contains these args in 'route.url_args'
    """
    return request["route.url_args"].get(arg, default)


class OpenGraphFixture(Fixture):
    def on_success(self, context):
        if isinstance(context.get("output"), dict):
            uuid = get_path_arg_dynamically("id")
            context["output"]["metadata"] = get_and_format_metadata(uuid)


opengraph_metadata_from_id = OpenGraphFixture()
