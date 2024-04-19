import pprint
import typing

if typing.TYPE_CHECKING:
    from gluon import SQLFORM

    from ..models.db import auth, db

is_allowed = auth.has_membership(
    role="education_warehouse", cached=True
) or auth.has_membership(role="ioldb", cached=True)


# ---- example index page ----
def index():
    return dict()


@auth.requires(is_allowed, requires_login=True)
def netwerken():
    grid = SQLFORM.smartgrid(
        db.Netwerken,
        csv=False,
        advanced_search=False,
        buttons_placement="left",
        # paginate=100_000,
        maxtextlength=50,
    )
    print(db._lastsql)
    return dict(grid=grid)


@auth.requires(is_allowed, requires_login=True)
def socialmedia():
    grid = SQLFORM.smartgrid(
        db.Social_media,
        csv=False,
        advanced_search=False,
        buttons_placement="left",
        # paginate=100_000,
        maxtextlength=150,
    )
    return dict(grid=grid)


# ---- API (example) -----
@auth.requires(is_allowed, requires_login=True)
def api_get_user_email():
    if not request.env.request_method == "GET":
        raise HTTP(403)
    return response.json({"status": "success", "email": auth.user.email})


# ---- Smart Grid (example) -----
@auth.requires_membership("admin")  # can only be accessed by members of admin groupd
def grid():
    response.view = "generic.html"  # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables:
        raise HTTP(403)
    grid = SQLFORM.smartgrid(
        db[tablename], args=[tablename], deletable=False, editable=False
    )
    return dict(grid=grid)


@auth.requires_still_exists()
def whoami():
    me = auth.user.as_dict()

    query = db.auth_membership.user_id == me["id"]  # WHERE
    query &= db.auth_membership.group_id == db.auth_group.id  # JOIN

    groups = db(query).select(db.auth_group.ALL).as_dict()

    return str(
        PRE(
            pprint.pformat(
                {
                    "me": me,
                    "groups": groups,
                }
            )
        )
    )


#
# # ---- Embedded wiki (example) ----
# def wiki():
#     auth.wikimenu()  # add the wiki to the menu
#     return auth.wiki()


# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    import ssl

    saved = ssl._create_default_https_context
    ssl._create_default_https_context = ssl._create_unverified_context
    result = dict(form=auth())
    ssl._create_default_https_context = saved
    return result


# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
