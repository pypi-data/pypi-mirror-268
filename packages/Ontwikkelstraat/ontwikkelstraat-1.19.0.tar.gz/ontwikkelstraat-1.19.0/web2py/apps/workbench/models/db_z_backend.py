import binascii
import os
import typing
from uuid import UUID

import edwh.core.applog.signalemitter
from edwh.core.applog import tasks
from edwh.core.applog.diskcachesink import DequeSink
from edwh.core.backend import (
    Backend,
    Item,
    ItemSearchResult,
    SortOrder,
    User,
    Validated,
)
from edwh.core.data_model import Visibility

if typing.TYPE_CHECKING:
    from edwh.core.backend import Backend, Validated

SignalEmitter = edwh.core.applog.signalemitter.SignalEmitter


app_id = os.getenvb(b"WEB2PY_APPLOG_ID")
app_key = binascii.unhexlify(os.getenvb(b"WEB2PY_APPLOG_KEY"))
# /!\ autocommit is false, so the server MUST .commit AFTER the response is written to the socket, if possible.
sink = DequeSink(
    tasks.process_applog_batch,
    app_id,
    app_key,
    autocommit=True,
)


class Web2pyBackend(Backend):
    @property
    def token(self):
        return session.get(BACKEND_SESSION_TOKEN, None)

    @property
    def eddie_token(self):
        return session.get(EDDIE_TOKEN, None)

    @property
    def me(self):
        return session[BACKEND_ME]

    @property
    def is_registered_user(self):
        return session[BACKEND_ME] is not None

    @property
    def is_anonymous(self):
        return session[BACKEND_ME] is None

    def login(
        self,
        email: str,
        hardware: dict,
        password: str | None = None,
        password_hash: str | None = None,
    ) -> Validated:
        resp = super().login(email, hardware, password, password_hash)
        if resp.ok:
            print("User creds opgeslagen in  in session")
            # session[BACKEND_SESSION_TOKEN] = resp.token
            session[BACKEND_ME] = resp.user
        return resp

    def pratices(
        self,
        search: str | None = None,
        first: int | None = 9,
        offset: int = 0,
        with_tags: list[list[UUID] | UUID] | None = None,
        search_in: list[UUID] | None = None,
        author: UUID | None = None,
        order: SortOrder | None = None,
        included: list[Visibility] | None = None,
        excluded: list[Visibility] | None = None,
    ) -> ItemSearchResult:
        """Vraagt items op via de GraphQL backend.

        :param limit: hoeveel items er maximaal opgevraagd mogen worden.
        :param offset: offset
        :param order: op volgorde van... RANDOM, RECENT_ASC  RECENT_DESC, POPULARITY_ASC, POPULARITY_DESC, VIEWS_ASC,
                                        VIEWS_DESC, THUMBS_ASC THUMBS_DESC
        :return: JSON response van items.
        """
        search_result = self.search_items(
            me=self.me,
            with_tags=with_tags,
            order=order,
            first=first,
            offset=offset,
            search=search,
            search_in=search_in or ["tag", "name", "description", "author"],
            author=author,
            included_visibilities=included,
            excluded_visibilities=excluded,
        )
        item_search_result = ItemSearchResult(
            available=search_result.available,
            found=[Item.load(self.db, gid) for gid in search_result.found],
        )
        return item_search_result


backend = Web2pyBackend(
    database,
    sink=sink,
    applog=SignalEmitter(
        signal_processor=sink,
        signal_source="web2py.front_end",
        session_gid=None,
        user_gid=None,
        timestamp=datetime.datetime.now(),
        origin_domain=os.getenv("HOSTINGDOMAIN"),
    ),
)


def is_authorized_to_edit(item_gid: str | UUID, me: User) -> bool:
    """Valideert of de huidige backend.me gebruiker een
    item aan mag passen.

    :return: boolean. geeft aan of de gebruiker een item aan mag passen.
    """
    item = backend.item(id=item_gid)
    return me.may_edit(item)


def upload_attachments(rows: list) -> list:
    """Upload attachments via backend.upload_attachment

    :param rows: source_file rows.
    :return: lijst met gids van geüploade attachments.
    """
    if not rows:
        return rows

    gids = []
    for row in rows:
        if not row.gid:
            # als een attachment geen gid heeft, dan houdt dat in dat deze nog niet geupload is naar b2.
            # dus gaan we deze uploaden via de GraphQL.
            file_path = os.path.join(request.folder, "uploads", row.attachment)

            # bestand openen en encode naar base64.
            with open(file_path, "rb") as f:
                content = base64.b64encode(f.read())
            # omdat de attachment uploader geen bytes ondersteund converteren
            # we de content naar UTF-8.
            content = content.decode("utf-8")

            gid = backend.upload_attachment(
                filename=row.name, content=content, purpose="ATTACHMENT"
            )
            # source_file row updaten met de gid die uit de backend komt.
            row.update(gid=gid)
            # voor de zekerheid opslaan.
            row.update_record()
        else:
            gid = row.gid

        gids.append(gid)

    return gids
