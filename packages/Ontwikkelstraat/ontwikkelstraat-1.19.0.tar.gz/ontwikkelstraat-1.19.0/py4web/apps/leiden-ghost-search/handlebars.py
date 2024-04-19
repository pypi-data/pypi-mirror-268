"""
Handlebars exposes [pybars](https://pypi.org/project/pybars4/) as a
Fixture for use with (py4web)[https://www.py4web.com].

The Handlebars class is based on the Template fixture, mimicing it's behaviour.
For example, it will cache the compiled template but invalidate the cache on a changed mdate of the template file.

Example:
    # create a partials dictionary.
    # each of these precompiled partials can be reused over and over
    # and set as globals for each Handlebars fixture decorated controller functions.
    #
    partials = dict(
        page_header=Handlebars.precompile(
            "templates/page_header.hbs", relative_to_folder_of=__file__
        )
    )

    # Add any special (block) helpers
    # Here's an example from one of the tests.
    def _list(this, options, items):
        result = [u"<ul>"]
        for thing in items:
            result.append(u"<li>")
            result.extend(options["fn"](thing))
            result.append(u"</li>")
        result.append(u"</ul>")
        return result

    # partials and helpers are optional but show the strength of these globally defined
    # helper functions.

    @action("handlebars_demo")
    @action.uses(Handlebars("demo.hbs", partials=partials, helpers=dict(list=_list)))
    def handlebars_demo():

        # you can of course define locally available helpers, that's up to you
        # helpers = {"list": _list}

        # Add partials based on string literals directly.
        header = Handlebars.compiler.compile(
            u"<h2>People</h2> <div>header this: {{this}} </div>"
        )
        partials = {"this_page_header": header}

        # Render the template with the given context. Helpers and partials are optional
        # and added on top of the global helpers and partials assigned in the decorator above.
        # You can override global names locally.
        # Mind you to explicitly set the 'context' key.
        return dict(
            context={
                "people": [
                    {"firstName": "Pietje", "lastName": "Katz"},
                    {"firstName": "Carl", "lastName": "Lerche"},
                    {"firstName": "Alan", "lastName": "Johnson"},
                ]
            },
            # helpers=helpers,
            partials=partials,
        )

Template used:
    templates/page_header.hbs:

    <h1>Page header</h1>

    templates/demo.hbs:
    {{>page_header}}
    {{>this_page_header}}
    {{this}}
    {{#list people}}
        {{lastName}}/{{firstName}}
    {{/list}}

"""
__author__ = "Remco Boerma, Robin van der Noord"
__version__ = "1.5.0"

## 1.5.0: added 'dehtml' helper to strip HTML from some text
## 1.4.5: added prefix version from edwh header
## 1.4.4: added first version of EDWH URL helper that simply prefixes the URL with /front_end/
## 1.4.3: made pagination logic better, based on JS example
## 1.4.2: fix for pagination: disabled should not be clickable!
## 1.4.1: small pagination improvements
## 1.4.0: added pagination helper, to build bulma pagination
## 1.3.0: added escape helper, to urlencode a string
## 1.2.1: fixed that precompile could not find the templates folder
## 1.2.0: to facilitate .hbs extending templates, and have template changes recognized, cache uses
##        the max age of any file in the templates folder.
## 1.1.0: json helper added
## 1.0.2: fixed precompile, removed _title helper
## 1.0.1: reapplied yatl templating
## 0.2.0: added helpers
## 0.1.0: added yatl
## 0.0.1: initial version

import glob
import json
import math
import os
import re
from typing import AnyStr, Callable, Dict, Optional, Union

import pybars
import yatl
from ycecream import y

import py4web
from py4web import URL, Flash, request

y.configure(enabled=os.getenv("ENABLE_ICECREAM"))

### HELPERS ##############
### HELPERS ##############
### HELPERS ##############


# demo url helper
# used like :
#     <ajax-component id="demo_component" url="{{URL 'component' 'bla' }}">
#     </ajax-component>
# or
#     <!-- You've gotta have utils.js -->
#     <script src="{{URL 'static/js/utils.js'}}"></script>
#
def URL_helper(
    this,
    *parts,
    vars=None,
    hash=None,
    scheme=False,
    signer=None,
    use_appname=None,
    static_version=None,
):
    """
    Vars werkt niet vanaf pybars, in zoverre dat je al een dictikonary moet hebben, want die is niet aan te maken in handlebars.

    Examples:
    URL('a','b',vars=dict(x=1),hash='y')       -> /{script_name?}/{app_name}/a/b?x=1#y
    URL('a','b',vars=dict(x=1),scheme=None)    -> //{domain}/{script_name?}/{app_name}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme=True)    -> http://{domain}/{script_name?}/{app_name}/a/b?x=1
    URL('a','b',vars=dict(x=1),scheme='https') -> https://{domain}/{script_name?}/{app_name}/a/b?x=1
    URL('a','b',vars=dict(x=1),use_appname=False) -> /{script_name?}/a/b?x=1
    """
    return pybars.strlist(
        [
            URL(
                *parts,
                vars=vars,
                hash=hash,
                scheme=scheme,
                signer=signer,
                use_appname=use_appname,
                static_version=static_version,
            )
        ]
    )


def EDWH_URL_helper(this, *parts, **kwargs):
    # te gebruiken in de front_end app

    return os.path.join(request.json["FRONT_END_BASE"], *parts)

    # todo: moeten we nou nog iets met die X-EDWH-VER header?? vast.

    # EDWH_URL: prefixed with version (if using path e.g. /0.9/front_end)
    if prefix := request.headers.get("X-EDWH-VER", ""):
        prefix = f"/{prefix}"

    # prefix can't be inserted into the URL helper, since this want an app
    # as first argument. We always use front_end for this.
    return prefix + str(URL_helper("front_end", *parts, **kwargs))


def FRONT_END_URL_helper(this, *parts):
    # alleen voor development, te gebruiken in de /ghost app

    # standaard voor development: zelfde URL
    return os.path.join("/front_end", *parts)


# demo list helper, used
# {{#list people}}
#   {{lastName}} / {{firstName}}: {{this}}
# {{/list}}
def _list(this, options, items):
    result = ["<ul>"]
    for thing in items:
        result.append("<li>")
        result.extend(options["fn"](thing))
        result.append("</li>")
    result.append("</ul>")
    return result


def _flash(this):
    flash_data = json.dumps(getattr(Flash.local, "flash", None))
    if flash_data:
        return pybars.strlist(
            [f"""<flash-alerts class="" data-alert='{flash_data}'></flash-alerts>"""]
        )
    else:
        return pybars.strlist()


def _concat(this, *parts):
    # print(parts)
    return pybars.strlist([str(_) for _ in parts])


def _json(this, object):
    return pybars.strlist([json.dumps(object, indent=4)])


def _dict(this, *list_of_double_values):
    args = []
    list_of_double_values = list(list_of_double_values)
    while list_of_double_values:
        a, b = list_of_double_values.pop(0), list_of_double_values.pop(0)
        args.append((a, b))
    return dict(list_of_double_values)


from urllib.parse import quote


def _escape(this, text):
    return quote(text)


def _paginate(this, available, first, offset):
    # https://gist.github.com/kottenator/9d936eb3e4e3c3e02598
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


def _html_strip(this, text):
    return re.sub("<[^<]+?>", "", text)


handlebars_helpers = {
    "list": _list,
    "URL": URL_helper,
    "EDWH_URL": EDWH_URL_helper,
    "FRONT_END_URL": FRONT_END_URL_helper,
    "flash": _flash,
    "concat": _concat,
    "dict": _dict,
    "json": _json,
    "escape": _escape,
    "paginate": _paginate,
    "dehtml": _html_strip,
}


### MAIN HANDLEBARS ############
### MAIN HANDLEBARS ############
### MAIN HANDLEBARS ############


class Handlebars(py4web.core.Template):
    compiler = pybars.Compiler()

    def __init__(
        self,
        filename: Union[str, None],
        path: str = None,
        global_context: dict = None,
        helpers: dict = None,
        partials: dict = None,
        yatl_context: dict = None,
    ):
        # path can point to a folder where the .hbs files are located.
        # defaults to $PY4WEB_APPS_FOLDER/<request.app_name>/templates
        super().__init__(filename, path)
        self.helpers = helpers or {}
        self.partials = partials or {}
        self.global_context = global_context or {}
        self.yatl_context = yatl_context or {}

    def reader(self, filename: AnyStr, path: AnyStr) -> Callable[..., AnyStr]:
        """Cached compiled file reader, only reads template if it has changed"""

        def raw_read():
            with open(filename, encoding="utf8") as stream:
                yatl_prepared = yatl.render(
                    stream=stream,
                    filename=filename,
                    context=self.yatl_context,
                    path=path,
                    delimiters="[[ ]]",
                )
                return Handlebars.compiler.compile(yatl_prepared)

        # SPEEDUP: when no longer required, the os.path.getmtime should be disabled
        # to avoid disk reads.
        return Handlebars.cache.get(
            filename,
            raw_read,
            expiration=1,
            monitor=lambda: max(
                [
                    os.path.getmtime(fn)
                    for fn in glob.glob(os.path.join(path, "**"), recursive=True)
                ]
            ),
        )

    def precompile(self, filename, templates_abs_path=None) -> Callable[..., AnyStr]:
        """Compile filename using self.reader(filename).
        If filename doesn't exist as is, it's calculated relative to the folder containing a file.
        If relative_to_folder_of is given, it's always used. `/etc/fstab` with a relative_to_folder_of set will not expose
        your systems fstab.

        Security Warning: never use unsanitized user-generated filenames or relative_to_folder_of's values.

        Example:
            # from foo/bar/baz.py
            compiled = Handlebars.precompile('templates/foo.hbs',__file__):
        Here compiled will be the compiled handlebars callable for the file at /foo/bar/templates/foo.hbs.

        """
        # set the ./templates as default
        templates_abs_path = templates_abs_path or self.templates_foldername()

        filename = (
            filename
            if (templates_abs_path is None) and os.path.exists(filename)
            else os.path.abspath(os.path.join(templates_abs_path, filename))
        )
        return self.reader(filename, templates_abs_path)

    def transform(
        self, output: Union[AnyStr, Dict], shared_data: Optional[Dict] = None
    ) -> AnyStr:
        """Fixture standard function."""
        if not isinstance(output, dict):
            return output
        context = dict(request=request)
        # context.update(py4web.core.HELPERS) # yatl helpers
        context.update(URL=URL)
        if shared_data:
            context.update(shared_data.get("template_context", {}))
        context.update(output)
        context["__vars__"] = output

        # from which path are the hbs files hosted ?
        path = self.path or self.templates_foldername()
        filename = os.path.join(path, self.filename)
        if not os.path.exists(filename):
            generic_filename = os.path.join(path, "generic.hbs")
            if os.path.exists(generic_filename):
                filename = generic_filename

        # compile and cache the file for the given filename
        compiled = self.reader(filename, path)

        # helpers and partials come from globals,
        # added with specific helpers and partials for this call
        helpers = {}
        helpers.update(self.helpers)
        helpers.update(context.get("helpers", {}))
        partials = {}
        partials.update(self.partials)
        partials.update(context.get("partials", {}))
        # create a view specific context, because it's only the 'context' key
        # and not everything from the context.
        view_context = {}
        view_context.update(self.global_context)
        view_context.update(context.get("context", context))
        # print(helpers)
        # print(partials)
        # print(view_context)
        # print(filename)

        # execute the compiled function
        output = compiled(view_context, helpers=helpers, partials=partials)
        return output

    def on_success(self, context):
        context["output"] = self.transform(context["output"], context)

    @classmethod
    def templates_foldername(cls):
        return os.path.join(os.path.split(__file__)[0], "templates")
        # return os.path.join(
        #     os.environ["PY4WEB_APPS_FOLDER"], request.app_name, "templates"
        # )  request.app_name doesn't exist yet when this is called.
