import os

from py4web import DAL
from py4web import action as Action
from py4web.core import Reloader

from . import settings

lts_users_db = DAL(
    settings.LTS_USERS_DB_URI,
    folder=settings.LTS_USERS_DB_FOLDER,
    pool_size=settings.LTS_USERS_DB_POOL_SIZE,
    migrate=settings.LTS_USERS_DB_MIGRATE,
    fake_migrate=settings.LTS_USERS_DB_FAKE_MIGRATE,
)


def jsonned_path(path):
    """
    a/b/c.html/<def>          >> a/b/c.json/<def>
    a/b/c.html                >> a/b/c.json
    a/b                       >> a/b.json
    a/b/<arg>                 >> a/b.json/<arg>
    a/b/<arg>/<arg2>          >> a/b.json/<arg>/<arg2>
    a/b.json/<arg>/<arg2>     >> a/b.json/<arg>/<arg2>
    """
    static_base = []
    for element in path.split("/"):
        if "<" not in element:
            static_base.append(element)
        else:
            break
    search_for = "/".join(static_base)
    base, ext = os.path.splitext(static_base[-1])
    replace_with = (
        "/".join(static_base).replace(ext, ".json")
        if ext
        else "/".join(static_base) + ".json"
    )
    return path.replace(search_for, replace_with)


class action(Action):
    def __call__(self, func):
        """Building the decorator - copied and modified from py4web core.py action."""
        app_name = action.app_name
        if self.path[0] == "/":
            path = self.path.rstrip("/") or "/"
        else:
            base_path = "" if app_name == "_default" else f"/{app_name}"
            path = (f"{base_path}/{self.path}").rstrip("/")

        Reloader.register_route(app_name, path, self.kwargs, func)
        # NEW! .json variant for every extensionless path:
        json_supported_path = jsonned_path(path)
        if json_supported_path != path:
            Reloader.register_route(app_name, json_supported_path, self.kwargs, func)
            ### see JSONFixture (used in 'BaseTemplateSettings')
            ### for the logic of actually returning JSON instead of HTML.

        if path.endswith("/index"):  # /index is always optional
            short_path = path[:-6] or "/"
            Reloader.register_route(app_name, short_path, self.kwargs, func)

        return func
