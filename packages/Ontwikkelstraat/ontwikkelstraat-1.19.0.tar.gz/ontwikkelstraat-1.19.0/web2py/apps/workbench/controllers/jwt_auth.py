"""
Usage:
```
auth = EddieAuth(
    db,
    jwt_provider=f"https://web2py.{hosting_domain}/init/jwt_auth",
)
```
"""
import time
import typing

import yarl
from edwh.core.jwt_tools import jwt_encode, urlsafe_base64_decode

if typing.TYPE_CHECKING:
    from gluon import URL, auth, redirect, request

    from ..models.db import db


def send_back(payload: dict, with_next=True):
    """
    Send the user back after login, to the URL specified in '?_edwh_target_url',
        with the payload and an expiry time.
    """
    target_url = yarl.URL(urlsafe_base64_decode(request.vars["_edwh_target_url"]))

    expire_after_s = int(request.vars.get("_edwh_expire_after") or 30)

    if with_next:
        payload["next"] = str(target_url)

    encoded_jwt = jwt_encode(
        {
            "data": payload,
            # meta:
            "exp": int(time.time()) + expire_after_s,
        }
    )

    target_url %= {"_edwh_jwt": encoded_jwt}

    return redirect(str(target_url))


@auth.requires_login()
def login():
    """
    After login, build up a payload with user info.
    """
    me = auth.user

    query = auth.db.auth_membership.user_id == me.id  # where
    query &= auth.db.auth_group.id == auth.db.auth_membership.group_id  # join

    groups = auth.db(query).select(auth.db.auth_group.ALL)

    payload = {
        "me": me.as_dict(),
        "groups": groups.as_list(),
    }

    return send_back(payload)


def register():
    """
    Redirect to the native login page, with a "?_next", which ends up at the 'login' function above.
    """
    return redirect(
        URL(
            "user",
            "register",
            vars={
                "_next": URL(
                    "jwt_auth",
                    "login",
                    vars={"_edwh_target_url": request.vars["_edwh_target_url"]},
                )
            },
        )
    )


def profile():
    """
    Redirect to the profile edit page. Includes a ?next, but after saving it just reloads the profile edit page.
    """
    return redirect(
        URL(
            "user",
            "profile",
            vars={
                "_next": URL(
                    "jwt_auth",
                    "login",
                    vars={"_edwh_target_url": request.vars["_edwh_target_url"]},
                )
            },
        )
    )


def change_password():
    """
    Redirect to the password edit page. Includes a ?next, but after saving it just reloads the profile edit page.
    """
    return redirect(
        URL(
            "user",
            "change_password",
            vars={
                "_next": URL(
                    "jwt_auth",
                    "login",
                    vars={"_edwh_target_url": request.vars["_edwh_target_url"]},
                )
            },
        )
    )


def retrieve_password():
    """
    Redirect to the password reset page.
    """
    return redirect(
        URL(
            "user",
            "retrieve_password",
            vars={
                "_next": URL(
                    "jwt_auth",
                    "login",
                    vars={"_edwh_target_url": request.vars["_edwh_target_url"]},
                )
            },
        )
    )


def not_authorized():
    """
    Redirect to the not authorized page.
    """
    return redirect(
        URL(
            "user",
            "not_authorized",
        )
    )


@auth.requires_login()
def validate():
    """
    Check if the current user is still valid (logged in, not removed)
    """
    try:
        is_valid = bool(db.auth_user(auth.user.id))
    except:
        is_valid = False

    payload = {
        "valid": is_valid,
    }

    return send_back(payload)
