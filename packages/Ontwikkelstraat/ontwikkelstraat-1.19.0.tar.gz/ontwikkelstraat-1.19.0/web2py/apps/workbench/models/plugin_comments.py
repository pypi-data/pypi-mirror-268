workbench_db.define_table(
    "plugin_comments_comment",
    Field("tablename", readable=False, writable=False),
    Field("record_id", "integer", readable=False, writable=False),
    Field("parent_node", "integer", readable=False, writable=False),
    Field("body"),
    Field("deleted", "boolean", default=False, readable=False, writable=False),
    Field("votes", "integer", default=1, readable=False, writable=False),
    Field(
        "created_by",
        "integer",
        default=lambda: auth.user_id,
        readable=False,
        writable=False,
    ),
    Field(
        "created_on", "datetime", default=request.now, readable=False, writable=False
    ),
    Field("system_generated", "boolean", default=False),
)


def plugin_comments(tablename="0", record_id=0):
    return LOAD(
        "plugin_comments",
        args=[tablename, record_id],
        vars=dict(label="Overleg"),
        ajax=True,
    )


def add_comment(tablename, record_id, body, parent_node=0):
    workbench_db.plugin_comments_comment.insert(
        tablename=tablename,
        record_id=record_id,
        parent_node=parent_node,
        body=body,
        system_generated=True,
    )
    workbench_db.commit()
