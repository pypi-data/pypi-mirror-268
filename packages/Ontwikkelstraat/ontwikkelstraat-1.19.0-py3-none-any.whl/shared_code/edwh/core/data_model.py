import datetime
import enum
import json
import random
import uuid

import iso3166
from edwh.core.pgcache import ValueSortableEnum
from pydal import DAL, Field
from pydal.validators import (
    IS_EMAIL,
    IS_EMPTY_OR,
    IS_HTTP_URL,
    IS_IN_DB,
    IS_IN_SET,
    IS_LENGTH,
    IS_LIST_OF,
    IS_MATCH,
    IS_NULL_OR,
    IS_UPPER,
    IS_URL,
)

SO_CLUSTER = {
    1: "Cluster 1: blind, slechtziend",
    2: "Cluster 2: doof, slechthorend of taals-praakontwikkelingstoornis",
    3: "Cluster 3: lichamelijk/verstandelijk gehandicapt, langdurig ziek (somatisch)",
    4: "Cluster 4: psychisch stoornissen en gedragsproblemen",
}

EDUCATION_LEVEL = dict(
    bo="Basis onderwijs",
    po="Praktijk onderwijs",
    lwoo="LWOO",
    bb="VMBO Basis beroeps",
    bk="VMBO Kader beroeps",
    gl="VMBO Gemende leerweg",
    tl="VMBO theoretische leerweg",
    havo="HAVO",
    vwo="VWO",
    gym="Gymnasium",
)

EDUCATION_SECTOR = dict(
    po="Primair onderwijs",
    so="Speciaal onderwijs",
    vo="Voortgezet onderwijs",
    vso="Voortgezet speciaal onderwijs",
    mbo="Middelbaar beroeps onderwijs",
    hbo="Hoger beroeps onderwijs",
    wo="Wetenschappelijk onderwijs",
)

EDUCATION_TYPE = dict(r="Regulier onderwijs", s="Speciaal onderwijs")

COUNTRIES = {
    code: f"{country.apolitical_name} ({country.alpha2})"
    for code, country in iso3166.countries_by_alpha2.items()
}

DENOMINATION = {
    "Onbekend": "Onbekend",
    "Openbaar": "Openbaar",
    "Algemeen bijzonder": "Algemeen bijzonder",
    "Rooms-Katholiek": "Rooms-Katholiek",
    "Protestants-Christelijk": "Protestants-Christelijk",
    "Gereformeerd": "Gereformeerd",
    "Reformatorisch": "Reformatorisch",
    "Samenwerking PC, RK": "Samenwerking PC, RK",
    "Overige": "Overige",
    "Samenwerking RK, Alg. Bijz.": "Samenwerking RK, Alg. Bijz.",
    "Samenwerking PC, RK, Alg. Bijz": "Samenwerking PC, RK, Alg. Bijz",
    "Samenwerking PC, Alg. Bijz.": "Samenwerking PC, Alg. Bijz.",
    "Antroposofisch": "Antroposofisch",
    "Samenwerking Opb., PC": "Samenwerking Opb., PC",
    "Samenwerking Opb., PC, RK, Alg": "Samenwerking Opb., PC, RK, Alg",
    "Protestants-Christelijk/Evange": "Protestants-Christelijk/Evange",
    "Samenwerking Opb., RK": "Samenwerking Opb., RK",
    "Samenwerking Opb., Alg. Bijz.": "Samenwerking Opb., Alg. Bijz.",
    "Interconfessioneel": "Interconfessioneel",
    "Joods orthodox": "Joods orthodox",
    "Evangelisch": "Evangelisch",
    "Protestants Christelijk/Reform": "Protestants Christelijk/Reform",
    "Islamitisch": "Islamitisch",
    "Gereformeerd vrijgemaakt": "Gereformeerd vrijgemaakt",
    "Hindoestisch": "Hindoestisch",
    "Evangelische broedergemeenscha": "Evangelische broedergemeenscha",
    "Samenwerking Opb., PC, Alg. Bi": "Samenwerking Opb., PC, Alg. Bi",
}


class OrganisationPriority(enum.Enum):
    HISTORY = 0
    DUO = 100
    MINION = 200
    EDDIE = 500


class Visibility(ValueSortableEnum):
    ALL = "all"  # public to all, 'delen.meteddie.nl' platform
    DELETED = "deleted"  # hide deleted, can be mixed with others
    HIDDEN = "hidden"  # hide hidden, can be mixed with others
    DEBUG = "debug"  # only visible to developers
    PIPELINE = "pipeline"  # work in progress, typically named 'indicators'
    PLATFORM_LEF_ONLY = "lef"  # show only on the LEF platform


# default tiles visibilities:
DEFAULT_INCLUDED_VISIBILITY = {Visibility.ALL}
DEFAULT_EXCLUDED_VISIBILITY = {
    Visibility.DELETED,
    Visibility.HIDDEN,
    Visibility.DEBUG,
    Visibility.PIPELINE,
}
# for new items:
DEFAULT_ITEM_VISIBILITY = {Visibility.PIPELINE, Visibility.ALL}


def new_uuid():
    return str(uuid.uuid4())


def now():
    return datetime.datetime.now()


# noinspection PyPep8Naming
def BELONGS_TO(db, where_generator):
    """
    Requires the value to be within a database.
    Example:
        requires=BELONGS_TO(database, lambda db, v: db.organisation.gid == v)
    """

    # graciously copied from web2py
    # (value, error) = validator(value)
    def validator(value):
        if db(where_generator(db, value)).count() > 0:
            return value, None
        else:
            return value, "404: {} not found as a reference"
        pass

    return validator


# from pydal import SQLCustomType
# http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer?search=virtualfield#Custom-Field-types
# JsonCustomType(type='json', native='json', encode=)

ONDERBOUWING_OPTIES = {
    "EKeE": "Eigen kennis en ervaring",
    "GOW": "Gebaseerd op wetenschap",
    "EBE": "Elders bewezen effectief",
    "HBE": "Hier bewezen effectief",
}

LICENSES = {
    "pd": "public domain",
    "cc0": "CC0 (no rights reserved)",
    "cc-by-4.0": "CC BY (attribution)",
    "cc-by-sa-4.0": "CC BY SA (attribution, sharealike)",
    "cc-by-nc-4.0": "CC BY NC (attribution, non-commercial)",
    "cc-by-nc-sa-4.0": "CC BY NC SA (attribution, non-commercial, sharealike)",
    "cc-by-nd-4.0": "CC BY ND (attribution, no-derivatives)",
    "cc-by-nd-nc-4.0": "CC BY ND NC (attribution, no-derivatives, non-commercial)",
    "copyright": "Copyright (all rights reserved)",
}

DEFAULT_LICENSE = "cc-by-sa-4.0"


# noinspection PyUnusedLocal
def setup_db_tables(database: DAL, *p, enable_versioning=False, **kwp) -> DAL:
    """Define the tables for the given database.
    supported KWP:
        * 'enable_versioning' to enable pydals record versioning on select tables (board, organisation, ...?)
    """
    database.define_table(
        "comment",
        Field("platform", "string"),  # Debug, SvS, ION
        Field("author"),
        Field("gid", default=new_uuid),
        Field("concerning"),  # gid of item  # TODO: rename to subject_gid
        Field("in_response_to"),  # gid of parent comment
        Field("body"),
        Field("ts_created", "datetime", default=now),
        Field("ts_last_change", "datetime", default=now),
    )

    # noinspection HttpUrlsUsage
    database.define_table(
        "item",
        Field("platform", "string", default="SvS"),  # Debug, SvS, ION
        Field("gid", default=new_uuid),
        Field("author"),  # user_gid
        Field("name"),
        Field("thumbnail", default="http://lorempixel.com/400/200/"),
        Field("short_description", "text", requires=IS_LENGTH(2**15)),
        Field("ts_changed", "datetime"),
        Field("tags", "list:string"),  # list of tags/tagids
        Field("slug"),
        Field("alternatives", "list:string"),  # list of item gids
        Field("backgrounds", "list:string"),  # list of attachment gids
        Field("attachments", "list:string"),  # list of attachment gids
        Field(
            "since_when", "date", comment="Wanneer is deze ontwikkelpraktijk gestart?"
        ),
        Field(
            "upto_when",
            "date",
            comment="Wanneer is deze ontwikkelpraktijk geëindigd? S.v.p. leeg laten als de ontwikkelpraktijk nog aan de gang is.",
        ),
        Field(
            "video_urls",
            "list:string",
            requires=IS_URL(
                mode="generic",
                allowed_schemes=["http", "https"],
                prepend_scheme="https",
            ),
            comment="Vul hier eventuele URLs in die naar video's verwijzen. Voorbeeld: https://youtube.com/watch?voorbeeld",
        ),
        Field(
            "onderbouwing",
            "string",
            length=6,
            requires=IS_IN_SET(ONDERBOUWING_OPTIES),
            default="EKeE",
        ),
        Field("onderbouwing_bronnen", "list:string"),  # list of attachment gids
        Field("onderbouwing_links", "list:string"),  # lijst van urls
        Field(
            "license", "string", requires=IS_IN_SET(LICENSES), default=DEFAULT_LICENSE
        ),
        Field(
            "extra_contactgegevens",
            "list:string",
            requires=IS_LIST_OF(
                IS_EMPTY_OR(
                    IS_MATCH(
                        r".*;[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]+",
                        strict=True,
                        error_message="Gebruik het formaat: 'naam;emailadres'",
                    )
                )
            ),
        ),
        Field(
            "visibility",
            "list:string",
            default=["pipeline"],
            requires=IS_IN_SET(
                [v.value for v in Visibility], multiple=True, zero="pipeline"
            ),
        ),
    )
    if enable_versioning:
        database.item._enable_record_versioning(
            archive_name="item_archive",
            current_record="current_record",
            is_active="is_active",
        )
    database.define_table(
        "user",
        Field("platform", "list:string", default=["debug"]),  # Debug, SvS, ION
        Field("name"),
        Field("email"),
        Field("password"),
        Field("gid"),
        Field("api_token"),
        Field("has_validated_email", "boolean", default=False),
        Field(
            "email_verification_code",
            "integer",
            default=lambda: random.randint(10000, 999999),
        ),  # # def new_user and update_user will override based on email.
        Field("property_bag", "json"),
        Field("avatar"),  # GID or None
        Field("firstname", "string", length=128),
        Field("lastname", "string", length=128),
        Field("user_provided_organisation", "string", length=256),
        Field("user_provided_primary_organisational_role", "string", length=128),
        Field("user_provided_organisation_location", "string", length=128),
        Field("reset_key", "string"),
    )

    database.define_table(
        "session",
        Field("platform", "string"),  # Debug, SvS, ION
        Field("user_gid"),
        Field("session_token", default=new_uuid),
        Field("hw_specs"),
        Field("started", "datetime", default=datetime.datetime.now),
        Field("last_seen", "datetime"),
        Field("upgrades", "list:string"),
        Field("gid_hash", "string", length=20),
    )

    database.define_table(
        "tag",
        Field("platform", "string"),  # Debug, SvS, ION
        Field("gid", default=new_uuid),
        Field("name"),
        Field("slug"),
        Field("parents", "list:string"),  # which is the parent tag, None is root
        Field("children", "list:string"),  # direct descendants, in order
        Field("description"),
        Field("meta_tags", "list:string"),
        Field("akas", "list:string"),
        Field("search_hints", "text"),
        Field("definition_source", "string"),
        Field("restrictions", "text"),
        Field("definition", "text"),
        Field("instructions", "text"),
        Field("remarks", "text"),
        Field("deprecated", "boolean", default=False),
        Field("replaced_by"),  # uuid
        Field("questions", "list:string"),
        Field("definitions_of_done", "list:string"),
        Field("related", "list:string"),
    )

    database.define_table(
        "tag_comment",
        Field("gid", "string", default=new_uuid),
        Field(
            "tag_gid", "string", requires=IS_IN_DB(database, "tag.gid", "%(tag.name)s")
        ),
    )

    database.define_table(
        "fav_list",
        Field("platform", "string"),  # Debug, SvS, ION
        Field("gid", default=new_uuid),
        Field("name"),
        Field("slug"),  # non unique!!!
    )

    database.define_table(
        "fav_list_member",
        Field("platform", "string"),  # Debug, SvS, ION
        Field("gid", default=new_uuid),
        Field("list_gid", "string"),  # uuid of the list
        Field("user_gid"),  #
        Field("ts", "datetime"),  # since when?
        Field("list_role", "string", default="owner"),
    )

    database.define_table(
        "mark",  # favorites live here as well!
        Field("platform", "string"),  # Debug, SvS, ION
        Field("gid", default=new_uuid),  # gid of this vote
        Field("user_gid"),  # refers to user
        Field("subject_gid"),  # refers to whatever is being voted
        Field("subject_type"),  # item/comment/user/tag
        Field("list_gid", "string"),  # uuid of the list
        Field(
            "mark", "integer"
        ),  # what value is being voted/marked , depends on vote_type
        Field("name", "string"),  # what aspect of subject is being voted, or favorite
        Field("ts", "datetime"),  # last update
    )
    database.define_table(
        "event_stream",
        Field("gid", default=new_uuid),  # gid of this organisation
        Field("platform", "string"),  # Debug, SvS, ION
        Field("user_gid"),
        Field("subject_gid"),
        Field("subject_type"),  # item/comment/user/tag
        Field("ts", "datetime"),  # last update
        Field("title"),
        Field("msg"),
        Field("doc", "blob"),  # pickle of
        Field("crud", length=1),
        Field("session_token"),
    )

    database.define_table(
        "user_notification",
        Field("gid", default=new_uuid),  # gid of this organisation
        Field("platform", "string"),  # Debug, SvS, ION
        Field("user_gid"),
        Field("subject_gid"),
        Field("subject_type"),  # item/comment/user/tag/fav_list
        Field("ts", "datetime"),  # last update
        Field("title"),
        Field("msg"),
        Field("read_ts", "datetime"),  # datetime stamp or Null
    )
    database.define_table(
        "board",
        Field("gid", default=new_uuid),  # gid of this organisation
        Field("name", description="doopnaam, officiele (DUO) naam.", label="Naam"),
        Field("street", "string", length=128, label="Straat"),
        Field("number", "string", length=128, label="Huisnummer"),
        Field("postalcode", "string", label="Postcode"),
        Field("city", "string", length=128, requires=IS_UPPER(), label="Plaats"),
        Field(
            "website",
            "string",
            length=512,
            description="Bestuur website",
            requires=IS_EMPTY_OR(IS_URL()),
        ),
        Field("last_saved_by"),
        Field("last_saved_when", "datetime"),
    )
    if enable_versioning:
        database.board._enable_record_versioning(
            archive_name="board_archive",
            current_record="current_record",
            is_active="is_active",
        )

    organisation = database.define_table(
        "organisation",
        Field(
            "platform", "string", default="SvS", writable=False, readable=False
        ),  # Debug, SvS, ION
        Field("effdt", "datetime", readable=True, writable=False),
        Field("effstatus", "boolean", default=True),
        Field("gid", default=new_uuid),  # gid of this organisation
        Field("prio", "integer", default=0, writable=False),  # gid of this organisation
        Field(
            "brin",
            "string",
            label="Instellingscode",
            requires=IS_NULL_OR(
                [
                    IS_UPPER(),
                    IS_MATCH(
                        r"[0-9]{2}[a-zA-Z]{2}", "BRIN format is 2 decimalen, 2 letters"
                    ),
                ]
            ),
        ),
        Field(
            "vestigingscode",
            "string",
            requires=IS_NULL_OR(
                [
                    IS_UPPER(),
                    IS_MATCH(
                        r"[0-9]{2}[a-zA-Z]{2}[0-9]{2}",
                        "Vestigingscode is BRIN format + 2 decimalen",
                    ),
                ]
            ),
        ),
        Field("name", description="Officiele (DUO) naam.", label="Doopnaam"),
        Field(
            "aka",
            "string",
            description="Naam zoals de school bekend staat",
            label="Roepnaam",
        ),
        Field(
            "website",
            "string",
            length=512,
            description="School website",
            requires=IS_NULL_OR([IS_HTTP_URL()]),
        ),
        Field(
            "country_code",
            "string",
            default="NL",
            requires=IS_NULL_OR([IS_IN_SET(COUNTRIES, zero="NL")]),
            label="Land code",
        ),
        Field("coc", "integer", label="KVK Nummer"),
        Field("coc_location", "integer", label="KVK Vestigings nummer"),
        Field("phone", "string", length=15, label="Tel."),
        Field("street", "string", length=128, label="Straat"),
        Field("number", "string", length=128, label="Huisnummer"),
        Field("postalcode", "string", label="Postcode"),
        Field("city", "string", length=128, label="Plaats"),
        Field(
            "country_code",
            "string",
            default="NL",
            requires=IS_NULL_OR(IS_IN_SET(COUNTRIES)),
            label="Land",
        ),
        Field("correspondence_city", "string", readable=False, writable=False),
        Field("correspondence_street", "string", readable=False, writable=False),
        Field("correspondence_number", "string", readable=False, writable=False),
        Field(
            "correspondence_postalcode",
            "string",
            requires=IS_UPPER(),
            readable=False,
            writable=False,
        ),
        Field(
            "correspondence_country",
            "string",
            length=2,
            default="NL",
            requires=IS_NULL_OR(IS_IN_SET(COUNTRIES)),
            readable=False,
            writable=False,
        ),
        Field(
            "tag_gid",
            "string",
            length=36,
            requires=IS_EMPTY_OR(IS_IN_DB(database, "tag.gid", "%(name)s")),
            comment="De tag moet al bestaan, deze kun je aanmaken via het Tags menu en hier koppelen. "
            "Let op: de tag moet de parent 'Organisations' hebben!",
        ),
        Field(
            "lonlat",
            "point",
            comment="`(4.4678539,52.1414083)` bijvoorbeeld. Point type, longitude-latitude (net andersom dan google)",
            label="Coordinaten",
        ),
        Field(
            "scholen_op_de_kaart_url",
            "string",
            length=512,
            requires=IS_EMPTY_OR(IS_HTTP_URL()),
        ),
        Field("email", "string", length=512, requires=IS_EMPTY_OR(IS_EMAIL())),
        Field(
            "ceo_name",
            "string",
            length=512,
            label="Directeur naam",
            readable=False,
            writable=False,
        ),
        Field(
            "ceo_email",
            "string",
            length=512,
            label="Directeur email",
            readable=False,
            writable=False,
        ),
        Field(
            "ceo_phone",
            "string",
            length=512,
            label="Directeur telefoon",
            readable=False,
            writable=False,
        ),
        Field(
            "quality_assurance_plan",
            "string",
            requires=IS_NULL_OR(IS_HTTP_URL()),
            label="Schoolplan",
        ),
        Field("aantekeningen", "text", comment="Aantekeningen voor eddies onderling."),
        Field(
            "validated_by",
            "string",
            length=36,
            label="Gevalideerd door",
            writable=False,
        ),
        Field("validated_ts", "datetime", label="Gevalideerd op", writable=False),
        Field(
            "education_type",
            "string",
            length=1,
            requires=IS_NULL_OR(IS_IN_SET(EDUCATION_TYPE)),
            default=None,
            label="Onderwijs type",
        ),
        Field(
            "sector",
            "list:string",
            length=5,  # 3 + 2 reserve
            requires=IS_NULL_OR(IS_IN_SET(EDUCATION_SECTOR, multiple=True)),
            default=None,
        ),
        Field(
            "education_level",  # alleen voor VO en VSO
            "list:string",
            requires=IS_NULL_OR(
                IS_IN_SET(
                    EDUCATION_LEVEL,
                    multiple=True,
                )
            ),
            label="Onderwijsniveau",
        ),
        Field(
            "so_cluster",  # alleen voor SO en VSO
            "integer",
            requires=IS_NULL_OR(IS_IN_SET(SO_CLUSTER)),
            label="Speciaal onderwijs cluster",
        ),
        Field("so_type", "string", label="Speciaal onderwijs type"),
        Field(
            "denomination",
            "string",
            # TODO: requires met mogelijkheid tot toevoegen van een nieuwe optie, vrmdlk via autocomplete
            label="Denominatie",
            requires=IS_NULL_OR(IS_IN_SET(DENOMINATION)),
        ),
        Field(
            "concept",
            "string",
            # TODO: requires met mogelijkheid tot toevoegen van een nieuwe optie, vrmdlk via autocomplete
        ),
        Field("student_count", "integer"),
        Field(
            "subjects_with_specialised_teachers",
            "list:string",
            # todo: IS IN LIST van maken met autocomplete?
            label="Vakleerkrachten voor",
            comment="Voor welke vakken zijn er vakleerkrachten? 1 vak per regel.",
        ),
        Field(
            "board_gid",
            "string",
            # requires=IS_NULL_OR(BELONGS_TO(database, lambda db, v: db.board.gid == v)),
            requires=IS_NULL_OR(
                IS_IN_DB(
                    database, "board.gid", "%(name)s (%(city)s)", zero="Kies bestuur"
                )
            ),
            label="bestuur",
        ),
        Field(
            "last_saved_by", "string", default=None, writable=False
        ),  # autopopulation set in the web2py model
        # Field.Virtual("needle", lambda row: f'{row.name} {row.city}'),
    )

    database.organisation.latlon = Field.Virtual(
        lambda row: tuple(row.organisation.lonlat.strip("()").split(",")[::-1])
    )

    database.define_table(
        "organisation_effdted_now",
        organisation,
        migrate=False,
        rname="organisation_effdted_now",
    )

    database.define_table(
        "email_domain",
        Field(
            "platform", "string", default="SvS", writable=False, readable=False
        ),  # Debug, SvS, ION
        Field("gid", default=new_uuid, readable=False, writable=False),
        Field(
            "org_gid",
            requires=BELONGS_TO(
                database, lambda db, v: db.organisation_effdted_now.gid == v
            ),
            default="8fa76d9f-ec85-4018-8dd4-3352798aeafc",
            writable=False,
            readable=False,
        ),
        Field("domain"),
        Field("is_new_user_allowed", "boolean"),
    )

    database.define_table(
        "attachment",
        Field("platform", "string"),  # Debug, SvS, ION
        Field("gid", default=new_uuid),
        Field(
            "attachment",
            "upload",
            uploadfolder="/uploaded_attachments/",
            uploadseparate=True,
            autodelete=True,
        ),
        Field("filename"),
        Field("purpose"),
        Field("ts_uploaded", "datetime", default=now),
        Field("owner_gid"),  # gid of the user
        # not to do: support uploadfs  for CDN ...
        # that's for the microservices to fix
        Field("b2_uri", "string", default=None),
    )
    database.define_table(
        "stats_subject_views",
        Field("gid"),
        Field("tokens", "integer"),
        migrate=False,  # is a view
        primarykey=["gid"],
    )

    database.define_table(
        "stats_subject_thumbs",
        Field("gid"),
        Field("thumbs", "integer"),
        migrate=False,  # is a view
        primarykey=["gid"],
    )

    database.define_table(
        "stats_subject_favs",
        Field("gid"),
        Field("favs", "integer"),
        migrate=False,  # is a view
    )

    database.define_table(
        "mv__item_tags",
        Field("item_gid", "uuid"),
        Field("tag_gid", "uuid"),
        Field("item_name", "string"),
        Field("tag_name", "string"),
        migrate=False,  # is a TEMPORARY materialized view
        primarykey=[
            "item_gid"
        ],  # vereist, IS NIET DE SLEUTEL, maar wel nodig voor table joins.
    )

    database.define_table(
        "property_bag",
        Field("gid", default=new_uuid, length=36),
        Field("belongs_to_gid", "string", length=36),
        Field("properties", "json"),
    )

    database.define_table(
        "sticker",
        Field("tag_gid", length=36, required=True),
        Field("attachment_gid", length=36, required=True),
    )

    # the following MUST NOT be used directly
    # these are here for maintenance purposes, and quick
    # access using the workbenches
    database.define_table(
        "click__url",
        Field("short_code", length=20, unique=True),
        Field("long_url", "text"),
        rname="click.url",
    )

    database.define_table(
        "click__event",
        # use the shortcode as the unique reference
        # instead of a gid, because short code is already unique
        # and we don't use the ID field, which might be errorneous
        # when merging different databases...
        Field("short_code", length=20),
        # the hash is used here because we might not want to know
        # who clicked, but maybe we do. While not wanting to expose
        # the session token in each and every URL we hash a
        # 10 character code from the session_token, so it MIGHT be
        # 'reverse-lookuped' later on.
        Field("session_gid_hash", length=20),
        # We want to know from what article or page or whatever the
        # link was activated. That's this one.
        Field("from_item_gid", length=36),
        # when in datetime format.
        Field("ts", "datetime"),
        # created this is in click schema to seperate some logic
        rname="click.event",
    )

    database.define_table(
        "evidence",
        Field(
            "gid",
            "string",
            length=36,
            default=uuid.uuid4,
            comment="globaly unique id",
        ),
        Field(
            "session_gid",
            "string",
            length=36,
            comment="to what session does this evidence belongs, if any",
        ),
        Field(
            "source",
            "json",
            comment="whatever source can be given, arbitrary data, based on the signal definition.",
        ),
        Field(
            "sha1_digest",
            "string",
            length=40,
            comment="to deduplicate source, it is hashed with sha1 and the same id used",
        ),
    )

    database.define_table(
        "signal",
        Field("gid", "string", length=36, default=uuid.uuid4),
        Field("ts", "datetime", default=datetime.datetime.now),
        Field("name", "string", required=True),
        Field("source", "string", required=True, length=40),
        Field(
            "session_gid",
            "string",
            length=36,
            comment="to what session does this belong, if any",
        ),
        Field(
            "user_gid",
            "string",
            length=36,
            comment="to what user is this signal related, if any",
        ),
        # niet alles heeft een bewijs nodig
        Field(
            "evidence_id",
            "reference evidence",
        ),
        Field(
            "evidence_gid",
            "string",
            length=36,
        ),
        Field(
            "related",
            "string",
            length=36,
            comment="some string to relate different signals from same request",
        ),
    )
    database.define_table(
        "counts_per_minute",
        Field("gid", "string", length=36, default=uuid.uuid4),
        Field("ts", "datetime", default=datetime.datetime.now),
        Field("name", "string", required=True),
        # alles heeft een bewijs nodig, maar dat bewijs mag meermalen gebruikt
        # worden, dus counts_per_minute:evidence == N:1
        Field(
            "evidence_id",
            "reference evidence",
        ),
        Field(
            "evidence_gid",
            "string",
            length=36,
        ),
        Field("count", "integer"),
    )

    database.define_table(
        "organisation_changes_source",
        Field(
            "gid", "string", length=35, default=new_uuid, unique=True, writable=False
        ),
        Field("display_name", "string", unique=True, requires=IS_UPPER()),
        Field(
            "prio",
            "integer",
            unique=True,
            comment="Prioriteit, hoger is belangrijker. ",
        ),
    )
    database.define_table(
        "organisation_changelog",
        Field("org_gid", "string", comment="organisational gid"),
        Field("fieldname", "string", comment="fieldname of the table"),
        Field(
            "field_value",
            "json",
            comment="json representation of the value, array with one element",
        ),
        Field(
            "mutation_type",
            "string",
            length=1,
            requires=IS_IN_SET(dict(c="Create", u="Update", d="Delete")),
        ),
        Field(
            "status",
            "string",
            requires=IS_IN_SET(
                "automatisch aangenomen, onbekend, over-ruled, handmatig aangenomen"
            ),
        ),
        Field(
            "source",
            "string",
            length=36,
            requires=IS_IN_DB(database.organisation_changes_source, "gid"),
        ),
        Field("source_detail", "text", comment="email/filename"),
    )

    database.define_table(
        "vw_item_applog",
        Field("signal_gid", "uuid"),
        Field("evidence_gid", "uuid"),
        Field("signal_session_gid", "uuid"),
        Field("evidence_session_gid", "uuid"),
        Field("signal_ts", "datetime"),
        Field("log_action", rname="action"),
        Field("source"),
        Field("origin_domain"),
        Field("item_gid", "uuid"),
        Field("by_eddie_email"),
        Field(
            "changes",
            "json",
            filter_out=lambda value: json.loads(value) if value else {},
        ),
        migrate=False,  # is a TEMPORARY materialized view
        primarykey=[
            "signal_gid",
            "evidence_gid",
        ],  # vereist, IS NIET DE SLEUTEL, maar wel nodig voor table joins.
        rname="vw__item_applog",  # <- toggle between vw and mv for fresh vs cached version
    )

    visibilities_by_value = {v.value: v for v in Visibility}
    database.define_table(
        "auto_tag",
        Field("needle", type="string", description="Search for"),
        Field(
            "visibilities",
            type="list:string",
            requires=IS_IN_SET(visibilities_by_value, multiple=True),
        ),
        Field("tag_gid", type="string"),
        Field("tagged_in_db", type="list:string"),
        Field("search_results", type="list:string"),
    )

    return database
