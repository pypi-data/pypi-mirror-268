import datetime
import re
import time
import uuid
from enum import Enum, auto
from pprint import pprint

from attrs import asdict, define, field
from pydal import DAL, Field, SQLCustomType
from pydal.validators import IS_EMAIL, IS_IN_SET, IS_MATCH

RE_EMAIL = re.compile(
    r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
)
RE_DOMAIN = re.compile(r"[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
RE_UUID = re.compile(
    r"[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}"
)


class Status(Enum):
    DRAFT = "draft"
    PROPOSED = "proposed"
    PUBLISHED = "published"
    # REJECTED = 'rejected'
    HIDDEN = "hidden"
    RETRACTED = "retracted"


class Role(Enum):
    LOCAL_EDITOR = auto()
    TEAM = auto()
    DOMAIN = auto()
    PUBLIC = auto()
    CENTRAL_EDITOR = auto()


values = lambda enum_items: {s.value for s in enum_items}
CENTRAL_EDITOR_QUERY_STATUSES = values(Status)
LOCAL_EDITOR_QUERY_STATUSES = values(
    {Status.DRAFT, Status.PROPOSED, Status.PUBLISHED, Status.RETRACTED}
)  # later uit te breiden met Status.hidden
TEAM_QUERY_STATUSES = values(
    {Status.PROPOSED, Status.PUBLISHED, Status.RETRACTED}
)  # later uit te breiden met Status.hidden
DOMAIN_QUERY_STATUSES = values(
    {Status.PROPOSED, Status.PUBLISHED, Status.RETRACTED}
)  # later mogelijk uit te breiden met Status.hidden
PUBLIC_QUERY_STATUSES = values(
    {Status.PUBLISHED, Status.RETRACTED}
)  # later mogelijk uit te breiden met Status.hidden

visible_statuses_per_role = {
    Role.LOCAL_EDITOR: LOCAL_EDITOR_QUERY_STATUSES,
    Role.TEAM: TEAM_QUERY_STATUSES,
    Role.DOMAIN: DOMAIN_QUERY_STATUSES,
    Role.PUBLIC: PUBLIC_QUERY_STATUSES,
    Role.CENTRAL_EDITOR: CENTRAL_EDITOR_QUERY_STATUSES,
}

status_dal_type = SQLCustomType(
    type="string",
    native="text",
    encoder=lambda status: status.value,
    decoder=lambda fromdb: Status(fromdb),
)
uuid_dal_type = SQLCustomType(
    type="string",
    native="uuid",
    encoder=lambda id: str(id),
    decoder=lambda fromdb: uuid.UUID(fromdb),
    represent=lambda _uuid: str(_uuid)[:5] + "+",
)
datetime_dal_type = SQLCustomType(type="datetime")


class Scope(Enum):
    EDITOR = auto()
    TEAM = auto()
    DOMAIN = auto()
    PUBLIC = auto()


@define
class State:
    gid: uuid.UUID = field()
    editor_status: Status = field()
    team_status: Status = field()
    domain_status: Status = field()
    public_status: Status = field()
    by: str = field()
    origin_domain: str = field()

    # remove microsecond part since this isn't stored in the database. And it's useless for our case.
    ts: datetime.datetime = field(
        factory=lambda: datetime.datetime.now().replace(microsecond=0)
    )
    transaction_gid: uuid.UUID = field(factory=uuid.uuid4)

    @by.validator
    def check_email(self, attribute, value):
        if not RE_EMAIL.fullmatch(value):
            raise ValueError(f"Invalid email format {value!r}")


def REQUIRED(fieldname):
    def wrapped():
        raise ValueError(f"Value missing for field {fieldname}")

    return wrapped


@define
class SomeState(State):
    __tablename = "some"
    value: str = field(
        default=REQUIRED("value")
    )  # required is a workaround to force a default argument

    @classmethod
    def from_db(cls, db, row):
        return cls(
            **{
                field: row[field]
                for field in db[cls.__tablename].fields
                if field != "id"
            }
        )

    @classmethod
    def from_row(cls, row: DAL.Row):
        return cls(
            gid=row.gid,
            editor_status=row.editor_status,
            team_status=row.team_status,
            domain_status=row.domain_status,
            public_status=row.public_status,
            by=row.by,
            origin_domain=row.origin_domain,
            ts=row.ts,
            transaction_gid=row.transaction_gid,
            value=row.value,
        )

    @classmethod
    def most_recent(
        cls, db: DAL, as_role: Role, domain: str, gid: uuid.UUID = None, debug=False
    ):
        """Dit moet de meest recente rij opgegeven binnen de opgegeven belemmeringen"""
        # TODO: domain wordt nu nog niet gebruikt, en de vraag is of dat nodig is.
        # immers een instantie mag alleen maar krijgen wat bij het eigen domein afkomstig is
        # of wat is aangeboden vanuit landelijk.
        field_for_role = {
            Role.LOCAL_EDITOR: "editor_status",
            Role.TEAM: "team_status",
            Role.DOMAIN: "domain_status",
            Role.PUBLIC: "public_status",
            Role.CENTRAL_EDITOR: "editor_status",
        }

        table = db[cls.__tablename]
        table_rname = table._rname
        # if given a gid, it should be considered, otherwise all the relevant rows should be returned
        gid_clause = f"{table_rname}.gid = '{str(gid)}'" if gid else "(true)"
        # as the central editor role, domain is irrelevant as a criteria
        origin_clause = (
            f"{table_rname}.origin_domain = '{domain}'"
            if as_role != Role.CENTRAL_EDITOR
            else "true"
        )

        # this subselect should return all the id's for the unique rows which should
        # be valid for the given the creteria. The fields are then selected given these id's (to avoid huge group by clauses)
        # for performance reasons this might turn into a CTE, but that's premature optimization for now.
        # the most accurate row can yield a HIDDEN status for the respective scope status.
        # Hidden rows are filtered in the query which consumes this one.
        # basically it's the effective dated rows, based on the domain and gid selection
        # If we would include the hidden check in here, we would filter out all the hidden rows, but that might be
        # effective status for this selection, so that filtering has to be done a layer up.
        # the where filters on BOTH gid and domain, because the status can be different for the same gid
        # across the different domains.
        subselect = f"""
            select id
              from {table_rname}
             where
                   {gid_clause}
                   and ts = (
                    select max(ts)
                      from {table_rname} as effdted
                      where effdted.gid = {table_rname}.gid
                        and effdted.origin_domain = {table_rname}.origin_domain
                        and {field_for_role[as_role]} in ({", ".join(f"'{_}'" for _ in visible_statuses_per_role[as_role])})
                   ) and ({origin_clause})
             group by id
        """
        if debug:
            print("subselect: ")
            print(subselect)
            print("subselect result: ")
            print(db.executesql(subselect))

        # the selection of fields and the filtering on the scope_status field being anything but 'hidden'
        sql = f"""
        select *
          from {table_rname}
         where id in (
            {subselect}
         )
        """
        if debug:
            print("complete query:")
            print(sql)
        result = (cls.from_row(row) for row in db.executesql(sql, fields=table))
        if debug:
            result_list = list(result)
            print("result:")
            pprint(result_list)
            # returna  new generator
            return (_ for _ in result_list)
        else:
            return result


def state_table(db: DAL):
    return db.Table(
        db,
        "state",
        Field(
            "gid",
            uuid_dal_type,
            comment="The GID of the object for which this is a state.",
        ),
        Field(
            "editor_status",
            status_dal_type,
            requires=IS_IN_SET(set(s.value for s in Status)),
        ),
        Field(
            "team_status",
            status_dal_type,
            requires=IS_IN_SET(set(s.value for s in Status)),
        ),
        Field(
            "domain_status",
            status_dal_type,
            requires=IS_IN_SET(set(s.value for s in Status)),
        ),
        Field(
            "public_status",
            status_dal_type,
            requires=IS_IN_SET(set(s.value for s in Status)),
        ),
        Field("by", "string", requires=IS_EMAIL),
        Field("origin_domain", "string", requires=IS_MATCH(RE_DOMAIN.pattern)),
        Field(
            "ts",
            "datetime",
            default=lambda: datetime.datetime.now().replace(microsecond=0),
        ),
        Field(
            "transaction_gid",
            uuid_dal_type,
            requires=IS_MATCH(RE_UUID.pattern),
            default=lambda: str(uuid.uuid4()),
        ),
    )
