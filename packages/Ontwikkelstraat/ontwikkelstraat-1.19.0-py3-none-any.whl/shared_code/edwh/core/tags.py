import uuid

import more_itertools
import slugify
from pydal import DAL
from pydal.objects import Row

# class refresh_tag(ContextDecorator):
#     def __init__(self, db):
#         self.db = db
#
#     def __enter__(self):
#         if Tag.db is None or Tag.db._adapter.connection != self.db._adapter.connection:
#             print("Refreshing tags...")
#             Tag.refresh(self.db)
#         return self
#
#     def __exit__(self, *exc):
#         if exc[0] is None:
#             print('commit "refresh_tag"', self.db._uri)
#             self.db.commit()


class Tag:
    parents: list[str]
    meta_tags: list[str]
    related: list[str]
    children: list[str]
    name: str
    gid: str

    def __init__(self, db: DAL, source: Row | uuid.UUID | str | int):
        # row could be a string
        if type(source) is str:
            if _row := db.tag(gid=source):
                source = _row
            else:
                rows = db(db.tag.name == source).select()
                if len(rows) != 1:
                    slugified = slugify.slugify(source)
                    rows = db(db.tag.slug == slugified).select()
                if len(rows) != 1:
                    raise KeyError(
                        f"Unknown or ambiguous tag gid,name or slug: {source}"
                    )
                source = rows[0]
        if type(source) is int:
            # use integers as reference to id field in db.tag
            source = db.tag(source)
        self.parents = source.parents or []
        self.meta_tags = source.meta_tags or []
        self.related = source.related or []
        self.children = source.children or []
        self.name = source.name
        self.gid = source.gid

    @classmethod
    def new(
        cls,
        db: DAL,
        name: str,
        description: str,
        *,
        slug: str = "",
        gid: str | uuid.UUID | None = None,
        parents: list["Tag | str"] = None,
        children: list["Tag | str"] = None,
        meta_tags: list["Tag | str"] = None,
    ):
        if parents is None:
            parents = []
        if children is None:
            children = []
        if meta_tags is None:
            meta_tags = []
        # parse slug, raise error if not unique
        slug = slug or slugify.slugify(name)
        if db(db.tag.slug == slug).count() > 0:
            raise ValueError(f"Slug `{slug}` already used.")
        # come up with a new guid
        gid = str(gid) if gid else uuid.uuid4()
        # insert new value in database
        _id = db.tag.insert(
            platform=None,  # not in use atm
            gid=gid,
            name=name,
            slug=slug,
            parents=[getattr(_, "gid", _) for _ in parents],
            description=description,
            meta_tags=[getattr(_, "gid", _) for _ in meta_tags],
            children=[getattr(_, "gid", _) for _ in children],
        )
        # read the row, create a new Tag
        tag = Tag(db, _id)
        # edit all parents to register this new child
        for parent in parents:
            parent.add_child(db, tag)
        # return the Tag
        return tag

    def __repr__(self):
        return f"<Tag {self.gid} '{self.name}'>"

    def parents(self, db: DAL):
        return [Tag(db, _) for _ in self.parents]

    def children(self, db: DAL):
        return [Tag(db, _) for _ in self.children or []]

    def children_by_parental_reference(self, db: DAL):
        return [
            Tag(db, _.gid)
            for _ in db(db.tag.parents.contains(self.gid)).select(db.tag.gid)
        ]

    def metatags(self, db: DAL):
        return [Tag(db, _) for _ in self.meta_tags]

    def tagged_with(self, db):
        return [
            Tag(db, _.gid)
            for _ in db(db.tag.meta_tags.contains(self.gid)).select(db.tag.gid)
        ]

    def save_reordered(self, db: DAL, relation: str, new_order: list["Tag | str"]):
        db(db.tag.gid == self.gid).update(
            **{relation: [getattr(_, "gid", _) for _ in new_order]}
        )

    def add_metatag(self, db: DAL, meta_tag: "Tag"):
        return self.add_abstract_relation(db, meta_tag, "meta_tags")

    def add_child(self, db: DAL, child: "Tag"):
        return self.add_abstract_relation(db, child, "children", "parents")

    def add_related(self, db: DAL, other: "Tag"):
        return self.add_abstract_relation(db, other, "related", "related")

    def add_parent(self, db: DAL, parent: "Tag"):
        return self.add_abstract_relation(db, parent, "parents", "children")

    def remove_metatag(self, db: DAL, meta_tag: "Tag"):
        return self.remove_abstract_relation(db, meta_tag, "meta_tags")

    def remove_child(self, db: DAL, child: "Tag"):
        return self.remove_abstract_relation(db, child, "children", "parents")

    def remove_related(self, db: DAL, other: "Tag"):
        return self.remove_abstract_relation(db, other, "related", "related")

    def remove_parent(self, db: DAL, parent: "Tag"):
        return self.remove_abstract_relation(db, parent, "parents", "children")

    def remove_abstract_relation(
        self,
        db: DAL,
        other: "Tag",
        relation: str = "related",
        reverse_relation: str = None,
    ):
        """Removes a relation between two tags.

        A relation is defined as a tag having a list of other tag gids.
        For example children or parents. These should exist as a field in the Tag table.

        For most relations there is a reverse relation field:
         * children have parents and vice versa.
         * related has related
         * meta_tags doesn't have this. It's a one way relationship.

        When a reverse relation is given, the other tag will also be updated with the
        relation. This is done to make sure the relation is always in sync.

        Returns True if the relation was removed, False if it didn't exist.
        """
        related_gids = getattr(self, relation)
        if other.gid not in related_gids:
            return False

        db(db.tag.gid == self.gid).update(
            **{relation: [gid for gid in related_gids if gid != other.gid]}
        )
        # make sure the parent is registered as such in the child
        if reverse_relation:
            reverse_related_gids = getattr(other, reverse_relation)
            db(db.tag.gid == other.gid).update(
                **{
                    reverse_relation: [
                        gid for gid in reverse_related_gids if gid != self.gid
                    ]
                }
            )
        return True

    def add_abstract_relation(
        self,
        db: DAL,
        other: "Tag",
        relation: str = "related",
        reverse_relation: str = None,
    ):
        """Adds a relation between two tags.

        A relation is defined as a tag having a list of other tag gids.
        For example children or parents. These should exist as a field in the Tag table.

        For most relations there is a reverse relation field:
         * children have parents and vice versa.
         * related has related
         * meta_tags doesn't have this. It's a one way relationship.

        When a reverse relation is given, the other tag will also be updated with the
        relation. This is done to make sure the relation is always in sync.

        Returns True if the relation was added, False if it already existed.
        """
        related_gids = getattr(self, relation)
        if other.gid in related_gids:
            return False

        # print(f"Set {self.name}'s {relation} with {related_gids + [other.gid]}")
        db(db.tag.gid == self.gid).update(**{relation: related_gids + [other.gid]})
        # make sure the parent is registered as such in the child
        if reverse_relation:
            reverse_related_gids = getattr(other, reverse_relation)
            if self.gid not in reverse_related_gids:
                db(db.tag.gid == other.gid).update(
                    **{reverse_relation: reverse_related_gids + [self.gid]}
                )
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

    @classmethod
    def used_meta_tags(cls, db: DAL) -> dict[str, "Tag"]:
        used_meta_tags = set(
            more_itertools.flatten(
                (row.meta_tags for row in db.tag().select(db.tag.meta_tags))
            )
        )
        used_meta_tags = {_: Tag(db, _) for _ in used_meta_tags}
        return used_meta_tags

    @classmethod
    def create_Tnamed_metatag_variables(cls, db: DAL, scope: dict):
        "Execute with Tag.create_Tnamed_tag_variables(locals()) to access TSystem etc"
        for meta_tag in cls.used_meta_tags(db).values():
            scope[f'T{meta_tag.name.capitalize().replace(" ", "_")}'] = meta_tag

    @classmethod
    def find_by_meta_tag(cls, db: DAL, meta_tag: "Tag"):
        return [
            Tag(db, _.gid)
            for _ in db(db.tag.meta_tag.contains(meta_tag.gid)).select(db.tag.gid)
        ]

    @classmethod
    def search(cls, db: DAL, q) -> list[str]:
        query = db.tag.name.contains(q)
        query |= db.tag.slug.contains(q)
        query |= db.tag.description.contains(q)
        query |= db.tag.akas.contains(q)
        query |= db.tag.search_hints.contains(q)
        query &= db.tag.deprecated == False
        return [row.gid for row in db(query).select(db.tag.gid)]


def names(iterable):
    return [getattr(_, "name", _) for _ in iterable]


# def find_out_of_sync_parent_child_relationships():
#     """Maintenace function to print the out of sync parent-child relationships."""
#     for row in Tag.all_tag_rows:
#         direct_child_names = sorted(names(Tag(row).children()))
#         derived_child_names = sorted(names(Tag(row).children_by_parental_reference()))
#         if direct_child_names != derived_child_names:
#             print(row.gid, row.name, direct_child_names, "!=", derived_child_names)
#             print(
#                 "  ",
#                 "missing children:",
#                 set(derived_child_names) - set(direct_child_names),
#             )
#             print(
#                 "  ",
#                 "superfluous children:",
#                 set(direct_child_names) - set(derived_child_names),
#             )
#             print()


def _print(tag, parent, depth):
    if tag == parent:
        return False
    print("   " * depth, tag.name, names(tag.metatags()))
    if tag.name == "User generated tags":
        print("   " * (depth + 1), " *** hidden ***")
    return tag.name != "User generated tags"


def init_tag_functionality(db):
    Tag.create_Tnamed_metatag_variables(db, locals())

    # they are now available as regular items in the python_environment

    TSystem = Tag(db, "19682a99-50a3-4fc0-bb67-e0f6eff5da55")
    TItem = Tag(db, "fc8a7d36-e23e-4aba-8ee9-f5269ecc8dfc")
    TUIRelated = Tag(db, "801d584c-d380-4a1d-95d5-c1c85aec89da")
    is_user_selectable = Tag(db, "dcaea9b5-879e-43f7-8860-67579e10166e")
    TStickers = Tag(db, "67ba8cd8-b564-4cb4-b1bc-10364c5edf16")
    TFilter = Tag(db, "8b78e33d-c4ab-442e-aaf6-411fda089b03")
    filter_tags = dict(
        [
            (t.name, [Tag(db, _) for _ in t.children])
            for t in Tag.find_by_meta_tag(db, TFilter)
        ]
    )
