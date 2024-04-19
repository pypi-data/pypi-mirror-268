import json
from pprint import pp

import pytest
from tools import *

# Example: TARGET = "https://web2py.dockers.local#requests".lower()
# TARGET = os.environ["WEBTEST_TARGET_URL"]  # this works by default.
# has to start with lowercase http.
# adding #requests makes sure the client lib is used. On my vortex machine #httplib (the default) resulted in 502 errors.
# They origniated from the fact that the client lib tried to use http://localhost instead of https://web2py.dockers.local
# Don't know why, but forcing requests lib fixed it.
# if TARGET == "LOCAL":
#     import gluon.main
#     TARGET = gluon.main.wsgibase


@pytest.mark.parametrize("path", publishable_controller_methods())
def test_security_redirect_on(app, path):
    """
    Security test: make sure every callable is either redirected to login or 404 if it's RPC callable.

    Exclude by adding `# NO_TEST_REDIRECT_ON` after the method definition. (but on the same line)
    """
    response: webtest.TestResponse = app.get(path, status="*")
    # make sure every callable is either redirected to login or 404 if it's RPC callable
    assert response.status.startswith("303 ") or response.status.startswith("404 ")
    if response.status.startswith("303"):
        assert (
            "user/login?_next" in response.text
            or "You are being redirected" in response.text
        )
    else:
        assert "invalid function" in response.text


@pytest.mark.parametrize("session", [admin_session, edwh_session, anonymous_session])
def test_cookies_stick(app, session):
    """
    Test if cookies stick between requests.

    A base requirement for the testing framework to have sessions that once logged in, stay logged in.
    """
    app.get("/default/index")
    cookietails: list[str] = [cookie_id(app)]
    app.get("/default/index")
    cookietails.append(cookie_id(app))

    assert (
        len(set(cookietails)) == 1
    ), "The cookiejar should be the same on every request: %r" % (cookietails)


def test_pyjwt_global(app):
    """
    Test if the jwt data is available in the request.env.http_x_edwh header.

    The code in the echo_edwh_webtest_data method echo's the header as json, adding a "seen" key.
    """
    response: webtest.TestResponse = app.get("/webtest_support/echo_edwh_webtest_data")
    assert (
        "is_test" in response.json
    ), "The jwt data should be available in the request.env.http_x_edwh header"
    assert "seen" in response.json, "Web2py added data back"


def test_pyjwt_extend_per_request(app, jwt):
    """
    Test if the jwt data is extendable per request, and not just per session.
    Uses the `jwt_extra` helper to add data to the HTTP_X_EDWH header.

    """
    response: webtest.TestResponse = app.get(
        "/webtest_support/echo_edwh_webtest_data",
        extra_environ=jwt_extra(jwt, test_pyjwt_extend_per_request=True),
    )
    assert (
        "test_pyjwt_extend_per_request" in response.json
    ), "The jwt data should be available in the request.env.http_x_edwh header"
    assert "seen" in response.json, "Web2py added data back"


def test_testing_as_admin(admin_session: CookieEnrichedTestApp):
    """
    Test if the admin_session logs a user in as an admin, and stays logged in.

    """
    response: webtest.TestResponse = admin_session.get(
        "/webtest_support/echo_edwh_webtest_data"
    )
    assert (
        "is_test" in response.json
    ), "The jwt data should be available in the request.env.http_x_edwh header"
    assert "seen" in response.json, "Web2py added data back"
    profile: webtest.TestResponse = admin_session.get("/user/profile")
    profile.mustcontain(admin_session.user.email)


def test_item_quick_create(edwh_session: CookieEnrichedTestApp, temp_item, jwt):
    gid, quick_edit = temp_item
    property_form = quick_edit.forms[0]

    backend_item = edwh_session.get(
        "/webtest_support/item_from_backend", extra_environ=jwt_extra(jwt, item_gid=gid)
    ).json
    # pp(backend_item)
    assert backend_item["name"] == property_form["name"].value
    assert (
        backend_item["license"] == "cc-by-sa-4.0"
    ), "The default license should be cc-by-sa-4.0"
    assert (
        backend_item["author"]["email"] == "eddie@educationwarehouse.nl"
    ), "Default author wrong."
    assert backend_item["visibility"] == [
        "pipeline"
    ], "Default visibility should be pipeline"
