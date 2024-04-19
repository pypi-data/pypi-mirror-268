import json
import typing

import yatl
from pydal.objects import Query, Rows

if typing.TYPE_CHECKING:
    from gluon import HTTP, request
    from pydal import DAL
    from yatl import *

    from ..models.db import auth, database, is_eddie

db = database


def colored(content, color):
    return SPAN(content, _style=f"color: {color}")


def add_color(value: str):
    if value.startswith("-"):
        return colored(value, "red")
    elif value.startswith("+"):
        return colored(value, "green")
    else:
        return colored(value, "#CC7722")


def format_diff(values):
    if isinstance(values, str):
        return add_color(values)
    if isinstance(values, list):
        values = [str(add_color(_)) for _ in values]
        return XML("<br/>".join(values))
    # else: ???
    return str(values)


paginate_yatl = """
    {{if prev:}}
    <a class="btn btn-link" href="{{=URL(args=request.args, vars=request.vars | {'page': prev})}}">
        &larr; Pagina {{=prev}}
    </a>
    {{pass}}

    {{if next:}}
    <a class="btn btn-link" href="{{=URL(args=request.args, vars=request.vars | {'page': next})}}">
        Pagina {{=next}} &rarr;
    </a>
    {{pass}}
"""


def _paginate(db: DAL, query: Query | bool, default_limit: int = 50):
    page = int(request.vars.get("page", 1))
    limit = int(request.vars.get("limit", default_limit))

    limitby = ((page - 1) * limit, page * limit)

    count = db(query).count()

    has_next_page = page * limit < count

    pag = {
        "count": count,
        "prev": page - 1 if page > 1 else False,
        "next": page + 1 if has_next_page else False,
    }

    return limitby, pag | {
        "render_paginate": lambda: XML(
            yatl.render(paginate_yatl, context=pag | locals() | globals())
        )
    }


@auth.requires(is_eddie)
def index():
    # index shows recent changes
    table = database.vw_item_applog

    query = table.item_gid != None
    # query &= table.log_action != "read-item"

    limitby, paginate = _paginate(database, query)

    changes = database(query).select(limitby=limitby, orderby=~table.signal_ts)

    items = (
        database(database.item.gid.belongs(set(changes.column("item_gid"))))
        .select(database.item.gid, database.item.name)
        .as_dict("gid")
    )

    return {
        "changes": changes,
        "items": items,
        "format_diff": format_diff,
    } | paginate


# def _get_read_count(gid: str) -> int:
#     table = database.vw_item_applog
#     query = table.item_gid == gid
#     query &= table.log_action == "read-item"
#     return database(query).count()
#
#
# def get_read_count(gid: str) -> int:
#     import time
#     before = time.time()
#     read_count = _get_read_count(gid)
#     print(f"Item was read {read_count} times; Query took {time.time() - before:.4f} sec.")
#     return read_count
#
#
# @auth.requires(is_eddie)
# def most_read():
#     table = database.vw_item_applog
#     top_count = 10  # Change this variable to retrieve a different number of top items
#
#     # Query to find the top 'top_count' most read items
#     query = (
#         (table.log_action == 'read-item')
#         & (table.item_gid != None)  # Ensure item_gid is not null
#     )
#
#     count_field = table.item_gid.count()
#     # Group by item_gid, count occurrences, and select top 'top_count' items
#     top_items = database(query).select(
#         table.item_gid,
#         count_field,
#         groupby=table.item_gid,
#         orderby=~count_field,
#         limitby=(0, top_count)  # Limit the result to top 'top_count' items
#     )
#
#     return json.dumps({_['vw_item_applog']['item_gid']: _[count_field] for _ in top_items}, indent=2)


def resolve_tag_gids(tag_changes: list[str]) -> dict[str, str]:
    """
    Find tag slug for every gid in tag_changes.
    """
    tag_changes = [_.removeprefix("-").removeprefix("+") for _ in tag_changes]

    return {
        _.gid: _.slug
        for _ in db(db.tag.gid.belongs(tag_changes)).select(db.tag.gid, db.tag.slug)
    }


def resolve_author_gids(author_changes: list[str]) -> dict[str, str]:
    """
    Find username (email without @) for every gid in author_changes.
    """
    author_changes = [_.removeprefix("-").removeprefix("+") for _ in author_changes]

    return {
        _.gid: _.email.split("@")[0]
        for _ in db(db.user.gid.belongs(author_changes)).select(
            db.user.id, db.user.gid, db.user.email
        )
    }


Resolver: typing.TypeAlias = typing.Callable[[list[str]], dict[str, str]]

gid_resolvers: dict[str, Resolver] = {
    "tags": resolve_tag_gids,
    "author": resolve_author_gids,
}


def resolve_gids(history: Rows):
    """
    Look up human-readable labels for some gids (see supported types in 'gid_resolvers' above)

    Returns a dict of {gid: value} for every gid found.
    """
    to_resolve = {k: [] for k in gid_resolvers}
    for row in history:
        if not row.changes:
            continue

        for key, value in row.changes.items():
            if key in gid_resolvers:
                if isinstance(value, list):
                    to_resolve[key].extend(value)
                else:
                    to_resolve[key].append(value)

    result = {}
    for category, values in to_resolve.items():
        resolver = gid_resolvers[category]

        result |= resolver(values)

    return result


def diff_formatter_with_labels(history):
    """
    Takes 'history' as input, which is a Pydal Rows object of 'table.vw_item_applog'

    Returns a callable (yatl helper), which works as a replacement for 'format_diff'
    """
    gid_labels = resolve_gids(history)

    def gid_to_label(value: str) -> str:
        prefix = value[0]
        gid = value[1:]
        if label := gid_labels.get(gid):
            return f"{prefix}{label} ({gid})"
        else:
            return value

    def gids_to_labels(gids: list[str]) -> list[str]:
        return [gid_to_label(_) for _ in gids]

    def _format_diff(values):
        return format_diff(gids_to_labels(values))

    return _format_diff


@auth.requires(is_eddie)
def item():
    table = database.vw_item_applog

    if not request.args:
        raise HTTP(400, "Missing item gid")
    item_gid = request.args[0]

    query = table.item_gid == item_gid
    log_actions = {"create-item", "update-item", "remove-item"}
    if request.vars.full == "1":
        log_actions.add("read-item")

    query &= table.log_action.belongs(log_actions)

    limitby, paginate = _paginate(database, query)

    history = database(query).select(orderby=~table.signal_ts, limitby=limitby)

    item_info = (
        database(database.item.gid == item_gid)
        .select(database.item.gid, database.item.name)
        .first()
    )

    # read_count = get_read_count(item_gid)

    return {
        "item": item_info,
        "timeline": history,
        # helpers:
        "format_diff": diff_formatter_with_labels(history),
    } | paginate


@auth.requires(is_eddie)
def author():
    table = database.vw_item_applog

    if not request.args:
        raise HTTP(400, "Missing author email")
    author_email = request.args[0]
    if "@" not in author_email:
        author_email = f"{author_email}@educationwarehouse.nl"

    query = table.by_eddie_email == author_email

    limitby, paginate = _paginate(database, query)

    their_changes = database(query).select(orderby=~table.signal_ts, limitby=limitby)

    item_gids = set(their_changes.column("item_gid"))

    items = (
        database(database.item.gid.belongs(item_gids))
        .select(database.item.gid, database.item.name)
        .as_dict("gid")
    )

    return {
        "author_email": author_email,
        "items": items,
        "changes": their_changes,
        "format_diff": diff_formatter_with_labels(their_changes),
    } | paginate


# def utcnow():
#     now = datetime.utcnow()
#     return now.replace(tzinfo=timezone.utc)

# def last_refreshed():
#     import humanize
#     humanize.i18n.activate("nl_NL")
#
#     resp = database.executesql("SELECT * FROM materialized_views WHERE mview = 'public.mv__vw_item_applog'")
#     if not resp:
#         return "?"
#
#     timestamp = resp[0][1]
#     delta = utcnow() - timestamp
#
#     if delta < timedelta(seconds=1):
#         return "Zojuist"
#     else:
#         return humanize.naturaldelta(delta) + " geleden"
#
#
# def refresh():
#     database.executesql(
#         """
#     REFRESH MATERIALIZED VIEW mv__vw_item_applog;
#     """
#     )
#
#     return "Bijgewerkt! <script>location.reload()</script>"
