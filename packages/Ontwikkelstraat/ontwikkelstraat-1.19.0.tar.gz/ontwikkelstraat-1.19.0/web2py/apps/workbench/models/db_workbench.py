import base64

workbench_db = DAL(myconf.get("workbench.db_uri"), migrate=True, pool_size=5)

workbench_db.define_table(
    "contact",
    Field("name", label="Naam"),
    Field("email", label="E-mail"),
    Field("org", label="Organisatie"),
    Field("location", label="Locatie"),
    # Field.Virtual('search',lambda row:f'{row.name} ({row.org})'),
    format=lambda row: f"{row.name} ({row.org})",
)

workbench_db.define_table(
    "item",
    Field(
        "contact_id",
        "reference contact",
        represent=lambda value, row: value if value else "-",
    ),
    Field("title", label="Titel"),
    Field(
        "raw_text",
        "text",
        label="Ruwe tekst",
        comment="Bedoeld als alleen-lezen kopie ter referentie",
    ),
    Field(
        "raw_frozen",
        "boolean",
        default=False,
        label="Bevries ruwe tekst.",
        comment="Bevries markdown input om leesbaarheid te vergroten, en vast te leggen wat de bron informatie is.",
    ),
    Field(
        "klad",
        "text",
        label="Klad versie",
        comment="Bedoeld om in te schrijven en te herzien (Markdown)",
    ),
    Field(
        "ori_uri",
        "string",
        comment="URL naar het oorspronkelijke artikel, indien aanwezig",
    ),
    Field(
        "usability",
        "string",
        comment="Mate van bruikbaarheid",
        represent=lambda value, row: value if value else "-",
    ),
    Field("ctime", "datetime", writable=False, default=request.now),
    Field("mtime", "datetime", writable=False, default=request.now),
    Field(
        "live_gid",
        "string",
        length=36,
        represent=lambda value, row: A(
            value, _href=f"https://delen.meteddie.nl/item/{value}"
        )
        if value
        else XML("&mdash;"),
    ),
    Field("property_bag", "json", default={}),
    # Field.Method('status',lambda r:'published' if r.live_gid else 'draft')
    Field.Method("status", lambda row: "published" if row.item.live_gid else "draft"),
)

if request.function not in ("call"):
    # services will use /call/
    workbench_db.item.contact_id.widget = SQLFORM.widgets.autocomplete(
        request,
        workbench_db.contact.name,
        db=workbench_db,
        id_field=workbench_db.contact.id,
        limitby=(0, 10),
        min_length=2,
        at_beginning=False,
    )


def apply_to_all_items(f, i):
    # f gets passed the OpRow object with data for insert or update.
    #     i gets passed the id of the newly inserted record.
    to_all = workbench_db.apply_to_all_items[1]
    for question_id in to_all.questions:
        workbench_db.item_question.insert(item_id=i, question_id=question_id)
    for dod_rule_id in to_all.dod_rules:
        workbench_db.item_dod_rule.insert(
            item_id=i,
            dod_rule_id=dod_rule_id,
        )


workbench_db.item._after_insert.append(lambda f, i: apply_to_all_items(f, i))


def update_mtime(set, values):
    values.mtime = request.now
    return None  # by true wordt afgebroken


workbench_db.item._before_update.append(update_mtime)

## Item-Tag met alle bijbehorende magie

workbench_db.define_table(
    "item_tag",
    Field("item_id", "reference item"),
    Field(
        "tag_gid",
        "string",
        length=36,
        comment="Zoek via autocomplete",
        label="Tag",
        represent=lambda v, r: database.tag(gid=v).name,
    ),  # TODO: requires=IS_IN_DB(database.tag,'gid')
    # use plugin_conmments with 'item_tag' and item_tag.id to discuss
    format=lambda row: row.item_id.name + row.tag_gid,
)

if request.function not in ("call"):
    tag_autocomplete_widget = SQLFORM.widgets.autocomplete(
        request,
        database.tag.name,
        id_field=database.tag.gid,
        limitby=(0, 10),
        min_length=2,
        at_beginning=False,
    )
else:
    tag_autocomplete_widget = None


def item_tag_changed_trigger(item_tag_id: int = None, item_tag_set=None):
    # print('Pure magie voor', item_tag_id or item_tag_set)
    item_tag = workbench_db.item_tag
    tag_dod_rule = workbench_db.tag_dod_rule
    tag_question = workbench_db.tag_question
    item_dod_rule = workbench_db.item_dod_rule
    item_question = workbench_db.item_question

    def extract(field, query):
        """Returns a set of field values extracted from workbench(query).select(field)"""
        return set(row.get(field.name) for row in workbench_db(query).select(field))

    def add_dod_rules(item_id, dod_rule_ids):
        # print('adding dod rules:', dod_rule_ids)
        for dod_rule_id in dod_rule_ids:
            item_dod_rule.insert(item_id=item_id, dod_rule_id=dod_rule_id)

    def add_questions(item_id, question_ids):
        # print('adding questions:', question_ids)
        for question_id in question_ids:
            was_deleted_query = workbench_db.item_question.item_id == item_id
            was_deleted_query &= workbench_db.item_question.question_id == question_id
            was_deleted_query &= workbench_db.item_question.deleted == True
            if workbench_db(was_deleted_query).count():
                workbench_db(was_deleted_query).update(deleted=False)
            else:
                item_question.insert(item_id=item_id, question_id=question_id)

    def remove_dod_rules(item_id, dod_rule_ids):
        # print('removing dod rules: ', dod_rule_ids)
        if not dod_rule_ids:
            return
        query = item_dod_rule.item_id == item_id
        query &= item_dod_rule.dod_rule_id.belongs(dod_rule_ids)
        workbench_db(query).update(deleted=True)

    def remove_questions(item_id, question_ids):
        # print('removing questions:', question_ids)
        if not question_ids:
            return
        query = item_question.item_id == item_id
        query &= item_question.question_id.belongs(question_ids)
        workbench_db(query).update(deleted=True)

    apply_to_all_items = workbench_db.apply_to_all_items[1]
    if item_tag_set:
        item_ids = [r.item_id for r in item_tag_set.select(item_tag.item_id)]
    elif item_tag_id:
        item_ids = [workbench_db.item_tag[item_tag_id].item_id]
    if not item_ids:
        item_ids = session.register_item_ids_to_check
        del session.register_item_ids_to_check
    for item_id in item_ids:
        # ga de wjizigingen na voor DoD regels
        # ga de wijzigingen na voor Question regels
        # print(f'item_id: {item_id}')
        all_tag_gids = extract(item_tag.tag_gid, item_tag.item_id == item_id)
        # print('tag_gids:', all_tag_gids)
        should_have_dod_rules = extract(
            tag_dod_rule.dod_rule_id, tag_dod_rule.tag_gid.belongs(all_tag_gids)
        )
        should_have_dod_rules |= set(apply_to_all_items.dod_rules)
        should_have_questions = extract(
            tag_question.question_id, tag_question.tag_gid.belongs(all_tag_gids)
        )
        should_have_questions |= set(apply_to_all_items.questions)
        # {1,2,3} - {2,4} = {1,3}
        # remove(has - should_have)
        # {2,4} - {1,2,3}  = {4}
        # add(should_have - has)
        has_dod_rules = extract(
            item_dod_rule.dod_rule_id,
            (item_dod_rule.item_id == item_id) & (item_dod_rule.deleted == False),
        )
        has_questions = extract(
            item_question.question_id,
            (item_question.item_id == item_id) & (item_question.deleted == False),
        )
        # print('has dod rules:',has_dod_rules)
        # print('should have dod rules:', should_have_dod_rules)
        # print('has questions:',has_questions)
        # print('should have questions:', should_have_questions)
        remove_dod_rules(item_id, has_dod_rules - should_have_dod_rules)
        remove_questions(item_id, has_questions - should_have_questions)
        add_dod_rules(item_id, should_have_dod_rules - has_dod_rules)
        add_questions(item_id, should_have_questions - has_questions)


# http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#callbacks-on-record-insert-delete-and-update
# As you can see:
#
#     f gets passed the OpRow object with data for insert or update.
#     i gets passed the id of the newly inserted record.
#     s gets passed the Set object used for update or delete.
if "register_item_ids_to_check" not in session:
    session.register_item_ids_to_check = []


def register_for_item_tag_changed(pydal_set):
    session.register_item_ids_to_check = [r.item_id for r in pydal_set.select()]


workbench_db.item_tag._after_insert.append(
    lambda f, i: item_tag_changed_trigger(item_tag_id=i)
)
workbench_db.item_tag._after_update.append(
    lambda s, f: item_tag_changed_trigger(item_tag_set=s)
)
workbench_db.item_tag._before_delete.append(lambda s: register_for_item_tag_changed(s))
workbench_db.item_tag._after_delete.append(
    lambda s: item_tag_changed_trigger(item_tag_set=s)
)

## definition of Done rules
workbench_db.define_table(
    "dod_rule",
    Field("name", "string", comment="Korte krachtige naam voor deze DoD rule"),
    Field(
        "note",
        "text",
        comment="Uitleg wat hiermee bedoeld wordt, wanneer is er aan deze regel voldaan?",
    ),
    format=lambda r: r.name,
)

workbench_db.define_table(
    "tag_dod_rule",
    Field(
        "tag_gid",
        "string",
        length=36,
        comment="Zoek via autocomplete",
        label="Tag",
        represent=lambda v, r: database.tag(gid=v).name,
    ),  # TODO: requires=IS_IN_DB(database.tag,'gid')
    Field("dod_rule_id", "reference dod_rule", label="D.o.D. regel"),
)
workbench_db.tag_dod_rule.tag_gid.widget = tag_autocomplete_widget

workbench_db.define_table(
    "item_dod_rule",
    Field("item_id", "reference item", readable=False),
    Field("dod_rule_id", "reference dod_rule"),
    Field("mtime", "datetime", writable=False, default=request.now),
    Field("ticked", "boolean", default=False),
    Field("note", "text"),
    Field(
        "last_changed_by",
        "integer",
        default=lambda: auth.user_id,
        writable=False,
        represent=lambda value, row: db.auth_user[value].first_name,
    ),
    Field("deleted", "boolean", default=False),
)
workbench_db.item_dod_rule._before_update.append(update_mtime)

## vragen

workbench_db.define_table(
    "question",
    Field("name"),
    Field("question"),
    Field("answer_type", requires=IS_IN_SET(("short", "long"))),
    Field("description", "text", comment="Toelichting"),
    format=lambda row: row.name,
)

workbench_db.define_table(
    "tag_question",
    Field(
        "tag_gid",
        "string",
        length=36,
        comment="Zoek via autocomplete",
        label="Tag",
        represent=lambda v, r: database.tag(gid=v).name,
    ),  # TODO: requires=IS_IN_DB(database.tag,'gid')
    Field("question_id", "reference question", label="Vraag"),
)
workbench_db.tag_question.tag_gid.widget = tag_autocomplete_widget

workbench_db.define_table(
    "item_question",
    Field("item_id", "reference item", readable=False),
    Field("question_id", "reference question"),
    Field("note", "text"),
    Field("mtime", "datetime", writable=False, default=request.now),
    Field(
        "last_changed_by",
        "integer",
        default=lambda: auth.user_id,
        writable=False,
        represent=lambda value, row: getattr(db.auth_user[value], "first_name", "?"),
    ),
    Field("deleted", "boolean", default=False),
)
workbench_db.item_question._before_update.append(update_mtime)
##  bijlagen

workbench_db.define_table(
    "source_file",
    Field("item_id", "reference item", writable=False),
    Field("name", "string"),
    Field("original_uri", "string", default=None),
    Field("attachment", "upload"),
    Field(
        "gid",
        "string",
        default=None,
        writable=False,
        readable=False,
        comment="GID van de attachment na het uploaden",
    ),
    Field(
        "added_by",
        "integer",
        default=lambda: auth.user_id,
        writable=False,
        represent=lambda value, row: db.auth_user[value].first_name
        if value
        else "Onbekend",
    ),
    Field("added_on", "datetime", default=request.now, writable=False),
)
import markdown2

workbench_db.define_table(
    "apply_to_all_items",
    Field("questions", "list:reference question"),
    Field("dod_rules", "list:reference dod_rule"),
)
if workbench_db(workbench_db.apply_to_all_items).count() == 0:
    # setup this one record or things will crash and burn when synchronising
    # without configuration here.
    workbench_db.apply_to_all_items.insert(questions=[], dod_rules=[])
    workbench_db.commit()

workbench_db.apply_to_all_items._after_update.append(
    # update alle items omdat generieke vragen misschien wel en misschein niet meer van toepassing zijn.
    lambda s, f: item_tag_changed_trigger(
        item_tag_set=workbench_db(workbench_db.item_tag.id > 0)
    )
)


def markdown(text):
    """Gebruikt in controllers/plugin_comment.py/index"""
    extras = ["fenced-code-blocks"]
    return DIV(
        XML(markdown2.markdown(text, extras=extras)),
        _style="background-color:#E0E0E0; padding: 0px 0px 0px 5px;;",
    )


def markdown_preview_widget(field, value):
    return DIV(
        TEXTAREA(
            value,
            _name=field.name,
            _id="%s_%s" % (field.tablename, field.name),
            _class=field.type,
            _style="display:none",
            requires=field.requires,
        ),
        markdown(value),
        _class="md-preview",
    )


def remove_delete_button_from_form(form, find="Deleted"):
    for div in form.elements("div"):
        if "_deleted__row" in div.attributes.get("_id", ""):
            div.elements("div", replace=SPAN())
    return form
