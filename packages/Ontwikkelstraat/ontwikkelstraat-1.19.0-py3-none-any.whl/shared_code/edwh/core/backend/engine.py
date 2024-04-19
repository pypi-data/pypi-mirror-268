import base64
import json
import mimetypes
import os
import random
import re
import sys
from contextlib import contextmanager
from datetime import date, datetime, timedelta
from enum import Enum, auto
from hashlib import blake2b, md5
from typing import Any, Callable, Pattern, Union
from uuid import UUID, uuid4

import bcrypt
import dill
import jwt
import markdown2
from attrs import asdict, define, field
from edwh.core.applog.signalemitter import SignalEmitter
from edwh.core.applog.sink import SignalSink
from edwh.core.backend.ntfy_sh import Priority, onbekend, warning
from edwh.core.data_model import (
    DEFAULT_EXCLUDED_VISIBILITY,
    DEFAULT_INCLUDED_VISIBILITY,
    DEFAULT_ITEM_VISIBILITY,
    EDUCATION_LEVEL,
    EDUCATION_TYPE,
    OrganisationPriority,
    Visibility,
)
from edwh.core.pgcache import Magic, cached, fromdb, todb
from psycopg2.errors import UniqueViolation
from pydal import DAL
from pydal.objects import Query, Table
from slugify import slugify

PROGRESS_GIF = (
    "https://f003.backblazeb2.com/file/nl-meteddie-delen-permalinkable/progress.gif"
)


def required_env(key):
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"Required key {key} not found.")
    return value


TAG_GID_USER_SELECTABLE = "dcaea9b5-879e-43f7-8860-67579e10166e"

Row = DAL.Row
Rows = DAL.Rows

PLATFORM = "SvS"
BACKEND_ME = "backend_me"
BACKEND_SESSION_TOKEN = "backend_session_token"
EDDIE_TOKEN = "eddie_token"
EDDIE_GID = "c8831058-34a3-42f1-ad83-eaf84aef2a30"
BACKEND_TIMEOUT = 60

CLICK_TRACKER_DOMAIN: str = "c." + required_env("HOSTINGDOMAIN")

MARKDOWN_LINK_RE: Pattern[str] = re.compile(r"\[(.*?)\]\((.*?)\)")
# https://regex101.com/r/DAA8ww/1 voor onderstaande "mark grubers' regexp for python"
REGULAR_LINK_RE: Pattern[str] = re.compile(
    r"\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'\"\\\/.,<>?\xab\xbb\u201c\u201d\u2018\u2019]))"
)
FIRST_SENT_RE: Pattern[str] = re.compile(r"([.?]) [A-Z0-9]")


class EdwhException(Exception):
    pass


class SecurityException(EdwhException):
    pass


class NotFoundException(EdwhException, KeyError):
    pass


class SortOrder(Enum):
    RANDOM = 0
    RECENT_ASC = 1
    RECENT_DESC = 2
    POPULARITY_ASC = 3
    POPULARITY_DESC = 4
    VIEWS_ASC = 5
    VIEWS_DESC = 6
    THUMBS_ASC = 7
    THUMBS_DESC = 8
    # STARS = 2
    # see other todo: add for faves, marks, tags, etc


class BackendError(RuntimeError):
    pass


def new_password():
    characters = (
        "abcdefghkmnpqrwxy24678abcdefghkmnpqrwxy24678abcdefghkmnpqrwxy24678!#$%"
    )
    password = "".join(random.choice(characters) for x in range(random.randint(8, 16)))
    return password.upper()


def hash_password(password):
    salt = "$2a$10$UFkhEG5ZjcRS57cXAmg9CO".encode("utf-8")
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def generate_email_verification_code(email: str) -> int:
    """Returns a 6 digit email validation code based on the email adres.

    This code should be hard to guess, so using some hashmagic with an arbitrary seed.
    """
    import hashlib

    h = hashlib.sha3_512()
    h.update(required_env("EMAIL_VERIFICATION_SEED").encode())
    h.update(email.strip().lower().encode())
    return str(int(h.hexdigest(), 16))[-6:]


def hash_gid(gid: UUID) -> str:
    """One-way shortener for gids, primarily for session_gid exposure, for exmaple in url tracking"""
    return blake2b(
        gid.bytes,
        digest_size=10,
    ).hexdigest()


def hash_url(url: str) -> str:
    """One-way shortener for gids, primarily for session_gid exposure, for exmaple in url tracking"""
    return blake2b(url.encode("utf-8"), digest_size=10).hexdigest()


def shorten_gid(gid: UUID) -> str:
    """Shorten a gid object to a shorter base64 representation"""
    return base64.b64encode(gid.bytes, b"+_").decode("utf-8").rstrip("=")


def make_uuid(s: str | UUID):
    try:
        return UUID(s)
    except:
        return s


def prepare_firstname(firstname: str):
    """capitalize the firstname if it wasn't capitalized. If it is, assume the user knows best, like "Rober-Jan" """
    firstname = firstname.strip()
    if firstname == firstname.lower():
        # no capitalization in name
        firstname = " ".join(n.capitalize() for n in firstname.split(" "))

    return firstname


def prepare_lastname(lastname: str):
    """
    Capitalize using Dutch surname capitalization rules, unless lastname already contains a capital.
    In that case, 'user knows best'.
    """
    lastname = lastname.strip()
    if lastname != lastname.lower():
        # if user used any capitalisation, assume they know best.
        # van der Knoop -> van der Knoop
        return lastname

    if " " not in lastname:
        # willems -> Willems
        return lastname.capitalize()

    # van der knoop -> van der Knoop

    lastname_parts = lastname.split(" ")
    official_lastname = lastname_parts[-1]
    # capitalize the offical lastname if it wasn't capitalized. If it is, assume the user knows best, like "Bladie-Pir"
    if official_lastname.lower() == official_lastname:
        official_lastname = official_lastname.capitalize()

    lastname_prefix = " ".join(lastname_parts[:-1]).lower()
    return f"{lastname_prefix} {official_lastname}"


def load_json_or_is_dict(j: str | dict | None):
    if j is None:
        return {}
    if isinstance(j, dict):
        return j
    return json.loads(j)


def serialize_backend_types(instance, field, value):
    """
    Used for attrs.asdict magic.

    See https://www.attrs.org/en/stable/api.html#attr.asdict :

    value_serializer (Optional[callable]) – A hook that is called for every attribute or
    dict key/value. It receives the current instance, field and value and must return the
    (updated) value. The hook is run after the optional filter has been applied.

    web2py example:

    def demo():
        from attrs import asdict

        # return response.json(asdict(backend.pratices(search=request.vars.q)))
        return response.json(
            asdict(
                backend.pratices(search=request.vars.q),
                value_serializer=serialize_backend_types,
            )
        )

    """
    if isinstance(value, UUID):
        return str(value)
    elif isinstance(value, bytes):
        return value.decode()
    elif isinstance(value, Visibility):
        return value.value
    return value


def filter_backend_types(attr, value):
    if attr.name.startswith("_"):
        return False
    elif attr.name == "backend":
        return False
    return True


def edwh_asdict(instance):
    return asdict(
        instance,
        value_serializer=serialize_backend_types,
        filter=filter_backend_types,
    )


def human_friendly_timedelta(delta: timedelta) -> str:
    weken, rem = divmod(delta.total_seconds(), 86400 * 7)
    dagen, rem = divmod(rem, 86400)
    uren, rem = divmod(rem, 3600)
    minuten, seconden = divmod(rem, 60)
    if seconden < 1:
        seconden = 1
    locals_ = locals()

    def label(n, magnitude):
        if n == 1:
            return {
                "weken": "week",
                "dagen": "dag",
                "uren": "uur",
                "minuten": "minuut",
                "seconden": "seconde",
            }[magnitude]
        return magnitude

    magnitudes_str = (
        f"{int(locals_[magnitude])} {label(int(locals_[magnitude]), magnitude)}"
        for magnitude in ("weken", "dagen", "uren", "minuten", "seconden")
        if locals_[magnitude]
    )
    return ", ".join(list(magnitudes_str)[:1]) + " geleden."


class Required(RuntimeError):
    pass


def update_effectivedated(
    db: DAL,
    table: Table,
    where: Query | bool,
    values: dict = None,
    prio: bool | int | OrganisationPriority = False,
    effdt: datetime = None,
    last_saved_by: str = Required,
    delete: bool = False,
):
    """Update  entitiy/entities in <table> based on <where> clause with <values> using effective date and optional priority.
    If priority is not False, a new row with the given priority is created based on the most active row (highest priority and effective).

    for example:
    >>> apply_update(db, table, db.table.gid=='existing pk', {'name':'new name'}) # update the existing row ignores priority
    >>> apply_update(db, table, db.table.gid=='existing pk', {'name':'new name'}, prio=200) # update the existing row with priority set to 200
    >>> apply_update(db, table, db.table.gid=='new primary key', {'gid':'new primary key', 'name':'new name'}, prio=200) # create a new row with priority set to 200

    """
    if not effdt:
        effdt = datetime.now()
    if last_saved_by is Required:
        raise Required("last_saved_by is a required argument. ")
    values = values or {}
    use_prio = prio is not False
    if isinstance(prio, OrganisationPriority):
        prio = prio.value

    if use_prio:
        prioed_subselect = db(where)._select(table.prio.max())
        prioed_effdt_subselect = db(
            where & table.prio.belongs(prioed_subselect)
        )._select(table.effdt.max())
        rows = db(
            where
            & table.prio.belongs(prioed_subselect)
            & table.effdt.belongs(prioed_effdt_subselect)
        ).select(table.ALL, orderby=~table.effdt)
    else:
        # get the latest row:
        ed_subselect = db(where)._select(table.effdt.max())
        rows = db(where & table.effdt.belongs(ed_subselect)).select(
            table.ALL, orderby=~table.effdt
        )
    record = {}
    if len(rows) == 1:
        record.update(rows.first().as_dict())
        # don't overwrite the primary key, this auto-increments
        del record["id"]
    elif len(rows) > 1:
        raise Exception(f"Multiple rows ({len(rows)}) found for update using {where}")
    # update the effective date to match the specified timestamp or now
    record["effdt"] = effdt
    # update the priority if specified
    if use_prio:
        # if the values don't overwrite any pervious non-null values, set the priority to
        # the max of the priority parameter and the current priority from the record.
        overlapping_keys = set(record.keys()) & set(values.keys())
        if all(
            [
                (record[k] in (None, "") or record[k] == values[k])
                for k in overlapping_keys
            ]
        ):
            prio = max(prio, record["prio"])
        record["prio"] = prio
    # update the last_saved_by field
    record["last_saved_by"] = last_saved_by
    # if delete is True, set the deleted flag to True
    if delete:
        if values:
            raise Exception("Cannot delete and update at the same time")
        record["effstatus"] = False
    else:
        if record["effstatus"] == False:
            raise NotImplementedError(
                "Cannot update a deleted record - though this would work, it is better not to do so. We do not know what you would want based on historic data."
            )
            # make up your mind and implement. ;)

    # update the old record with the new values parameter
    record.update(values)
    # insert a new record based on the accumulated values of the old record
    # and the parameters, effdate and optionally priority
    return table.insert(**record)


@define(frozen=True, slots=True)
class SessionToken:
    token: UUID = field(converter=make_uuid)
    user: "User" = field()
    upgrades: list[str] = field()

    def __str__(self):
        return str(self.token)

    @classmethod
    def from_row(cls, db: DAL, row: Row) -> "SessionToken":
        return cls(
            token=row.session_token,
            user=User.load(db, row.user_gid) if row.user_gid else None,
            upgrades=row.upgrades,
        )

    @classmethod
    def load(cls, db: DAL, token: UUID, seen=True):
        if seen:
            # select and update in 1 keer
            rows = db.executesql(
                """
            update session
            set last_seen = current_timestamp
            where session_token = %s
            returning * 
            """,
                placeholders=(str(token),),
                fields=db.session,
            )
            record = rows.first()
        else:
            record = db.session(session_token=token)
        if not record:
            raise NotFoundException(f"No gid for {cls} matches {token}")
        return cls.from_row(db, record)

    @classmethod
    def new(cls, db: DAL, user: "User" = None, hw_specs: dict = None):
        token = uuid4()
        db.session.insert(
            platform="SvS",
            user_gid=user.id if user else None,
            session_token=token,
            hw_specs=hw_specs,
            started=datetime.now(),
            last_seen=datetime.now(),
            upgrades=[],
            gid_hash=hash_gid(token),
        )
        return cls.load(db, token)


@define
class PropertyBag:
    id: UUID = field(
        converter=make_uuid,
    )
    belongs_to: UUID = field(converter=make_uuid)
    bag: dict = field(converter=load_json_or_is_dict)

    @classmethod
    def from_row(cls, db: DAL, row: Row, track: Callable = Magic) -> "PropertyBag":
        return (
            cls(id=UUID(track(row.gid)), belongs_to=row.belongs_to, bag=row.properties)
            if row
            else None
        )

    @classmethod
    def load(cls, db: DAL, gid: UUID, track: Callable = Magic) -> "PropertyBag":
        record = db.property_bag(gid=str(gid))
        if not record:
            return None
            # Een propertybag is een uitzondering, geen regel. dus hoeft NIET voor te komen
            # dan is None een duidelijk signaal genoeg.
            # raise NotFoundException(f"No gid for {cls} matches {gid}")
        return cls.from_row(db, record, track)


class DillableAttrsClass:
    @staticmethod
    def todb(item):
        return dill.dumps(edwh_asdict(item))

    @classmethod
    def fromdb(cls, dump):
        return cls(**dill.loads(dump))


@define(slots=False)
class Organisation(DillableAttrsClass):
    id: UUID = field(converter=make_uuid)
    name: str
    street: str | None = field(repr=False)
    number: str | None = field(repr=False)
    city: str | None = field(repr=False)
    lonlat: str | None = field(repr=False)
    item_tag: Union["Tag", None]
    coc: int = field(repr=False)
    aka: str | None = field(repr=False)
    validated_ts: datetime | None = field(repr=False)
    validated_by: str | None = field(repr=False)
    country_code: str | None = field(repr=False)
    website: str | None = field(repr=False)
    email: str | None = field(repr=False)
    scholen_op_de_kaart_url: str | None = field(repr=False)
    aantekeningen: str = field(repr=False)
    locatie: str | None = field(repr=False)
    student_count: int | None = field(repr=False)
    education_level: list[str] | None = field(repr=False)
    education_type: str | None = field(repr=False)

    @classmethod
    def from_row(cls, db: DAL, row: Row, track: Callable = Magic) -> "Organisation":
        if not row:
            raise
        return cls(
            id=row.gid,
            name=row.name,
            coc=row.coc,
            street=row.street,
            number=row.number,
            city=row.city,
            lonlat=row.lonlat,
            item_tag=Tag.load(db, track(row.tag_gid)) if row.tag_gid else None,
            aka=row.aka,
            validated_ts=row.validated_ts,
            validated_by=row.validated_by,
            country_code=row.country_code,
            website=row.website,
            email=row.email,
            scholen_op_de_kaart_url=row.scholen_op_de_kaart_url,
            aantekeningen=row.aantekeningen,
            locatie=row.lonlat,
            student_count=row.student_count,
            education_level=[
                EDUCATION_LEVEL.get(level, level) for level in row.education_level
            ]
            if row.education_level
            else None,
            education_type=EDUCATION_TYPE[row.education_type]
            if row.education_type
            else None,
        )

    @classmethod
    def load(cls, db: DAL, gid: UUID, track: Callable = Magic) -> "Organisation":
        record = db.organisation_effdted_now(gid=str(gid))
        if not record:
            raise NotFoundException(f"No gid for {cls} matches {gid}")
        return cls.from_row(db, record, track)


@define
class Attachment:
    id: UUID = field(converter=make_uuid)
    uri: str
    filename: str
    purpose: str

    @classmethod
    def from_row(cls, db: DAL, row: Row, track: Callable = Magic) -> "Attachment":
        return (
            cls(
                id=UUID(track(row.gid)),
                uri=row.b2_uri,
                filename=row.filename,
                purpose=row.purpose,
            )
            if row
            else None
        )

    @classmethod
    def load(cls, db: DAL, gid: UUID, track: Callable = Magic) -> "Attachment":
        record = db.attachment(gid=str(gid))
        if not record:
            raise NotFoundException(f"No gid for {cls} matches {gid}")
        return cls.from_row(db, record, track)

    @property
    def mime_type(self):
        return mimetypes.guess_type(self.filename, strict=False)[0]


@define
class User:
    id: UUID = field(converter=make_uuid)
    name: str
    email: str | None
    has_validated_email: bool | None = field(repr=False)
    email_verification_code: int = field(repr=False)
    avatar: Attachment = field(repr=False)
    property_bag: dict = field(converter=load_json_or_is_dict, repr=False)
    firstname: str | None = field(repr=False)
    lastname: str | None = field(repr=False)
    user_provided_primary_organisational_role: str | None = field(repr=False)
    user_provided_organisation: str | None = field(repr=False)
    user_provided_organisation_location: str | None = field(repr=False)
    gid_thumb_map: dict[UUID, int] = field(repr=False)

    def is_admin(self):
        return self.email.endswith("roc.nl") or self.email.endswith(
            "@educationwarehouse.nl"
        )

    def secure(self, me: "User") -> None:
        if not self.is_admin() and me.id != self.id:
            self.email = None
            self.has_validated_email = None

    def may_edit(self, item: "Item") -> bool:
        return item.author.id == self.id or self.is_admin()

    @classmethod
    def from_row(cls, db: DAL, row: Row, track: Callable = Magic) -> "User":
        return (
            cls(
                id=UUID(row.gid),
                name=row.name,
                email=row.email,
                has_validated_email=row.has_validated_email,
                email_verification_code=row.email_verification_code,
                avatar=Attachment.load(db, track(row.avatar)) if row.avatar else None,
                property_bag=row.property_bag,
                firstname=row.firstname,
                lastname=row.lastname,
                user_provided_primary_organisational_role=row.user_provided_primary_organisational_role,
                user_provided_organisation=row.user_provided_organisation,
                user_provided_organisation_location=row.user_provided_organisation_location,
                gid_thumb_map=cls.get_users_thumbs(db, user_gid=row.gid),
            )
            if row
            else None
        )

    @classmethod
    def load(cls, db: DAL, gid: UUID | str, track: Callable = Magic) -> "User":
        record = db.user(gid=str(gid))
        if not record:
            raise NotFoundException(f"No gid for {cls} matches {gid}")
        return cls.from_row(db, record, track)

    @property
    def bio(self):
        return self.property_bag.get("bio", "")

    @property
    def kvk(self):
        return self.property_bag.get("kvk", "")

    def set_password(self, db: DAL, password: str):
        if password.lower() == "new":
            password = new_password()
        db(db.user.gid == str(self.id)).update(
            password=hash_password(password), has_validated_email=True
        )
        db.commit()
        return password

    @classmethod
    def get_users_thumbs(cls, db, user_gid: UUID | str) -> dict[UUID, int]:
        """Returns the uuids for anything marked by the given user"""
        where = db.mark.user_gid == str(user_gid)
        where &= db.mark.name == "thumbs"
        rows = db(where).select(db.mark.subject_gid, db.mark.mark)
        gid_thumb_map = {row.subject_gid: row.mark for row in rows if row.mark != 0}
        return gid_thumb_map

    def update_gid_thumb_map(self, db: DAL) -> dict[UUID, int]:
        """Update and return the .gid_thumb_map from database. Use after updating marks."""
        self.gid_thumb_map = self.get_users_thumbs(db, self.id)
        return self.gid_thumb_map


class ValidationCode(Enum):
    OK = auto()
    INVALID_CREDENTIALS = auto()
    REQUIRES_EMAIL_VALIDATION = auto()


@define(frozen=True)
class Validated:
    code: ValidationCode
    feedback: str | None = field(default=None)
    user: User | None = field(default=None)
    token: SessionToken | None = field(default=None)


@define
class Tag:
    id: UUID = field(converter=make_uuid)
    name: str = field(repr=False)
    description: str | None = field(repr=False)
    slug: str
    meta_tags: list[UUID] = field(repr=False)
    parents: list[UUID] = field(repr=False)
    children: list[UUID] = field(repr=False)
    deprecated: bool = field(repr=False)

    @classmethod
    def from_row(cls, db, row: Row, track: Callable = Magic):
        if not row:
            return None
        tag = cls(
            id=UUID(track(row.gid)),
            name=row.name,
            slug=row.slug,
            description=row.description,
            meta_tags=[UUID(track(_)) for _ in row.meta_tags or []],
            parents=[UUID(track(_)) for _ in row.parents or []],
            children=[UUID(track(_)) for _ in row.children or []],
            deprecated=bool(row.deprecated),
        )
        return tag

    @classmethod
    def load(cls, db: DAL, gid: UUID | str, track: Callable = Magic):
        record = db.tag(gid=str(gid))
        if not record:
            raise NotFoundException(f"No gid for {cls} matches {gid}")
        return cls.from_row(db, record, track)

    def item_count(self, db, q: str, filtered_with: list[UUID]):
        pass

    def item_tree_count(self, db, q: str, filtered_with: list[UUID]):
        pass

    @property
    def is_user_selectable(self):
        return TAG_GID_USER_SELECTABLE in self.meta_tags


@define
class ItemMarkStatistics:
    thumbs_sum: int
    thumbs_min: int
    thumbs_max: int
    thumbs_avg: int
    thumbs_cnt: int
    favs_cnt: int


@define
class Sticker:
    id: UUID = field(converter=make_uuid)
    uri: str
    filename: str
    purpose: str
    sticker_tag: Tag

    @classmethod
    def from_row(
        cls, db: DAL, tag_gid: UUID, attachment_row: Row, track: Callable = Magic
    ) -> "Sticker":
        if not attachment_row:
            return
        tag = Tag.load(db, track(tag_gid))
        sticker = cls(
            id=UUID(track(attachment_row.gid)),
            uri=attachment_row.b2_uri,
            filename=attachment_row.filename,
            purpose=attachment_row.purpose,
            sticker_tag=tag,
        )
        return sticker

    @property
    def name(self):
        return self.sticker_tag.name

    def description(self, db: DAL, from_item: "Item"):
        return from_item.convert_markdown(
            db, self.sticker_tag.description, as_single_line=True
        )

    @property
    def svg(self):
        return self.uri.lower().endswith("svg")

    @classmethod
    def load(
        cls, db: DAL, tag_gid: UUID, attachment_gid: UUID, track: Callable = Magic
    ) -> "Sticker":
        record = db.attachment(gid=track(str(attachment_gid)))
        if not record:
            raise NotFoundException(f"No gid for {cls} matches {tag_gid}")
        return cls.from_row(db, track(tag_gid), record, track)


@define
class ItemBoundSticker(Sticker):
    """Sticker bound to an item, `bind` before use. Normally done in Item's from_row."""

    description_html: str = field(init=False)

    def bind(self, db: DAL, item: "Item"):
        self.description_html = item.convert_markdown(
            db, self.sticker_tag.description, as_single_line=True
        )


class WetenschappelijkeOnderbouwing(Enum):
    EIGEN_KENNIS_EN_ERVARING = "EKeE"
    GEBASEERD_OP_WETENSCHAP = "GOW"
    ELDERS_BEWEZEN_EFFECTIEF = "EBE"
    HIER_BEWEZEN_EFFECTIEF = "HBE"


class DuplicateSlugException(ValueError):
    slug: str
    collides_with: Row

    def __init__(self, slug: str, collides_with: Row):
        self.slug = slug
        self.collides_with = collides_with
        super().__init__(
            f"Ongeldige naam: er bestaat reeds een item met dezelfde slug: {slug}, namelijk: {collides_with}"
        )


@define
class Item:
    id: UUID = field(converter=make_uuid)
    name: str = field(repr=False)
    slug: str = field()
    author: User = field(repr=False)
    # short_description is the unprocessed markdown
    short_description: str = field(repr=False)
    # body is the processed markdown, with links converted to tracker links.
    body: str = field(repr=False, init=False)
    # firstline is the first line from the processed body, without links
    firstline: str = field(init=False, repr=False)
    # shorter_body and firstline combined make the complete body again.
    shorter_body: str = field(init=False, repr=False)
    attachments: list[Attachment] = field(repr=False)
    backgrounds: list[Attachment] = field(repr=False)
    tags: list[Tag] = field(repr=False)
    since_when: date = field(repr=False)
    upto_when: date = field(repr=False)
    video_urls: list[str] = field(repr=False)
    thumbnail: Attachment = field(repr=False)
    stickers: list[ItemBoundSticker] = field(repr=False)
    ts_changed: datetime = field(repr=False)
    property_bag: PropertyBag = field(repr=False)
    onderbouwing: WetenschappelijkeOnderbouwing | None = field(repr=False)
    onderbouwing_bronnen: list[Attachment] = field(repr=False)
    onderbouwing_links: list[str] = field(repr=False)
    license: str = field(repr=False)
    _teaser: str = field(init=False, default=None, repr=False)
    organisation_tags: list[Tag] = field(init=False, default=[], repr=False)
    extra_contactgegevens: list[str] = field(default=[], repr=False)
    visibility: list[str | Visibility] = field(default=DEFAULT_ITEM_VISIBILITY)

    def process_text(self, db: DAL) -> None:
        self.body = self.convert_markdown(db, self.short_description)

        # ------------------------------------
        # extract first_line and smaller_body
        extra = ""
        split_sequence = "</p>"
        body_parts = self.body.split(split_sequence)
        # find the firstline and clean, save as self.firstline
        firstline = body_parts[0] + split_sequence
        if found := FIRST_SENT_RE.search(firstline):
            # als de eerste <p> nog bestaat uit twee zinnen, split die hier:
            split_index = found.span()[0] + 1
            extra = firstline[split_index:]  # to append to shortDescription
            firstline = firstline[:split_index]
        self.firstline = firstline

        # save the tail to self.shorter_body
        shortdesc = body_parts[1:]
        if extra:
            shortdesc.insert(0, extra)

        self.shorter_body = split_sequence.join(shortdesc)

    def convert_markdown(self, db, markdown, as_single_line=False):
        # heette voorheen: def process_links_in_article(self, markdown_text:str, item_gid:UUID|str, session_gid:UUID):
        links = MARKDOWN_LINK_RE.findall(markdown)
        # haal een translate op voor elke link in (label, url), in links
        urls = [url for label, url in links]
        shortened_url_map: dict[Any, str] = {}
        short_item_gid = shorten_gid(self.id)
        for url in urls:
            url_hash = hash_url(url)
            if db(db.click__url.short_code == url_hash).count() == 0:
                try:
                    db.click__url.insert(short_code=url_hash, long_url=url)
                    db.commit()
                    # when new in db, flag in redis this key is available
                except UniqueViolation:
                    # silently ignore the insert, because it was already there.
                    db.rollback()

            # todo: verwarrende naamgeving van shorten_urls die long_urls teruglevert. niet handig.
            long_url = (
                f"https://{CLICK_TRACKER_DOMAIN}/c/xxx/{short_item_gid}/{url_hash}"
            )
            shortened_url_map[url] = long_url

        # vervang alle linkjes in md door opnieuw te zoeken, en de vervanging op te zoeken
        # in het resultaat van shortened_url_map
        def md_link_processor(match):
            label = match.group(1)
            url = shortened_url_map[match.group(2)]
            return f"[{label}]({url})"

        zonder_md_links = MARKDOWN_LINK_RE.sub(md_link_processor, markdown)
        # below will be used by the short_description property
        html = markdown2.markdown(zonder_md_links)
        if as_single_line:
            html = html.replace("<p>", "").replace("</p>", "")
        return html

    @classmethod
    def from_row(cls: "Item", db, row, track: Callable = Magic):
        if not row:
            return None
        try:
            author = User.load(db, row.author)
        except NotFoundException:
            author = None
        item = cls(
            id=UUID(track(row.gid)),
            name=row.name,
            slug=row.slug,
            author=author,
            short_description=row.short_description,
            attachments=[
                Attachment.load(db, att, track) for att in row.attachments or []
            ],
            backgrounds=[
                Attachment.load(db, att, track) for att in row.backgrounds or []
            ],
            tags=[Tag.load(db, tag, track) for tag in row.tags],
            since_when=row.since_when,
            upto_when=row.upto_when,
            video_urls=row.video_urls,
            thumbnail=Attachment.load(
                db, row.thumbnail if row.thumbnail else row.backgrounds[0], track
            )
            if row.thumbnail or row.backgrounds
            else None,
            ts_changed=row.ts_changed,
            property_bag=PropertyBag.load(db, make_uuid(row.gid), track),
            stickers=[
                ItemBoundSticker.load(
                    db,
                    make_uuid(sticker_row.tag_gid),
                    make_uuid(sticker_row.attachment_gid),
                    track=track,
                )
                for sticker_row in db(db.sticker.tag_gid.belongs(row.tags)).select()
            ],
            onderbouwing=row.onderbouwing,
            onderbouwing_links=row.onderbouwing_links or [],
            onderbouwing_bronnen=[
                Attachment.load(db, att, track)
                for att in row.onderbouwing_bronnen or []
            ],
            license=row.license,
            extra_contactgegevens=row.extra_contactgegevens,
            visibility=[Visibility(_) for _ in row.visibility],
        )
        # sets item.body based on processed markdown from short_description
        item.process_text(db)
        # update sticker descriptions to convert markdown to html using tracking links
        for sticker in item.stickers:
            sticker.bind(db, item)
        # find schools
        item.organisation_tags = [
            Tag.load(db, row[0])
            for row in db.executesql(
                """
                select mv.tag_gid as org_tag_gid
                  from tag org_tag inner join mv__item_tags mv on item_gid = %s and org_tag.children like '%%|' || mv.tag_gid || '|%%'
                 where org_tag.name = 'Organisations'
                """,
                placeholders=(str(item.id),),
            )
        ]
        return item

    @property
    def is_without_email(self) -> bool:
        return (
            (self.author.email is None)
            or (self.author.email.strip() == "")
            or self.author.email.strip().endswith("@educationwarehouse.nl")
        )

    @classmethod
    def load(cls, db: DAL, gid: UUID, track: Callable = Magic) -> "Item":
        record = db.item(gid=str(gid))
        if not record:
            raise NotFoundException(f"No gid for {cls} matches {gid}")
        return cls.from_row(db, record, track)

    @property
    def teaser(self) -> str:
        if self._teaser:
            return self._teaser
        lines = self.short_description.split("\n")
        while lines and (
            lines[0].strip().strip("*").lower().startswith("nb:")
            or lines[0].strip() == ""
        ):
            lines.pop(0)
        # fabricate the teaser
        teaser = lines[0] if lines else ""
        # remove all links
        teaser = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", teaser)
        # shorten if required
        teaser = teaser if len(teaser) < 500 else teaser[:500] + "..."
        self._teaser = teaser = markdown2.markdown(teaser)
        return teaser

    @property
    def is_current(self) -> bool:
        today = datetime.now().date()
        return (self.since_when or today) <= today <= (self.upto_when or today)

    @property
    def b64id(self) -> str:
        return base64.b64encode(self.id.bytes).decode("ascii")

    @property
    def permalink(self) -> str:
        short_gid = base64.b64encode(self.id.bytes, b"+_").decode("utf-8").rstrip("=")
        # return f"https://delen.meteddie.nl/p/{self.slug}/{short_gid}"
        return f"https://{os.environ['APPLICATION_NAME']}.{os.environ['HOSTINGDOMAIN']}/item/{short_gid}"

    @classmethod
    def unpermalink(cls, db: DAL, permalink_code: str) -> Union["Item", None]:
        try:
            gid = UUID(bytes=base64.b64decode(permalink_code + "======", b"+_"))
            return cls.load(db, gid)
        except:
            return

    @property
    def ts_changed_hf(self) -> str:
        "Human friendly ts_changed: time ago for 2 months, or date otherwise"
        # dt = datetime.datetime.fromisoformat(datetimestring)
        if self.ts_changed is None:
            return "?"
        updated_ago = datetime.now() - self.ts_changed
        if updated_ago.days > 8 * 7:
            return str(self.ts_changed.strftime("%d-%m-%Y"))
        else:
            return human_friendly_timedelta(updated_ago)

    @property
    def last_update(self):
        return self.ts_changed.date() if self.ts_changed else None

    def favorite_count(self, db):
        # Geen property, want heeft database nodig.
        return self.get_marks_count(db).favs_cnt

    def thumb_count(self, db):
        # Geen property, want heeft database nodig.
        return self.get_marks_count(db).thumbs_cnt

    # def has_my_thumb(self, db: DAL, me: User):
    #     # Geen property, want heeft database nodig.
    #     if not me:
    #         # anonymous never has
    #         return False
    #     where = db.mark.platform == PLATFORM
    #     where &= db.mark.subject_gid == str(self.id)
    #     where &= db.mark.user_gid == str(me.id)
    #     rows = db(where).select(db.mark.mark)
    #     return rows.first().mark > 0 if rows else False

    def get_marks_count(self, db) -> ItemMarkStatistics:
        # Geen property, want heeft database nodig.
        query = (
            (db.mark.platform == PLATFORM)
            & (db.mark.subject_gid == str(self.id))
            & (db.mark.mark != 0)
        )  # all non zero values
        s = db(query & (db.mark.name == "thumbs"))
        sum = db.mark.mark.sum()
        min = db.mark.mark.min()
        max = db.mark.mark.max()
        avg = db.mark.mark.avg()
        fav_cnt = db(query & (db.mark.name == "fav")).count()
        thumb_cnt = db(query & (db.mark.name == "thumbs")).count()

        row = s.select(
            sum, min, max, avg, groupby=db.mark.platform | db.mark.subject_gid
        ).first()
        if row is None:
            return ItemMarkStatistics(0, 0, 0, 0, 0, 0)
        else:
            return ItemMarkStatistics(
                row[sum], row[min], row[max], row[avg], thumb_cnt, fav_cnt
            )

    def alternatives(self, db):
        return [Item.load(db, alt) for alt in db.item(gid=self.id).alternatives or []]

    @property
    def time_to_read(self):
        return int(
            len(self.short_description.split(" ")) / 130
            if self.short_description
            else -111
        )

    @classmethod
    def create(
        cls,
        db: DAL,
        author: User | UUID | None,
        name: str,
        short_description: str = "Leeg artikel.",
        attachments: list[UUID] | list[str] | None = None,
        tags: list[UUID] | list[str] | None = None,
        thumbnail: str | None = None,
        visibility: list[Visibility] = None,
    ):
        gid = uuid4()
        if not author:
            author = User.load(db, UUID(EDDIE_GID))
        elif not isinstance(author, User):
            author = User.load(db, author)
        slug = slugify(name)
        if collides_with := db.item(slug=slug):
            raise DuplicateSlugException(
                slug=slug,
                collides_with=collides_with,
            )
        if visibility is None:
            visibility = [Visibility.PIPELINE]
        db.item.insert(
            platform=PLATFORM,
            author=str(author.id),
            name=name,
            gid=gid,
            short_description=short_description,
            attachments=attachments or [],
            backgrounds=[],
            thumbnail=thumbnail,
            slug=slug,
            tags=tags or [],
            visibility=[v.value for v in visibility],
        )
        return Item.load(db, gid=gid)

    @classmethod
    def calculate_similarity_by_tags(cls, item1_tags: set, item2_tags: set):
        if not isinstance(item1_tags, set):
            item1_tags = set(item1_tags)

        if not isinstance(item2_tags, set):
            item2_tags = set(item2_tags)

        same = len(item1_tags & item2_tags)
        total = len(item1_tags | item2_tags)
        return same / total

    @classmethod
    def calculate_similarity(
        cls, db, item1_id: "UUID | Item", item2_id: "UUID | Item"
    ) -> float:
        if not isinstance(item1_id, cls):
            item1 = cls.load(db, item1_id)
        else:
            item1 = item1_id

        if not isinstance(item2_id, cls):
            item2 = cls.load(db, item2_id)
        else:
            item2 = item2_id

        return cls.calculate_similarity_by_tags(
            {_.id for _ in item1.tags}, {_.id for _ in item2.tags}
        )

    def find_related(self, db, n=5, reverse=False, extra_fields=None) -> dict:
        tag_ids = {_.id for _ in self.tags}

        query = db.mv__item_tags.tag_gid.belongs(tag_ids)
        query &= db.mv__item_tags.item_gid != self.id

        count = db.mv__item_tags.item_gid.count()

        result = db(query).select(
            db.mv__item_tags.item_gid,
            count,
            groupby=db.mv__item_tags.item_gid,
            orderby=~count if not reverse else count,
            limitby=(0, n),
        )

        results = {_.mv__item_tags.item_gid: _[count] for _ in result}
        if not extra_fields:
            return results
        else:
            _select = [db.mv__item_tags.item_gid]
            _select.extend([db.mv__item_tags[_] for _ in extra_fields])

            items = db(db.mv__item_tags.item_gid.belongs(set(results.keys()))).select(
                *_select
            )

            return {_.item_gid: {"count": results[_.item_gid], **_} for _ in items}

    def organisations(self, db) -> list[Organisation]:
        organisation_ids = db(
            db.organisation_effdted_now.tag_gid.belongs(
                [tag.id for tag in self.organisation_tags]
            )
        ).select()
        organisations = [Organisation.from_row(db, row) for row in organisation_ids]
        return organisations

    def is_visible(
        self,
        include: set[Visibility] | None = DEFAULT_INCLUDED_VISIBILITY,
        exclude: set[Visibility] | None = DEFAULT_EXCLUDED_VISIBILITY,
    ) -> bool:
        """
        If include is None, allow any (= copy from item)
        If exclude is None, allow any (= empty set)
        """
        visibility = set(self.visibility)
        if include is None:
            include = visibility

        if exclude is None:
            exclude = {}

        return visibility & include and not (visibility & exclude)


@define(frozen=True)
class SearchResult:
    available: int
    found: Any


# @define(frozen=True)
class UUIDSearchResult(SearchResult):
    found: list[UUID | str]


@contextmanager
def temp_recursion_limit(new_limit: int):
    old_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(new_limit)
    try:
        yield
    finally:
        sys.setrecursionlimit(old_limit)


@define(frozen=True)
class ItemSearchResult(SearchResult):
    found: list[Item]
    first: int = field(default=0)
    offset: int = field(default=0)


class Backend:
    system_tag: Tag
    item_tag: Tag

    # applog sink and emitter
    sink: SignalSink
    applog: SignalEmitter

    def __init__(self, database: DAL, sink: SignalSink, applog: SignalEmitter):
        self.db = database
        self.system_tag = Tag.load(
            database, UUID("19682a99-50a3-4fc0-bb67-e0f6eff5da55")
        )
        self.item_tag = Tag.load(database, UUID("fc8a7d36-e23e-4aba-8ee9-f5269ecc8dfc"))
        self.sink = sink
        self.applog = applog

    def update_effectivedated(
        self,
        table: Table,
        where: Query,
        values: dict = None,
        prio: bool | int | OrganisationPriority = False,
        effdt: datetime.date = None,
        last_saved_by: str = Required,
        delete: bool = False,
    ):
        return update_effectivedated(
            self.db, table, where, values, prio, effdt, last_saved_by, delete
        )

    def get_item_type(self, subject_gid: str):
        db = self.db
        for table_name in db.tables:
            table = db[table_name]
            if "gid" in table.fields:
                field_name = "gid"
            elif table_name == "session":
                field_name = "session_token"
            else:
                # auth_user, etc.
                continue
            if db(table[field_name] == subject_gid).count() > 0:
                return table_name
        raise ValueError("404: Nothing was found for ID: {}".format(subject_gid))

    def console(self, text, *p):
        # url = 'https://api.flock.com/hooks/sendMessage/e6f8b447-ef6d-4105-bd50-6f758fa856f7'
        # httpx.post(url, json=dict(text=text))
        print(text, " ".join([str(_) for _ in p]))

    def new_session_token(
        self, hardware: dict, user_gid: UUID | None = None, platform=PLATFORM
    ) -> SessionToken:
        """Genereert een nieuwe session token

        :param hardware: user-agent hardware info
        :return: nieuwe session token.
        """
        token = SessionToken.new(
            self.db,
            user=User.load(self.db, user_gid) if user_gid else None,
            hw_specs=hardware,
        )
        self.applog.new_session_token(token.token, hardware)
        return token

    def search_organisations(
        self, search: str = None, location: str = None
    ) -> UUIDSearchResult:
        db = self.db
        table = db.organisation_effdted_now

        query = table.platform == PLATFORM

        if location:
            query &= table.city.ilike(location)

        if search:
            query &= table.name.ilike(f"%{search}%")

        gids = [_.gid for _ in db(query).select(table.gid)]
        return UUIDSearchResult(found=gids, available=len(gids))

    def search_items(
        self,
        me: User | None = None,
        with_tags: list[list[UUID] | UUID] | None = None,
        order: SortOrder | None = None,
        first: int | None = None,
        offset: int = 0,
        search: str | None = None,
        search_in: list[str] | None = None,
        author: UUID | None = None,
        included_visibilities: list[Visibility] | None = DEFAULT_INCLUDED_VISIBILITY,
        excluded_visibilities: list[Visibility] | None = DEFAULT_EXCLUDED_VISIBILITY,
    ) -> UUIDSearchResult:
        self.console(
            "Item search:",
            offset,
            "-",
            (first or 0) + offset,
            '"{}"'.format(search),
            with_tags,
            "by",
            author,
            search_in,
            "including",
            included_visibilities,
            "excluding",
            excluded_visibilities,
        )
        with temp_recursion_limit(3000):
            database = self.db
            select_parameters = {}
            # start with a base query: all products
            query = database.item.id > 0
            query &= database.item.platform == PLATFORM
            exclude_deleted_items = True
            if search_in is None:
                search_in = ["tag", "name", "description", "author"]
            # since we're poping from the lists, copy them first to be non-destructive to parent scopes
            included_visibilities = (
                list(included_visibilities).copy()
                if included_visibilities is not None
                else list(DEFAULT_INCLUDED_VISIBILITY)
            )
            excluded_visibilities = (
                list(excluded_visibilities).copy()
                if excluded_visibilities is not None
                else list(DEFAULT_EXCLUDED_VISIBILITY)
            )
            # search all items matching the included_visibilities but exclude based on the excluded_visibilities
            included_visibilities_clause = database.item.visibility.contains(
                included_visibilities.pop().value
            )
            while included_visibilities:
                included_visibilities_clause |= database.item.visibility.contains(
                    included_visibilities.pop().value
                )
            query &= included_visibilities_clause
            # exclude based on the excluded_visibilities
            excluded_visibilities_clause = ~database.item.visibility.contains(
                excluded_visibilities.pop().value
            )
            while excluded_visibilities:
                excluded_visibilities_clause &= ~database.item.visibility.contains(
                    excluded_visibilities.pop().value
                )
            query &= excluded_visibilities_clause
            query &= database.item.author == database.user.gid

            if with_tags:
                query = self._apply_tags(query, with_tags)

            if search:
                query = self._apply_search(query, search, search_in, select_parameters)

            # TODO: stars := faves, thumbs, marks, tags, whatevers...
            if order:
                self._apply_sort_order(order, select_parameters)

            if author:
                query &= database.item.author == author

            if first or offset:
                # pagination, default value for first is 10000
                if not first:
                    first = 100
                select_parameters["limitby"] = (offset, offset + first)

            if exclude_deleted_items:
                # skip items without a author, meaning they have been deleted.
                # only time you want to include these, is when searching through comments
                # including comments on deleted items.
                query &= database.item.author != None

            try:
                print(
                    "item-search-query attempt:\n",
                    database(query)._select(database.item.gid, **select_parameters),
                    "\n",
                )
            except Exception as e:
                print(f"?! Could not print parameters or query ...", e)

            rows: Rows = database(query).select(database.item.gid, **select_parameters)
            # problem with .count() it doesn't support left=... so it will return the values
            #  for the cartesian product of item and propertybag
            # therefore, because the amount of data is small at the moment we will request all 1's for each result
            # and sum them
            # before that, we need to remove the limitby constraints because those will change our count behaviour
            if "limitby" in select_parameters:
                del select_parameters["limitby"]

            ##  selecting ID because 1 is not supported
            count = len(database(query).select(database.item.id, **select_parameters))
            # gids = [r.gid for r in rows]
            gids = rows.column("gid")
            return UUIDSearchResult(count, gids)

    def _apply_tags(
        self, query: Query, with_tags: list[list[UUID] | UUID] | None
    ) -> Query:
        database = self.db
        # with_tags can be a list of tags (uuid), list of strings (tag-slug)
        # [a,b,c] in which case all are ANDED
        # but when tuples of uuid or names appear they are ored within the tuple
        # [(a,b,c), (x,y,z)] ( a or b or c) and (x or y or z)
        for tag in with_tags:
            if isinstance(tag, (list, tuple)):
                # fetch first item
                subquery = database.item.tags.contains(tag.pop(0))
                # OR all next items
                for subtag in tag:
                    # include each tag, including all at once will
                    # generate an "AND tags LIKE '%|..|%' OR tags like ..."
                    # we don't want that, we want to filter on all tags.
                    subquery |= database.item.tags.contains(subtag)
                query &= subquery
            else:
                query &= database.item.tags.contains(tag)
        return query

    def _apply_search(
        self, query: Query, search: str, search_in: list[str], select_parameters: dict
    ) -> Query:
        database = self.db
        # ## Item-gid search:
        # Use only itemgids:|<gid>[|<gid>[...]]| syntax to show only specific gids.
        # example: `itemgid:|7bcaa1cf-3d91-44b3-bbc9-79d9fb5e8d12|bb49c57c-5a5d-4abc-8906-b4a21e782ee1|`
        # >>> re.findall(r'itemgid:([\d,a-f,A-F,\-,\|]*)',
        #            'itemgid:|7bcaa1cf-3d91-44b3-bbc9-79d9fb5e8d12|bb49c57c-5a5d-4abc-8906-b4a21e782ee1|')
        # ['|7bcaa1cf-3d91-44b3-bbc9-79d9fb5e8d12|bb49c57c-5a5d-4abc-8906-b4a21e782ee1|']
        # will show only these two items
        only_these_item_gids = []
        for item_gids in re.findall(r"itemgid:([\d,a-f,A-F,\-,\|]*)", search):
            # remove this from the search
            search = search.replace("itemgid:" + item_gids, "")
            # remove outer | and split on the inner | to get a list of all the uuids required
            only_these_item_gids.extend(item_gids.strip("|").split("|"))
        if only_these_item_gids:
            # add this restriction to the query
            query &= database.item.gid.belongs(only_these_item_gids)
        # ## simpel
        # re.findall(r'#?[\w-]+', 'abc cde koppel-streep #zza af#23 a@b!c')
        # Out[9]: ['abc', 'cde', 'koppel-streep', '#zza', 'af', '#23', 'a', 'b', 'c']
        #
        # ## complexer
        # [''.join(hits).replace("'", "").replace('"', "") for hits in
        #  re.findall(r'''(-?#?".+?")|(-?#?'.+?')|(-?#?[\w-]+)''',
        #             'enkel enkel "2 woorden" #tag -#tag -niet-woord -"deze twee niet" #"tag met quotes" -#\'niet tag met quotes\'')]
        # Out[36]:
        # ['enkel',
        #  'enkel',
        #  '2 woorden',
        #  '#tag',
        #  '-#tag',
        #  '-niet-woord',
        #  '-deze twee niet',
        #  '#tag met quotes',
        #  '-#niet tag met quotes']

        terms = set(
            "".join(hits)
            .replace("'", "")  # after grouping they are not required
            .replace('"', "")  # after grouping they are not required
            for hits in re.findall(
                r"""(-?#?>?".+?")|(-?#?>?'.+?')|(-?#?>?[\w-]+)""", search
            )
        )

        for term in terms:
            # process all terms. special case when tag
            # for search in optionally connected tables:
            #   add to the subquery_parts the constraint
            #   add to the select_parameters the outer joins
            # when negated:
            #   add the exclusion to the subquery_parts the constraint
            #   add to the select_parameters the outers join to find, all others are not a problem
            #   by means of the outer join.

            # hashed_term wordt gebruikt voor tabel aliases
            hashed_term = md5(term.encode()).hexdigest()
            # subquery_parts is per term! en wordt ana het eind van de loop
            # aan query toegevoegd.
            subquery_parts = []
            negated_term = term.startswith("-")
            if negated_term:
                # strip the - for further processing of term
                term = term[1:]

            if term.startswith("#"):
                # special case of tag searches: only search for tags and ignore this term for
                # content based searches.
                term = term[1:]

                if recursive_term := term.startswith(">"):
                    # special case for recursive child searches:
                    term = term[1:]

                # hash prefixed items are tag searches. always.
                # if tags are postfixed with an ! they should be taken literally, not expanded.
                tag_gids = (
                    database(
                        database.tag.slug.ilike(
                            slugify(term)
                            if term.endswith("!")
                            else f"%{slugify(term)}%"
                        )
                        & (database.tag.deprecated == False)
                    )
                    .select(database.tag.gid)
                    .column("gid")
                )

                if recursive_term:
                    raw_sql = """
                    with recursive tag_cte as (select tag.id,
                                  tag.gid,
                                  0 as level,
                                  tag.children
                           from mv__tag_arrays as tag
                           where gid::text = ANY(%s)
                           union all
                           -- # --------------------------------
                           select tag.id,
                                  tag.gid,
                                  level + 1,
                                  tag.children
                           from mv__tag_arrays as tag
                                    inner join tag_cte on tag.gid = ANY (tag_cte.children))
                    select gid
                    from tag_cte
                    group by gid
                    """
                    # list of tuples, element 0 is the gid.
                    descendants = [
                        t[0]
                        for t in database.executesql(raw_sql, placeholders=[tag_gids])
                    ]
                    tag_gids = descendants

                if negated_term:
                    # in the contains: all=False means, any match will suffice to include in the output
                    # False seems to be the default here.
                    subquery_parts.append(
                        (~database.item.tags.contains(tag_gids, all=False))
                    )
                else:
                    subquery_parts.append(
                        database.item.tags.contains(tag_gids, all=False)
                    )
                # omdat er meerdere tags kunnen matchen per artikel, willen we niet
                # dat het item dan meerdere keren in het zoekresultaat verschijnt.
                # daarom is er een groupby nodig.
                # ordering heeft ook velden nodig en postgres vereist dat een veld
                # waarop gesorteerd wordt, ook op gegroepeerd is. Daarom is dit een lijst
                # en die wordt uitgebreid in de ordering criteria
                select_parameters["groupby"] = [
                    database.item.id,
                    database.item.gid,
                    database.item.author,
                    database.item.platform,
                    database.item.tags,
                ]
            else:
                search_anywhere = "%" + term + "%"
                if "tag" in search_in:
                    tag_gids = [
                        _.gid
                        for _ in database(
                            (
                                database.tag.slug.ilike(f"%{slugify(term)}%")
                                | database.tag.description.ilike(search_anywhere)
                                | database.tag.akas.ilike(search_anywhere)
                                | database.tag.search_hints.ilike(search_anywhere)
                            )
                            & (database.tag.deprecated == False)
                        ).select(database.tag.gid)
                    ]
                    self.console(*database._lastsql, tag_gids)
                    if tag_gids and len(tag_gids) < 50:
                        # only when applied and when not a massive amount of tags matches the given term
                        # "gr" or "ass" matches potentionally hundreds of tags, resulting in a performance degradation
                        # or even a recursion error
                        subquery_parts.append(database.item.tags.contains(tag_gids))
                        # omdat er meerdere tags kunnen matchen per artikel, willen we niet
                        # dat het item dan meerdere keren in het zoekresultaat verschijnt.
                        # daarom is er een groupby nodig.
                        # ordering heeft ook velden nodig en postgres vereist dat een veld
                        # waarop gesorteerd wordt, ook op gegroepeerd is. Daarom is dit een lijst
                        # en die wordt uitgebreid in de ordering criteria
                        select_parameters["groupby"] = [
                            database.item.id,
                            database.item.gid,
                            database.item.author,
                            database.item.platform,
                            database.item.tags,
                        ]
                if "name" in search_in:
                    subquery_parts.append(database.item.name.ilike(search_anywhere))
                    if negated_term:
                        subquery_parts[-1] = ~subquery_parts[-1]
                if "description" in search_in:
                    # search in description
                    subquery_parts.append(
                        database.item.short_description.ilike(search_anywhere)
                    )
                    if negated_term:
                        subquery_parts[-1] = ~subquery_parts[-1]

                    pb_searcher = database.property_bag.with_alias(
                        "pb_search_on_" + hashed_term
                    )
                    # include a possible match on just the property_bag.
                    subquery_parts.append(pb_searcher.properties.ilike(search_anywhere))
                    if negated_term:
                        subquery_parts[-1] = ~subquery_parts[-1] | (
                            pb_searcher.properties == None
                        )
                    select_parameters.setdefault("left", []).append(
                        pb_searcher.on(
                            (database.item.gid == pb_searcher.belongs_to_gid)
                            & (pb_searcher.properties.ilike(search_anywhere))
                        )
                    )
                if "comments" in search_in:
                    exclude_deleted_items = False
                    raise NotImplementedError(
                        "Searching through comments is not implemented yet."
                    )
                if "author" in search_in:
                    user_searcher = database.user.with_alias(
                        "user_search_on_" + hashed_term
                    )
                    subquery_parts.append(user_searcher.name.ilike(search_anywhere))
                    if negated_term:
                        subquery_parts[-1] = ~subquery_parts[-1] | (
                            user_searcher.name == None
                        )
                    select_parameters.setdefault("left", []).append(
                        user_searcher.on(
                            (user_searcher.gid == database.item.author)
                            & (user_searcher.name.ilike(search_anywhere))
                        )
                    )
                del search_anywhere
            if not subquery_parts:
                raise EdwhException("search_in parameter required")
            subquery = subquery_parts.pop(0)
            while subquery_parts:
                if negated_term:
                    # bij een exclusieve zoekterm, moeten alle losse onderdelen ge-and worden
                    # want term mag niet voorkomen in naam EN niet in omschrijving EN niet in auteur
                    subquery &= subquery_parts.pop()
                else:
                    # bij een positieve zoekterm moeten alle losse onderdelen ge-ord worden
                    # want de term mag voorkomen in naam OF in omschrijving OF in auteur ..
                    subquery |= subquery_parts.pop()
            # alle verschillende termen worden onderling ge-and, en komen samen met algemene
            # bepalingen zoals auteur mag niet null zijn enz
            query &= subquery
        return query

    def _apply_sort_order(self, order: SortOrder, select_parameters: dict):
        database = self.db

        if order == SortOrder.POPULARITY_ASC:
            select_parameters.setdefault("left", []).append(
                database.stats_subject_favs.on(
                    database.stats_subject_favs.gid == database.item.gid
                )
            )
            select_parameters["orderby"] = database.stats_subject_favs.favs
            if "groupby" in select_parameters:
                select_parameters["groupby"].append(database.stats_subject_favs.favs)

        elif order == SortOrder.POPULARITY_DESC:
            select_parameters.setdefault("left", []).append(
                database.stats_subject_favs.on(
                    database.stats_subject_favs.gid == database.item.gid
                )
            )
            select_parameters["orderby"] = ~database.stats_subject_favs.favs
            if "groupby" in select_parameters:
                select_parameters["groupby"].append(database.stats_subject_favs.favs)

        elif order == SortOrder.THUMBS_ASC:
            select_parameters.setdefault("left", []).append(
                database.stats_subject_thumbs.on(
                    database.stats_subject_thumbs.gid == database.item.gid
                )
            )

            select_parameters["orderby"] = database.stats_subject_thumbs.thumbs
            if "groupby" in select_parameters:
                select_parameters["groupby"].append(
                    database.stats_subject_thumbs.thumbs
                )

        elif order == SortOrder.THUMBS_DESC:
            select_parameters["left"] = database.stats_subject_thumbs.on(
                database.stats_subject_thumbs.gid == database.item.gid
            )
            select_parameters["orderby"] = ~database.stats_subject_thumbs.thumbs
            if "groupby" in select_parameters:
                select_parameters["groupby"].append(
                    database.stats_subject_thumbs.thumbs
                )

        elif order == SortOrder.RECENT_ASC:
            select_parameters["orderby"] = database.item.ts_changed
            if "groupby" in select_parameters:
                select_parameters["groupby"].append(database.item.ts_changed)

        elif order == SortOrder.RECENT_DESC:
            select_parameters["orderby"] = ~database.item.ts_changed
            if "groupby" in select_parameters:
                select_parameters["groupby"].append(database.item.ts_changed)

        elif order == SortOrder.RANDOM:
            pass

    # @diskcache.memoize_stampede(cache, expire=5, ignore=(0,))  # ignore self.
    def get_item_counts_per_tag_for_given_tag_combination_and_search_query(
        self,
        q: str,
        filtered_with: list = (),
        count_tree=False,
        included_visibilities: list[Visibility] | None = DEFAULT_INCLUDED_VISIBILITY,
        excluded_visibilities: list[Visibility] | None = DEFAULT_EXCLUDED_VISIBILITY,
    ):
        db = self.db
        select_parameters = {"groupby": db.mv__item_tags.tag_gid}
        query = db.mv__item_tags.tag_gid != None
        if filtered_with:
            # with_tags can be a list of tags (uuid)
            # [a,b,c] in which case all are ANDED
            # but when tuples of uuid appear they are ored in the query
            # [(a,b,c), (x,y,z)] ( a or b or c) OR!! (x or y or z)
            # [(a,b,c), d,e] (a or b or c) AND d AND e
            for tag in filtered_with:
                if isinstance(tag, (list, tuple)):
                    tag_list = tag
                    for tag in tag_list:
                        # left outer join voor OR functionaliteit
                        aliased_mv = db.mv__item_tags.with_alias(
                            "mv__item_tags__for__"
                            + tag.replace("-", "")
                            + "_"
                            + str(random.randint(10000, 100000))
                        )
                        select_parameters.setdefault("left", []).append(
                            aliased_mv.on(
                                (aliased_mv.item_gid == db.mv__item_tags.item_gid)
                                & (aliased_mv.tag_gid == tag)
                            )
                        )
                else:
                    # inner join voor AND functionaliteit
                    aliased_mv = db.mv__item_tags.with_alias(
                        "mv__item_tags__for__"
                        + tag.replace("-", "")
                        + "_"
                        + str(random.randint(10000, 100000))
                    )
                    select_parameters.setdefault("join", []).append(
                        aliased_mv.on(
                            (aliased_mv.item_gid == db.mv__item_tags.item_gid)
                            & (aliased_mv.tag_gid == tag)
                        )
                    )

        search_result = self.search_items(
            search=q,
            with_tags=filtered_with,
            search_in=["tag", "name", "description", "author"],
            included_visibilities=included_visibilities,
            excluded_visibilities=excluded_visibilities,
        )
        query &= db.mv__item_tags.item_gid.belongs(search_result.found)

        # craft the final query
        db_query = db(query)._select(
            db.mv__item_tags.tag_gid,
            db.mv__item_tags.item_gid.count(),
            **select_parameters,
        )
        # execute it to avoid dict handling and return tuples of values
        # [(tag-gid, count), ...]
        result = db.executesql(db_query)
        # convert the list of tuples to a dict for easy lookup
        return dict(result)

    def item(self, id: UUID, track: Callable = Magic) -> Item:
        """Vraagt een item op.

        :param id: id van het item.
        """

        @cached(self.db, key="core-backend-item-{id}", todb=todb, fromdb=fromdb)
        def fresh(id, track=Magic, cache_key=Magic):
            return Item.load(self.db, id, track)

        return fresh(
            id,
        )

    def user(
        self,
        id: UUID | str = None,
        email: str = None,
        parent_track: Callable = Magic,
    ) -> User:
        if email:
            if id:
                raise ValueError("Both ID and EMAIL are given, choose one. ")
            rows = self.db(self.db.user.email.lower() == email.lower().strip()).select(
                self.db.user.gid
            )
            if not rows:
                raise ValueError(f"No user found for email: {email!r}")
            id = rows.first().gid
        if id:

            @cached(self.db, key="core-backend-USER-{id}", todb=todb, fromdb=fromdb)
            def fresh(id, track=Magic, cache_key=Magic):
                parent_track(cache_key)
                return User.load(self.db, id, track)

            return fresh(id)
        raise ValueError("Either ID or EMAIL are required parameters. ")

    def property_bag(self, _id: UUID = None, belongs_to=None) -> PropertyBag:
        """Haalt de propertybag op met eigen uniek gid _id, of de propertybag die hoort bij belongs_to gid.

        :param _id: id van de property bag.
        :param belongs_to: id van het item, user, ....
        :return: property bag van een item.
        {
            id
            belongsTo
            bag
        }
        """
        if _id:
            # load based on property bags own gid
            row = self.db.property_bag(
                gid=str(_id),
            )
        else:
            # load based on related gid
            row = self.db.property_bag(belongs_to_gid=str(belongs_to))
        return PropertyBag(
            id=row.gid, belongs_to=row.belongs_to_gid, bag=row.properties
        )

    def available_items(self) -> int:
        """Geeft het aantal beschikbare items terug.

        :return:  aantal beschikbare items.

        """
        query = self.db.item.author != None
        query &= self.db.item.platform == PLATFORM
        return self.db(query).count()

    def login(
        self,
        email: str,
        hardware: dict,
        password: str | None = None,
        password_hash: str | None = None,
    ) -> Validated:
        """Logt de gebruiker in.

        :param email: email van de gebruiker.
        :param password_hash: password hash van de gebruiker.
        :param hardware: dictionary met hardware van de gebruiker.
        :return: Validated
        """
        if password:
            password_hash = hash_password(password)
        self.console("password_hash:", password_hash)
        db = self.db
        rows = db(db.user.email == email.strip().lower()).select()
        if not rows:
            self.console("invalid email: ", email)
            self.applog.login_failed(email, why="Invalid username or password")
            return Validated(
                ValidationCode.INVALID_CREDENTIALS, feedback="Invalid email"
            )
        row = rows.first()
        if row.password != password_hash:
            self.console("invalid password for ", email)
            self.applog.login_failed(email, why="Invalid username or password")
            return Validated(
                ValidationCode.INVALID_CREDENTIALS, feedback="Invalid password"
            )
        self.console("authenticated", email)

        if not (user := User.from_row(self.db, row)).has_validated_email:
            self.applog.login_failed(email, why="Unvalidated email address")
            return Validated(
                code=ValidationCode.REQUIRES_EMAIL_VALIDATION,
                feedback="Please validate your email address",
                user=user,
                token=self.new_session_token(hardware=hardware, user_gid=user.id),
            )
        session_token = self.new_session_token(hardware=hardware, user_gid=user.id)
        self.applog.login_user(hardware=hardware, user_gid=user.id)
        return Validated(ValidationCode.OK, token=session_token, user=user)

    def tags(
        self,
        first: int = None,
        with_tags: list[UUID | str] = None,
        offset: int = 0,
        order: SortOrder = SortOrder.RANDOM,
        search=None,
        ids=None,
        items_q=None,
        items_filtered_with=None,
    ) -> list[Tag]:
        db = self.db
        select_parameters = {}
        # start with a base query: all products
        query = db.tag.id > 0
        if with_tags:
            # convert possible UUIDs
            with_tags = [str(gid) for gid in with_tags]
            for tag in with_tags:
                # include each tag, including all at once will
                # generate an "AND tags LIKE '%|..|%' OR tags like ..."
                # we don't want that, we want to filter on all tags.
                query &= db.tag.meta_tags.contains(tag)
        if search:
            query &= db.tag.name.contains(search) | db.tag.description.contains(search)
        if ids:
            query &= db.tag.gid.contains(ids)
        elif order == SortOrder.RANDOM:
            pass
        else:
            raise ValueError("Unsupported sort order: " + str(order))
        if first or offset:
            # pagination, default value for first is 10000
            if not first:
                first = 10000
            select_parameters["limitby"] = (offset, offset + first)
        rows = db(query).select(db.tag.gid, **select_parameters)
        tags = [Tag.load(db, r.gid) for r in rows]

        return tags

    def contact(self, item: Item, question: str, me: User) -> tuple[bool, str]:
        if not me:
            return False, "U moet ingelogd zijn om een bericht te versturen."
        from edwh.core.backend.tasks import outbound_email_ask_question

        outbound_email_ask_question.delay(
            item.author.name,
            item.author.email,
            me.name,
            me.email,
            item.name,
            item_permalink=item.permalink,
            question=question,
        )
        self.applog.send_message(item.id, me.id, question, "ask_question")
        onbekend(
            f'{me.name} ({str(me.id)}) versturde bericht "{question}" over {item.name}({str(item.id)}) aan auteur {item.author.name}',
            "Bericht verstuurd op website",
            Priority.LOW,
            ["web-user-interaction"],
        )
        return True, "Bericht verstuurd. "

    def claim_ownership_unauthenticated(
        self, item: Item, email: str, tel: str, message: str
    ) -> tuple[bool, str]:
        # gegevens omzetten naar een link, opsturen per email ter
        # bevestiging van het email adres, daarna een bericht naaar de
        # eddie mailbox.
        domain = f'{os.getenv("APPLICATION_NAME")}.{os.getenv("HOSTINGDOMAIN")}'
        payload = dict(
            email=email,
            tel=tel,
            message=message,
            item_id=str(item.id),
        )
        token = jwt.encode(
            payload, os.getenv("EMAIL_VALIDATION_JWT_SECRET"), algorithm="HS256"
        )
        validation_link = f"https://{domain}/fragmentx/validate_for_claim?token={token}"
        from edwh.core.backend.tasks import outbound_email_validate_for_claim

        outbound_email_validate_for_claim.delay(
            email, item.name, message, validation_link
        )
        self.applog.anonymous_claimed(item.id, email, tel, message)
        onbekend(
            f'Anoniem claimt {item.name}({str(item.id)}) aan {email}/{tel} met bericht "{message}"',
            "Claim van item",
            Priority.LOW,
            ["web-user-interaction", "item-claim"],
        )
        return True, "Bevestigings e-mail verstuurd."

    def validate_ownership_claim(self, token) -> tuple[bool, str]:
        try:
            payload = jwt.decode(
                token, os.getenv("EMAIL_VALIDATION_JWT_SECRET"), algorithms=["HS256"]
            )
            email = payload["email"]
            tel = payload["tel"]
            message = payload["message"]
        except jwt.exceptions.InvalidSignatureError:
            return False, "Ongeldige token"
        except jwt.exceptions.ExpiredSignatureError:
            return False, "Token is verlopen"
        except jwt.exceptions.DecodeError:
            return False, "Ongeldige token"
        item = Item.load(self.db, payload["item_id"])
        if not item:
            return False, "Item niet gevonden"
        from edwh.core.backend.tasks import outbound_email_claim_notification_to_eddie

        outbound_email_claim_notification_to_eddie.delay(
            item.name, item.permalink, False, None, email, tel, message
        )
        self.applog.authenticated_claimed(item.id, payload["message"])
        onbekend(
            f'{email} gevalideerd voor claim op  {item.name}({str(item.id)}) met "{message}" ',
            "Claim adres gevalideerd",
            Priority.LOW,
            ["web-user-interaction", "item-claim"],
        )
        return True, "Bericht verstuurd. "

    def claim_ownership_authenticated(
        self, item: Item, me: User | str, tel: str, message: str
    ) -> tuple[bool, str]:
        from edwh.core.backend.tasks import outbound_email_claim_notification_to_eddie

        outbound_email_claim_notification_to_eddie.delay(
            item.name,
            item.permalink,
            True,
            me.name if isinstance(me, User) else None,
            me.email if isinstance(me, User) else me,
            tel,
            message,
        )
        self.applog.authenticated_claimed(item.id, message)
        onbekend(
            f'{me.name} ({str(me.id)}) claimde {item.name}({str(item.id)}) met "{message}" ',
            "Claim door bekende gebruiker",
            Priority.LOW,
            ["web-user-interaction", "item-claim"],
        )
        return True, "Bericht verstuurd. "

    def create_item(
        self,
        author: User | UUID | None,
        name: str,
        short_description: str,
        attachments=None,
        tags=None,
        thumbnail=None,
        by_eddie_email=None,
    ) -> Item:
        """Maakt een item aan.

        :param name: naam van het item.
        :param short_description: beschrijving van het item.
        :param attachments: attachment_rows die bij het item horen.
        :param tags: tag gids die bij het item horen.
        :param thumbnail: thumbnail van het item.
        :param by_eddie_email: email adres van de ingelogde eddie als dit door een eddie is gemaakt.
        :return: Item
        """
        item = Item.create(
            self.db,
            author=author,
            name=name,
            short_description=short_description,
            attachments=attachments,
            tags=tags,
            thumbnail=thumbnail,
        )
        self.applog.create_item(item.id, item.author.id, by_eddie_email)
        return item

    def update_item(
        self, id, name, short_description, attachments, tags, thumbnail
    ) -> None:
        """

        :param id: huidige id van het item.
        :param name: nieuwe naam van het item.
        :param short_description: nieuwe beschrijving van het item.
        :param attachments: nieuwe lijst met attachment_rows die bij het item horen.
        :param tags: nieuwe lijst met tag gids die bij het item horen.
        :param thumbnail: thumbnail van het item.
        :return: JSON response.
        """
        return None

    def update_user(
        self,
        me: User,
        user: User,
        email: str = None,
        password: str = None,
        firstname: str = None,
        lastname: str = None,
        location: str = None,
        organisation: str = None,
        primary_organisational_role: str = None,
        property_bag: dict = None,
        avatar: Attachment = None,
    ) -> User:
        db = self.db
        if me.id != user.id:
            raise SecurityException("You are not allowed to change someone else.")
        if db(db.user.email == email).count() > 0 and email != me.email:
            raise ValueError("403: Email address already in use")
        # user_record = db.user(gid=str(user.id))
        # old = user_record.copy()
        changes = {}
        if firstname:
            firstname = prepare_firstname(firstname)
            changes["firstname"] = firstname
        if lastname:
            lastname = prepare_lastname(lastname)
            changes["lastname"] = lastname
        if firstname or lastname:
            # if either firstname or lastname is given, but not both
            # the new lastname cannot be combined. load the missing value from the database record.
            firstname = firstname if firstname else user.firstname
            lastname = lastname if lastname else user.lastname
            name = f"{firstname} {lastname}"
            changes["name"] = name
        if organisation:
            changes["user_provided_organisation"] = organisation
        if primary_organisational_role:
            changes[
                "user_provided_primary_organisational_role"
            ] = primary_organisational_role
        if location:
            changes["user_provided_organisation_location"] = location
        if email:
            changes["email"] = email
        if password:
            changes["password"] = hash_password(password)
        if property_bag:
            # merge dictionaries, remove any None values
            changes["property_bag"] = {
                k: v
                for k, v in {**user.property_bag, **property_bag}.items()
                if v is not None
            }
        if avatar:
            if (
                db(
                    (db.attachment.gid == str(avatar.id))
                    & (db.attachment.purpose == "avatar")
                ).count()
                == 0
            ):
                raise EdwhException(
                    "404: avatar {} not found, or guid is not an avatar".format(avatar)
                )
            changes["avatar"] = str(avatar.id)
        if email:
            email = email.lower().strip()
            email_code = generate_email_verification_code(email)
            # step 1: mark email as new
            changes["has_validated_email"] = False
            changes["email_verification_code"] = email_code
        user_record = db.user(gid=str(user.id))
        user_record.update_record(**changes)
        db.commit()
        # reload the user
        user = User.load(db, gid=user.id)
        if email:
            from edwh.core.backend.tasks import outbound_email_verification_code

            # step 2: send a new email
            outbound_email_verification_code.delay(user.name, str(email_code), email)
        # signal_user_change(
        #     old,
        #     db(db.user.gid == user_id).select().first(),
        #     me,
        #     me.session_token,
        #     db=db,
        # )
        return user

    def upload_attachment(
        self,
        me: User,
        filename: str,
        filecontent: str,
        purpose: str,
        ts: datetime = None,
    ) -> Attachment:
        """Voegt een attachment toe.

        :param filename: bestandsnaam.
        :param content: b64-encoded bestand.
        :param purpose: purpose, moet 'background', 'avatar' of 'attachment' zijn.
        :param token: gebruikt deze token om te uploaden (eddie token uit session bijv), default: self.token
        :return: Attachment object.
        """
        known_purposes = ("background", "avatar", "attachment", "onderbouwing")
        if purpose not in known_purposes:
            raise BackendError("Unknown purpose: %s" % purpose)
        if ts is None:
            ts = datetime.now()
        gid = uuid4()
        self.db.attachment.insert(
            platform="SvS",
            gid=str(gid),
            attachment=None,
            filename=filename,
            purpose=purpose,
            ts_uploaded=ts,
            owner_gid=str(me.id),
            b2_uri=PROGRESS_GIF,
        )
        from edwh.core.backend.tasks import upload_attachment

        upload_attachment.delay(gid=gid, filename=filename, content=filecontent)
        self.applog.upload_attachment(attachment_gid=gid)
        onbekend(
            f"Upload van {gid} aangevraagd door {me} tbv {purpose}, base64 lengte:{len(filecontent)}."
        )
        return Attachment.load(self.db, gid)

        ### for reference: this is the old code, used to store the data in the database directly using
        ### web2py's own attachment technique (file on disk, filename in the database)
        # gid = uuid4()
        # attachment_id = self.db.attachment.insert(
        #     gid=gid,
        #     attachment=content,
        #     filename=filename,
        #     owner_gid=me.id,
        #     platform=PLATFORM,
        #     purpose=purpose,
        # )
        # row = self.db.attachment[attachment_id]
        # filename, fullname = db.attachment.attachment.retrieve(
        #     row.attachment, nameonly=True
        # )
        # self.dispatch(
        #     "attachment_saved", value=dict(filename=fullname, attachment_gid=gid)
        # )
        # return Attachment.load(self.db, gid)

    def upload_avatar(self, me: User, filename, filecontent, ts: datetime):
        """Saves the base64encoded filecontent for filename, stamped ts to db.attachment as an avatar.

        A dedicated URL is saved first, and the edwh.core.backend.tasks.upload_attachment is scheduled
        to process the upload of the filecontent, and update the URL after upload.
        """
        return self.upload_attachment(me, filename, filecontent, "avatar", ts)
        # gid = uuid4()
        # self.db.attachment.insert(
        #     platform="SvS",
        #     gid=str(gid),
        #     attachment=None,
        #     filename=filename,
        #     purpose="avatar",
        #     ts_uploaded=ts,
        #     owner_gid=str(self.me.id),
        #     b2_uri=PROGRESS_GIF,
        # )
        # upload_attachment.delay(gid=gid, filename=filename, content=filecontent)
        # self.applog.upload_attachment(attachment_gid=gid)
        # onbekend(f"Upload van {gid} aangevraagd, base64 lengte:{len(filecontent)}.")
        # return Attachment.load(self.db, gid)

    def add_organisation(self, name):
        org_row = self.db.organisation[self.db.organisation.insert(name=name)]
        self.applog.create_organisation(gid=org_row.gid, name=name)
        onbekend(f"Nieuwe organisatie: '{name}' : {org_row.gid}")
        return org_row.gid

    def create_user(
        self,
        email,
        password,
        firstname,
        lastname,
        organisation,
        location,
        primary_organisational_role,
        property_bag,
    ) -> User:
        # TODO: nieuwe error classes van maken en die raisen, zodat afhandeling specifieker kan.
        db = self.db
        email = email.lower().strip()
        if (not email.lower().endswith("@educationwarehouse.nl")) and db(
            db.user.email == email
        ).count() > 0:
            # disallow duplicate email addresses unless it's an educationwarehouse.nl address
            raise ValueError("403: Email address already in use")
        domain = email.split("@", 1)[1]
        if "@" in domain:
            # disllow pietje@puk@bla.nl
            raise ValueError("400: invalid email address")
        query = db.email_domain.domain.lower() == domain
        domain_row = db(query).select().first()
        if not domain_row:
            raise SecurityException('403: unknown domain "{}" '.format(domain))
        if not domain_row.is_new_user_allowed:
            raise SecurityException(
                '403: known domain "{}" is disallowed to join new members'.format(
                    domain
                )
            )
        # TODO: enforce complexity requirements for the password
        user_gid = uuid4()
        email_code = generate_email_verification_code(email)
        firstname = prepare_firstname(firstname)
        lastname = prepare_lastname(lastname)
        name = f"{firstname} {lastname}"
        new_id = db.user.insert(
            gid=user_gid,
            firstname=firstname,
            lastname=lastname,
            user_provided_organisation=organisation,
            user_provided_organisation_location=location,
            user_provided_primary_organisational_role=primary_organisational_role,
            name=name,
            email=email,
            api_token=None,
            email_verification_code=email_code,
            password=hash_password(password),
            property_bag=property_bag,
            platform=[PLATFORM],  # TODO: uitbreiden indien mogelijk
            has_validated_email=False,
        )
        db.commit()
        self.console("Created new user", email, "as", user_gid)
        from edwh.core.backend.tasks import outbound_email_verification_code

        outbound_email_verification_code.delay(firstname, str(email_code), email)
        # signal_user_change(
        #     None, db.user[new_id], None, session_token, platform=platform, db=db
        # )
        return User.load(self.db, user_gid)

    def recover(self, email):
        # test if there is a matching user
        rows = self.db(self.db.user.email == email.lower()).select()
        user_gid = rows.first().gid if rows else None
        # register this event
        self.applog.reset_password(email, user_gid)
        # if a user exists, convert to user object and send email
        if user_gid:
            user = User.load(self.db, user_gid)
            password = user.set_password(self.db, "NEW")
            # only send recovery email if a user record was found
            from edwh.core.backend.tasks import outbound_email_new_password

            outbound_email_new_password.delay(
                user.firstname if user.firstname else user.name, password, email
            )
            return user
        return None

    def validate_email_address(self, user: User, entered_code: str):
        if entered_code.strip() == str(user.email_verification_code):
            self.db(self.db.user.gid == str(user.id)).update(has_validated_email=True)
            self.db.commit()
            self.applog.email_validated(user.id)
        else:
            self.applog.invalid_email_code(user.id)
            warning(
                f"Ongeldige email validatie code voor gebruiker {user.id}/{user.email}"
            )
            raise SecurityException("403: Onjuiste email validatie code")

    def mark(
        self,
        user: User,
        subject_gid: UUID,
        name: str,
        mark: int,
        list_gid: UUID | None = None,
    ):  # mark is the value
        if not (user and user.has_validated_email):
            raise SecurityException(
                "403: anonymous or unvalidated user is not allowed to mark"
            )
        db = self.db
        name = name.lower()
        subject_gid = str(subject_gid)
        if name not in ("fav", "thumbs"):
            raise ValueError("mark {} is not supported".format(mark))
        if name == "fav":
            # if list_id is not given it's the usual bunch. Can be used if the interface doesn't use different lists
            if mark not in (0, 1):
                raise ValueError(
                    "Favorite mark should be either 0 or 1, not " + str(mark)
                )
        elif name == "thumbs":
            if mark not in (-1, 0, 1):
                raise ValueError(
                    "Thumbs mark should be either -1, 0 or 1, not " + str(mark)
                )
        if list_gid:
            if db(db.fav_list.gid == list_gid).count() == 0:
                raise EdwhException(
                    "404: List_id {} references an unknown list ".format(list_gid)
                )
        subject_type = self.get_item_type(subject_gid)
        gid = uuid4()
        where = (
            (db.mark.user_gid == str(user.id))
            & (db.mark.subject_gid == subject_gid)
            & (db.mark.name == name)
            & (db.mark.list_gid == list_gid)
        )
        db.mark.update_or_insert(
            where,
            gid=gid,
            platform=PLATFORM,
            user_gid=str(user.id),
            subject_gid=subject_gid,
            subject_type=subject_type,
            mark=mark,
            name=name,
            ts=datetime.now(),
            list_gid=list_gid,
        )
        self.applog.update_mark(subject_gid, mark, name)
        db.commit()
        return subject_type, gid

    def invalidate_search_results(self) -> None:
        from edwh.core.pgcache import clear_cache

        clear_cache(self.db, "%[searchresult]%")

    def invalidate(self, table: str | DAL.Table, gid: UUID | str):
        if isinstance(table, str):
            if table not in self.db.tables:
                raise KeyError(
                    f'INVALIDATOIN ERROR: Table "{table}" is unknown in dal: {self.db}'
                )
            table = getattr(self.db, table)
        if "gid" not in table.fields:
            raise KeyError(
                f'INVALIDATION ERROR: Table "{table}" does not have field gid but:{table.fields}. '
            )
        print(f"Invalidating {table}.{gid}")
        from edwh.core.pgcache import cache_ids_that_depend_on, define_models

        try:
            define_models.define_model(self.db)
        except Exception as e:
            print(e)
        try:
            cache_entry = (
                self.db(self.db.cache.gid == gid).select(self.db.cache.id).first().id
            )
            print(
                "Should remove:\n",
                cache_ids_that_depend_on(self.db, cache_entry),
            )
        except Exception as e:
            print(e)
            cache_entry = None

        self.db(table.gid == str(gid)).update(gid=str(gid))
        self.db.commit()

    # def download(self, id: str):
    # oude download, bedoeld voor als files niet opgeslagen zijn op B2
    #     query = """
    #     query download($token:UUID!, $id:UUID!){
    #         auth(sessionToken: $token){
    #             download(id:$id){
    #                 uri,
    #                 b64Content
    #             }
    #         }
    #     }
    #     """
    #     env = dict(token=backend.token, id=id)
    #
    #     resp = self.query(query, env, "download")
    #     data = dotmap.DotMap(resp["data"])
    #
    #     download = data["auth"]["download"]
    #     if not download:
    #         return ""
    #
    #     uri = download["uri"]
    #     if not uri:
    #         uri = f"data:image/*;base64,{download['b64Content']}"
    #     self.applog.download_attachment(attachment_gid=id, from_backend=not uri)
    #     return uri
