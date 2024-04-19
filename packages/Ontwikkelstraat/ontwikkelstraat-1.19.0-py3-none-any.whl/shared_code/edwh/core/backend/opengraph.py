import datetime as dt
import json
import typing
from datetime import datetime
from uuid import UUID

import diskcache as dc
from attr import define
from pydal import DAL

from .engine import PLATFORM, DillableAttrsClass


@define(slots=False)
class OpengraphMeta(DillableAttrsClass):
    # internal
    gid: UUID
    updated_at: dt.datetime

    # https://ogp.me
    title: str
    type: str  # article, profile
    description: str
    image_url: typing.Optional[str] = None
    url: typing.Optional[str] = None  # <- filled in by front-end (cmsx)
    # ... extra?


class DiskCacher:
    cache: dc.Index

    def __init__(self, db: DAL):
        self.cache = dc.Index("/shared_cache/opengraph")
        self.db = db

    def update_all(self):
        return [
            self.empty(),
            self.update_all_items(),
            self.update_all_users(),
            self.update_all_organisations(),
        ]

    def empty(self):
        self.cache.clear()

    def _all_items_with_thumbnail(self):
        db = self.db

        query = db.item.platform == PLATFORM
        return db(query).select(
            db.item.gid,
            db.item.name,
            db.item.short_description,
            db.attachment.b2_uri,
            left=db.attachment.on(db.item.thumbnail == db.attachment.gid),
        )

    def _all_users_with_avatar(self):
        db = self.db
        query = db.user.platform.contains(PLATFORM)
        return db(query).select(
            db.user.gid,
            db.user.name,
            db.user.property_bag,
            db.attachment.b2_uri,
            left=db.attachment.on(db.user.avatar == db.attachment.gid),
        )

    def _all_organisations(self):
        db = self.db
        query = db.organisation_effdted_now.platform == PLATFORM
        return db(query).select(
            db.organisation_effdted_now.gid,
            db.organisation_effdted_now.name,
        )

    def update_all_items(self):
        now = datetime.utcnow()
        rows = self._all_items_with_thumbnail()
        for row in rows:
            item = row.item
            attachment = row.attachment
            self.cache[item.gid] = OpengraphMeta(
                gid=item.gid,
                updated_at=now,
                title=item.name,
                description=item.short_description,
                type="article",
                image_url=attachment.b2_uri,
            )

        return len(rows)

    def update_all_users(self):
        now = datetime.utcnow()
        rows = self._all_users_with_avatar()
        for row in rows:
            user = row.user
            attachment = row.attachment

            if user.property_bag:
                description = user.property_bag.get("bio", "")
            else:
                description = ""

            self.cache[user.gid] = OpengraphMeta(
                gid=user.gid,
                updated_at=now,
                title=user.name,
                description=description,
                type="profile",
                image_url=attachment.b2_uri,
            )

        return len(rows)

    def update_all_organisations(self):
        now = datetime.utcnow()
        rows = self._all_organisations()
        for organisation in rows:
            self.cache[organisation.gid] = OpengraphMeta(
                gid=organisation.gid,
                updated_at=now,
                title=organisation.name,
                description=organisation.name,
                type="profile",
            )

        return len(rows)

    def update_by_gid(self, gid: UUID):
        raise NotImplementedError()
