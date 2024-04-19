# sourcery skip: remove-redundant-if
# noinspection PyUnreachableCode
if False:
    from web2py.gluon import *

    from ..models.webtest_jwt_support import webtest_added_data

    request = current.request
    response = current.response
    session = current.session
    cache = current.cache
    T = current.T
    import attrs
    from edwh.core.backend import *
    from pydal import *

    from ..models.article_importers import *
    from ..models.db import *
    from ..models.db_workbench import *
    from ..models.db_z_backend import *
    from ..models.menu import *
    from ..models.processes import *
    from ..models.scheduler import *
    from ..models.tags import *

    backend: Web2pyBackend

    database: DAL


def echo_edwh_webtest_data():  # NO_TEST_REDIRECT_ON
    # see webtest_jwt_support.py
    return response.json({**webtest_added_data, "seen": True})


def assign_roles_to_user():  # NO_TEST_REDIRECT_ON
    """securely apply roles to a user using webtest_added_data."""
    user_email, roles = webtest_added_data["email"], webtest_added_data["roles"]
    user = db.auth_user(email=user_email)
    if not user:
        raise HTTP(404, "User not found")
    if not roles:
        raise HTTP(400, "No roles given")
    # delete current roles
    db(db.auth_membership.user_id == user.id).delete()
    for role in roles:
        db.auth_membership.insert(
            user_id=user.id, group_id=db.auth_group(role=role.strip()).id
        )
    db.commit()
    return "Okay"


def remove_user_from_db():  # NO_TEST_REDIRECT_ON
    """securely remove a user from the database using webtest_added_data."""
    user_email = webtest_added_data["email"]
    count = db(db.auth_user.email == user_email).delete()
    if not count:
        raise HTTP(404, "User not found")
    db.commit()
    return "Okay"


def remove_item_from_db():  # NO_TEST_REDIRECT_ON
    """securely remove a user from the database using webtest_added_data."""
    item_gid = webtest_added_data["item_gid"]
    count = database(database.item.gid == item_gid).delete()
    if not count:
        raise HTTP(404, "Item not found")
    db.commit()
    return "Okay"


def item_from_backend():  # NO_TEST_REDIRECT_ON
    item = Item.load(database, webtest_added_data["item_gid"])
    return response.json(edwh_asdict(item))
