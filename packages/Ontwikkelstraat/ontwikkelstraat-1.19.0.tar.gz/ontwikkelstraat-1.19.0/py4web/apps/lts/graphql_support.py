# def invalidate(gid, data_loader_type=None):
#     "invalidate gid from the redis cache, dispatching a clear_cache event when data_loader_type is given"
#     # invalidate the redis cache so a new retrieval will reload data from the database
#     import redis_cache
#     redis_cache.invalidate(redis_cache.redis, gid)
#
#     # send a signal to the backend graphql-services to clear their dataloader caches
#     from nameko.standalone.events import event_dispatcher
#     ed = event_dispatcher(dict(AMQP_URI='pyamqp://guest:guest@127.0.0.1:5672/'))
#     ed("graphql",'clear_cache',dict(value=dict(which=data_loader_type,gid=gid)))
import binascii
import collections
import copy
import datetime
import json
import os
import re
from typing import Callable
from urllib.parse import urlparse
from uuid import UUID, uuid4

import dill
import markdown2
import pydal
import user_agents
from attrs import define, field
from edwh.core.applog.signalemitter import SignalEmitter
from edwh.core.applog.sink import SignalSink
from edwh.core.backend import *
from edwh.core.backend.ntfy_sh import error, onbekend, warning
from edwh.core.backend.tasks import outbound_email_new_password, upload_attachment
from edwh.core.data_model import Visibility
from edwh.core.pgcache import Magic, cached, fromdb, todb
from pydal import DAL
from ycecream import y

from py4web import Cache, request, response
from py4web.core import Fixture

from .common import db, session, sink

PLATFORM = "SvS"

EXPIRATION_USER_QUERY = 3600
EXPIRATION_FILTER_TAGS_QUERY = 3600
EXPIRATION_QUICKFILTER_QUERY = 3600
EXPIRATION_ITEM_QUERY = 3600
EXPIRATION_ITEMS_QUERY = 600

BACKEND_ME = "backend_me"
SESSION_TOKEN = "session_token"
cache = Cache(size=10000)

BACKEND_TIMEOUT = 50
BACKEND_SESSION_TOKEN = "backend_session_token"

y.configure(enabled=required_env("ENABLE_ICECREAM"))


class Unknown:
    pass


#
# class Uncachable(BaseException):
#     """Some items should not be cached. Uncacheable is raised if a cache key is generated while trying"""
#
#
# def craft_item_cache_key(id, backend):
#     if backend.is_registered_user:
#         raise Uncachable("User is logged in, item cannot be cached. ")
#     return str(
#         collections.OrderedDict(
#             _type="item",
#             id=id,
#         )
#     )


import dotmap


def dotmapify(method):
    def wrapper(*a, **kw):
        resp = method(*a, **kw)
        return dotmap.DotMap(resp)

    return wrapper


#
# def craft_tiles_cache_key(env, backend):
#     if backend.is_registered_user:
#         raise Uncachable("User is logged in, item cannot be cached. ")
#     key = copy.copy(env)
#     if "loggedIn" in key:
#         del key["loggedIn"]
#     if "token" in key:
#         del key["token"]
#     return str(key)


class BackendError(RuntimeError):
    """Indicates an error in the graphql backend."""

    pass


class QueryWarning(UserWarning):
    pass


class Py4webBackend(Fixture, Backend):
    backend_session_token: SessionToken

    def __init__(self, database: DAL, sink: SignalSink, applog: SignalEmitter):
        super().__init__(database, sink, applog)

    def on_request(self, ctx):
        try:
            db.rollback()
        except:
            db._adapter.reconnect()
        self.refresh_me()
        session_dict = session.get("token")
        if session_dict:
            # lees dat ding uit naar een session:
            self.token = SessionToken(**session_dict)
        else:
            # maak een nieuw session:
            agent = user_agents.parse(
                "" if backend else request.headers.get("User-Agent", "")
            )
            hardware = dict(
                is_email_client=agent.is_email_client,
                is_pc=agent.is_pc,
                is_bot=agent.is_bot,
                is_mobile=agent.is_mobile,
                is_tablet=agent.is_tablet,
                is_touch_capable=agent.is_touch_capable,
                os_family=agent.os.family,
                os_version=agent.os.version,
                device_family=agent.device.family,
                device_brand=agent.device.brand,
                device_model=agent.device.model,
                browser_family=agent.browser.family,
                browser_version=agent.browser.version,
            )
            self.token = self.new_session_token(hardware, self.me)
            session["token"] = edwh_asdict(self.token)

        origin_domain = request.headers.get("origin")
        if origin_domain:
            # strip http and everything after the origin domain
            origin_domain = urlparse(origin_domain).netloc
        else:
            origin_domain = request.urlparts.netloc
        me = self.me
        # bind every request to username
        self.applog = SignalEmitter(
            signal_processor=sink,
            signal_source="py4web.front_end",
            session_gid=self.token.token,
            user_gid=me.id if me else None,
            timestamp=datetime.datetime.now(),
            origin_domain=origin_domain,
        )

    def on_error(self, ctx):
        print(ctx["exception"])

    def on_success(self, status):
        pass

    def transform(self, output, shared_data=None):
        response.set_header("X-EDWH-PID", os.getpid())
        return output

    def refresh_me(self) -> None:
        # follow up with backend.me, because this will use
        # the above saved BACKEND_SESSION_TOKEN value.
        # order of execution is important here.
        session[BACKEND_ME] = edwh_asdict(self.me) if self.me else None
        session.save()

    @property
    def is_registered_user(self):
        # "BACKEND_ME" is saved on (anonymous) login
        return session.get(BACKEND_ME) is not None

    @property
    def is_anonymous(self):
        # "BACKEND_ME" is saved on (anonymous) login
        return session.get(BACKEND_ME) is None

    @property
    def me(self):
        return User(**session.get(BACKEND_ME)) if self.is_registered_user else None

    @property
    def anon_or_id(self):
        return self.me.id if self.me else "anon"

    @classmethod
    def timeago(cls, datetimestring):
        dt = datetime.datetime.fromisoformat(datetimestring)
        return human_friendly_timedelta(datetime.datetime.now() - dt)

    def item(self, id: UUID, track: Callable = Magic) -> Item:
        item = super().item(id, track)
        return item

    @cached(
        db,
        key="fx-gs-tiles-{self.anon_or_id}-{limit}-{offset}-{order}-{search}-{author}-{tags}",
        todb=todb,
        fromdb=fromdb,
        silence_key_warning=True,
    )
    def tiles(
        self,
        limit: int = 9,
        offset: int = 0,
        order: str = "RECENT_DESC",
        search: str = None,
        tags: [[str]] = None,
        author: str = None,
        track: Callable = Magic,
        include: list[Visibility] | None = None,
        exclude: list[Visibility] | None = None,
    ) -> ItemSearchResult:
        search_result = self.search_items(
            me=self.me,
            with_tags=tags,
            order=SortOrder[order],
            first=limit,
            offset=offset,
            search=search,
            search_in=["tag", "name", "description", "author"],
            author=author,
            included_visibilities=include,
            excluded_visibilities=exclude,
        )
        found = []
        for gid in search_result.found:
            found.append(self.item(track(gid), track))
        item_search_result = ItemSearchResult(
            available=search_result.available,
            found=found,
            first=limit,
            offset=offset,
        )
        return item_search_result

    def login(
        self,
        email: str,
        hardware: dict,
        password: str | None = None,
        password_hash: str | None = None,
    ) -> Validated:
        validated = super().login(email, hardware, password, password_hash)
        if validated.code == ValidationCode.OK:
            session[BACKEND_ME] = edwh_asdict(validated.user)
            session[SESSION_TOKEN] = edwh_asdict(validated.token)
            # session[BACKEND_SESSION_TOKEN] = str(validated.token.token)
            session.save()
        elif validated.code == ValidationCode.REQUIRES_EMAIL_VALIDATION:
            # used in self.validate_email_address
            session["PREAUTH"] = edwh_asdict(validated.user)
            session["PREAUTH_SESSION"] = edwh_asdict(validated.token)
        return validated

    @dotmapify
    def signup(
        self,
        email: str,
        password: str,
        firstname: str,
        lastname: str,
        organisation: str,
        location: str,
        primary_organisational_role: str,
        kvk: str,
    ) -> User:
        new_user = self.create_user(
            email=email,
            password=password,
            firstname=firstname,
            lastname=lastname,
            organisation=organisation,
            location=location,
            primary_organisational_role=primary_organisational_role,
            session_token=...,
            property_bag={"kvk": kvk},
        )
        self.applog.new_user(email=email, user_gid=new_user.id)
        return response

    @dotmapify
    def update_me(self, fields):
        email = (
            None
            if backend.me().get("email") == fields.get("username")
            else fields.get("username")
        )
        # todo: organisation -> userProvidedOrganisation?

        if password := fields.get("password"):
            password = hash_password(password)

        del fields["password"]

        env = dict(token=backend.token, email=email, password=password, **fields)

        response = self.query(query, env, "update_me")
        new_me = self.refresh_me()
        self.applog.update_me(user_gid=new_me.get("id"))
        return response

    def user(self, id: str):
        # logging is done in the controller

        @define
        class UserWithItems(User):
            items: UUIDSearchResult = field(init=False)

            def __attrs_post_init__(self):
                self.items = backend.search_items(author=self.id)

        user = UserWithItems.load(db, UUID(id))
        return user

    def filter_tags_to_tag_tree(
        self,
        tags: list[Tag],
        with_tags: list[str],
        settings: dict,
        track: Callable = Magic,
    ) -> tuple[list, list[str]]:
        "Convert a list of Tags to a tree of dicts (for templating) and a set of tag.id"
        flat_ids = set()
        counts_per_tag = (
            self.get_item_counts_per_tag_for_given_tag_combination_and_search_query(
                settings.get("q", ""), []
            )
        )

        def prepare_dict_tree(arg: Tag | list[Tag]):
            if isinstance(arg, list):
                arg: list[Tag]
                dict_list = [prepare_dict_tree(_) for _ in arg]
                return dict_list
            elif isinstance(arg, Tag):
                arg: Tag
                d = edwh_asdict(arg)
                d["label"] = arg.name
                d["tag"] = str(arg.id)

                d["itemCount"] = counts_per_tag.get(str(arg.id), 0)
                d["itemTreeCount"] = counts_per_tag.get(str(arg.id), 0)

                # -1 is used while itemTreeCount was not implemented,
                # so in that case we don't show the count.
                d["hasItemTreeCount"] = d["itemTreeCount"] > 0

                flat_ids.add(str(track(arg.id)))

                d["children"] = prepare_dict_tree(
                    [Tag.load(self.db, track(child_gid)) for child_gid in arg.children]
                )
                return d
            else:
                print("what is this:", type(arg), arg)

        return prepare_dict_tree(tags), flat_ids

    @classmethod
    def _filter_tags(cls, settings: dict, with_tags: list[str]) -> tuple[str, Callable]:
        """Moest een key en een callable opleveren tbv caching, callable voerde de query uit en leverde dus een dict."""
        search_q = settings.get("q", "")
        # convert to list of UUIDS
        items_filtered_with = [UUID(_) for _ in settings.get("tags", [])]
        return (
            f"{with_tags!r}-filter-tags-{search_q!r}-{sorted([str(g) for g in items_filtered_with])!r}",
            lambda: backend.tags(
                with_tags=with_tags,
                items_q=search_q,
                items_filtered_with=items_filtered_with,
            ),
        )

    @cached(
        db,
        "gs.py4webbackend.filter_tags.{with_tags}.{settings}",
        todb=todb,
        fromdb=fromdb,
        ttl=3600,
    )
    def filter_tags(
        self, with_tags: list[str], settings: dict, track: Callable = Magic
    ) -> tuple[list[dict], set[str]]:
        "Returns a prepared_dict_tree:dict and a flat list of all tag ids (as string)"
        key, fn = self._filter_tags(settings, with_tags)
        tags = fn()
        # filter_tags = copy.deepcopy(fn()) # werd gewijzigd door de functie, dus kopie van maken om cached kopie niet te veranderen.
        return self.filter_tags_to_tag_tree(
            tags, with_tags=with_tags, settings=settings, track=track
        )

    @cached(
        db, "gs.py4webbackend.quick-filter-tags", todb=todb, fromdb=fromdb, ttl=3600
    )
    def quick_filter_tags(self, track: Callable = Magic):
        TFilterBalk = "c05e9cea-76c0-4b48-8f91-4cee4ff7f0ab"
        tag_tree, gid_list = self.filter_tags(
            with_tags=[TFilterBalk], settings={}, track=track
        )
        return [Tag.load(db, gid) for gid in gid_list if gid != TFilterBalk]

    def get_tags(cls, taglist):
        return [Tag.load(db, id) for id in taglist]

    @dotmapify
    def like(self, subject, toggle, action="THUMBS"):
        # # FAVORITE = star
        # # THUMBS = heart
        # query = """
        # mutation Like($token: UUID!, $subject: UUID!, $toggle: Int!, $action: MarkEnum!){
        #   auth(sessionToken: $token){
        #     mark(subject: $subject, mark: $toggle, name: $action) {
        #       _
        #     }
        #   }
        # }
        # """
        #
        # env = dict(
        #     token=backend.token,
        #     subject=subject,
        #     toggle=int(toggle),
        #     action=action,
        # )
        #
        # self.applog.update_mark(subject_gid=subject, mark=toggle, mark_type=action)

        return self.query(query, env, allow_empty=True)

    @classmethod
    def notifications(cls):
        # query = """
        # query notifications($token: UUID!) {
        #   auth(sessionToken: $token) {
        #     notifications (first: 10, offset: 0){
        #       id
        #       when
        #       title
        #       message
        # #       concerning {
        # #         __typename
        # #         ... on Item {
        # #           id
        # #         }
        # #         ... on Comment {
        # #           id
        # #         }
        # #         ... on FavoriteList{
        # #           id
        # #         }
        # #      }
        #       concerningType
        #       readTimestamp
        #     }
        #   }
        # }
        # """
        # env = dict(token=backend.token)
        #
        # return cls.query(query, env)
        return {}

    @classmethod
    def notification_seen(cls, notification):
        # backend.applog.seen_global_notification()
        # backend.applog.seen_user_notifications()
        # query = """
        # mutation markAsRead($token: UUID!, $notification: UUID!) {
        #   auth(sessionToken: $token) {
        #     markAsSeen(notifications: [$notification]){
        #       result
        #     }
        #   }
        # }
        # """
        # env = dict(token=backend.token, notification=notification)
        return cls.query(query, env)

    def upload_avatar(self, filename, filecontent, ts: datetime):
        gid = uuid4()
        db.attachment.insert(
            platform="SvS",
            gid=str(gid),
            attachment=None,
            filename=filename,
            purpose="avatar",
            ts_uploaded=ts,
            owner_gid=str(self.me.id),
            b2_uri="https://f003.backblazeb2.com/file/nl-meteddie-delen-permalinkable/progress.gif",
        )
        upload_attachment.delay(gid=gid, filename=filename, content=filecontent)
        self.applog.upload_attachment(attachment_gid=gid)
        onbekend(f"Upload van {gid} aangevraagd, base64 lengte:{len(filecontent)}.")
        return Attachment.load(self.db, gid)

    def organisation(self, id: str):
        # query = """
        # query organisation($token: UUID!, $school: UUID!) {
        #   auth(sessionToken: $token){
        #     organisation(id:$school) {
        #       id name permalink  thumbCount street number city lonlat itemTag {
        #         id name
        #       }
        #     }
        #   }
        # }
        # """
        # env = {
        #     "token": backend.token,
        #     "school": id,
        # }
        # org = self.query(query, env, "organisation")["data"]["auth"]["organisation"]
        #
        # self.applog.read_organisation(org_gid=id)

        return org

    @classmethod
    def organisations(cls, ids: list):
        # org_queries = "\n".join(
        #     [
        #         """
        #         org_%d: organisation(id:"%s") {
        #           id name permalink  thumbCount street number city lonlat itemTag {
        #             id name
        #           }
        #         }"""
        #         % (idx, org_id)
        #         for idx, org_id in enumerate(ids)
        #     ]
        # )
        #
        # query = (
        #     """
        #                                             query organisation($token: UUID!) {
        #                                               auth(sessionToken: $token){
        #                                                 %s
        #                                               }
        #                                             }
        #                                             """
        #     % org_queries
        # )
        # env = {
        #     "token": backend.token,
        # }
        return cls.query(query, env, "organisation")["data"]["auth"]

    # noinspection PyMethodOverriding
    def validate_email_address(self, entered_code: str):
        # set in self.login
        user = User(**session["PREAUTH"])
        super().validate_email_address(user, entered_code)
        # als geen exception:
        session[BACKEND_ME] = edwh_asdict(user)
        session[BACKEND_SESSION_TOKEN] = session["PREAUTH_SESSION"]
        del session["PREAUTH"]
        del session["PREAUTH_SESSION"]
        session.save()


backend = Py4webBackend(
    database=db,
    sink=sink,
    applog=SignalEmitter(
        signal_processor=sink,
        signal_source="py4web.front_end",
        session_gid=None,
        user_gid=None,
        timestamp=datetime.datetime.now(),
        origin_domain=required_env("HOSTINGDOMAIN"),
    ),
)
