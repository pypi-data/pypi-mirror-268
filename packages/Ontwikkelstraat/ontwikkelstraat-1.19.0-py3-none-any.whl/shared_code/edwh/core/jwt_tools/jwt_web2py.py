import os
import sys
import typing
from typing import Optional

import jwt
import yarl
from gluon import URL, current, redirect
from gluon.tools import Auth
from pydal import DAL

from .shared import SharedAuth, urlsafe_base64_encode


class DontUseMe:
    """
    You should use 'current.request' instead!!!
    """


request = DontUseMe()  # Use current.request instead!


class EddieAuth(Auth, SharedAuth):
    """
    The flow should work as following:
    1. use EddieAuth instead of normal (w2p) Auth, but this should be a drop-in replacement
        (in terms of decorators etc). You only need to add a 'jwt_provider' provider url controller:
        'https://web2py.meteddie.nl/init/jwt_auth'
    2. the user is redirected to the JWT provider's login (/init/jwt_auth/login), which uses the regular w2p login
    3. a JWT token is generated, containing the basic user info and groups
    4. the user is redirected back to this app, where the JWT token is parsed.
    5. A auth_user entry is created or updated for the user (by ID), groups and memberships are also updated.
    6. Other auth actions are disabled or redirected to the provider when possible.
    """

    def __init__(
        self,
        db: DAL,
        jwt_provider: str,
        environment=None,
        mailer=True,
        hmac_key=None,
        controller="default",
        function="user",
        cas_provider=None,
        signature=True,
        secure=False,
        csrf_prevention=True,
        propagate_extension=None,
        url_index=None,
        jwt=None,
        host_names=None,
    ):
        """
        See Auth().

        Extra: jwt_provider (required), url path to a web2py controller (with at least a login and register function)
        """

        if jwt or not jwt_provider:
            raise NotImplementedError(
                "Default JWT functionality is replaced. Use a `jwt_provider` instead!"
            )

        self.jwt_provider = yarl.URL(jwt_provider)

        super().__init__(
            db=db,
            environment=environment,
            controller=controller,
            function=function,
            cas_provider=cas_provider,
            hmac_key=hmac_key,
            signature=signature,
            secure=secure,
            csrf_prevention=csrf_prevention,
            propagate_extension=propagate_extension,
            mailer=mailer,
            url_index=url_index,
            host_names=host_names,
        )

    def requires_still_exists(self):
        """
        Makes sure the currently logged in user is still valid on the server's end
            (i.e. the account is not deleted).

        If the account is invalid, redirects to the 'not authorized' page.

        Usage:
        ```
        auth = EddieAuth(session, db, 'jwt_provider=f"https://web2py.{hosting_domain}/init/jwt_auth")

        @auth.requires_still_exists()
        def some_path(): ...
        ```
        """

        # actively checks if the user wasn't deleted
        # todo: possibility to remove the (local) user if it doesn't exist anymore

        def condition():
            if not current.request.vars.get("_edwh_jwt"):
                return self.action_redirect(
                    "validate", strip_query=True, _edwh_expire_after=5
                )

            try:
                data = self.decode_jwt_response()
                return data["valid"]
            except jwt.ExpiredSignatureError:
                # you may try again
                return self.action_redirect(
                    "validate", strip_query=True, _edwh_expire_after=5
                )
            except Exception as e:
                # clearly not a valid response if something about it results in an error.
                print(f"JWT error: {e}", file=sys.stderr)
                return False

        return self.requires(condition)

    def decode_jwt_response(
        self,
        key="_edwh_jwt",
        issuer: Optional[str] = None,
        audience: Optional[str] = None,
        leeway: Optional[int] = None,
        **kwargs: typing.Any,
    ):
        return super().decode_jwt_response(
            current.request.vars[key],
            issuer=issuer,
            audience=audience,
            leeway=leeway,
            **kwargs,
        )

    def go_next(self, url: str = None):
        """
        Redirect to the 'next' url (either via the 'url' arg, _next query param or otherwise to Index.)
        """
        return redirect(url or current.request.vars.get("_next") or URL("index"))

    def action_redirect(
        self, action: str = None, strip_query: bool = False, **extra_data
    ):
        """
        Redirect an action to the auth provider (login, register, profile)

        You can use '_edwh_expire_after' to expire the JWT after some amount of seconds (default: 30).
        """
        action = action or current.request.args[0]

        hostingdomain = os.environ["HOSTINGDOMAIN"]
        uri: str = current.request.env.request_uri
        if strip_query:
            uri = uri.split("?")[0]
        target_url = f"https://web2py.{hostingdomain}" + uri
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
        if self.is_logged_in():
            return self.go_next()
        return self.action_redirect("login")

    def action_register(self):
        """
        Redirect to the jwt auth provider unless already logged in.
        """
        if self.is_logged_in():
            return self.go_next()
        return self.action_redirect("register")

    def action_default(self):
        return super().__call__()

    def action_disabled(self):
        """
        Don't perform any action but show an 'unsupported action' message
        """
        return f"Unsupported action {current.request.args}"

    def __call__(self):
        """
        Functionality of auth() via /user.

        Looks up the right action from the action_ functions above ^
        """
        if current.request.vars["_edwh_jwt"]:
            return self.handle_jwt_response()

        # else, default behavior:

        actions = {
            "login": self.action_login,
            "register": self.action_register,
            "profile": self.action_redirect,
            "change_password": self.action_redirect,
            "retrieve_password": self.action_redirect,
            "not_authorized": self.action_default,
            "logout": self.action_default,
        }

        if not (current.request.args and current.request.args[0] in actions):
            # return super().__call__()
            return self.action_disabled()
        else:
            return actions[current.request.args[0]]()
