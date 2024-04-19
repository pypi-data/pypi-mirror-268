import math
import sys
import urllib.parse
from urllib.parse import quote

from py4web import request


def escape(text):
    return quote(text)


def paginate(tiles):
    # https://gist.github.com/kottenator/9d936eb3e4e3c3e02598
    available, first, offset = tiles.available, tiles.first, tiles.offset
    current = int(offset / first + 1)
    last = math.ceil(available / first)
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

    previous_disabled = "" if current - 1 else "disabled"
    next_disabled = "" if current < last else "disabled"
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


def BetterURL(
    *parts,
    vars=None,
    hash=None,
    scheme=False,
    signer=None,
    use_appname=None,
    static_version=None,
    domain=None,
):
    """
    Like that of py4web but better!

    Examples:
    URL('a','b',vars=dict(x=1),hash='y')       -> /{script_name?}/{app_name?}/a/b?x=1#y
    URL('a','b',vars=dict(x=1),scheme=None)    -> //{domain}/{script_name?}/{app_name?}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme=True)    -> http://{domain}/{script_name?}/{app_name?}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme='https') -> https://{domain}/{script_name?}/{app_name?}/a/b?x=1
    URL('a','b',vars=dict(x=1),use_appname=False) -> /{script_name?}/a/b?x=1
    """
    if use_appname is None:
        # force use_appname on domain-unmapped apps
        use_appname = not request.environ.get("HTTP_X_PY4WEB_APPNAME")
    if use_appname:
        # app_name is not set by py4web shell
        app_name = getattr(request, "app_name", None)
    has_appname = use_appname and app_name
    script_name = (
        request.environ.get("SCRIPT_NAME", "")
        or request.environ.get("HTTP_X_SCRIPT_NAME", "")
    ).rstrip("/")
    if parts and parts[0].startswith("/"):
        prefix = ""
    elif has_appname and app_name != "_default":
        prefix = "%s/%s/" % (script_name, app_name)
    else:
        prefix = "%s/" % script_name
    broken_parts = []
    for part in parts:
        broken_parts += str(part).rstrip("/").split("/")
    if static_version != "" and broken_parts and broken_parts[0] == "static":
        if not static_version:
            # try to retrieve from __init__.py
            app_module = "apps.%s" % app_name if has_appname else "apps"
            try:
                static_version = getattr(
                    sys.modules[app_module], "__static_version__", None
                )
            except KeyError:
                static_version = None
        if static_version:
            broken_parts.insert(1, "_" + static_version)

    url = prefix + "/".join(map(urllib.parse.quote, broken_parts))
    # Signs the URL if required.  Copy vars into urlvars not to modify it.
    urlvars = dict(vars) if vars else {}
    if signer:
        # Note that we need to sign the non-urlencoded URL, since
        # at verification time, it will be already URLdecoded.
        signer.sign(prefix + "/".join(broken_parts), urlvars)
    if urlvars:
        url += "?" + "&".join(
            "%s=%s" % (k, urllib.parse.quote(str(v))) for k, v in urlvars.items()
        )
    if hash:
        url += "#%s" % hash
    if scheme is not False or domain is not None:
        original_url = request.environ.get("HTTP_ORIGIN") or request.url
        orig_scheme, _, new_domain = original_url.split("/", 3)[:3]

        domain = domain or new_domain

        if scheme is True:
            scheme = orig_scheme
        elif scheme is None:
            scheme = ""
        else:
            scheme += ":"
        url = "%s//%s%s" % (scheme, domain, url)
    return url


def ServerURL(*a, **kw):
    """
    Generate an url with the domain of this server:
    """
    return BetterURL(*a, **kw, domain=request.urlparts.netloc)
