import os
import pprint

from edwh.core.jwt_tools.jwt_py4web import EddieAuth
from yatl import PRE

from py4web import DAL, URL, Session, action

db = DAL("sqlite://example.db", migrate=True)
session = Session(secret="my secret key")

hosting_domain = os.environ["HOSTINGDOMAIN"]

auth = EddieAuth(
    session, db, jwt_provider=f"https://web2py.{hosting_domain}/init/jwt_auth"
)
auth.enable()


@action("index")
@action.uses(session, db)
def index_page():
    result = ""

    cnt = db(db.auth_user).count()
    result += f"There are {cnt} Users. <br/>"

    if auth.is_logged_in:
        url = URL("auth/logout")
        result += f"<a style='color: red' href='{url}'>Click here to log out</a>"
    else:
        url = URL("user")
        result += f"<a style='color: green' href='{url}'>Click here to log in</a>"

    return result


@action("user")
@action.uses(session, db, auth.user, auth.requires_still_exists)
def user_page():
    me = auth.get_user()

    query = db.auth_membership.user_id == me["id"]  # WHERE
    query &= db.auth_membership.group_id == db.auth_group.id  # JOIN

    groups = db(query).select(db.auth_group.ALL).as_dict()

    return str(
        PRE(
            pprint.pformat(
                {
                    "me": me,
                    "groups": groups,
                }
            )
        )
    )
