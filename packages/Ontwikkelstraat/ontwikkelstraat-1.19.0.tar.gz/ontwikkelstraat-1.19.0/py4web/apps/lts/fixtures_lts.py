import base64
import enum
import json
import typing
import urllib.parse

from edwh.core.backend import edwh_asdict

from py4web import request
from py4web.core import HTTP, Fixture, response


class JSONFixture(Fixture):
    """
    Parent class;
     can be inherited by a Fixture to add this functionality and overwrite the (empty) on_success_html logic.
    """

    auth_username: typing.Optional[str] = None
    auth_secret: typing.Optional[str] = None

    @staticmethod
    def json_dumper(value: typing.Any) -> str | None:
        # custom json dumper for values need assistance in being jsonified
        # usage: json.dumps(..., default=cls.json_dumper)
        if hasattr(value, "__attrs_attrs__"):
            return edwh_asdict(value)

        if callable(value):
            # method, don't include in json
            return None

        if isinstance(value, enum.Enum):
            return value.value

        return str(value)

    @classmethod
    def check_authorization_header(cls) -> bool:
        """
        Returns whether the auth is valid
        """
        try:
            auth_info = base64.b64decode(
                request.headers["Authorization"].removeprefix("Basic ")
            ).decode()
            username, password = auth_info.split(":")

            # if auth_username or auth_password are set to None, they are not checked with the input.
            return cls.auth_username in (None, username) and cls.auth_secret in (
                None,
                password,
            )
        except Exception:
            return False

    @classmethod
    def check_authorization_via_secret(cls):
        data = request.json or request.params  # {**request.params}

        return data.get("secret") == cls.auth_secret

    @classmethod
    def ensure_valid_authorization(cls) -> None:
        """
        Raises an error if the auth is invalid
        """
        if not (
            cls.check_authorization_header() or cls.check_authorization_via_secret()
        ):
            raise HTTP(
                403, json.dumps({"error": "Invalid authorization", "status": 403})
            )

    @classmethod
    def on_success_json(cls, ctx):
        response.headers["Content-Type"] = "application/json"
        cls.ensure_valid_authorization()

        output = ctx["output"]
        if isinstance(output, dict):
            ctx["output"] = json.dumps(output, default=cls.json_dumper)

    @classmethod
    def on_success_html(cls, ctx):
        # abstract, can be overwritten by subclasses but can also be left empty
        pass

    @classmethod
    def on_success(cls, ctx):
        """
        Convert output to JSON if .json route or run the default html on_success
        """
        path = urllib.parse.urlparse(request.url).path
        if path.endswith(".json") or ".json/" in path:
            return cls.on_success_json(ctx)
        else:
            return cls.on_success_html(ctx)
