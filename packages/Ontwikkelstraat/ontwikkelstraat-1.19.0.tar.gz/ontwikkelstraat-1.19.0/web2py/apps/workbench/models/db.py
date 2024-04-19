# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
import datetime
import importlib
import json  # noqa
import os
import random
import re
import string
import sys
import uuid

import bcrypt
from diskcache import Index
from edwh.core.data_model import OrganisationPriority, setup_db_tables, Visibility
from gluon.tools import Auth, PluginManager, Service, prettydate
from gluon.validators import Validator

if "/shared_code" not in sys.path:
    sys.path.insert(0, "/shared_code")
import edwh.core.backend

if "reload" in request.vars:
    edwh.core.backend = importlib.reload(edwh.core.backend)

from edwh.core.backend import *
from edwh.core.data_model import OrganisationPriority, setup_db_tables

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
# myconf = AppConfig(reload=True)
myconf = {
    "db.uri": "sqlite://storage.sqlite",
    "db.migrate": True,
    "host.name_in_email": "web2py.meteddie.nl",
    "workbench.db_uri": "sqlite://workbench.sqlite",
    "forms.formstyle": "bootstrap3_inline",
}

db = DAL(
    myconf.get("db.uri"),
    pool_size=5,
    migrate_enabled=myconf.get("db.migrate"),
    check_reserved=["sqlite"],
)

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ["*"] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get(
    "forms.formstyle"
)  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get("forms.separator") or ""

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------


# host names must be a list of allowed host names (glob syntax allowed)
HOSTINGDOMAIN = os.getenv("HOSTINGDOMAIN")
auth = Auth(
    db,
    host_names=f"localhost:*, 127.0.0.1:*, web2py.{HOSTINGDOMAIN}:*, {HOSTINGDOMAIN}:* ,*",
)
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False, signature=False)

# IOLDB_DOMAINS = ["cito.nl", "kennisnet.nl", "slo.nl", "ptvt.nl", "vo-content.nl", "beeldengeluid.nl"]
# easier for .endswith:
IOLDB_DOMAINS = (
    "@cito.nl",
    "@kennisnet.nl",
    "@slo.nl",
    "@ptvt.nl",
    "@vo-content.nl",
    "@beeldengeluid.nl",
)


def possibly_assign_ioldb_role(user, id):
    # e.g. robinvandernoord@cito.nl -> group ioldb
    if not user.email.lower().endswith(IOLDB_DOMAINS):
        # do nothing special with these users
        return
    # ensure group exists:
    if not db(db.auth_group.role == "ioldb").count():
        auth.add_group(
            "ioldb", "Users from specific domains can access the IOL database"
        )

    auth.add_membership("ioldb", id)


db.auth_user._after_insert.append(possibly_assign_ioldb_role)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
SMTP_FAKE = os.environ.get("SMTP_FAKE") == "1"

SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = os.environ.get("SMTP_PORT", "587")
SMTP_URI = f"{SMTP_SERVER}:{SMTP_PORT}"

SMTP_SENDER = os.environ.get("SMTP_SENDER")

if not SMTP_SENDER and SMTP_FAKE:
    # required even for logging 'client'
    SMTP_SENDER = "console@edwh.nl"

SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
SMTP_LOGIN = f"{SMTP_USER}:{SMTP_PASSWORD}" if SMTP_USER else None

SMTP_TLS = os.environ.get("SMTP_TLS") == "1"
SMTP_SSL = os.environ.get("SMTP_SSL") == "1"
mail = auth.settings.mailer
mail.settings.server = (
    "logging"
    if request.is_local or SMTP_FAKE
    else (SMTP_URI or myconf.get("smtp.server"))
)
mail.settings.sender = SMTP_SENDER or myconf.get("smtp.sender")
mail.settings.login = SMTP_LOGIN or myconf.get("smtp.login")
mail.settings.tls = SMTP_TLS or myconf.get("smtp.tls", False)
mail.settings.ssl = SMTP_SSL or myconf.get("smtp.ssl", False)

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True


# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)


def new_uuid():
    return str(uuid.uuid4())


# todo: create an admin or graphql interface for this stuff


def setup_required_roles():
    roles = {
        "admin": "Admins",
        "education_warehouse": "Eddies",
        "minion": "Minions",
        "remove_stickers": "Remove stickers permission",
        "edit_tag_structure": "Edit tag structure permission",
    }

    if db(db.auth_group.role.belongs(roles)).count() == len(roles):
        # every required role already exists!
        return

    print("Missing some roles, adding/updating them.")

    for role, description in roles.items():
        db.auth_group.update_or_insert(
            db.auth_group.role == role, role=role, description=description
        )


def setup_required_users():
    if db(db.auth_user).count() != 0:
        # a user already exists!
        return

    print("Clean database: adding Remco et al.")

    remco = db.auth_user.insert(
        firstname="Remco",
        lastname="Boerma",
        email="remco.b@educationwarehouse.nl",
        password="pbkdf2(1000,20,sha512)$8978be935d4b9203$d3447405ad29876f754574d8e12983f4a4559b24",
    )
    mike = db.auth_user.insert(
        firstname="Mike",
        lastname="Hoppezak",
        email="mike.h@educationwarehouse.nl",
        password="pbkdf2(1000,20,sha512)$969f8ba19a4cf748$c12090293d380795df9b92860405ed7f8e5510b5",
    )
    robin = db.auth_user.insert(
        firstname="Robin",
        lastname="van der Noord",
        email="robin.vdn@educationwarehouse.nl",
        password="pbkdf2(1000,20,sha512)$8843615b73be958f$87a8b09f41a0b1e3e668150ad73f7157657bc0cb",
    )
    # groups already exist thanks to 'setup_required_roles'.
    admin_id = db.auth_group(role="admin")
    eddie_id = db.auth_group(role="education_warehouse")

    for user_id in [remco, mike, robin]:
        db.auth_membership.insert(user_id=user_id, group_id=admin_id)
        db.auth_membership.insert(user_id=user_id, group_id=eddie_id)


@cache(
    "setup_roles_and_users", cache_model="ram", time_expire=60 * 60 * 24 * 7
)  # = 1 week of caching
def setup_roles_and_users():
    setup_required_roles()
    setup_required_users()
    db.commit()


setup_roles_and_users()

database = DAL(
    os.getenv("POSTGRES_URI"),
    migrate_enabled=False,  # LET OP , ALTIJD OP FALSE!!
    check_reserved=["sqlite"],
    pool_size=5,
)


def update_field(field, **attrs):
    "Use to update fiels in a similar manner to the field constructor."
    for k, v in attrs.items():
        setattr(field, k, v)


setup_db_tables(database, enable_versioning=False)
for tablename in database._tables:
    table = database[tablename]
    if field := getattr(table, "last_saved_by", None):
        field.readable = True
        field.writable = False
        field.default = auth.user.email if auth.user else None
        # also forced in the effective_dated_grid function
    if field := getattr(table, "last_saved_when", None):
        field.writable = False
        field.default = request.now

database.organisation.effdt.default = request.now


def pretty_author(value, row):
    user = (
        database(database.user.gid == value)
        .select(cache=(cache.ram, 3600), cacheable=True)
        .first()
    )
    return XML(
        "<strong>{name}</strong><br/>{email}".format(**user.as_dict())
        if user
        else "Verwijderd"
    )


class IS_VALID_END_DATE(Validator):
    def __init__(
        self, begin, error_message="This date is invalid compared to begin date."
    ):
        self.begin = begin
        self.error_message = error_message

    def __call__(self, value):
        if value is None or value == "":
            return value, None
        if value < self.begin and value is not None:
            self.error_message = "Praktijk kan niet eerder eindigen dan dat het begint."
            return value, self.error_message
        else:
            return value, None


update_field(database.item.author, represent=pretty_author)
update_field(
    database.item.upto_when, requires=IS_VALID_END_DATE(request.vars.since_when)
)
database.item.overdragen = Field.Virtual(
    "overdragen",
    lambda row: XML(A("overdragen", _href=URL(f="overdragen", args=[row.item.gid]))),
)

database.item.tags.format = lambda row, value: "T" + value
database.item.tags.requires = IS_EMPTY_OR(
    IS_IN_DB(database, "tag.gid", "%(name)s", multiple=True)
)

update_field(database.user.platform)
database.user.Author = Field.Virtual(
    "Author",
    lambda row: XML(
        A(
            "{}'s items".format(row.item.name),
            _href=URL(f="useritems", args=[row.item.author]),
        )
    ),
)
update_field(
    database.user.reset_key,
    default=None,
    writable=False,
    readable=False,
    label="Wachtwoord reset sleutel.",
)

is_admin = auth.has_membership("admin", cached=True)
is_eddie = auth.has_membership(role="education_warehouse", cached=True)
is_minion = auth.has_membership(role="minion", cached=True)
may_remove_stickers = is_admin or auth.has_membership(
    role="remove_stickers", cached=True
)
may_edit_tag_structure = is_admin or auth.has_membership(
    role="edit_tag_structure", cached=True
)

if is_admin or is_eddie:
    organisation_priority_level = OrganisationPriority.EDDIE.value
elif is_minion:
    organisation_priority_level = OrganisationPriority.MINION.value

is_ioldb = auth.has_membership(role="ioldb", cached=True)


def hash_password(password):
    salt = "$2a$10$UFkhEG5ZjcRS57cXAmg9CO".encode("utf-8")
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def generate_reset_key(size=15, chars=string.ascii_uppercase + string.digits):
    """Generates a temporary reset key"""
    # chars_list is de lijst met karakters zonder [01345OQLIAES]
    chars_list = re.sub("[01345OQLIAES]", "", chars)
    # temp_pw is het tijdelijke wachtwoord uit de chars_list
    temp_pw = "".join(random.choice(chars_list) for _ in range(size))
    return temp_pw


# copy van de basepaddo
def prepare_payload_for_dispatch(source, event_name, payload):
    """Dispatch an event from the current paddo with auto enhanced payload.

    :param event_name: which event to raise
    :type event_name: str
    :param payload: the payload to send with this event
    :type payload: object

    :returns None

    payload is enhanced with:
        * gid: new uuid
        * value: the original payload parameter, meant to be extracted in the handler
        * event_name : the name of the event given to raise
        * source: the self.name of the paddo.
        * ts: current timesamp in UTC zone

    uses: self.__ew_dispatch
    """
    # ts = datetime.datetime.timestamp(datetime.datetime.now())
    ts = datetime.datetime.timestamp(datetime.datetime.utcnow())
    return {
        "gid": uuid.uuid4(),
        "value": payload,
        "source": source,
        "event_name": event_name,
        "timestamp": ts,
    }


def get_sticker_collections():
    # TODO: dit uit de database halen op basis van tag structuur
    # NIET op basis van sticker tabel, want deze volgt pas als er een attachment
    # voor geupload is.
    STICKERS_GID = "67ba8cd8-b564-4cb4-b1bc-10364c5edf16"
    stickers_children = database.tag(gid=STICKERS_GID).children
    sticker_rows = database(database.tag.gid.belongs(stickers_children)).select()
    # stickers_by_name = {'test-sticker':'1e4184c9-29d5-40e1-9e51-673ef88a3e3d'}
    stickers_by_name = {sticker.name: sticker.gid for sticker in sticker_rows}
    stickers_by_gid = {v: k for k, v in stickers_by_name.items()}
    image_uri_by_tag_gid = {
        row.tag_gid: database.attachment(gid=row.attachment_gid).b2_uri
        for row in database(database.sticker).select()
    }
    return stickers_by_gid, stickers_by_name, image_uri_by_tag_gid


def get_first_eddie_session():
    eddie = database.user(email="eddie@educationwarehouse.nl")
    return (
        database(database.session.user_gid == eddie.gid)
        .select(orderby=db.session.started)
        .first()
    )


def get_last_remco_session():
    remco = database.user(email="remco@roc.nl")
    return (
        database(database.session.user_gid == remco.gid)
        .select(orderby=database.session.started)
        .first()
    )


update_field(database.attachment.attachment, writable=False, readable=False)


def add_attachment_to_item(item_gid, attachment_gid):
    item = database.item(gid=item_gid)
    attachments = item.attachments or []
    old_attachments = attachments.copy()

    attachments.append(attachment_gid)
    item.update_record(attachments=attachments)
    database.commit()
    backend.applog.update_item(
        item.gid,
        by_eddie_email=auth.user.email,
        fields_before={"attachments": old_attachments},
        fields_after={"attachments": attachments},
    )


def last_opened_warning(key_prefix: str, key: str = None):
    last_opened = Index("/shared_cache/last_opened")
    last_arg = request.args[-1] if request.args else None
    key = str(last_arg) if (not key) and last_arg and str(last_arg).isdigit() else None
    try:
        key = str(uuid.UUID(last_arg))
    except:
        pass
    if not key:
        return None

    last_opened_key = key_prefix + "-" + key
    warning = None
    if last_opened_key:
        previous_visit = last_opened.get(last_opened_key, None)
        # if there is a registered previous visit and it's not the current users visit, add a warning
        if previous_visit and previous_visit.get("email", None) != auth.user.email:
            seconds_since = (request.now - previous_visit["when"]).total_seconds()
            since = prettydate(previous_visit["when"])
            if seconds_since <= 300:
                alert_level = "danger"
            elif seconds_since > 300 and seconds_since < 600:
                alert_level = "warning"
            elif seconds_since >= 600 and seconds_since <= 3600:
                alert_level = "info"
            elif seconds_since > 3600 and seconds_since < 24 * 3600:
                alert_level = "light"
            else:
                alert_level = None
            warning = (
                SPAN(
                    f'Let op: activiteit door {previous_visit["name"]} sinds/op {since}',
                    _class=f"alert alert-{alert_level}",
                )
                if alert_level
                else ""
            )
        last_opened[last_opened_key] = {
            "email": auth.user.email,
            "when": request.now,
            "name": f"{auth.user.first_name.capitalize()} {auth.user.last_name.capitalize()}",
        }
    return warning
