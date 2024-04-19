#
# Example usage:
# # A table called "somedata" is born,
# # With fields to store data until dawn,
# # Effdt, a date time that's set with care,
# # Readable yes, but writable, no way there!
# #
# # Effstatus, a boolean with a simple goal,
# # To show true or false, the data's role,
# # Key, bb, cc, strings that bring delight,
# # To store words and numbers, in their sight.
# #
#
# db.define_table(
#     "somedata",
#     Field("effdt", "datetime", readable=True, writable=False, default=request.now),
#     Field("effstatus", "boolean", default=True),
#     Field("key", "string"),
#     Field("bb", "string"),
#     Field("cc", "string"),
# )
#
#
# def setup():
#     # The function called "setup" brings life,
#     # To the table, with data and no strife,
#     # It clears the table, a fresh start anew,
#     # And fills it with values, chosen just for you.
#     #
#     # Effdt is calculated, with time's delight,
#     # Adding or subtracting, day and night,
#     # The data is inserted, row by row,
#     # With key, bb, cc, a story to show.
#     #
#     # The table is now filled, with data untold,
#     # Ready to be used, and its story to be told!
#     db.somedata.truncate()
#     db.somedata.insert(
#         key=1, bb=1, cc=1, effdt=request.now - datetime.timedelta(4), effstatus=True
#     )
#     db.somedata.insert(
#         key=2, bb=2, cc=2, effdt=request.now - datetime.timedelta(2), effstatus=True
#     )
#     db.somedata.insert(
#         key=3, bb=-3, cc=-3, effdt=request.now - datetime.timedelta(2), effstatus=True
#     )
#     db.somedata.insert(
#         key=3, bb=3, cc=3, effdt=request.now - datetime.timedelta(1), effstatus=True
#     )
#     db.somedata.insert(
#         key=3, bb=33, cc=33, effdt=request.now + datetime.timedelta(1), effstatus=True
#     )
#     db.commit()
#     redirect(URL(f="index"))
#
#
#
#
#
# def index():
#     """Simple effective dated grid example."""
#     # setup()
#     grid = effective_dated_grid(
#         db.somedata,
#         keyfieldname="key",
#         csv=False,
#         advanced_search=False,
#         fields=[db.somedata.key, db.somedata.bb, db.somedata.cc],
#         archive_fields=[
#             db.somedata.effdt,
#             db.somedata.effstatus,
#             db.somedata.key,
#             db.somedata.bb,
#             db.somedata.cc,
#         ],
#     )
#     return dict(form=grid)
import functools
import typing
from typing import Optional

import edwh_web2py_effdted_prio_grid
from gluon import HTTP, URL, current
from gluon.html import CAT, INPUT, OPTION, SELECT, XML
from gluon.sqlhtml import SQLFORM
from pydal import Field
from pydal.objects import Query
from typing_extensions import deprecated

# !!! .writable = False won't send the field in the form, but this read only widget will:
ReadonlyWidget = functools.partial(SQLFORM.widgets.string.widget, _readonly=True)


@deprecated("Use `edwh_web2py_effdted_prio_grid.hide` instead.")
def hide(field: Field):
    """Sets a field to be not readable or writable, returns the field for chaining."""
    return edwh_web2py_effdted_prio_grid.hide(field)


@deprecated("Use `edwh_web2py_effdted_prio_grid.effective_dated_grid` instead.")
def effective_dated_grid(
    table: edwh_web2py_effdted_prio_grid.EffectiveDatedTable,
    keyfieldname: str = "key",
    query: Optional[Query] = None,
    use_prio=False,
    **kwp,
):
    """This function creates an effective dated grid, which allows for multiple rows with the same key, but only
    one active row per key. The active row is the one with the latest effective date <= now. The grid allows for
    creating new rows, editing existing rows, and deleting rows.

    Deleting a row will create a new row with the
    same key, but with an effective date of today and an effstatus of False. This will mark the row inactive,
    but will not remove it from the database.

    The grid will also show all rows with an effstatus of False,
    but will not allow for editing or deleting them.

    kwp can be used to pass in any of the parameters used by SQLFORM.grid, with the exception of
    deletable, editable, and create. These are set by the function.

    When using use_prio, the grid will only show the rows with the highest priority for each key,
    and the max effective date <= now and effstatus = True. (so the most recent row within the highest priority)
    """
    return edwh_web2py_effdted_prio_grid.effective_dated_grid(
        table,
        keyfieldname,
        query=query,
        use_prio=use_prio,
        **kwp,
    )


V = typing.TypeVar("V")


def convert_attrs(attrs: dict[str, V]) -> dict[str, V]:
    return {(k if k.startswith("_") else f"_{k}"): v for k, v in attrs.items()}


"""
    def __init__(
        self,
        request,
        field,
        id_field=None,
        db=None,
        orderby=None,
        limitby=(0, 10),
        distinct=False,
        keyword="_autocomplete_%(tablename)s_%(fieldname)s",
        min_length=2,
        help_fields=None,
        help_string=None,
        at_beginning=True,
        default_var="ac",
        user_signature=True,
        hash_vars=False,
    ):
"""


class HTMXAutocompleteWidget:
    _class = "string"

    def __init__(
        self,
        request,
        field,  # label
        id_field=None,  # human
        db=None,
        orderby=None,
        limitby=(0, 10),
        distinct=False,
        keyword="_htmx_autocomplete_%(tablename)s_%(fieldname)s",
        # todo:
        # min_length=2,
        # help_fields=None,
        # help_string=None,
        # at_beginning=True,
        # default_var="ac",
        # user_signature=True,
        # hash_vars=False,
        query: Query = None,
        **__,  # catch any vars used by default autocomplete widget
    ):
        self.request = request or current.request
        self.db = db

        # _htmx_autocomplete_tag_name
        self.keyword = keyword % dict(tablename=field.tablename, fieldname=field.name)
        self.db = db or field._db

        self.select_kwargs = {}

        if limitby:
            self.select_kwargs["limitby"] = limitby

        if orderby:
            self.select_kwargs["orderby"] = orderby

        if distinct:
            self.select_kwargs["distinct"] = distinct

        self.field = field
        self.id_field = id_field or field

        self.base_query = query or (id_field != None)

        if hasattr(request, "application"):
            self.url = URL(args=request.args)
            self.callback()
        else:
            self.url = request

    def build_options(self):
        db = self.db
        request = self.request

        data = {**request.post_vars}
        search_query = data[self.keyword]

        query = self.base_query
        # todo: levenshtein/fuzzy?
        for term in search_query.split(" "):
            query &= db.tag.name.ilike(f"%{term}%")

        mapping = db(query).select(db.tag.gid, db.tag.name, **self.select_kwargs)

        result = ""
        for row in mapping:
            result += f'<option value="{row.gid}">{row.name}</option>'

        return result

    def lookup_current_value(self, value) -> typing.Optional[str]:
        row = self.db(self.id_field == value).select(self.field).first()
        return row[self.field] if row else None

    def callback(self):
        if self.request.method == "POST" and self.keyword in self.request.post_vars:
            result = self.build_options()
            raise HTTP(200, XML(result))

    def __call__(self, field: Field, value: str, **attributes):
        # NOTE: 'datalist' works differently in each browser, and can't be styled.
        # due to this, it's been replaced with a custom implementation
        # (search input + 'select' multiple.
        # You still have to choose one, but 'multiple' makes it look like a list instead of a dropdown)
        input_id = str(field).replace(".", "_")
        request = self.request

        current_value = request.post_vars.get(field.name) or value

        options_id = f"htmx_{input_id}_options"
        # todo: support actual multi-select!
        placeholder = self.lookup_current_value(current_value) or current_value

        input_options = {
            "id": input_id,
            "value": placeholder,
            "placeholder": placeholder,
            "list": options_id,
            "autocomplete": "off",  # only use datalist
            "hx-post": self.url,
            "hx-trigger": "keyup delay:250ms",
            "hx-target": f"#{options_id}",
            "hx-vals": """js:{
                    %s: %s.value,
                }"""
            % (self.keyword, input_id),
            "__": "on change send ew:validate to %s" % (options_id,),
        }

        htmx_input = INPUT(
            **convert_attrs(input_options),
        )

        preselected = (
            [
                OPTION(
                    placeholder,
                    _value=current_value,
                    _selected="selected",
                )
            ]
            if current_value
            else []
        )

        htmx_select = SELECT(
            *preselected,
            **convert_attrs(
                dict(
                    id=options_id,
                    name=field.name,
                    multiple=True,
                    value=current_value,
                    _class="form-control",
                    __="""
                    on change
                      send ew:validate
                    end -- on change
                    
                    on ew:validate
                      set parent to closest .form-group
                      set text_input to #%s
                      set gid to the event's currentTarget's value

                      set selected to <option:checked /> in #%s
                      
                      set valid to selected.length == 1

                      if valid
                        set the value of text_input to the first selected's text
                        remove .has-error from parent                    
                      else
                        add .has-error to parent
                      end -- if
                    end -- ew:validate
                """
                    % (input_id, options_id),
                )
            ),
        )

        return CAT(htmx_input, htmx_select)
