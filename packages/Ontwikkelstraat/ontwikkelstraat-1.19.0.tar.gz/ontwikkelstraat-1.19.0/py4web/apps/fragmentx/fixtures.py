import json
from pathlib import Path

import attrs
from edwh.core.data_model import (
    DEFAULT_EXCLUDED_VISIBILITY,
    DEFAULT_INCLUDED_VISIBILITY,
    Visibility,
)
from yatl import PRE, XML

from py4web import request
from py4web.core import Fixture, render
from py4web.utils.factories import Inject

from . import helpers
from .common import db
from .helpers import PY4WEB_URL, DotMap
from .settings import APP_FOLDER

__all__ = [
    # relevant voor pagina's met tiles:
    "TilesHelpers",
    # relevant voor vrijwel alle pagina's:
    "BaseTemplateSettings",
]


class BaseTemplateSettings(Fixture):
    """
    Tries to load state from the given post payload.

    Looks for q, tags, and some template strings."""

    default_settings = dict(
        q="",
        tags=[],
        order="RECENT_DESC",
        author="",
        page=1,  # -> offset
        limit=9,  # -> first
        paginate=True,
        item_new_tab=True,
        # a helper is generated for every setting ending in _template
        item_uri_template="https://delen.meteddie.nl/item/{}",
        user_uri_template="https://delen.meteddie.nl/profile/{}",
        menu_style="default",  # see def filter()
        include=DEFAULT_INCLUDED_VISIBILITY,
        exclude=DEFAULT_EXCLUDED_VISIBILITY,
        # item-specific page:
        map_zoom_level=7,
        # map_center="(52.150216,4.895168)",
        map_center="average",  # Either a point, 'auto' or 'average'
        map_center_fallback="(52.150216,4.895168)",  # used if map_center is 'auto' and no point available
    )

    @classmethod
    def on_request(cls, ctx):
        request.settings = settings = cls.default_settings.copy()

        if data := request.json or request.query or request.params:
            # BEFORE changing type():
            data["include"] = cls.validated_visibilities(
                data.get("include", DEFAULT_INCLUDED_VISIBILITY)
            )
            data["exclude"] = cls.validated_visibilities(
                data.get("exclude", DEFAULT_EXCLUDED_VISIBILITY)
            )

            # copy the value from the json payload if available, otherwise use
            # the default settings.
            for key, default_value in cls.default_settings.items():
                value = data.get(key, default_value)  # default value is set later!
                # convert the value to the type expected from the default_settings.
                # type(default_value) could be str or list, which is a callable to assert the good type.
                var_type = type(default_value)
                if var_type == bool and isinstance(value, str):
                    # extra rules
                    if value in {"0", "false", "off"}:
                        value = False

                settings[key] = var_type(value)

            # filter out any None values (which are to indicate an empty set,
            # which is otherwise a little hard to send from the javascript part
            settings["tags"] = [
                [qf_gid.strip() for qf_gid in _.split(";")] if ";" in _ else _
                for _ in settings.get("tags", [])
                if _
            ]

    @staticmethod
    def validated_visibilities(
        visibilities: list[str] | list[Visibility],
    ) -> list[Visibility]:
        """Accept only valid visibilities, return a list of Visibility objects."""
        if visibilities in (DEFAULT_INCLUDED_VISIBILITY, DEFAULT_EXCLUDED_VISIBILITY):
            return visibilities

        if isinstance(visibilities, str):
            visibilities = visibilities.split(",")

        validated = []
        for visibility in visibilities:
            try:
                validated.append(Visibility(visibility.lower()))
            except:
                # todo: catch specific exception
                print("ERROR: invalid visibility:", visibility)
        return validated

    @classmethod
    def generic_helpers(cls) -> dict:
        # relevant voor vrijwel alle pagina's:
        return {
            "escape": helpers.escape,
            "PY4WEB_URL": PY4WEB_URL,
            # todo: only if debug:
            "dump": lambda o: PRE(
                json.dumps(
                    o,
                    default=lambda o: attrs.asdict(o)
                    if hasattr(o, "__attrs_attrs__")
                    else str(o),
                    indent=2,
                )
            ),
        }

    @classmethod
    def on_success(cls, ctx):
        """
        add custom helpers (that depend on the request) to context before rendering the yatl
        (structure stolen from Inject)
        """
        output = ctx["output"]
        if isinstance(output, dict):

            def _partial(key: str):
                """
                Helper to generate a partial, if it exists in the partials dict in the context
                (with return dict(partials={...}, ...)

                Note: due to py4web/renoir caching breaking dynamic partials, the usage changed:
                Previous usage: `[[include partial(...)]]`
                New usage:      `[[=partial(...)]]`
                """
                fname = output["partials"].get(key)

                if not fname:
                    raise ValueError(
                        f"Partial key {key} not found in the partials dict!"
                    )

                partials_path = Path(APP_FOLDER) / "templates/partials"
                partial_path = partials_path / fname

                return XML(
                    render(
                        filename=str(partial_path), path=partials_path, context=output
                    )
                )

            output.update(
                cls.uri_templates(),
            )
            output.update(cls.generic_helpers())

            output.update(
                settings=DotMap(request.settings),
                partial=_partial,  # helper (needs ctx so can't be defined in yatl_helpers)
            )

    @staticmethod
    def uri_templates() -> dict:
        """
        Generate helpers with the same name as the templates in the base template settings.

        Works dynamically using request.settings.
        """

        def helper_builder(tmpl: str):
            """
            The helper builder should exist **OUTSIDE** the for loop.
            when calling the helper_builder, a copy of the argument is used so
            the template as an argument is not the same as the template that will be
            updated within the for loop below this function.
            """

            def helper(*args, **kwargs):
                return tmpl.format(*args, **kwargs)

            return helper

        helpers = {}
        for key, template in request.settings.items():
            if key.endswith("_template"):
                # execute a function to have the template variable be an argument
                # that way the template here is assigned a new value in the loop
                # but the argument ot the function retains its original value,
                # assigned when the function is called..
                # #headache.
                helpers[key] = helper_builder(template)

        return helpers


# relevant voor pagina's met tiles:
TilesHelpers = Inject(
    thumb_count=lambda item: item.thumb_count(db),
    has_my_thumb=lambda item: str(item.id) in request.me.gid_thumb_map
    if request.me
    else False,
    paginate=lambda tiles: XML(helpers.paginate(tiles)),
)
