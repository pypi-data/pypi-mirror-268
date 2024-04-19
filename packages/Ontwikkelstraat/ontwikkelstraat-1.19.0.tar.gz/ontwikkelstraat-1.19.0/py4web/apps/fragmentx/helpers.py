import base64
import json
import math
import os
from urllib.parse import quote, unquote

import dotmap
import yarl


def escape(text):
    return quote(text)


def _PY4WEB_URL(*path_parts, **params) -> yarl.URL:
    """
    Internal version of the py4web url helper which returns a yarl URL
    """
    path = "/".join(path_parts)
    if path[0] != "/":
        path = f"/{path}"
    host = "py4web." + os.getenv("HOSTINGDOMAIN", "local")
    return yarl.URL.build(scheme="https", host=host, path=path, query=params)


def PY4WEB_URL(*path_parts, **params) -> str:
    """
    Public version of the py4web url helper, to be used in a YATL template, which returns a string.
    """
    url = _PY4WEB_URL(*path_parts, **params)
    return str(url)


def paginate(tiles):
    # https://gist.github.com/kottenator/9d936eb3e4e3c3e02598
    available, first, offset = tiles.available, tiles.first, tiles.offset
    if not first:
        # prevent ZeroDivisionError
        current = 0
        last = 0
        previous_disabled = "disabled"
        next_disabled = "disabled"
    else:
        current = int(offset / first + 1)
        last = math.ceil(available / first)
        previous_disabled = "" if current - 1 else "disabled"
        next_disabled = "" if current < last else "disabled"

    delta = 2
    left = current - delta
    right = current + delta + 1
    normal_range = []
    range_with_dots = []
    l = 0

    for i in range(1, last + 1):
        if i == 1 or i == last or i >= left and i < right:
            normal_range.append(i)

    for i in normal_range:
        if l:
            if i - l == 2:
                range_with_dots.append(l + 1)
            elif i - l != 1:
                range_with_dots.append("...")

        range_with_dots.append(i)
        l = i

    # end converted JS, start building:

    paginate_string = f"""
    <nav class="pagination is-centered is-rounded" role="navigation" id="tiles-pagination">
  <a style="border:none;" class="pagination-previous" {previous_disabled} onclick="change_page(this, {current - 1})"><svg viewBox="0 0 9.25 15" width="9" height="15" class="Icon_icon__3M72n"><path d="M9.25 1.75L7.5 0 0 7.5 7.5 15l1.75-1.75L3.5 7.5z" fill="#000000" fill-rule="evenodd"></path></svg>&nbsp; Vorige</a>
  <a style="border:none;" class="pagination-next" {next_disabled} onclick="change_page(this, {current + 1})">Volgende &nbsp;<svg viewBox="0 0 9.25 15" width="9" height="15" class="Icon_icon__3M72n"><path d="M0 1.75L1.75 0l7.5 7.5-7.5 7.5L0 13.25 5.75 7.5z" fill="#000000" fill-rule="evenodd"></path></svg></a>
  <ul class="pagination-list">"""

    for i in range_with_dots:
        if i == "...":
            paginate_string += (
                """<li><span class="pagination-ellipsis">&hellip;</span></li>"""
            )
        else:
            c = "is-current" if i == current else ""
            paginate_string += f"""<li><a style="border:none;"  class="pagination-link {c}" onclick="change_page(this, {i})">{i}</a></li>"""

    return paginate_string + "</ul></nav>"


class DotMap(dotmap.DotMap):
    def __str__(self) -> str:
        """
        By default, an empty dotmap is represented as DotMap()
        This is however not useful when filling in forms.
        This class is represented by an empty string if the value is
        not found in the dotmap.

        :return: empty string value
        """
        return ""


def b64decode(string: str) -> dict:
    """
    Custom decoder die web safe base 64 JSON gebruikt
    (vanuit jsonify_details in front-end)
    """
    if not string:
        return {}
    try:
        return json.loads(base64.b64decode(unquote(string)).decode("UTF-8"))
    except Exception:
        return {}
