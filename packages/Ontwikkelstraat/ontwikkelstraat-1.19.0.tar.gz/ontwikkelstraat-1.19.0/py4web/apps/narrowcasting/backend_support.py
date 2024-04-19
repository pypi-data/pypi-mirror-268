# def invalidate(gid, data_loader_type=None):
#     "invalidate gid from the redis cache, dispatching a clear_cache event when data_loader_type is given"
#     # invalidate the redis cache so a new retrieval will reload data from the database
#     import redis_cache
#     redis_cache.invalidate(redis_cache.redis, gid)
#
import datetime
import os
import string
import typing
import unicodedata
from typing import Callable
from urllib.parse import urlparse
from uuid import UUID

import dill
import user_agents
from attrs import define, field
from edwh.core.applog.signalemitter import SignalEmitter
from edwh.core.applog.sink import SignalSink
from edwh.core.backend import *
from edwh.core.backend.engine import PROGRESS_GIF
from edwh.core.data_model import (
    DEFAULT_EXCLUDED_VISIBILITY,
    DEFAULT_INCLUDED_VISIBILITY,
    Visibility,
)
from edwh.core.pgcache import Magic, cached, fromdb, hash, todb
from ycecream import y

from py4web import DAL as Py4WebDAL
from py4web import Cache, request, response
from py4web.core import Fixture

from .common import db, session, sink
from .helpers import PY4WEB_URL
from .settings import APP_NAME

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

# lower
STOP_WORDS = {
    "",
    "de",
    "het",
    "een",
    "dit",
    "dat",
    "in",
    "je",
    "zo",
    "op",
    "met",
    "bij",
    "wat",
    "als",
    "hoe",
}
# lijst gebaseerd op huidige delen.meteddie data

# letterplaatjes exist for all lowercase ASCII letters (so no digits etc)
LETTERPLAATJES = set(string.ascii_lowercase)

y.configure(enabled=required_env("ENABLE_ICECREAM"))


class Unknown:
    pass


def remove_accents(input_str: str) -> str:
    # https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
    # files kunnen geen éä en zo aan, dus normalize names hier:
    return "".join(
        c
        for c in unicodedata.normalize("NFD", input_str)
        if unicodedata.category(c) != "Mn"
    )


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
    """Indicates an error in the backend."""

    pass


class QueryWarning(UserWarning):
    pass


@define(slots=False)
class OrganisationWithItems(Organisation):
    items: UUIDSearchResult = field(init=False)
    backend: Backend = field(init=False)  # is a class variable, not an instance var.

    # backend is set when Backend is initialized.

    def __attrs_post_init__(self):
        if self.item_tag:
            self.items = self.backend.search_items(with_tags=[self.item_tag.id])
        else:
            self.items = UUIDSearchResult(0, [])

    @classmethod
    def fromdb(cls, data):
        dump = dill.loads(data)
        items = UUIDSearchResult(**dump["items"])
        del dump["items"]
        dump["item_tag"] = Tag(**dump["item_tag"]) if dump["item_tag"] else None
        instance = cls(**dump)
        instance.items = items
        return instance


class Py4webBackend(Fixture, Backend):
    backend_session_token: SessionToken

    def __init__(self, database: Py4WebDAL, sink: SignalSink, applog: SignalEmitter):
        if not hasattr(self, "__prerequisites__"):
            self.__prerequisites__ = []
        self.__prerequisites__.append(database)
        self.__prerequisites__.append(session)

        super().__init__(database, sink, applog)

    def on_request(self, ctx):
        # try:
        #     db.rollback()
        # except:
        #     db._adapter.reconnect()
        self.refresh_me()
        request.me = self.me
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

    def refresh_me(self, updated_me: User | None = None) -> None:
        """Saves self.me as an edwh_dict to the session, or uses updated_me to use that object instead."""
        # follow up with backend.me, because this will use
        # the above saved BACKEND_SESSION_TOKEN value.
        # order of execution is important here.
        session[BACKEND_ME] = edwh_asdict(updated_me or self.me) if self.me else None
        session.save()

    @property
    def is_registered_user(self):
        """Returns True if a user is logged in this session."""
        # "BACKEND_ME" is saved on (anonymous) login
        return session.get(BACKEND_ME) is not None

    @property
    def is_anonymous(self):
        """Returns True if no user has logged in for this session."""
        # "BACKEND_ME" is saved on (anonymous) login
        return session.get(BACKEND_ME) is None

    @property
    def me(self) -> User:
        """Returns a User instance based on recovered (from session) edwh_dict or None"""
        try:
            # return the already created User object
            return request.me
        except AttributeError:
            # create a new user object and save it to the request
            if self.is_registered_user:
                request.me = me = User(**session.get(BACKEND_ME))
                return me
            # none otherwise
        # none otherwise

    @property
    def anon_or_id(self):
        """Quick self.me.id or 'anon'"""
        return self.me.id if self.me else "anon"

    @classmethod
    def timeago(cls, datetimestring):
        dt = datetime.datetime.fromisoformat(datetimestring)
        return human_friendly_timedelta(datetime.datetime.now() - dt)

    @classmethod
    def fallback_thumbnail_url(cls, item: Item) -> str:
        """
        Generate a thumbnail based on the first letter of the item's title, excluding stop-words.
        """

        title = remove_accents(item.name).lower()  # Één -> een

        # grab first letter of first word not in wordlist
        first_letter = next(
            (
                word[0]
                for word in title.split(" ")
                if word not in STOP_WORDS and word[0] in LETTERPLAATJES
            ),
            title[
                0
            ],  # default to first letter of title, in case it's all stop words (for some reason)
        )
        return PY4WEB_URL(APP_NAME, f"static/images/thumbnails/{first_letter}.png")

    @classmethod
    def thumbnail_url(cls, item: Item) -> str:
        """
        Show the related background attachment
            or generate a thumbnail based on the first letter of the item's title, excluding stop-words.
        """
        if not item:
            # nothing to do
            return ""
        elif item.thumbnail and (uri := item.thumbnail.uri) and uri != PROGRESS_GIF:
            return uri
        else:
            return cls.fallback_thumbnail_url(item)

    @cached(
        db,
        key="fx-gs-tiles-[searchresult]-{self.anon_or_id}-{limit}-{offset}-{order}-{search}-{author}-{tags}-{include}-{exclude}",
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
        tags: list[list[str]] = None,
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

        # convert list of UUID's to list of Tiles:
        found_items = self.items_for_gid_list(search_result.found)

        # return new ItemSearchResult (for working pagination)

        return ItemSearchResult(
            # copy found:
            found=found_items,
            # use original available, limit and offset (for paginate):
            available=search_result.available,
            first=limit,
            offset=offset,
        )

        # found = []
        # for gid in search_result.found:
        #     found.append(self.item(track(gid), track))
        # item_search_result = ItemSearchResult(
        #     available=search_result.available,
        #     found=found,
        #     first=limit,
        #     offset=offset,
        # )
        # return item_search_result

    @cached(
        db,
        key=lambda uuids, **vars: f"fx.gs.items_from_gid_list:{hash(repr(uuids))}",
        todb=todb,
        fromdb=fromdb,
        silence_key_warning=True,
    )
    def items_for_gid_list(
        self,
        uuids: list[UUID],  # ','.join([str(u) for u in uuids])
        track: Callable = Magic,
    ) -> list[Item]:
        """
        Similar to search_result_from_gid_list but without first and offset since these pagination variables
         can depend on other settings that exist in the cache key (e.g. page and limit)
        """
        found = []
        for gid in uuids:
            found.append(self.item(track(gid), track))
        return found

    # todo: organisations_for_gid_list ?

    @cached(
        db,
        key=lambda uuids, **vars: f"fx.gs.search_result_from_gid_list:{hash(repr(uuids))}",
        todb=todb,
        fromdb=fromdb,
        silence_key_warning=True,
    )
    def search_result_from_gid_list(
        self,
        uuids: list[UUID],  # ','.join([str(u) for u in uuids])
        available: int = None,
        limit: int = 0,
        offset: int = 0,
        track: Callable = Magic,
    ) -> ItemSearchResult:
        """
        For proper pagination, use items_for_gid_list !!!
        """

        found = []
        for gid in uuids:
            found.append(self.item(track(gid), track))
        item_search_result = ItemSearchResult(
            available=available if available else len(found),
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
        """
        Validates the user credentials, on succes saves the user and session token to the current session.

        When the user still requires email validation, the session isn't logged in, but a preauth user and
        session are saved. These are used in the login controller functions.
        """
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
        """
        Creates a new user, returning the new User object.
        """
        new_user = self.create_user(
            email=email,
            password=password,
            firstname=firstname,
            lastname=lastname,
            organisation=organisation,
            location=location,
            primary_organisational_role=primary_organisational_role,
            property_bag={"kvk": kvk},
        )
        self.applog.new_user(email=email, user_gid=new_user.id)
        return new_user

    def user(self, id: str):
        # logging is done in the controller

        @define
        class UserWithItems(User):
            items: UUIDSearchResult = field(init=False)

            def __attrs_post_init__(self):
                self.items = backend.search_items(author=self.id)

        return UserWithItems.load(db, UUID(id))

    def filter_tags_to_tag_tree(
        self,
        tags: list[Tag],
        with_tags: list[str],
        settings: dict,
        track: Callable = Magic,
    ) -> tuple[list[dict[str, typing.Any]], set[str]]:
        "Convert a list of Tags to a tree of dicts (for templating) and a set of tag.id"
        flat_ids = set()

        include = request.settings.get("include", DEFAULT_INCLUDED_VISIBILITY)
        exclude = request.settings.get("exclude", DEFAULT_EXCLUDED_VISIBILITY)

        counts_per_tag = (
            # get the item count based on the query and the item-tags from the user.
            # using the with_tags is false, as those are not the item-tags and will nullify
            # the results of the item-count per tag. So don't.
            self.get_item_counts_per_tag_for_given_tag_combination_and_search_query(
                settings.get("q", ""),
                settings.get("tags", []),
                included_visibilities=include,
                excluded_visibilities=exclude,
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
        # convert to list of UUIDS or list of list of UUIDs
        items_filtered_with = [
            [UUID(_) for _ in tags] if isinstance(tags, list) else UUID(tags)
            for tags in settings.get("tags", [])
        ]
        return (
            f"{with_tags!r}-filter-tags-{search_q!r}-{hash(sorted([str(g) for g in items_filtered_with]))}",
            lambda: backend.tags(
                with_tags=with_tags,
                items_q=search_q,
                items_filtered_with=items_filtered_with,
            ),
        )

    @cached(
        db,
        key=lambda with_tags, settings, **vars: f"gs.py4webbackend.filter_tags.{hash(repr(with_tags))}.{hash(repr(settings))}",
        todb=todb,
        fromdb=fromdb,
        ttl=3600,
    )
    def filter_tags(
        self, with_tags: list[str], settings: dict, track: Callable = Magic
    ) -> tuple[list[dict[str, typing.Any]], set[str]]:
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

    def get_tags(self, taglist: typing.Iterable):
        return [Tag.load(db, id) for id in taglist]

    def like(self, subject: UUID | str, toggle: int, action="thumbs"):
        subject_type, gid = self.mark(request.me, subject, action, toggle)
        self.applog.update_mark(subject_gid=subject, mark=toggle, mark_type=action)
        table = db[subject_type]
        # perform a no-op update that will trigger the update of the table
        # this way cache will be invalidated for comments, items etc.
        db(table.gid == str(subject)).update(gid=subject)
        # update the current users list of favorites
        request.me.update_gid_thumb_map(db)
        # save the current users changes to the session
        self.refresh_me()
        return subject_type, str(gid)

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

    @cached(
        db,
        "gs-py4webbackend-organisation-{id}",
        todb=OrganisationWithItems.todb,
        fromdb=OrganisationWithItems.fromdb,
    )
    def organisation(self, id: str | UUID, track: Callable = Magic):
        self.applog.read_organisation(org_gid=track(id))
        org = OrganisationWithItems.load(db, id, track=track)
        for item in org.items.found:
            track(item)
        return org

    # def organisations(self):
    #     # todo: applog.search_organisation ?
    #     org_ids = self.search_organisations()
    #
    #     # convert list of UUID's to list of Tiles:
    #     found_items = self.organisations_for_gid_list(org_ids.found)

    @cached(
        db,
        "gs-py4webbackend-organisations-with-coc-{search}-{location}-{limit}",
        todb=todb,
        fromdb=fromdb,
        ttl=3600,
    )
    def list_schools_for_register(
        self, search: str = None, location: str = None, limit: int = 0
    ) -> dict[str, int]:
        table = db.organisation_effdted_now

        org_ids = self.search_organisations(
            search=search,
            location=location,
        )

        rows = db(table.gid.belongs(org_ids.found)).select(
            table.name, table.coc, limitby=(0, limit)
        )

        return {row.name: row.coc for row in rows}

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
OrganisationWithItems.backend = backend
