"""
This file defines the database models
"""
import os

from pydal import Field
from pydal.tools.tags import Tags
from pydal.validators import IS_EMAIL, IS_IN_SET

from py4web.core import URL, Fixture, redirect

from .common import auth
from .common_lts import DAL, lts_users_db, settings

# LTS groups
# requires auth_user first (setup in common.py)!
groups = Tags(lts_users_db.auth_user, "groups")

# groups: admin, guest (= no tags)
# e.g.:
# groups.add(1, 'admin')
POSSIBLE_GROUPS = ["admin"]  # no roles = guest

# LTS registrations

table_email_registration = lts_users_db.define_table(
    "email_registration",
    Field("email", "string", requires=IS_EMAIL(), required=True),
    Field("pagina", "string"),
    Field(
        "voorkeur",
        "string",
        required=True,
        requires=IS_IN_SET(["major", "minor", "patch"]),
    ),
    Field("subscribed_at", "datetime"),
    Field("unsubscribe_code", "string", required=True),
)

lts_users_db.commit()


def get_my_groups() -> set:
    """
    Return a list of groups the current user belongs to
    """
    me = auth.get_user()
    if not me:
        return set()
    return set(groups.get(me["id"]))


class IsAdminFixture(Fixture):
    def __init__(self):
        if not hasattr(self, "__prerequisites__"):
            self.__prerequisites__ = []

        self.__prerequisites__.extend([lts_users_db, auth, auth.user])

    def on_success(self, context):
        my_groups = get_my_groups()
        is_admin = "admin" in my_groups
        if not is_admin:
            # and this fixture is used -> not allowed!
            return redirect(URL("manage"))


is_admin = IsAdminFixture()


# if .sql exists: import it and don't migrate
# if it is missing, migrate and export sql


def setup_static_assets_db():
    # db file lives in /tmp so it can be replicated with multiple bjoerns
    db_file = os.path.join(
        settings.LTS_ASSETS_DB_FOLDER, f"{settings.LTS_ASSETS_NAME}.db"
    )
    # sql file lives in shared apps folder, so it can be mounted by docker
    sql_file = os.path.join(settings.DB_FOLDER, f"{settings.LTS_ASSETS_NAME}.sql")

    if os.path.exists(sql_file):
        migrate = False
        if os.path.exists(db_file):
            os.unlink(db_file)
        os.system(f"sqlite3 {db_file} < {sql_file}")
    else:
        # create new
        migrate = True
        if os.path.exists(db_file):
            os.unlink(db_file)
        # remove table file(s): (todo: is acf...1933 static?)
        table_files = ["acf6b24b7d71fa2118b63a9aacec1944_bundle_version.table"]
        for table_file in table_files:
            if os.path.exists(table_file):
                os.unlink(table_file)

    db = lts_assets_db = DAL(
        settings.LTS_ASSETS_DB_URI,
        folder=settings.LTS_ASSETS_DB_FOLDER,
        pool_size=settings.LTS_ASSETS_DB_POOL_SIZE,
        # migrate=migrate,
        # fake_migrate=False,
    )

    bundle_versions = lts_assets_db.define_table(
        "bundle_version",
        db.Field("filetype", "string"),  # css or js
        db.Field("version", "string"),  # e.g. 3.1.2
        db.Field("filename", "string"),  # bundle-3.1.2.js
        # just for ease of use:
        db.Field("major", "integer"),  # 3
        db.Field("minor", "integer"),  # 1
        db.Field("patch", "integer"),  # 2
        db.Field("hash", "string"),  # to compare
        db.Field("created_at", "datetime"),  # release date
        db.Field("changelog", "text"),  # we love a good documentation
        db.Field("contents", "text"),  # raw file contents
        migrate=migrate,
    )

    bundle_versions.contents.readable = False
    bundle_versions.contents.writable = False

    def update_sql(*_):
        lts_assets_db.commit()
        assert not os.system(f"sqlite3 {db_file} .dump > {sql_file}")

    # update .sql after change:
    bundle_versions._after_insert.append(update_sql)
    bundle_versions._after_update.append(update_sql)
    bundle_versions._after_delete.append(update_sql)

    return lts_assets_db


lts_assets_db = setup_static_assets_db()
