import difflib
import typing
import uuid
from datetime import datetime
from typing import List, Union
from uuid import UUID

from ..data_model import Visibility
from .sink import SignalSink


def gidstr(gid: UUID | str):
    """
    Turn a UUID into a string.
    """
    return str(gid) if gid else None


def normalize_for_diff(value) -> list[str]:
    """
    Prepare a value so it can be better parsed by difflib.unified_diff.

    Used on both the 'before' and 'after' variable in 'find_difference' to make comparing them easier.
    """
    if not value:
        return []

    if isinstance(value, str):
        if "\n" in value:
            return value.splitlines(keepends=True)

        return [value]

    if isinstance(value, typing.Iterable):
        return [str(_) for _ in value]
    else:
        return [str(value)]


def find_difference(before, after) -> list[str]:
    """
    Compare a 'before' and 'after' value (which can be a string or some other type).

    Difflib is used to generate a minimal diff. This is stored for item changes in the applog (see `update_item`).
    """

    multiline_str = (isinstance(before, str) and "\n" in before) or (
        isinstance(after, str) and "\n" in after
    )
    context = 2 if multiline_str else 0
    # context only makes sense for multiline strings, not other data types.

    before = normalize_for_diff(before)
    after = normalize_for_diff(after)

    if before == after:
        return []

    changes = list(difflib.unified_diff(before, after, n=context))[3:]

    return [_ for _ in changes if not _.startswith("@")]


class SignalEmitter:
    """
    SignalEmitter class to help spawn multiple signals from one request, provide as many details as possible.

    Timestamp defaults to now.
    Related is derived from api_activity_gid or api_umbrella_request_id, or made up with a new uuid4.
    """

    def __init__(
        self,
        signal_processor: SignalSink = None,  # will receive .signal() messages
        signal_source=None,  # what logs these statistics
        session_gid=None,  # backend-session gid if known
        user_gid=None,  # logged in users have a user_gid, anonymous is None
        timestamp=None,  # when this happened
        api_activity_gid=None,  # when the source is the api_activity table, this refers to the gid
        api_umbrella_request_id=None,  # when api_umbrella is the source, this refers to the specific request
        fragments_cookie=None,  # the cookie used on a used fragments server (py4web), if any, None otherwise
        workbench_cookie=None,  # the cookie used on a workbench application (web2py), if any, None otherwise
        cms_domain_cookie=None,  # cookies for the specific domain (delen.../leiden... cookies) to differ users
        origin_domain=None,  # string like delen.meteddie.nl or onderwijsindeleidseregio.nl or similar.
    ):
        # signal_processor  was een SignalService in het workbook
        self.sink = signal_processor

        base_evidence = dict(
            api_activity_gid=gidstr(api_activity_gid), origin_domain=origin_domain
        )
        if fragments_cookie:
            base_evidence["fragments_cookie"] = fragments_cookie
        if workbench_cookie:
            base_evidence["workbench_cookie"] = workbench_cookie
        if cms_domain_cookie:
            base_evidence["cms_domain_cookie"] = cms_domain_cookie

        self.ts = timestamp or datetime.now()  # writeable from outside
        self.signal_source = signal_source
        self.session_gid = gidstr(session_gid)  # writable from outside
        self.user_gid = gidstr(user_gid)  # writable from outside
        self.base_evidence = base_evidence
        # related is only set in the __init__
        # writable from the outside!!
        # functions both as the source_gid as well as a reference. 'group by' kind of field.
        self.related = str(
            api_activity_gid or api_umbrella_request_id or uuid.uuid4()
        ).encode("utf-8")

    def relate(self, related_gid: str | UUID):
        self.related = gidstr(related_gid).encode("utf-8")
        self.base_evidence["api_activity_gid"] = gidstr(related_gid).encode("utf-8")
        return self

    def commit(self):
        self.sink.commit()

    def _fire(self, name, **evidence):
        """Internal function to fire and forget the signal to the signal service"""
        signal_evidence = self.base_evidence.copy()
        if not signal_evidence["api_activity_gid"]:
            # clean this field if None, to save storage.
            del signal_evidence["api_activity_gid"]
        signal_evidence.update(evidence)

        self.sink.signal(
            name,
            signal_source=self.signal_source,
            session_gid=gidstr(self.session_gid),
            evidence=signal_evidence,
            user_gid=gidstr(self.user_gid),
            related=self.related,
            ts=self.ts,
        )
        return self

    def info(self, **kwp):
        """General info, don't use too often. Meant  for testing/development purposes"""
        return self._fire("info", **kwp)

    def server_event(self, what, who, why, **kwp):
        """Starts, stops, flushes etc"""
        return self._fire("server event", what=what, who=who, why=why, **kwp)

    def clean_redis(self, email: str):
        return self._fire("clean redis", email=email)

    def api_activity(self, related: Union[str, None] = None, **kwp):
        """Generic api activity, saving whatever arguments as evidence"""
        if related:
            self.relate(related)
        # TODO: extract useful info like is_phone, is_script etc
        # kwp.update(
        #     dict(
        #         # event_id, event_gid, started, endpoint, session_token,
        #         # x_forward_for, umbrella_request_id, origin, _from, referer,
        #         # user_agent, email, is_ourselves, ip_is_hq, is_bot, is_tablet,
        #         # is_pc, is_phone, is_script, client_os
        #     )
        # )
        return self._fire("api-activity", **kwp)

    def login_failed(self, email: str, why: str):
        return self._fire("login-failed", email=email, why=why)

    def login_user(self, hardware: dict, user_gid: str | UUID):
        return self._fire("login-user", hardware=hardware, user_gid=gidstr(user_gid))

    def new_user(self, user_gid, email):
        return self._fire("new-user", gid=gidstr(user_gid), email=email)

    def new_user_failed(self, email, details: dict):
        return self._fire("new-user-failed", email=email, details=details)

    def reset_password(self, email: str = None, user_gid: str | UUID = None):
        return self._fire("reset-password", email=email, user_gid=gidstr(user_gid))

    def reset_password_failed(self, message: str, email: str = None):
        return self._fire("reset-password-failed", email=email, message=message)

    def email_validation_sent(self, user_gid: str | UUID, email: str):
        """Sent by email microservice"""
        return self._fire(
            "email-validation-sent", user_gid=gidstr(user_gid), email=email
        )

    def email_validation_requested(self, user_gid: str | UUID):
        return self._fire("email-validation-requested", user_gid=gidstr(user_gid))

    def email_validated(self, user_gid: str | UUID):
        return self._fire("email-validated", user_gid=gidstr(user_gid))

    def invalid_email_code(self, user_gid: str | UUID):
        return self._fire("invalid-email-code", user_gid=gidstr(user_gid))

    def update_me(self, user_gid: str | UUID):
        return self._fire("update_me", user_gid=gidstr(user_gid))

    def create_item(
        self, item_gid: str | UUID, author_gid: str | UUID, by_eddie_email: str = None
    ):
        return self._fire(
            "create-item",
            gid=gidstr(item_gid),
            author_gid=gidstr(author_gid),
            by_eddie_email=by_eddie_email,
        )

    def update_item(
        self,
        item_gid: str | UUID,
        by_eddie_email: str,
        fields_before: dict,
        fields_after: dict,
    ):
        changes = {}
        for key in fields_before.keys() | fields_after.keys():
            value_before = fields_before.get(key)
            value_after = fields_after.get(key)
            if value_before == value_after:
                # no change
                continue

            if delta := find_difference(value_before, value_after):
                changes[key] = delta

        return self._fire(
            "update-item",
            gid=gidstr(item_gid),
            by_eddie_email=by_eddie_email,
            changes=changes,
        )

    def remove_item(
        self, item_gid: str | UUID, email: str = None, user_gid: str | UUID = None
    ):
        # indien Eddie moet er een email bijstaan
        return self._fire(
            "remove-item",
            gid=gidstr(item_gid),
            by_eddie_email=email,
            user_gid=gidstr(user_gid),
        )

    def read_item(
        self,
        item_gid: str | UUID,
        session_token: UUID | str = None,
        user_gid: UUID | str = None,
    ):
        return self._fire("read-item", gid=gidstr(item_gid), user_gid=gidstr(user_gid))

    def read_user(self, user_gid: str | UUID):
        return self._fire("read-user", gid=gidstr(user_gid))

    def read_organisation(self, org_gid: str | UUID):
        return self._fire("read-organisation", gid=gidstr(org_gid))

    def request_adoption(self, item_gid: str | UUID, new_author_gid: str | UUID):
        # dit gebeurt alleen vanuit de eddie gebruiker
        return self._fire(
            "request-adoption",
            gid=gidstr(item_gid),
            author=gidstr(new_author_gid),
        )

    def accept_adoption(self, item_gid: str | UUID, new_author_gid: str | UUID):
        # dit gebeurt alleen vanuit de eddie gebruiker
        return self._fire(
            "accept-adoption",
            gid=gidstr(item_gid),
            author=gidstr(new_author_gid),
        )

    def send_message(
        self, item_gid: str | UUID, author_gid: str | UUID, message, reason
    ):
        return self._fire(
            "send-message",
            visitor=gidstr(self.user_gid),
            author=gidstr(author_gid),
            message=message,
            from_item=gidstr(item_gid),
            reason=reason,
        )

    def anonymous_claimed(
        self, item_gid: str | UUID, email: str, tel: str, message: str
    ):
        return self._fire(
            "anonymous-claimed",
            visitor=gidstr(self.user_gid),
            item=gidstr(item_gid),
            message=message,
            email=email,
            tel=tel,
        )

    def authenticated_claimed(self, item_gid: str | UUID, message: str):
        return self._fire(
            "authenticated-claimed",
            item=gidstr(item_gid),
            message=message,
        )

    def seen_global_notification(self, user_gid: str | UUID):
        return self._fire("seen-global-notification", user_gid=gidstr(user_gid))

    def seen_user_notifications(
        self, user_gid: str | UUID, notification_gids: List[str | UUID]
    ):
        # TODO: argumenten worden nog niet gebruikt.
        return self._fire("seen-user-notifications", count=count, method=method)

    def new_session_token(self, new_token: str | UUID, hardware: dict):
        return self._fire(
            "new-session-token", session_token=new_token, hardware=hardware
        )

    def download_attachment(
        self,
        attachment_gid: str | UUID,
        from_backend: bool,
        purpose: str = None,
        filename: str = None,
    ):
        return self._fire(
            "download-attachment",
            attachment_gid=gidstr(attachment_gid),
            purpose=purpose,
            filename=filename,
            from_backend=from_backend,
        )

    def upload_attachment(self, attachment_gid: str | UUID):
        return self._fire("upload-attachment", attachment_gid=gidstr(attachment_gid))

    def create_comment(self, subject_gid: str | UUID, comment_gid: str | UUID, comment):
        return self._fire(
            "create-comment",
            subject_gid=gidstr(subject_gid),
            comment_gid=gidstr(comment_gid),
        )

    def read_comment(self, comment_gid: str | UUID):
        return self._fire("read-comment", gid=gidstr(comment_gid))

    def delete_comment(self, comment_gid: str | UUID):
        return self._fire("delete-comment", gid=gidstr(comment_gid))

    def update_comment(self, comment_gid: str | UUID, comment):
        return self._fire("update-comment", gid=gidstr(comment_gid), comment=comment)

    def update_mark(self, subject_gid: str | UUID, mark, mark_type="THUMBS"):
        return self._fire(
            "update-mark", gid=gidstr(subject_gid), mark=mark, mark_type=mark_type
        )

    def new_list(self, list_gid: str | UUID, list_name):
        return self._fire("new-list", list_name=list_name, list_gid=gidstr(list_gid))

    def version(self, version):
        return self._fire("version", version=version)

    def clicked(self, url, source_gid: str | UUID, session_token):
        return self._fire(
            "clicked",
            url=url,
            source_gid=gidstr(source_gid),
            session_token=session_token,
        )

    def search(
        self,
        search: str,
        tags: Union[None, List[List[str]], List[str]],
        author: Union[None, str],
        found_tiles_cnt: int,
        found_tiles_gids: List[str | UUID],
        limit: int,
        offset: int,
        order: str,
        loggedIn: bool,
        include: list[Visibility],
        exclude: list[Visibility],
    ):
        return self._fire(
            "search",
            search=search,
            tags=tags,
            author=author,
            found_tiles_cnt=found_tiles_cnt,
            found_tiles_gids=found_tiles_gids,
            limit=limit,
            offset=offset,
            order=order,
            loggedIn=loggedIn,
            include=include,
            exclude=exclude,
        )
