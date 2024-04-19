import abc
import base64
import typing
from pathlib import Path
from typing import Optional

import jwt
import yarl
from pydal import DAL


class EddieJwtFormat(typing.TypedDict):
    iat: typing.NotRequired[int]
    exp: typing.NotRequired[int]
    nbf: typing.NotRequired[int]
    iss: typing.NotRequired[str]
    aud: typing.NotRequired[str]
    data: typing.Any


# https://gist.github.com/cameronmaske/f520903ade824e4c30ab - base64 that actually encodes URL safe (no '=' nonsense)


def urlsafe_base64_encode(string: str) -> str:
    """
    Removes any `=` used as padding from the encoded string.
    """
    encoded = base64.urlsafe_b64encode(string.encode())
    return encoded.decode().rstrip("=")


def urlsafe_base64_decode(string: str) -> str:
    """
    Adds back in the required padding before decoding.
    """
    padding = 4 - (len(string) % 4)
    string = string + ("=" * padding)
    return base64.urlsafe_b64decode(string.encode()).decode()


def jwt_encode(payload: dict, key_location="/shared_keys/jwt.key"):
    key_path = Path.cwd() / key_location
    if not key_path.exists():
        raise ValueError(f"Key at {key_path} does not exist!")

    return jwt.encode(payload, key_path.read_bytes(), algorithm="HS256")


def jwt_decode(
    payload: str,
    key_location="/shared_keys/jwt.key",
    issuer: Optional[str] = None,
    audience: Optional[str] = None,
    leeway: Optional[int] = None,
    **kwargs: typing.Any,
):
    key_path = Path.cwd() / key_location
    if not key_path.exists():
        raise ValueError(f"Key at {key_path} does not exist!")

    if issuer is not None:
        kwargs["issuer"] = issuer

    if audience is not None:
        kwargs["audience"] = audience

    if leeway is not None:
        kwargs["leeway"] = leeway

    return jwt.decode(payload, key_path.read_bytes(), algorithms="HS256", **kwargs)


class SharedAuth(abc.ABC):
    """
    The flow should work rougly as following (can differ slightly per framework):
    1. use EddieAuth instead of normal (p4w/w2p) Auth, but this can be a drop-in replacement
        (in terms of decorators/fixtures etc). You only need to add a 'jwt_provider' provider url controller:
        'https://web2py.meteddie.nl/init/jwt_auth'.
        NOTE: since the server is web2py, this does NOT change to `py4web.meteddie` when using a py4web client!
    2. the user is redirected to the JWT provider's login (/init/jwt_auth/login), which uses the regular w2p login
    3. a JWT token is generated, containing the basic user info and groups
    4. the user is redirected back to this app, where the JWT token is parsed.
    5. A auth_user entry is created or updated for the user (by ID), groups and memberships are also updated.
        (note: groups and memberships are not built-in to py4web,
        so they are added together with auth_user during `auth.define_tables()`)
    6. Other auth actions are disabled or redirected to the provider when possible.
    """

    jwt_provider: yarl.URL
    db: DAL
    requires_still_exists: typing.Callable  # decorator or Fixture

    def _jwt_url(self, action: str = "login", **query_vars: typing.Any) -> str:
        """
        Convert an action and a vars to a JWT url.

        Example:
            self._jwt_url('login', {'_next': '/myapp/user/profile'})
            # -> 'https://web2py.myjwtprovider/jwt_auth/login?_next=/myapp/user/profile'
        """
        url = self.jwt_provider / action % query_vars
        return str(url)

    def decode_jwt_response(
        self,
        data: str,  # can be 'key' in framework-specific functions
        issuer: Optional[str] = None,
        audience: Optional[str] = None,
        leeway: Optional[int] = None,
        **kwargs: typing.Any,
    ):
        """
        Similar to
        """
        full: EddieJwtFormat = jwt_decode(
            data,
            issuer=issuer,
            audience=audience,
            leeway=leeway,
            **kwargs,
        )

        # other fields are used by pyjwt to check things like expiry.
        return full["data"]

    def handle_jwt_response(self):
        """
        Parse '_edwh_jwt' from the request query params.

        - create/update the user
        - create/update the related groups
        - assign the right memberships (also removes old memberships)
        """
        db = self.db
        auth_user = db.auth_user

        data = self.decode_jwt_response()

        me = data["me"]

        auth_user.update_or_insert(
            auth_user.id == me["id"],
            **me,
        )

        user = auth_user(me["id"])

        # purge old memberships:
        self.db(self.db.auth_membership.user_id == me["id"]).delete()

        # ensure groups exist:
        for group in data.get("groups", []):
            self.db.auth_group.update_or_insert(
                self.db.auth_group.id == group["id"], **group
            )

            # add current memberships:
            db.auth_membership.insert(
                user_id=me["id"],
                group_id=group["id"],
            )

        self.login_user(user)

        return self.go_next(data.get("next"))

    @abc.abstractmethod
    def login_user(self, user: dict):
        """
        Framework-specific login logic
        """

    @abc.abstractmethod
    def go_next(self, url: str = None):
        """
        Framework-specific ?next/?_next handling
        """

    @abc.abstractmethod
    def action_redirect(
        self, action: str = None, strip_query: bool = False, **extra_data
    ):
        """
        Framework-specific redirect logic
        """

    @abc.abstractmethod
    def action_login(self):
        """
        Action to handle registering a new user (-> framework-specific redirect to login via action_redirect)
        """

    @abc.abstractmethod
    def action_register(self):
        """
        Action to handle registering a new user (-> framework-specific redirect to register via action_redirect)
        """

    @abc.abstractmethod
    def action_default(self):
        """
        Action to use when no specific one is available.
        """

    @abc.abstractmethod
    def action_disabled(self):
        """
        Action that shows an error message, indicating the action is not allowed.
        """
