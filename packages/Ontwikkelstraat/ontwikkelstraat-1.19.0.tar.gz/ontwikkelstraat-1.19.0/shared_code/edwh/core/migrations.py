# coding=utf-8
import datetime
from typing import Union

import psycopg2
import psycopg2.errors
import pydal.objects
from edwh_migrate import migration
from pydal import DAL, Field


# BEWARE
# when writing new tasks, make sure:
#  * executesql() returns tuples, explicitly use as_dict or as_ordered_dict to have easy acces for results
#  * arguments and placeholders use the `where gid = %(gid)s` syntax, where gid should be a key in the `placeholders`
#    argument given to executesql
#  * MAKE SURE ALL DATABSE OBJECT REFERENCES USE SCHEMA NOTATION!!!
#    - public."user"
#    - public.item
#    forget and fail...
#  * use pycharms remote debugging to ease up when things go wrong.
#


@migration
def feature_educationwarehouse_email_domain(db):
    import uuid

    db.executesql(
        """
    INSERT INTO "public"."email_domain" ("id", "platform", "gid", "org_gid", "domain", "is_new_user_allowed") VALUES (DEFAULT, 'SvS', '{}', '9dbbc253-2de4-4b25-88e9-452bffa9b9e9', 'educationwarehouse.nl', 'T')
    """.format(
            uuid.uuid4()
        )
    )
    return True


@migration
def property_bag_table_creation(db):
    db.executesql(
        """
    CREATE TABLE public.property_bag
    (
        id serial PRIMARY KEY NOT NULL,
        gid char(36) NOT NULL,
        belongs_to_gid char(36) NOT NULL,
        properties text
    );
    CREATE UNIQUE INDEX property_bag_id_uindex ON public.property_bag (id);
    CREATE UNIQUE INDEX property_bag_gid_uindex ON public.property_bag (gid);    
    """
    )
    return True


@migration
def api_activity_creation(db):
    db.executesql(
        """
    create table api_activity
    (
        gid    uuid   not null
            constraint api_activity_pk
                primary key,
        input  json,
        output json,
        id     serial not null
    );

    comment on table api_activity is 'Input and output from the GraphQL API';

    alter table api_activity
        owner to graphql;

    create unique index api_activity_gid_uindex
        on api_activity (gid);

    """
    )
    return True


@migration
def sticker_creation(db):
    db.executesql(
        """
    CREATE TABLE public.sticker
    (
        id serial PRIMARY KEY NOT NULL,
        tag_gid char(36) NOT NULL,
        attachment_gid char(36) NOT NULL
    );
    CREATE UNIQUE INDEX sticker_id_uindex ON public.sticker (id);
    CREATE UNIQUE INDEX sticker_gids_uindex ON public.sticker (tag_gid,attachment_gid);    
    """
    )
    return True


@migration
def url_shortner_inital_db_objects(db):
    # requires GRANT CREATE ON DATABASE graphql TO ggraphql;
    db.executesql(
        """
    CREATE SCHEMA IF NOT EXISTS click;    
    create table click.url (
        id serial primary key not null,
        short_code char(20) not null unique,
        long_url varchar
    );

    create unique index click_url_id_uidex on click.url(id);
    create unique index click_url_short_code_uidex on click.url(short_code);

    create table click.event (
        id serial primary key not null,
        short_code char(20) not null,
        session_gid_hash char(20),
        from_item_gid char(36),
        ts timestamp
    );

    create unique index click_event_id_uidex on click.event(id);

    """
    )


@migration
def session_hash_add_and_populate_column(db: DAL):
    db.executesql(
        """
    alter table public.session
        add gid_hash char(20) unique;
        -- autogenerates unique index
    """
    )

    def populate():
        import uuid
        from hashlib import blake2b

        def hash_gid(gid: uuid.UUID) -> str:
            """One-way shortener for gids, primarily for session_gid exposure, for exmaple in url tracking"""
            # copied from paddo_helpers
            return blake2b(
                gid.bytes,
                digest_size=10,
            ).hexdigest()

        print("hashing a lot of rows probably, this can take a while...")
        for row in db.executesql(
            """
                  select id, session_token 
                  from session
                  where gid_hash is null 
                """,
            as_dict=True,
        ):
            db.executesql(
                """
            update session 
               set gid_hash = %(hash)s
             where id = %(id)s
            """,
                placeholders=dict(
                    id=row["id"], hash=hash_gid(uuid.UUID(row["session_token"]))
                ),
            )

    populate()
    return True


@migration
def click_tracker_stats_views_00(db: DAL):
    db.executesql(
        """
    create or replace view stats_follow_link_activity_detail as
    select  e.ts as timestamp, u.name as username, u.email, i.name as item_name , url.long_url as followed_url, 'https://delen.meteddie.nl/item/'||i.gid as item_url, i.gid as item_gid, u.gid as user_gid
      from session s inner join click.event e on gid_hash = session_gid_hash
      left outer join "user" u on s.user_gid = u.gid
      inner join item i on i.gid = e.from_item_gid
      inner join click.url url on url.short_code = e.short_code
    ;"""
    )
    db.executesql(
        """
    create or replace view stats_follow_link_date_domain_count as
    select date(event_root.ts) as date, array_to_string(regexp_matches(long_url, '://([^/]*)'),'')  as domain, count(*) as number_of_clicks
      from click.event event_root
      inner join click.url url on url.short_code = event_root.short_code
      group by date(event_root.ts), array_to_string(regexp_matches(long_url, '://([^/]*)'),'')
    order by date(event_root.ts) desc
    """
    )
    return True


@migration
def add_first_name_last_name_to_user_table(db: DAL):
    db.executesql(
        """
        alter table "user"
            add firstname varchar(128) default null;

        alter table "user"
            add lastname varchar(128) default null;
    """
    )
    db.commit()
    return True


@migration
def add_user_provided_organisation_role_and_location_to_user(db: DAL):
    db.executesql(
        """
        alter table "user"
            add user_provided_organisation varchar(256) default null;

        alter table "user"
            add user_provided_primary_organisational_role varchar(128) default null;

        alter table "user"
            add user_provided_organisation_location varchar(128) default null;
    """
    )
    db.commit()
    return True


@migration(
    requires=[
        add_user_provided_organisation_role_and_location_to_user,
        add_first_name_last_name_to_user_table,
    ]
)
def provision_user_provided_org_details_and_firstname_and_lastname_from_the_user_propertybag(
    db: DAL,
):
    updated = 0
    print("doe dan iets!")
    # db = pydal.DAL("postgres://postgres@localhost:5432/backend")
    users = db.executesql(
        """select gid, property_bag
                           , property_bag::json -> 'schoolName' as schoolname
                           , property_bag::json -> 'city' as city
                           , property_bag::json -> 'title' as title
                    from public."user"
                    where property_bag is not  null
        """,
        as_ordered_dict=True,
    )
    print(users)
    for row in users:
        print(row)
        # unpack the row tuple
        print("updating user record", row["gid"])
        db.executesql(
            'update "user" set user_provided_organisation = %(schoolname)s where gid = %(gid)s',
            placeholders=row,
        )
        db.executesql(
            'update "user" set user_provided_organisation_location = %(city)s where gid = %(gid)s',
            placeholders=row,
        )
        db.executesql(
            'update "user" set  user_provided_primary_organisational_role = %(title)s where gid = %(gid)s',
            placeholders=row,
        )
        updated += 1
    db.commit()
    print(f"committed {updated} user records to the database")
    return True


@migration
def provision_item_date_started_and_date_ended_and_video_urls_from_propertybag_20210714(
    db: DAL,
):
    db.executesql(
        """
        alter table item
        add since_when date default null ;

        alter table item
        add upto_when date default null;

        alter table item
        add video_urls text default null;
        """
    )
    updated = 0
    # db = pydal.DAL("postgres://postgres@localhost:5432/backend")
    bags = db.executesql(
        """select property_bag.gid as pb_gid 
                , item.gid as item_gid
                , properties::json -> 'fieldDateStart' as date_start
                , properties::json -> 'fieldDateEnd' as date_end
                , properties::json -> 'fieldVideos' as videos
            from public.property_bag 
                 inner join public.item on (public.item.gid = public.property_bag.belongs_to_gid  and public.item.author is not null and public.item.platform = 'SvS')
            where property_bag is not null
        """,
        as_ordered_dict=True,
    )

    def to_date(s):
        try:
            return datetime.datetime.strptime(s, "%d-%m-%Y").date()
        except ValueError:
            try:
                return datetime.datetime.strptime(s, "%Y-%m-%d").date()
            except ValueError:
                try:
                    datetime.datetime.strptime(s, "%d-%m-%y").date()
                except ValueError:
                    return None

    for row in bags:
        # unpack the row tuple
        print("updating item record", row["item_gid"])
        if row["date_start"]:
            db.executesql(
                "update item set since_when = %(since_when)s where gid = %(item_gid)s",
                placeholders=dict(
                    item_gid=row["item_gid"], since_when=to_date(row["date_start"])
                ),
            )
        if row["date_end"]:
            db.executesql(
                "update item set upto_when = %(upto_when)s where gid = %(item_gid)s",
                placeholders=dict(
                    item_gid=row["item_gid"],
                    upto_when=to_date(row["date_end"]),
                ),
            )
        videos = row["videos"]
        if videos:
            print(row["item_gid"], videos)
            # kan gekke dingen bevatten:
            # 05b7e5cf-1e4a-43a5-998c-4637afa259aa [{'value': 'https://youtu.be/m34Q-CGqyZM', 'id': 'c79c5866-7a30-4edd-8060-d911e95e94e2'}]
            for idx, video in enumerate(videos):
                if isinstance(video, dict):
                    videos[idx] = video["value"]
            db.executesql(
                "update item set video_urls = %(videos)s where gid = %(item_gid)s",
                placeholders=dict(
                    item_gid=row["item_gid"],
                    videos="|" + "|".join(videos) + "|",
                ),
            )
        updated += 1
    db.commit()
    print(f"committed {updated} item records to the database")
    return True


@migration
def set_password_for_automatischetest_user_and_testing_for_jesper(db: DAL):
    db.executesql(
        """
    UPDATE public."user" SET password = '$2a$10$UFkhEG5ZjcRS57cXAmg9CO8dpFT4nEWMKjXjh5KFF0GYHRElz6jOy' WHERE email = 'jesper.b@educationwarehouse.nl'
    """
    )
    db.executesql(
        """
    UPDATE public."user" SET password = '$2a$10$UFkhEG5ZjcRS57cXAmg9COb/4tnAAR25M7Nmn5vFun8M3nJnmPssy' WHERE email = 'automatischetest@roc.nl'
    """
    )
    db.commit()
    return True


# noinspection Assert
@migration
def migrate_user_generated_tags_from_item_propertybag_to_real_tags(db: DAL):
    # setup the database schema, assume these tables exist:
    import json
    import uuid

    import slugify

    db.define_table(
        "tag",
        Field("platform", "string"),  # Debug, SvS, ION
        Field("gid", default=uuid.uuid4),
        Field("name"),
        Field("slug"),
        Field("parents", "list:string"),  # which is the parent tag, None is root
        Field("children", "list:string"),  # direct descendants, in order
        Field("description"),
        Field("meta_tags", "list:string"),
    )
    db.define_table(
        "property_bag",
        Field("gid", default=uuid.uuid4, length=36),
        Field("belongs_to_gid", "string", length=36),
        Field("properties", "json"),
    )
    # noinspection HttpUrlsUsage
    db.define_table(
        "item",
        Field("platform", "string"),  # Debug, SvS, ION
        Field("author"),  # user_gid
        Field("name"),
        Field("gid", default=uuid.uuid4),
        Field("thumbnail", default="http://lorempixel.com/400/200/"),
        Field(
            "short_description",
        ),
        Field("ts_changed", "datetime"),
        Field("tags", "list:string"),  # list of tags/tagids
        Field("slug"),
        Field("alternatives", "list:string"),  # list of item gids
        Field("backgrounds", "list:string"),  # list of attachment gids
        Field("attachments", "list:string"),  # list of attachment gids
    )

    class Tag:
        all_tag_rows = db(db.tag).select()
        tag_gid_map = {row.gid: row for row in all_tag_rows}

        def __init__(self, tag_identifier: Union[str, int, pydal.objects.Row]):
            # row could be a string
            if type(tag_identifier) is str:
                if _row := self.tag_gid_map.get(tag_identifier):
                    tag_identifier = _row
                else:
                    rows = self.all_tag_rows.find(lambda r: r.name == tag_identifier)
                    if len(rows) != 1:
                        rows = self.all_tag_rows.find(
                            lambda r: r.slug == slugify.slugify(tag_identifier)
                        )
                    if len(rows) != 1:
                        raise KeyError(
                            f"Unknown tag gid,name or slug: {tag_identifier}"
                        )
                    tag_identifier = rows[0]
            if type(tag_identifier) is int:
                # use integers as reference to id field in db.tag
                tag_identifier = db.tag[tag_identifier]
            # assume tag is a row
            self.row = tag_identifier
            self.name = tag_identifier.name
            self.gid = tag_identifier.gid

        @classmethod
        def new(
            cls, name, description, slug=None, parents=(), children=(), meta_tags=()
        ):
            # parse slug, raise error if not unique
            slug = slug or slugify.slugify(name)
            assert not db.tag(slug=slug), "Slug should be unique"
            # come up with a new guid
            new_gid = uuid.uuid4()
            # insert new value in database
            _id = db.tag.insert(
                platform=None,  # not in use atm
                gid=new_gid,
                name=name,
                slug=slug,
                parents=[_.gid for _ in parents],
                description=description,
                meta_tags=[_.gid for _ in meta_tags],
                children=[_.gid for _ in children],
            )
            # read the row, create a new Tag
            row = db.tag[_id]
            tag = Tag(row)
            # save the record in cls.tag_gid_map
            cls.tag_gid_map[new_gid] = tag
            # edit all parents to register this new child
            for parent_gid in [_.gid for _ in parents]:
                Tag(parent_gid).add_child(tag)
            # update the new all_tag_rows
            cls.all_tag_rows = db(db.tag).select()
            # return the Tag
            return tag

        def __repr__(self):
            return f"<Tag {self.name} {self.row}>"

        def parents(self):
            return [Tag(_) for _ in self.row.parents]

        def children(self):
            return [Tag(_) for _ in self.row.children] if self.row.children else []

        def children_by_parental_reference(self):
            return [
                Tag(_) for _ in self.all_tag_rows.find(lambda _: self.gid in _.parents)
            ]

        def metatags(self):
            return [Tag(_) for _ in self.row.meta_tags]

        def tagged_with(self):
            return [
                Tag(_)
                for _ in self.all_tag_rows.find(lambda _: self.gid in _.meta_tags)
            ]

        def add_metatag(self, meta_tag):
            # meta_tag moet een Tag instance zijn
            if meta_tag.gid in self.row.meta_tags:
                return False
            meta_tags = self.row.meta_tags + [meta_tag.gid]
            self.row.update_record(meta_tags=meta_tags)
            return True

        def add_child(self, child):
            # meta_tag moet een Tag instance zijn
            if self.row.children and (child.gid in self.row.children):
                return False
            children = (self.row.children or []) + [child.gid]
            self.row.update_record(children=children)
            child_parents = child.row.parents
            if self.gid not in child_parents:
                child.row.update_record(parents=child_parents + [self.gid])
            return True

        def walk(
            self,
            func=lambda tag, parent, depth: tag,
            direction="children",
            parent=None,
            depth=0,
        ):
            bunch = getattr(self, direction)()
            if func(self, parent, depth):
                for tag in bunch:
                    tag.walk(func, direction, parent=self, depth=depth + 1)

    # noinspection PyPep8Naming
    TItem = Tag("fc8a7d36-e23e-4aba-8ee9-f5269ecc8dfc")
    # noinspection PyPep8Naming
    TUser_generated_tags = Tag("38f7b956-6315-4676-8076-8aeef258563e")

    print("items and bags:")
    for row in db(
        (db.item.gid == db.property_bag.belongs_to_gid)
        & (db.item.author is not None)
        & (db.item.platform.belongs(["SvS"]))
    ).select():
        bag = json.loads(row.property_bag.properties)
        tags_str = bag.get("fieldUsersubmittedTags", "")
        tags = [t.strip() for t in tags_str.split(";") if t.strip()]
        print(row.item.gid, tags)
        item_tags = row.item.tags
        update_row = False
        for tag_name in tags:
            # kijk of de tag bestaat, gebruikt de slugify functie die al in Tag() is ingebouwd.
            try:
                tag_object = Tag(tag_name)
            except KeyError:
                # bestaat nog niet. Dan aanmaken
                print("Adding new tag: ", tag_name)
                tag_object = Tag.new(
                    tag_name,
                    "Imported from the propertybag (june 2021)",
                    meta_tags=[TItem, TUser_generated_tags],
                )
            # print(tag_object)
            # kijk of de tag gekoppeld is aan het item
            if tag_object.gid not in row.item.tags:
                item_tags.append(tag_object.gid)
                update_row = True
            # zo niet: koppel
            # zo wel: ignore
        # sla de nieuwe tags op aan de item
        if update_row:
            print(f"updating item {row.item.gid} with new tags")
            db(db.item.gid == row.item.gid).update(tags=item_tags)
        # verwijder de tags uit de propertybag om te voorkomen dat we deze exercitie nogmaals moeten doen.
        if "fieldUsersubmittedTags" in bag:
            print(
                "removing fieldUsersubmittedTags from propertybag", row.property_bag.gid
            )
            del bag["fieldUsersubmittedTags"]
            db(db.property_bag.gid == row.property_bag.gid).update(properties=bag)

    db.commit()
    return True


# OOPS. de backup bevat de signal installatie melding nog niet, dus om dat te voorkomen hier een stomme comment...
# FIXME: bijwerken ewh_implemented_features tabel voor signal_schema_creation en een nieuwe backup maken
# @migration
# def signal_schema_creation(db: DAL):
#     db.executesql(
#         """
#     create schema signal;
#
#     comment on schema signal is 'Alles over signalen';
#
#     alter schema signal owner to graphql;
#
#     """
#     )
#     return True


@migration(requires=migrate_user_generated_tags_from_item_propertybag_to_real_tags)
def remove_items_without_content_bugging_our_queries(db: DAL):
    print(
        db.executesql(
            """
            update public.item set author = null 
             where public.item.gid in (
                select i.gid
                    -- i.name,
                    -- i.author,
                    -- i.platform,
                    -- i.short_description
                from public.item i
                where i.short_description is null
                  and i.platform = 'SvS'
                  and i.author is not null
            )   
            """
        )
    )
    return True


@migration
def add_org_columns_coc_street_number_city_lonlat_taggid(db: DAL):
    db.executesql(
        """
        alter table public.organisation
            add coc int default null;

        alter table public.organisation
            add street varchar(128) default null;

        alter table public.organisation
            add number varchar(12) default null;

        alter table public.organisation
            add city varchar(128) default null;

        alter table public.organisation
            add lonlat point default null;

        alter table public.organisation
            add tag_gid varchar(36) default null;
    """
    )
    db.commit()
    return True


@migration
def add_organisations_meta_tag_e5b80b90185142d9aebc87327e87ed09(db: DAL):
    if db.executesql(
        "select count(*) from public.tag where public.tag.gid = 'e5b80b90-1851-42d9-aebc-87327e87ed09'"
    )[0][0]:
        return True
    db.executesql(
        """
        INSERT INTO public.tag (platform, gid, name, slug, parents, description, meta_tags, children) 
        VALUES (
            null, 'e5b80b90-1851-42d9-aebc-87327e87ed09', 'Organisations', 'organisations', 
            '|19682a99-50a3-4fc0-bb67-e0f6eff5da55|', 'Organisaties zijn gekoppeld aan items via children tags van deze tag.', '|19682a99-50a3-4fc0-bb67-e0f6eff5da55|', '||'
        );
        """
    )
    db.commit()
    return True


@migration
def fix_user_generated_tag_parents_field_for_wrongly_imported_tags_2021_07_07(db: DAL):
    # er zijn al een paar user-generated-tags die wel al goed ingesteld staan, en er zijn er ook die gekoppeld
    # zijn met stickers via de parents. Dus alleen de parents='||' fixen.
    db.executesql(
        """
        update public.tag 
           set parents='|38f7b956-6315-4676-8076-8aeef258563e|' 
         where meta_tags like '%|38f7b956-6315-4676-8076-8aeef258563e|%' 
           and parents = '||' 
       """
    )
    db.commit()
    return True


@migration(
    requires=[
        set_password_for_automatischetest_user_and_testing_for_jesper,
        provision_item_date_started_and_date_ended_and_video_urls_from_propertybag_20210714,
    ]
)
def add_testable_item_record_for_automated_testing_2021_07_29(db: DAL):
    db.executesql(
        """
        insert into public.item (platform, author, name, gid, thumbnail, short_description, ts_changed, tags, slug, alternatives, backgrounds, attachments, since_when, upto_when, video_urls)
        values (
            'SvS', -- platform
            'a2f28371-72fe-4962-ab28-6c72624e3282', -- author : automatischetest@roc.nl
            'Migrate test item namenamename', --name
            '56f67e7a-24f6-4202-9f51-bbf9de6b8348', --gid
            '221f84f1-1926-4af3-b9e5-e57672693b01', --thumbnail ; bestaat al, is het educationwarehouse.svg logo van het stickers item van remco@roc.nl
            'zoekterm: descriptiondescriptiondescription leren ', --short_description "leren" wordt gebruikt in de tests
            '2021-07-29 14:51:15.910925'::timestamp, --ts_changed timestamp
            '|bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7|722a1d89-b585-495f-8895-9f12fc0d054a|146214d3-6091-4aff-bfdf-3f50d41d2e8a|cfebbbba-61ce-41de-b8a8-536e84143363|d624105b-34b8-4ef7-a4eb-dc75c80f8653|', --tags
            'migrate-test-item-slugslugslug', --slug
            null, --alternatives
            '|221f84f1-1926-4af3-b9e5-e57672693b01|', --backgrounds ; zelfde als thumbnail
            '|220b5555-b95a-4ffb-ae21-d1bc46434702|', --attachments ; komt van stickers item, is een regenboog plaatje
            '2021-03-17', --since_when date
            '2022-05-13', --upto_when date
            '|https://www.youtube.com/watch?v=rfscVS0vtbw|' --video_urls
        )
    """
    )
    db.commit()
    return True


@migration
def add_statistics_tables_signal_evidence_and_counts_per_minute_2021_12_03(db: DAL):
    generate_signal = """
    create table public.signal
    (
        id           serial
            primary key,
        gid          varchar(36),
        ts           timestamp,
        name         varchar(512),
        source       varchar(40),
        session_gid  varchar(36),
        user_gid     varchar(36),
        evidence_id  integer
            references public.evidence
                on delete cascade,
        evidence_gid varchar(36),
        related      varchar(36)
    );

    alter table public.signal
        owner to postgres;
    """
    generate_evidence = """
    create table public.evidence
    (
        id          serial
            primary key,
        gid         varchar(36),
        session_gid varchar(36),
        source      json,
        sha1_digest varchar(40)
    );

    alter table public.evidence
        owner to postgres;
    """
    generate_counts_per_minute = """
    create table public.counts_per_minute
    (
        id           serial
            primary key,
        gid          varchar(36),
        ts           timestamp,
        name         varchar(512),
        evidence_id  integer
            references public.evidence
                on delete cascade,
        evidence_gid varchar(36),
        count        integer
    );

    alter table public.counts_per_minute
        owner to postgres;
    """
    for script in (generate_evidence, generate_signal, generate_counts_per_minute):
        db.executesql(script)
        db.commit()
    return True


@migration(
    requires=[add_statistics_tables_signal_evidence_and_counts_per_minute_2021_12_03]
)
def alter_statistics_columns_to_uuid_type_2021_12_21(db: DAL):
    db.executesql(
        """
        alter table evidence alter column session_gid type uuid using session_gid::uuid;
        alter table evidence alter column gid type uuid using gid::uuid;
        alter table signal alter column gid type uuid using gid::uuid;
        alter table signal alter column session_gid type uuid using session_gid::uuid;
        alter table signal alter column user_gid type uuid using user_gid::uuid;
        alter table signal alter column evidence_gid type uuid using evidence_gid::uuid;
        alter table signal alter column related type uuid using related::uuid;
        """
    )
    db.commit()
    return True


@migration
def add_tag_materialized_views_and_indexes_2022_03_09(db: DAL):
    # refresh with "REFRESH MATERIALIZED VIEW mv__item_tags;"
    # zie https://taiga.edwh.nl/project/remco-ewcore/us/213?milestone=57
    db.executesql(
        """
        drop index if exists idx_item__gid__id;
        drop index if exists idx_tag__gid__id;
        drop index if exists idx_item_tags;
        create unique index idx_item__gid__id on public.item (gid) include (id); 
        create unique index idx_tag__gid__id on public.tag (gid) include (id); 
        create unique index idx_item_tags on public.item (gid) include (tags); 
        """
    )
    db.executesql(
        r"""
        drop materialized view if exists mv__item_tags; 
        create materialized view mv__item_tags as 
        with item_tags as (
            -- produces an array of tag gids per item.gid. `array_remove` trimms the empty values due to the split
            -- and the split_to_array is similar to python's `'|a|b|c|'.split('|')` 
            select item.gid, array_remove(regexp_split_to_array(item.tags, E'\\|'), '') as tags
              from item
        ), used_items as (
            -- just a list of item gids 
            select item.gid, item.name 
              from item inner join "user" on item.author = "user".gid and "user".email not like '%@roc.nl'
        )
        select item_tags.gid::uuid as item_gid, tag.gid::uuid as tag_gid, used_items.name as item_name, tag.name as tag_name     
          from item_tags 
               inner join tag on tag.gid = ANY(item_tags.tags)
               inner join used_items on item_tags.gid = used_items.gid
        """
    )
    db.executesql(
        r"""
        drop materialized view if exists mv__tag_arrays; 
        create materialized view mv__tag_arrays as 
        select 
            tag.id, 
            tag.gid::uuid, 
            tag.name as search,
            array_remove(regexp_split_to_array(tag.children, E'\\|'), '')::uuid[] as children,
            array_remove(regexp_split_to_array(tag.parents, E'\\|'), '')::uuid[] as parents,
            array_remove(regexp_split_to_array(tag.meta_tags, E'\\|'), '')::uuid[] as meta_tags
        from tag 
        """
    )
    db.commit()
    return True


@migration
def add_mv__item_tags__indexes_2022_03_14(db: DAL):
    # maakt een index op item_gid waarmee tags te vinden zijn
    # en een index op tag_gid waarmee item_gid te vinden is.
    db.executesql(
        """
        create index if not exists idx_mv__item_tags__item_gid on public.mv__item_tags (item_gid) include (tag_gid);
        create index if not exists idx_mv__item_tags__tag_gid on public.mv__item_tags (tag_gid) include (item_gid);
        """
    )
    db.commit()
    return True


@migration
def add_tracking_colums_to_organisations_2022_03_31(db: DAL):
    # https://taiga.edwh.nl/project/remco-ewcore/issue/276
    # Bo heeft voor het verwerken van de organisaties gegevens 2 extra velden nodig
    #     validated_ts: gecontroleerd op
    #     validated_by: gecontroleer door
    #
    # Zo kan ze haar werkgegevens bijhouden over de organisaties, en kan ze bijhouden wat ze nog moet doen en wat op een
    # later moment weer opnieuw opgeschoond moet worden. Vergelijkbaar wat Manon ook graag wil bij de tags.
    # Aangezien dit vereist is voor de Oekraine pagina, moet dit met hoge spoed toegevoegd worden.

    db.executesql(
        """
        alter table organisation
            add validated_ts timestamp;

        alter table organisation
            add validated_by varchar(40);
        """
    )
    db.commit()
    return True


@migration
def add_country_column_to_organisation_and_remove_stale_views_and_convert_varchar_columns_to_text_2022_04_01(
    db: DAL,
):
    # ivm Oekraine moet er snel een land bij de organisaties

    # verwijderde views, zie [Deels verwijderde views](https://joplin.edwh.nl/shares/WVpfstCQirqQFl343c17JsG0oYYpMvqM)
    db.executesql(
        """
    drop view all_guids_with_source;
    drop view all_guids;
    drop view livegang_tags; 
    drop view livegang_tag_gebruik; 
    drop view livegang_actieve_items;
    drop view api_activity_with_user_context_vw; 
    drop view api_activity_details_vw; 
    """
    )
    db.executesql(
        """
        alter table organisation
            add country_code varchar;
        alter table organisation
        alter column platform type text using platform::text;

        alter table organisation
            alter column gid type text using gid::text;

        alter table organisation
            alter column name type text using name::text;

        alter table organisation
            alter column street type text using street::text;

        alter table organisation
            alter column street drop default;

        alter table organisation
            alter column number type text using number::text;

        alter table organisation
            alter column number drop default;

        alter table organisation
            alter column city type text using city::text;

        alter table organisation
            alter column city drop default;

        alter table organisation
            alter column tag_gid type text using tag_gid::text;

        alter table organisation
            alter column tag_gid drop default;

        alter table organisation
            alter column validated_by type text using validated_by::text;

        """
    )
    db.commit()
    return True


@migration
def set_organisations_to_dutch_2022_04_01(db: DAL):
    # alles in de database is in eerste instantie nederlands.
    db.executesql(
        """
        update organisation set country_code = 'NLD';
        """
    )
    db.commit()
    return True


@migration
def add_roepnaam_to_organisation_2022_04_01(db: DAL):
    # alles in de database is in eerste instantie nederlands.
    db.executesql(
        """
        alter table organisation
            add aka text;
        """
    )
    db.commit()
    return True


@migration
def add_website_email_sodkurl_aantekeningen_to_organisation_2022_04_08(db: DAL):
    # https://taiga.edwh.nl/project/remco-ewcore/issue/279
    db.executesql(
        """
        alter table organisation
            add website text;

        alter table organisation
            add email text;

        alter table organisation
            add scholen_op_de_kaart_url text;

        alter table organisation
            add aantekeningen text;

        """
    )
    db.commit()
    return True


@migration
def add_pgcache_cache_tables_2022_11_07(db: DAL):
    db.executesql(
        """
        create table public.cache
        (
            id    serial PRIMARY KEY NOT NULL,
            gid   text               not null,
            value bytea
        );
        
        comment on table public.cache is 'pgcache related';
        
        alter table public.cache
            owner to postgres;
        
        create unique index unique_cache_gid
            on public.cache (gid);
        
        create table public.deps
        (
            id         serial PRIMARY KEY NOT NULL,
            cache_id   integer,
                -- constraint fk_deps_cache_id
                --    references public.cache (id),
            depends_on integer
                -- constraint fk_deps_depends_on 
                --     references public.cache (id)  
        );
        
        comment on table public.deps is 'pgcache requirement';
        
        alter table public.deps
            owner to postgres;
        
        create index deps_cacheid_with_dependencies
            on public.deps (cache_id desc) include (depends_on);
        
        create index deps_dependencies_with_cacheid
            on public.deps (depends_on desc) include (cache_id);
        """
    )

    # create the trigger functions
    db.executesql(
        """
    create or replace function derivatives(param_cache_id integer) returns TABLE(cache_id integer) as $$
        with recursive composite as (
          select deps.id, deps.cache_id, deps.depends_on
            from deps
           where deps.depends_on = param_cache_id
          UNION
          select deps.id, deps.cache_id, deps.depends_on
            from deps
                  inner join composite on deps.depends_on = composite.cache_id
        )
        select composite.depends_on
        from composite
        union
        select composite.cache_id
        from composite;
    $$ language  sql
    """
    )

    def cache_hook_table_with_gid(db, table_rname):
        # db.executesql('listen cacheinvalidation')
        # db.rollback()
        db.executesql(
            f"""
        CREATE OR REPLACE FUNCTION cache_{table_rname}_update() RETURNS trigger AS $cache_{table_rname}_update$
            declare
                cache_id int;
            BEGIN
                select id into cache_id from cache where cache.gid = NEW.gid;
                delete from cache using derivatives(cache_id) dep where cache.id = dep.cache_id;
                -- perform pg_notify('cacheinvalidation', NEW.gid::text);
                RETURN NEW;
            END;
        $cache_{table_rname}_update$ LANGUAGE plpgsql;
        """
        )
        db.executesql(
            f"""
        create or replace TRIGGER cache_{table_rname}_update_trigger AFTER UPDATE ON item
            FOR EACH ROW EXECUTE FUNCTION cache_{table_rname}_update();
        """
        )
        db.commit()

    cache_hook_table_with_gid(db, "item")
    cache_hook_table_with_gid(db, "user")
    cache_hook_table_with_gid(db, "comment")
    cache_hook_table_with_gid(db, "attachment")
    cache_hook_table_with_gid(db, "mark")
    cache_hook_table_with_gid(db, "organisation")
    cache_hook_table_with_gid(db, "tag")
    cache_hook_table_with_gid(db, "user_notification")
    db.commit()

    return True


@migration
def add_timestamp_to_pgcache_2022_11_11(db: DAL):
    db.executesql(
        """
    alter table cache
    add ts timestamp default current_timestamp;

    """
    )
    return True


@migration
def add_reads_and_last_read_to_pgcache_2022_11_11(db: DAL):
    db.executesql(
        """
    alter table cache
        add lr timestamp default current_timestamp;
    
    alter table cache
        add reads integer default 0;
    """
    )
    return True


@migration
def add_onderbouwing_to_item_2022_11_15_00(db: DAL):
    db.executesql(
        """
    alter table item
        add onderbouwing char(6) default 'EKeE';
    
    alter table item
        add onderbouwing_bronnen text;
    
    alter table item
        add onderbouwing_links text;

    """
    )
    return True


@migration
def split_name_to_firstname_lastname_2022_11_17_00(db: DAL):
    for user_rec in db.executesql('select * from "user"', as_dict=True):
        if user_rec["firstname"]:
            # ignore already propogated names
            continue
        # split on first '  ' if available, assume firstname only otherwise
        firstname, lastname = (
            user_rec["name"].split(" ", 1)
            if " " in user_rec["name"]
            else (user_rec["name"], "")
        )
        db.executesql(
            """
        update "user"
        set firstname = %s, lastname=%s
        where gid=%s;
        """,
            placeholders=(firstname, lastname, user_rec["gid"]),
        )
    db.commit()
    return True


@migration
def add_ttl_to_cache_2022_11_18_00(db: DAL):
    db.executesql(
        """
    alter table public.cache
        add ttl integer;
    """
    )
    db.commit()
    return True


@migration
def change_onderbouwing_datatype_2022_11_28_00(db: DAL):
    db.executesql(
        """
    alter table item
        alter column onderbouwing type varchar(6) using onderbouwing::varchar(6);
    """
    )
    db.commit()
    return True


@migration
def add_license_to_item_2022_12_01_00(db: DAL):
    db.executesql(
        """
    alter table item
        add license varchar(15);
    """
    )
    db.commit()
    return True


@migration
def add_license_to_item_2022_12_01_01(db: DAL):
    db.executesql(
        """
    update item set license = 'copyright';
    """
    )
    db.commit()
    return True


@migration
def add_applog_sha1_index_2022_12_21_01(db: DAL):
    db.executesql(
        """
    create index evidence_sha1_digest_index
    on signal.evidence (sha1_digest asc);
    """
    )
    db.commit()
    return True


@migration
def add_tag_columns_2023_01_12_01(db: DAL):
    db.executesql(
        """
    alter table public.tag
        add akas varchar default null;
    
    comment on column public.tag.akas is 'Alternatieve benamingen voor de name';
    
    alter table public.tag
        add search_hints text;
    
    comment on column public.tag.search_hints is 'extra zoekwoorden';
    
    alter table public.tag
        add definition_source text default null;
    
    comment on column public.tag.definition_source is 'url of tekst met de definitie, of toelichting op de definitie';
    
    alter table public.tag
        add restrictions text default null;
    
    comment on column public.tag.restrictions is 'toelichting wanneer wel of niet deze tag gebruikt mag worden';
    """
    )
    db.commit()
    return True


@migration
def add_tag_comment_2023_01_12_02(db):
    db.executesql(
        """
    CREATE TABLE public.tag_comment
    (
        id serial PRIMARY KEY NOT NULL,
        gid char(36) NOT NULL,
        tag_gid char(36) not null, 
        user_email text NOT NULL,
        comment text
    );
    CREATE UNIQUE INDEX tag_comment_id_uindex ON public.tag_comment (id);
    CREATE UNIQUE INDEX tag_comment_gid_uindex ON public.tag_comment (gid);    
    CREATE INDEX tag_comment_tag_gid_uindex ON public.tag_comment (tag_gid);    
    """
    )
    db.commit()
    return True


@migration
def add_extra_contactgegevens_20230207_001(db):
    db.executesql(
        """
    alter table public.item 
        add extra_contactgegevens text;
    """
    )
    db.commit()
    return True


@migration
def add_board_table_2023_01_17_01(db):
    # vereist voor #873
    db.executesql(
        """
    create table public.board (
        id serial primary key not null, 
        gid char(36) NOT NULL,
        "name" varchar not null, 
        street varchar not null,
        number varchar not null, 
        postalcode varchar, 
        city varchar not null, 
        website varchar
    )
    """
    )
    db.commit()
    return True


@migration
def alter_organisation_table_2023_01_17_01(db):
    # vereist voor #873
    db.executesql(
        """
    comment on column public.organisation.id is 'pydal requirement';
    
    comment on column public.organisation.platform is 'deprecated';
    
    comment on column public.organisation.gid is 'Unieke gid, als string representatie';
    
    comment on column public.organisation.name is 'Formele naam (doopnaam)';
    
    comment on column public.organisation.coc is 'KVK inschrijvingsnummer';
    
    comment on column public.organisation.street is 'Straat';
    
    comment on column public.organisation.number is 'Huisnummer';
    
    comment on column public.organisation.city is 'Plaats';
    
    comment on column public.organisation.lonlat is 'GEO Locatie';
    
    comment on column public.organisation.tag_gid is 'Het GID van de Tag bijbehorende deze organisatie';
    
    comment on column public.organisation.validated_ts is 'timestamp laatst gevalideerd';
    
    comment on column public.organisation.validated_by is 'email adres door wie gevalideerd';
    
    comment on column public.organisation.country_code is 'ISO3166 alpha2  code';
    
    alter table public.organisation
        alter column country_code type varchar(2) using country_code::varchar(2);
    
    alter table public.organisation
        alter column country_code set default 'NL';
    
    comment on column public.organisation.aka is 'Also Known As, zoals de school bekend staat. ';
    
    comment on column public.organisation.website is 'Hoofdpagina schoolwebsite';
    
    comment on column public.organisation.email is 'administratieve email adres';
    
    comment on column public.organisation.scholen_op_de_kaart_url is 'URL voor scholen op de kaart';
    
    comment on column public.organisation.aantekeningen is 'Aantekeningen gedurende het werkproces, moet naar commentaren';
    
    alter table public.organisation
        add brin varchar(4);
    
    comment on column public.organisation.brin is 'BRIN (van DUO)';
    
    alter table public.organisation
        add vestigingscode varchar(6);
    
    comment on column public.organisation.vestigingscode is 'BRIN instellingscode of vestigingscode';
    
    alter table public.organisation
        add coc_location integer;
    
    comment on column public.organisation.coc_location is 'KVK vestigingsnummer';
    
    alter table public.organisation
        add phone varchar(15);
    
    comment on column public.organisation.phone is 'algemeen telefoonnummer';
    
    alter table public.organisation
        add postalcode varchar(20);
    
    comment on column public.organisation.postalcode is 'postcode';
    
    alter table public.organisation
        add correspondence_city text;
    
    comment on column public.organisation.correspondence_city is 'correspondentie adres';
    
    alter table public.organisation
        add correspondence_street text;
    
    comment on column public.organisation.correspondence_street is 'correspondentie straat';
    
    alter table public.organisation
        add correspondence_number text;
    
    comment on column public.organisation.correspondence_number is 'correspodentie huisnummer';
    
    alter table public.organisation
        add correspondence_postalcode varchar(20);
    
    alter table public.organisation
        add correspondence_country varchar(2);
 
    comment on column public.organisation.correspondence_postalcode is 'correspondentie postcode';
    
    comment on column public.organisation.country_code is 'ISO3166 country alpha2 code';

    alter table public.organisation
        alter column country_code type varchar(2) using country_code::varchar(2);
    
    alter table public.organisation
        alter column country_code set default 'NL';
    
    alter table public.organisation
        add ceo_name varchar;
    
    comment on column public.organisation.ceo_name is 'directeur naam';
    
    alter table public.organisation
        add ceo_email varchar;
    
    comment on column public.organisation.ceo_email is 'directeur email adres';
    
    alter table public.organisation
        add ceo_phone varchar(15);
    
    comment on column public.organisation.ceo_phone is 'directeur telefoonnummer';
    
    alter table public.organisation
        add quality_assurance_plan varchar;
    
    comment on column public.organisation.quality_assurance_plan is 'URL schoolplan';
      
    comment on column public.organisation.aantekeningen is 'werk aantekeningen';

    alter table public.organisation
        add education_type char(1);
    
    comment on column public.organisation.education_type is 'regulier/speciaal';
    
    alter table public.organisation
        add sector varchar(5);
    
    comment on column public.organisation.sector is 'po/vo/so/vso/mbo/hbo/wo, lower case code';
    
    alter table public.organisation
        add education_level varchar;
    
    comment on column public.organisation.education_level is 'po/lwoo/bb/bk/gl/tl/havo/vwo/gym lower case code';
    
    alter table public.organisation
        add so_cluster integer;
    
    comment on column public.organisation.so_cluster is 'speciaal onderwijscluster';
    
    alter table public.organisation
        add so_type text;
    
    comment on column public.organisation.so_type is 'een speciaal onderwijs type';
    
    alter table public.organisation
        add denomination text;
    
    comment on column public.organisation.denomination is 'denominatie';
    
    alter table public.organisation
        add concept text;
    
    comment on column public.organisation.concept is 'onderwijs visie';
    
    alter table public.organisation
        add subjects_with_specialised_teachers text;
    
    comment on column public.organisation.subjects_with_specialised_teachers is 'pydal lijst van vakken met vakdocenten';
    
    alter table public.organisation
        add board_gid varchar;
    
    comment on column public.organisation.board_gid is 'gid van het bestuur';
    

    """
    )
    db.commit()
    return True


@migration
def add_organisation_changelog_20230120_01(db):
    db.executesql(
        """
    create table public.organisation_changelog
    (
        id            serial,
        org_gid       uuid       not null,
        fieldname     varchar    not null,
        field_value   json       not null,
        mutation_type varchar(1) not null,
        status        varchar    not null,
        source        uuid       not null,
        source_detail text       not null
    );
    
    comment on table public.organisation_changelog is 'Changes on the organisation data';
    
    comment on column public.organisation_changelog.org_gid is 'organisatie id ';
    
    comment on column public.organisation_changelog.fieldname is 'fieldname van organisation';
    
    comment on column public.organisation_changelog.field_value is 'waarde voor het bijbehorende veld, json array. geen is [null]';
    
    comment on column public.organisation_changelog.mutation_type is 'Wat voor mutatie is dit, Create Update Delete?';
    
    comment on column public.organisation_changelog.status is 'automatisch aangenomen, onbekend, overruled of aangenomen';
    
    comment on column public.organisation_changelog.source is 'source gid ';
    
    comment on column public.organisation_changelog.source_detail is 'details, filename, email zoiets';
    
    create table public.organisation_changes_source
    (
        id            serial,
        gid           uuid       not null unique,
        display_name  text       not null unique,
        prio          integer    not null unique
    );
    comment on column public.organisation_changes_source.gid is 'global id van de change source';
    
    comment on column public.organisation_changes_source.display_name is 'naam om weer te geven aan gebruikers, duo/edwh, zoiets. ';
      
    insert into public.organisation_changes_source (id, gid, display_name, prio) values (1, '7916d098-2b71-4594-aed6-36b8059390ac', 'EDWH', 100);
    insert into public.organisation_changes_source (id, gid, display_name, prio) values (2, '18b5c5ab-d301-404f-8e9d-3422f7e4e966', 'DUO', 50);
    insert into public.organisation_changes_source (id, gid, display_name, prio) values (1, '9e175f6d-8325-4d2e-b0e5-7fc57779640b', 'HIST', 1);

    """
    )
    db.commit()
    return True


def create_archive_sql_snippet(tablename: str) -> str:
    """
    LET OP:  bij wijzigingen aan gearchiveerde tabellen moeten die ook aan het archief tabel worden toegevoegd!
    TODO: #1029: hier een scan van maken en controleren of tabellen wel kloppen qua structuur
    """
    return f"""
    -- add the required column to prevent deletion 
    alter table public.{tablename} 
        add column is_active varchar(1) default 'T';
    -- drop any archive may it exist from previous dev builds 
    -- drop table if exists public.{tablename}_archive; 
    -- create a copy table from the base table 
    create table public.{tablename}_archive as (select * from public.{tablename}) with no data; 
    -- add the current_record field to reference {tablename}.id 
    alter table public.{tablename}_archive 
        add column current_record integer; 
    -- make the id column a unique key again 
    alter table public.{tablename}_archive
        alter column id set not null;
    alter table public.{tablename}_archive
        alter column id add generated always as identity;
    """


@migration
def add_archive_table_for_board_20230124_01(db):
    db.executesql(create_archive_sql_snippet("board"))
    db.commit()
    return True


@migration
def alter_board_table_2023_01_18_01(db):
    # vereist voor #873
    db.executesql(
        """
    alter table public.board 
        add column last_saved_by varchar;
    alter table public.board 
        add column last_saved_when timestamp;
    alter table public.board_archive
        add column last_saved_by varchar;
    alter table public.board_archive
        add column last_saved_when timestamp; 
    """
    )
    db.commit()
    try:
        # fix typo postcalcode -> postalcode, but may not exist anymore
        # on different installations
        db.executesql(
            """
                alter table public.board
                    rename column postcalcode to postalcode;
                alter table public.board_archive
                    rename column postcalcode to postalcode;
                """
        )
    except:
        db.rollback()
    else:
        db.commit()
    return True


@migration
def add_archive_table_for_organisation_20230124_02(db):
    db.executesql(create_archive_sql_snippet("organisation"))
    db.commit()
    return True


@migration
def add_archive_table_for_item_20230124_03(db):
    db.executesql(create_archive_sql_snippet("item"))
    db.commit()
    return True


@migration
def enable_effdt_on_organisations(db):
    db.executesql(
        """
    delete
    from organisation
    where platform is null;
    
    alter table organisation
        add column effdt     timestamp,
        add column effstatus varchar(1);
    
    update organisation
    set effstatus = 'T';
    
    update organisation
    set effdt = coalesce(validated_ts, '#1999-01-01#');
    
    update organisation
    set effstatus = 'F'
    where name = '';

    drop index if exists organisation_id_effdt;
    create index organisation_id_effdt
    on public.organisation (gid asc, effdt desc, id asc);

    """
    )
    db.commit()
    return True


def create_organisation_effdted_now_view(db):
    """
    Reuable function to create the organisation_effdt_now view.
    Since no date is appended, reuse this function when the organisation table is changed.
    """
    db.executesql(
        """
    create or replace view organisation_effdted_now as
    -- 1. get the max effdt for each gid where effdt <= now()
    -- 2. join the subquery on effdt and gid with the organisation table
    -- 3. filter on effstatus = 'T' to filter out removed records
    select organisation.*
    from organisation
             join (select org.gid, max(org.effdt) as effdt
                   from organisation org
                   where org.effdt <= now()
                   group by org.gid) as organisation_ed
                  on organisation.gid = organisation_ed.gid
                      and organisation.effdt = organisation_ed.effdt
    where organisation.effstatus = 'T';
    """
    )
    db.commit()
    return True


@migration
def create_organisation_effdt_now_view_2023_02_06_01(db):
    """create the organisation_effdt_now view using create_organisation_effdt_now_view_2023_02_06_01."""
    return create_organisation_effdted_now_view(db)


@migration
def add_organisational_fields_20230206_001(db):
    db.executesql(
        """
        alter table organisation
        add column student_count integer default 0, 
        add column last_saved_by varchar; 
        """
    )
    db.commit()
    return True


@migration
def create_organisation_effdt_now_view_2023_02_06_02(db):
    """create the organisation_effdt_now view using create_organisation_effdt_now_view_2023_02_06_01."""
    return create_organisation_effdted_now_view(db)


@migration
def drop_redunant_oragnisation_tables_2023_02_09_01(db):
    db.executesql(
        """
    drop table if exists organisation_archive;
    drop table if exists organisation_changelog;
    drop table if exists organisation_changes_source;
    """
    )
    db.commit()
    return True


@migration
def add_organisational_fields_2023_02_09_02(db):
    db.executesql(
        """
        alter table organisation
        add column prio integer default 0
        """
    )
    db.commit()
    return True


@migration
def replace_the_organisation_effdted_now_vw_to_work_with_prios_2023_02_09_03(db):
    db.executesql(
        """
        create or replace view organisation_effdted_now as
        select organisation.*
        -- select each organisation based on the highest prio
        -- and the latest effdt <= now, where prio is more important than effdt. 
        -- Filter on effstatus = 'T' to filter out removed records
        from public.organisation
                 join (select org.gid, max(org.prio) as max_prio
                       from organisation org
                       where org.effdt <= now()
                       group by org.gid 
                       ) as org_prio on org_prio.gid = organisation.gid 
                       and org_prio.max_prio = organisation.prio 
                 join (select org.gid, org.prio, max(org.effdt) as effdt
                       from organisation org
                       where org.effdt <= now()
                       group by org.gid, org.prio
                       ) as org_ed
                      on organisation.gid = org_ed.gid
                          and organisation.prio = org_ed.prio
                          and organisation.effdt = org_ed.effdt
        where organisation.effstatus = 'T'; 
        DROP INDEX IF EXISTS organisation_gid_effdt_prio;
        CREATE INDEX organisation_gid_effdt_prio 
            ON public.organisation (gid, effdt, prio);
        DROP INDEX IF EXISTS organisation_gid_prio_effdt;
        CREATE INDEX organisation_gid_prio_effdt 
            ON public.organisation (gid, prio, effdt);
        DROP INDEX IF EXISTS organisation_gid_prio_concatenated;
        CREATE INDEX organisation_gid_prio_concatenated 
            ON public.organisation ((gid || '.' || prio));
        -- CREATE INDEX organisation_gid_prio_effdt_concatenated 
        --     ON public.organisation ((gid || '.' || prio || '.' || effdt));

        """
    )
    db.commit()
    return True


@migration
def remove_default_value_for_organisational_data_20230210_01(db):
    """apply_update function for updating prio based, and effdt based tables
    works best when the default values are not set.
    """
    db.executesql(
        """
    alter table public.organisation
        alter column student_count set default null;
    update public.organisation set student_count = null where student_count = 0;
    """
    )
    db.commit()
    return True


@migration
def extend_sector_in_organisation_to_contain_a_list_20230213_001(db):
    db.executesql(
        """
    drop view if exists organisation_effdted_now;
    alter table public.organisation 
        alter column sector type text using sector::varchar(255);
    """
    )
    if create_organisation_effdted_now_view(db):
        db.commit()
        return True
    return False


@migration
def add_scope_and_set_default_values_based_on_author_and_author_email_20230221_01(db):
    db.executesql(
        """
    
    alter table public.item
        add scope text default '||' not null;
    comment on column public.item.scope is 'mogelijkheid om weergave te beperken tot netwerken, maar ook deleted, hidden enz. ';
        
    update public.item set scope = '|debug|' where platform = 'debug';
    update public.item set scope = '|all|' where platform = 'SvS';
    update public.item set scope = scope || 'deleted|' where author is null;
    update public.item set scope = scope || 'hidden|' from "user" where public.item.author = "user".gid and "user".email ilike '%@roc.nl';

    """
    )
    db.commit()
    return True


@migration
def rename_scope_to_visibility_20230221_02(db):
    db.executesql(
        """
    
    alter table public.item
        rename column scope to visibility;

    """
    )
    db.commit()
    return True


@migration
def rerun_alter_board_table_20230316_001(db):
    # vereist voor #873

    # zie de vier functies hier na

    return True


@migration
def rerun_alter_board_table_20230316_002(db):
    # vereist voor #873
    try:
        db.executesql(
            "select * from public.board where last_saved_by is not null limit 1;"
        )
    except psycopg2.errors.UndefinedColumn:
        db.rollback()
        db.executesql(
            """
        alter table public.board 
            add column last_saved_by varchar;
        """
        )

    db.commit()

    return True


@migration
def rerun_alter_board_table_20230316_003(db):
    # vereist voor #873
    try:
        db.executesql(
            "select * from public.board where last_saved_when is not null limit 1;"
        )
    except psycopg2.errors.UndefinedColumn:
        db.rollback()
        db.executesql(
            """
        alter table public.board 
            add column last_saved_when varchar;
        """
        )

    db.commit()

    return True


@migration
def rerun_alter_board_table_20230316_004(db):
    # vereist voor #873
    try:
        db.executesql(
            "select * from public.board_archive where last_saved_by is not null limit 1;"
        )
    except psycopg2.errors.UndefinedColumn:
        db.rollback()
        db.executesql(
            """
        alter table public.board_archive 
            add column last_saved_by varchar;
        """
        )

    db.commit()

    return True


@migration
def rerun_alter_board_table_20230316_005(db):
    # vereist voor #873
    try:
        db.executesql(
            "select * from public.board_archive where last_saved_when is not null limit 1;"
        )
    except psycopg2.errors.UndefinedColumn:
        db.rollback()
        db.executesql(
            """
        alter table public.board_archive 
            add column last_saved_when varchar;
        """
        )

    db.commit()

    return True


@migration
def add_tag_columns_for_metadata_eddie_opruimen_2020_2022_20230328_001(db):
    return True


@migration
def add_tag_columns_for_metadata_eddie_opruimen_2020_2022_20230328_002(db):
    db.executesql(
        """
    alter table public.tag
        add IF NOT EXISTS definition text;
    comment on column public.tag.definition is 'definitie van de tag';
    """
    )
    db.executesql(
        """
    alter table public.tag
        add IF NOT EXISTS instructions text;
    
    comment on column public.tag.instructions is 'instructies aan de eddie rondom deze tag';
    """
    )
    db.executesql(
        """
    alter table public.tag
        add IF NOT EXISTS remarks text;
    
    comment on column public.tag.remarks is 'opmerkingen tbv proces';
    """
    )
    db.executesql(
        """
    alter table public.tag
        add IF NOT EXISTS deprecated char(1) default 'F' not null;
    
    comment on column public.tag.deprecated is 'web2py boolean field';
    """
    )
    db.executesql(
        """
    alter table public.tag
        add IF NOT EXISTS replaced_by uuid;
    
    comment on column public.tag.replaced_by is 'Vervangen door de gid in dit veld indien deprecated; gewoon verwijderd indien deprecated d en replaced_by is null ';
    """
    )
    db.executesql(
        """
    alter table public.tag
        add IF NOT EXISTS questions text;
    
    comment on column public.tag.questions is 'pydal list:string - vragen die horen bij deze tag';
    """
    )
    db.executesql(
        """
    alter table public.tag
        add IF NOT EXISTS definitions_of_done text;
    
    comment on column public.tag.definitions_of_done is 'pydal list:string - definties of done die horen bij deze tag';
    """
    )
    db.commit()
    return True


@migration
def add_related_column_to_tag_20230405_01(db):
    db.executesql(
        """
    alter table public.tag add IF NOT EXISTS related text;
    comment on column public.tag.related is 'pydal list:string - gerelateerde tags';
    """
    )
    db.commit()
    return True


@migration
def change_license_from_copyright_to_ccbysa_2023_05_04_01(db: DAL):
    db.executesql(
        """
    update public.item 
        set license = 'cc-by-sa-4.0' 
        where license = 'copyright';
    """
    )
    db.commit()
    return True


@migration
def add_projecttag_2023_05_18_01(db):
    from edwh.core.tags import Tag

    if "tag" not in db.tables:
        # normally the DB connection will not have the tables defined
        # but the Tag object requires these. So we sed them up here.
        from edwh.core.data_model import setup_db_tables

        setup_db_tables(db)

    TSystem = Tag(db, "19682a99-50a3-4fc0-bb67-e0f6eff5da55")
    Tag.new(
        db,
        "Project Tags",
        "Container tag bedoeld voor specifieke projecten",
        gid="a15ecba0-8e27-4225-a110-50a081397bec",
        parents=[TSystem],
        meta_tags=[TSystem],
    )
    db.commit()
    return True


@migration
def change_tag_replaced_by_field_from_uuid_to_varchar_because_of_ilike_searches_in_grids_2023_05_24_01(
    db: DAL,
):
    db.executesql(
        """
    alter table public.tag
        alter column replaced_by type varchar(32) using replaced_by::varchar(32);
    """
    )
    db.commit()
    return True


@migration
def create_applog_item_view_20231201_001(db: DAL):
    db.executesql(
        """
    DROP VIEW IF EXISTS vw__item_applog CASCADE;

    CREATE OR REPLACE VIEW vw__item_applog AS
    SELECT s.gid                         as signal_gid,
           e.gid                         as evidence_gid,
           s.session_gid                 as signal_session_gid,
           e.session_gid                 as evidence_session_gid,
           s.ts                          as signal_ts,
           s.name                        as action,
           s.source                      as source,
           e.source                      as js,
           e.source ->> 'origin_domain'  as origin_domain,
           e.source ->> 'gid'            as item_gid,
           e.source ->> 'by_eddie_email' as by_eddie_email,
           e.source ->> 'changes'        as changes
    FROM signal s
             INNER JOIN evidence e ON e.id = s.evidence_id
    WHERE s.name in ('create-item', 'update-item', 'remove-item')
    ORDER BY s.ts DESC;
    
    CREATE INDEX IF NOT EXISTS evidence_source_gid ON evidence((source->>'gid'));
    """
    )

    db.commit()
    return True


@migration
def create_materialized_view_meta_view_20231206_001(db: DAL):
    db.executesql(
        """
    CREATE OR REPLACE VIEW materialized_views AS
        WITH pgdata AS (SELECT setting AS path
                        FROM pg_settings
                        WHERE name = 'data_directory'),
             path AS (SELECT CASE
                                 WHEN pgdata.separator = '/' THEN '/' -- UNIX
                                 ELSE '\' -- WINDOWS
                                 END AS separator
                      FROM (SELECT SUBSTR(path, 1, 1) AS separator FROM pgdata) AS pgdata)
        SELECT ns.nspname || '.' || c.relname                                                    AS mview,
               (pg_stat_file(pgdata.path || path.separator ||
                             pg_relation_filepath(ns.nspname || '.' || c.relname))).modification AS refresh
        FROM pgdata,
             path,
             pg_class c
                 JOIN
             pg_namespace ns ON c.relnamespace = ns.oid
        WHERE c.relkind = 'm'
;
    """
    )

    # usage:
    # SELECT * FROM materialized_views WHERE mview = 'public.mv__item_applog'
    db.commit()
    return True


@migration
def fix_non_item_gids_in_applog_20231208_001(db: DAL):
    from data_model import setup_db_tables

    db = setup_db_tables(db)

    table = db.vw_item_applog

    broken_items = db(~table.item_gid.like("%-%")).select()

    if not broken_items:
        print("Good news: nothing to fix!")
        return True

    success = failures = 0

    to_fix = {}  # evidence gid: item id
    for item in broken_items:
        if not item.item_gid or not item.item_gid.isdigit():
            # unfixable
            failures += 1
            continue

        to_fix[item.evidence_gid] = int(item.item_gid)

    items = (
        db(db.item.id.belongs(set(to_fix.values())))
        .select(db.item.id, db.item.gid)
        .as_dict("id")
    )

    for evidence_gid, item_id in to_fix.items():
        if item := items.get(item_id):
            item_gid = item["gid"]
            evidence = db.evidence(gid=evidence_gid)
            evidence.source["gid"] = item_gid
            evidence.update_record()
            success += 1
        else:
            failures += 1

    db.commit()

    if failures:
        warnings.warn(
            f"Not all applog item entries could be fixed! {success} success; {failures} failures."
        )
        return False
    else:
        print(f"Fixed {success} applog item entry gids!")

    return True


@migration
def update_applog_item_view_20231222_002(db: DAL):
    db.executesql(
        """
    DROP VIEW IF EXISTS vw__item_applog CASCADE;

    CREATE OR REPLACE VIEW vw__item_applog AS
    SELECT s.gid                         as signal_gid,
           e.gid                         as evidence_gid,
           s.session_gid                 as signal_session_gid,
           e.session_gid                 as evidence_session_gid,
           s.ts                          as signal_ts,
           s.name                        as action,
           s.source                      as source,
           e.source                      as js,
           e.source ->> 'origin_domain'  as origin_domain,
           e.source ->> 'gid'            as item_gid,
           e.source ->> 'by_eddie_email' as by_eddie_email,
           e.source ->> 'changes'        as changes
    FROM signal s
             INNER JOIN evidence e ON e.id = s.evidence_id
    WHERE s.name in ('create-item', 'update-item', 'remove-item') -- 'read-item'
    ORDER BY s.ts DESC;

    CREATE INDEX IF NOT EXISTS evidence_source_gid ON evidence((source->>'gid'));
    """
    )

    db.commit()
    return True


@migration
def create_auto_tag_20240314_001(db: DAL):
    # pydal2sql create --magic --dialect postgres --format edwh-migrate
    db.executesql(
        """
        CREATE TABLE "auto_tag"(
            "id" SERIAL PRIMARY KEY,
            "needle" VARCHAR(512),
            "visibilities" TEXT,
            "tag_gid" VARCHAR(512),
            "tagged_in_db" TEXT,
            "search_results" TEXT
        );
    """
    )
    db.commit()
    return True


# @migration
# def functionalname_date_sequencenr(db):
#     db.executesql('''
#     ''')
#     db.commit()
#     return True
