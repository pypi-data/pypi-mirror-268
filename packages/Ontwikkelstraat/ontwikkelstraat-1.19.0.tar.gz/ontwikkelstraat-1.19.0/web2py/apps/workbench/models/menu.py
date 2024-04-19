# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(
    B("EW dashboard"),
    XML("&trade;&nbsp;"),
    _class="navbar-brand",
    _href=URL(c="default", f="index"),
    _id="web2py-logo",
)
# response.title = request.application.replace("_", " ").title()
# Set document.title to 'workbench' (instead of 'init') for Keepass title matching support.
response.title = f"Workbench ({request.controller})"
response.subtitle = request.controller

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get("app.author")
response.meta.description = myconf.get("app.description")
response.meta.keywords = myconf.get("app.keywords")
response.meta.generator = myconf.get("app.generator")

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None


# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------
def without_none(l: list):
    return [_ for _ in l if _ is not None]


response.menu = without_none(
    [
        (
            T("Domeinen"),
            False,
            None,
            [
                (T("Overzicht"), False, URL("default", "domeinen"), []),
                (T("Controleer "), False, URL(c="default", f="check_domeinen"), []),
            ],
        )
        if auth.has_membership(role="education_warehouse", cached=True)
        else None,
        (
            T("Items"),
            False,
            None,
            [
                (T("Overzicht (verhuizen/editen)"), False, URL("default", "items"), []),
                (T("Nieuw item"), False, URL("default", "quick_create"), []),
                (T("Stickeren"), False, URL("default", "taggem"), []),
                (T("Geschiedenis"), False, URL("applog", "index"), []),
            ],
        )
        if auth.has_membership(role="education_warehouse", cached=True)
        else None,
        (
            T("Tags"),
            False,
            None,
            [
                (T("Search"), False, URL("default", "tag_search"), []),
                (T("Nieuwe tag"), False, URL("default", "new_tag"), []),
                (T("Sticker beheer"), False, URL("default", "sticker_beheer"), []),
                (T("Automatische Tag Regels"), False, URL("default", "auto_tags"), []),
            ],
        )
        if auth.has_membership(role="education_warehouse", cached=True)
        else None,
        (
            T("Organisaties"),
            False,
            None,
            [
                (T("Besturen"), False, URL("organisations", "boards"), []),
                (T("Scholen"), False, URL("organisations", "index"), []),
                (T("Nieuwe school"), False, URL("organisations", "quick_create"), []),
                # (T('DoD Regels'), False, URL('workbench', 'dod_rules'), []),
            ],
        )
        if (
            auth.has_membership(role="education_warehouse", cached=True)
            or auth.has_membership(role="minion", cached=True)
        )
        else None,
        (
            T("Workbench"),
            False,
            None,
            [
                (T("Overzicht"), False, URL("workbench", "index"), []),
                (T("Contacten"), False, URL("workbench", "contacts"), []),
                (T("Nieuw"), False, URL("workbench", "new"), []),
                (T("Vragen"), False, URL("workbench", "questions"), []),
                (T("Beheer tags"), False, URL("workbench", "tag_beheer"), []),
                # (T('Zoek tag'), False, URL('default', 'tag_search'), []), # om verwarring te voorkomen, dit niet ophnemen in het workbench menu
                (
                    T("Beheer generieke vragen & regels."),
                    False,
                    URL("workbench", "apply_to_all"),
                    [],
                ),
                # (T('DoD Regels'), False, URL('workbench', 'dod_rules'), []),
            ],
        )
        if auth.has_membership(role="education_warehouse", cached=True)
        else None,
        (
            T("Gevaarlijk"),
            False,
            None,
            [
                (T("(her)starten"), False, URL("default", "herstart"), []),
                (
                    T("Clean Redis (Let op: dit logt mensen uit!)"),
                    False,
                    URL("default", "clean_redis"),
                    [],
                ),
                (T("Uncache"), False, URL("default", "uncache"), []),
            ],
        )
        if auth.has_membership(role="education_warehouse", cached=True)
        else None,
        (
            T("Users"),
            False,
            None,
            [
                (T("Lijst"), False, URL("default", "users"), []),
                (
                    T("Techie Lijst"),
                    False,
                    URL("default", "users", vars=dict(tech=1)),
                    [],
                ),
                (
                    T("Email footer generator"),
                    False,
                    URL("default", "email_footer"),
                    [],
                ),
            ],
        )
        if auth.has_membership(role="education_warehouse", cached=True)
        else None,
        (
            T("Markdown hulp"),
            False,
            None,
            [
                (
                    T("Let op: onderstaande vervangen je huidige venster"),
                    False,
                    None,
                    [],
                ),
                (T("Dillinger.io online editor"), False, "https://dillinger.io/", []),
                (
                    T("StackEdit.io online editor"),
                    False,
                    "https://stackedit.io/app/",
                    [],
                ),
                (
                    T("Markdown cheatsheet"),
                    False,
                    "https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf",
                    [],
                ),
            ],
        ),
    ]
)

DEVELOPMENT_MENU = False


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------


def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T("My Sites"), False, URL("w2p_admin", "default", "site")),
        (
            T("This App"),
            False,
            "#",
            [
                (T("Design"), False, URL("w2p_admin", "default", "design/%s" % app)),
                LI(_class="divider"),
                (
                    T("Controller"),
                    False,
                    URL(
                        "w2p_admin", "default", "edit/%s/controllers/%s.py" % (app, ctr)
                    ),
                ),
                (
                    T("View"),
                    False,
                    URL(
                        "w2p_admin",
                        "default",
                        "edit/%s/views/%s" % (app, response.view),
                    ),
                ),
                (
                    T("DB Model"),
                    False,
                    URL("w2p_admin", "default", "edit/%s/models/db.py" % app),
                ),
                (
                    T("Menu Model"),
                    False,
                    URL("w2p_admin", "default", "edit/%s/models/menu.py" % app),
                ),
                (
                    T("Config.ini"),
                    False,
                    URL("w2p_admin", "default", "edit/%s/private/appconfig.ini" % app),
                ),
                (
                    T("Layout"),
                    False,
                    URL("w2p_admin", "default", "edit/%s/views/layout.html" % app),
                ),
                (
                    T("Stylesheet"),
                    False,
                    URL(
                        "w2p_admin",
                        "default",
                        "edit/%s/static/css/web2py-bootstrap3.css" % app,
                    ),
                ),
                (T("Database"), False, URL(app, "appadmin", "index")),
                (T("Errors"), False, URL("w2p_admin", "default", "errors/" + app)),
                (T("About"), False, URL("w2p_admin", "default", "about/" + app)),
            ],
        ),
        (
            "web2py.com",
            False,
            "#",
            [
                (
                    T("Download"),
                    False,
                    "http://www.web2py.com/examples/default/download",
                ),
                (T("Support"), False, "http://www.web2py.com/examples/default/support"),
                (T("Demo"), False, "http://web2py.com/demo_admin"),
                (
                    T("Quick Examples"),
                    False,
                    "http://web2py.com/examples/default/examples",
                ),
                (T("FAQ"), False, "http://web2py.com/AlterEgo"),
                (T("Videos"), False, "http://www.web2py.com/examples/default/videos/"),
                (T("Free Applications"), False, "http://web2py.com/appliances"),
                (T("Plugins"), False, "http://web2py.com/plugins"),
                (T("Recipes"), False, "http://web2pyslices.com/"),
            ],
        ),
        (
            T("Documentation"),
            False,
            "#",
            [
                (T("Online book"), False, "http://www.web2py.com/book"),
                LI(_class="divider"),
                (T("Preface"), False, "http://www.web2py.com/book/default/chapter/00"),
                (
                    T("Introduction"),
                    False,
                    "http://www.web2py.com/book/default/chapter/01",
                ),
                (T("Python"), False, "http://www.web2py.com/book/default/chapter/02"),
                (T("Overview"), False, "http://www.web2py.com/book/default/chapter/03"),
                (T("The Core"), False, "http://www.web2py.com/book/default/chapter/04"),
                (
                    T("The Views"),
                    False,
                    "http://www.web2py.com/book/default/chapter/05",
                ),
                (T("Database"), False, "http://www.web2py.com/book/default/chapter/06"),
                (
                    T("Forms and Validators"),
                    False,
                    "http://www.web2py.com/book/default/chapter/07",
                ),
                (
                    T("Email and SMS"),
                    False,
                    "http://www.web2py.com/book/default/chapter/08",
                ),
                (
                    T("Access Control"),
                    False,
                    "http://www.web2py.com/book/default/chapter/09",
                ),
                (T("Services"), False, "http://www.web2py.com/book/default/chapter/10"),
                (
                    T("Ajax Recipes"),
                    False,
                    "http://www.web2py.com/book/default/chapter/11",
                ),
                (
                    T("Components and Plugins"),
                    False,
                    "http://www.web2py.com/book/default/chapter/12",
                ),
                (
                    T("Deployment Recipes"),
                    False,
                    "http://www.web2py.com/book/default/chapter/13",
                ),
                (
                    T("Other Recipes"),
                    False,
                    "http://www.web2py.com/book/default/chapter/14",
                ),
                (
                    T("Helping web2py"),
                    False,
                    "http://www.web2py.com/book/default/chapter/15",
                ),
                (T("Buy web2py's book"), False, "http://stores.lulu.com/web2py"),
            ],
        ),
        (
            T("Community"),
            False,
            None,
            [
                (
                    T("Groups"),
                    False,
                    "http://www.web2py.com/examples/default/usergroups",
                ),
                (T("Twitter"), False, "http://twitter.com/web2py"),
                (T("Live Chat"), False, "http://webchat.freenode.net/?channels=web2py"),
            ],
        ),
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
