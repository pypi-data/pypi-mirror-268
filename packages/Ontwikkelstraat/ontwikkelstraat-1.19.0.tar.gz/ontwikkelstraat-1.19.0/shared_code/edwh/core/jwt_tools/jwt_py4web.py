import typing
from typing import Optional

import jwt
import yarl

from py4web import DAL, URL, Field, Session, action, redirect, request
from py4web.core import HTTP, Fixture
from py4web.utils.auth import Auth

from .shared import SharedAuth, urlsafe_base64_encode


class RequiresStillExistsFixture(Fixture):
    """
    Makes sure the currently logged in user is still valid on the server's end
        (i.e. the account is not deleted).

    If the account is invalid, redirects to the 'not authorized' page.

    Usage:
    ```
    auth = EddieAuth(session, db, 'jwt_provider=f"https://web2py.{hosting_domain}/init/jwt_auth")

    @action('some/path')
    @action.uses(auth.user, auth.requires_still_exists)
    def some_path(): ...
    ```
    """

    def __init__(self, auth: "EddieAuth"):
        self.auth = auth

    def is_valid(self):
        if not request.query.get("_edwh_jwt"):
            return self.auth.action_redirect(
                "validate", strip_query=True, _edwh_expire_after=5
            )

        try:
            data = self.auth.decode_jwt_response()
            return data["valid"]
        except jwt.ExpiredSignatureError:
            # you may try again
            return self.auth.action_redirect(
                "validate", strip_query=True, _edwh_expire_after=5
            )
        except Exception as e:
            # clearly not a valid response if something about it results in an error.
            print(f"JWT error: {e}", file=sys.stderr)
            return False

    # actively checks if the user wasn't deleted
    # todo: possibility to remove the (local) user if it doesn't exist anymore
    def on_request(self, context):
        if not self.is_valid():
            return self.auth.action_redirect("not_authorized")


class EddieAuth(Auth, SharedAuth):
    """
    The flow should work as following:
    1. use EddieAuth instead of normal (p4w) Auth, but this should be a drop-in replacement
        (in terms of fixtures etc). You only need to add a 'jwt_provider' provider url controller:
        'https://web2py.meteddie.nl/init/jwt_auth'
    2. the user is redirected to the JWT provider's login (/init/jwt_auth/login), which uses the regular w2p login
    3. a JWT token is generated, containing the basic user info and groups
    4. the user is redirected back to this app, where the JWT token is parsed.
    5. A auth_user entry is created or updated for the user (by ID), groups and memberships are also updated.
        (note: groups and memberships are not built-in to py4web,
        so they are added together with auth_user during `auth.define_tables()`)
    6. Other auth actions are disabled or redirected to the provider when possible.
    """

    session: Session
    db: DAL

    def __init__(
        self,
        session: Session,
        db: DAL,
        jwt_provider: str,
        # defaults:
        define_tables=True,
        sender=None,
        use_username=True,
        use_phone_number=False,
        registration_requires_confirmation=True,
        registration_requires_approval=False,
        inject=True,
        extra_fields=None,
        login_expiration_time=3600,  # seconds
        password_complexity="default",
        block_previous_password_num=None,
        allowed_actions=None,
        use_appname_in_redirects=None,
        password_in_db=True,
        two_factor_required=None,
        two_factor_send=None,
    ):
        """
        See Auth().

        Extra: jwt_provider (required), url path to a web2py controller (with at least a login and register function)
        """

        self.jwt_provider = yarl.URL(jwt_provider)

        super().__init__(
            session,
            db,
            define_tables=define_tables,
            sender=sender,
            use_username=use_username,
            use_phone_number=use_phone_number,
            registration_requires_confirmation=registration_requires_confirmation,
            registration_requires_approval=registration_requires_approval,
            inject=inject,
            extra_fields=extra_fields,
            login_expiration_time=login_expiration_time,
            password_complexity=password_complexity,
            block_previous_password_num=block_previous_password_num,
            allowed_actions=allowed_actions,
            use_appname_in_redirects=use_appname_in_redirects,
            password_in_db=password_in_db,
            two_factor_required=two_factor_required,
            two_factor_send=two_factor_send,
        )

    def define_tables(self):
        super().define_tables()
        db = self.db
        if "auth_group" not in db.tables:
            db.define_table("auth_group", Field("role"), Field("description"))
        if "auth_membership" not in db.tables:
            db.define_table(
                "auth_membership",
                Field("user_id", "reference:auth_user"),
                Field("group_id", "reference:auth_group"),
            )

    def enable(self, route: str = "auth", **_):
        """Enables Auth, aka generates login/logout/register/etc API pages"""
        self.route = route = route.rstrip("/")

        actions = {
            "login": self.action_login,
            "register": self.action_register,
            "profile": self.action_redirect,
            "change_password": self.action_redirect,
            "retrieve_password": self.action_redirect,
            "not_authorized": self.action_default,
            "logout": self.action_logout,
        }

        # expose one API route that catches all:
        @action(route, method=["GET", "POST"])
        @action(f"{route}/<path:path>", method=["GET", "POST"])
        @action.uses(self.db, self.session)
        def _(
            path: str = None,
        ):
            if request.query.get("_edwh_jwt"):
                return self.handle_jwt_response()

            parts = path.split("/") if path else []
            if not (parts and parts[0] in actions):
                return self.action_disabled()
            else:
                return actions[parts[0]]()

    @property
    def requires_still_exists(self):
        return RequiresStillExistsFixture(self)

    def decode_jwt_response(
        self,
        key="_edwh_jwt",
        issuer: Optional[str] = None,
        audience: Optional[str] = None,
        leeway: Optional[int] = None,
        **kwargs: typing.Any,
    ):
        return super().decode_jwt_response(
            request.query[key],
            issuer=issuer,
            audience=audience,
            leeway=leeway,
            **kwargs,
        )

    def login_user(self, user: dict | int | str):
        if not isinstance(user, (int, str)):
            user = user["id"]

        self.store_user_in_session(user)

    def go_next(self, url: str = None):
        """
        Redirect to the 'next' url (either via the 'url' arg, _next query param or otherwise to Index.)
        """
        return redirect(url or request.query.get("next") or URL("index"))

    def action_redirect(
        self, action: str = None, strip_query: bool = False, **extra_data
    ):
        """
        Redirect an action to the auth provider (login, register, profile)

        You can use '_edwh_expire_after' to expire the JWT after some amount of seconds (default: 30).
        """
        ombott_request = {**request["ombott.request"]}

        action = action or request["route.url_args"]["path"]

        host = ombott_request["HTTP_HOST"]
        path = ombott_request["PATH_INFO"]
        query = ombott_request.get("QUERY_STRING")
        query = f"?{query}" if query else ""

        # ombott sometimes has 'ombott.request.url' but not consistently, so build it up here:
        target_url = f"https://{host}{path}{query}"

        print(f"target_url = {target_url[:100]}")

        if strip_query:
            target_url = target_url.split("?")[0]

        # redirect to JWT provider:

        return redirect(
            self._jwt_url(
                action, _edwh_target_url=urlsafe_base64_encode(target_url), **extra_data
            )
        )

    def action_login(self):
        """
        Redirect to the jwt auth provider unless already logged in.
        """
        if self.is_logged_in:
            return self.go_next()
        return self.action_redirect("login")

    def action_register(self):
        """
        Redirect to the jwt auth provider unless already logged in.
        """
        if self.is_logged_in:
            return self.go_next()
        return self.action_redirect("register")

    def action_logout(self):
        # del self.session['user']
        self.session.clear()
        if "HTTP_REFERER" in request.environ:
            return redirect(request.environ["HTTP_REFERER"])
        else:
            return redirect(URL("index"))

    def action_default(self):
        raise HTTP(400, "Action not supported")

    def action_disabled(self):
        """
        Don't perform any action but show an 'unsupported action' message
        """
        raise HTTP(403, "Action not allowed")
