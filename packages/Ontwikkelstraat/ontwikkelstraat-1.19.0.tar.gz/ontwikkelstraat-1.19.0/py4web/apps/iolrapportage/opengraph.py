import typing
from uuid import UUID

import diskcache as dc
from bs4 import BeautifulSoup
from edwh.core.backend.opengraph import OpengraphMeta
from markdown2 import markdown
from yatl import XML

from py4web import URL, request

opengraph_cache = dc.Index("/shared_cache/opengraph")


def get_metadata(gid: UUID | str) -> OpengraphMeta:
    return opengraph_cache.get(gid)


def _remove_markdown(md_string: str) -> str:
    html = markdown(md_string)
    soup = BeautifulSoup(html)
    # todo: limit: e.g. textwrap.shorten(text, width=length, placeholder="...")
    return soup.get_text()


def format_metadata(og: OpengraphMeta) -> typing.Optional[XML]:
    if not og:
        return None
    else:
        url = request.url
        description = _remove_markdown(og.description) if og.description else ""
        image = og.image_url or URL("static/images/logo.png")
        return XML(
            f"""
  <meta property="og:url" content="{url}">
  <meta property="og:type" content="{og.type}">
  <meta property="og:title" content="{og.title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{image}">
"""
        )


def get_and_format_metadata(gid: UUID | str) -> XML:
    return format_metadata(get_metadata(gid))
