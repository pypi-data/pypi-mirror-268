import re

dbco = workbench_db.plugin_comments_comment


def error(code=404):
    raise HTTP(code)


def SUL(*a, **b):
    return UL(*[u for u in a if u], **b)


script = SCRIPT(
    """
var action = null;
var formhtml = null;
function plugin_comments_init() {
  function delete_all_forms() { jQuery('div.plugin_comments .reply').html(''); }
  function capture_form() {
     jQuery('div.plugin_comments #close').click(function(){
       delete_all_forms();
     });
    jQuery('div.plugin_comments :submit').click(function(){
      var form = jQuery(this).parent()
      var body = form.children('textarea[name="body"]').val();
       jQuery.post(action+'/'+form.parent().prev().attr('id'),
                  'body='+encodeURIComponent(body),
                   function(data,r){ if(data) { form.parent().next().prepend(data);
                                                form.children('textarea[name="body"]').val('')
                                                delete_all_forms();
                                                plugin_comments_init(); }
                   },'html');
      return false;
    });
  }
  jQuery('div.plugin_comments #toggle').click(function(){
     jQuery(this).parent().next().next().slideToggle();
  });
  jQuery('div.plugin_comments #reply').click(function(){
     delete_all_forms();
     jQuery(this).parent().next().next().slideDown();
     jQuery(this).parent().next().html(formhtml); capture_form(); 
  });
  jQuery('div.plugin_comments #delete').click(function(){
    delete_all_forms();
    var parent = jQuery(this).parent()
    jQuery.post(action+'/delete/'+parent.attr('id'),null,function(data,r){parent.html('deleted');});
  });
}
jQuery(document).ready(function() {
  action = jQuery('div.plugin_comments form').attr('action');  
  formhtml = jQuery('div.plugin_comments form').parent().html();
  jQuery('div.plugin_comments #toggle').parent().next().next().hide();
  jQuery('div.plugin_comments .reply').html('');
  plugin_comments_init()}
);
"""
)


@auth.requires_login()
def index():
    tablename = request.args(0) or error()
    record_id = request.args(1) or error()
    parent_id = request.args(2)  # must be None, 'delete', 'r0', 'r#'
    thread = {0: []}

    def node(comment):
        if not comment.deleted:
            return LI(
                DIV(
                    markdown(comment.body),
                    DIV(
                        T(
                            "posted by %(first_name)s %(last_name)s",
                            db.auth_user[comment.created_by].as_dict()
                            if db.auth_user[comment.created_by]
                            else {"first_name": "import", "last_name": "robot"},
                        ),
                        " ",
                        T("on %s", comment.created_on),
                        " [",
                        A(T("toggle"), _id="toggle"),
                        "|" if auth.user_id else "",
                        A(T("reply"), _id="reply") if auth.user_id else "",
                        "|" if comment.created_by == auth.user_id else "",
                        A(T("delete"), _id="delete")
                        if comment.created_by == auth.user_id
                        else "",
                        "]",
                        _id="r%s" % comment.id,
                        _style="float:right; margin-top:-4ex;",
                    ),
                ),
                DIV(_class="reply"),
                SUL(*[node(comment) for comment in thread.get(comment.id, [])]),
            )
        elif comment.id in thread:
            return LI(
                DIV(T("DELETED"), " [", A(T("toggle"), _id="toggle"), "]"),
                DIV(_class="reply"),
                SUL(*[node(comment) for comment in thread.get(comment.id, [])]),
            )
        else:
            return None

    if parent_id == "delete":
        if workbench_db(dbco.created_by == auth.user_id)(dbco.tablename == tablename)(
            dbco.record_id == record_id
        )(dbco.id == request.args(3)[1:]).update(deleted=True):
            return "deleted"
        else:
            return error()
    elif parent_id:
        if not request.vars.body or not auth.user_id:
            return error()
        dbco.parent_node.default = parent_id[1:]
        dbco.tablename.default = tablename
        dbco.record_id.default = record_id
        dbco.created_by.default = auth.user_id
        if len(re.compile("\s+").sub("", request.vars.body)) < 1:
            return ""
        item = dbco.insert(body=request.vars.body.strip())
        return node(item)
    comments = workbench_db(dbco.tablename == tablename)(
        dbco.record_id == record_id
    ).select(orderby=~dbco.created_on)
    for comment in comments:
        thread[comment.parent_node] = thread.get(comment.parent_node, []) + [comment]
    return DIV(
        script,
        DIV(
            BUTTON(
                T(request.vars.get("label", "post")),
                _id="reply",
                _class="btn btn-secondary",
                _type="button",
            ),
            _id="r0",
        )
        if auth.user_id
        else A(T("login to post"), _href=URL(r=request, c="default", f="user")),
        DIV(
            FORM(
                TEXTAREA(_name="body", _style="width:100%; height: 80px"),
                INPUT(_type="submit", _value=T("post"), _style="float:right"),
                A(
                    T("help"),
                    _href="http://daringfireball.net/projects/markdown/",
                    _target="_blank",
                    _style="float:right; padding-right: 10px",
                ),
                A(T("close"), _id="close", _style="float:right; padding-right: 10px"),
                _method="post",
                _action=URL(r=request, args=[tablename, record_id]),
            ),
            _class="reply",
        ),
        SUL(*[node(comment) for comment in thread[0]]),
        _class="plugin_comments",
    )
