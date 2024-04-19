# hier moet test code in
import functools
import os
import random
import re
import typing
from collections.abc import Callable
from dataclasses import dataclass
from http import cookiejar as http_cookiejar
from pathlib import Path
from typing import TypeAlias, TypeVar

import pytest  # https://docs.pytest.org/en/7.1.x/how-to/fixtures.html
import webtest  # https://docs.pylonsproject.org/projects/webtest/en/latest/ , uses wsgiproxy2 for real server testing.

jwt_encoder: TypeVar = Callable[[dict], str]
gid_str: TypeAlias = str


def jwt_extra(jwt, *args, **kwp):
    "Helper to avoid having to type the HTTP_X_EDWH header for each enhanced request."
    d = {}
    for arg in args:
        d |= arg
    d |= kwp
    return {"HTTP_X_EDWH": jwt(d)}


### web2py compatible test app ###################
class CookieEnrichedTestApp(webtest.TestApp):
    """Keeps the user logged in by adding the cookie to the extra_environ, so it will be included for each request from this session."""

    _last_response: webtest.TestResponse = None
    user: "User" = None

    def do_request(self, req, status=None, expect_errors=None):
        response = super().do_request(req, status, expect_errors)
        self.extra_environ |= {"HTTP_COOKIE": response.headers["Set-Cookie"]}
        return response


def new_session(jwt: jwt_encoder, user: "User" = None) -> CookieEnrichedTestApp:
    jar = http_cookiejar.CookieJar()
    app = CookieEnrichedTestApp(
        os.environ["WEBTEST_TARGET_URL"],
        cookiejar=jar,
        extra_environ={"HTTP_X_EDWH": jwt({"is_test": True})},
        lint=False,
    )
    if user:
        app.user = user
    return app


@pytest.fixture(scope="module")
def jwt() -> jwt_encoder:
    import jwt  # shadows the function name, but that's intended.

    key_file = Path("../private/jwt.key")
    try:
        private_key = key_file.read_text()
    except FileNotFoundError:
        private_key = random.randbytes(4096).hex()
        key_file.touch()
        key_file.write_text(private_key)
    return functools.partial(jwt.encode, key=private_key, algorithm="HS256")


@pytest.fixture(scope="module")
def app(jwt):
    # Use this specific header (HTTP_ prefix) is required to pass through to
    # the requests library. On the web2py side this header is available as request.env.http_x_edwh
    return new_session(jwt)


### extra tools ##################################
def cookie_id(session):
    return session.cookies.get("session_id_init", "-?").split("-")[-1]


def publishable_controller_methods():
    paramless_def = re.compile(r"def\s+([a-zA-Z0-9_]+)\s*\(\).*")
    for controller in Path("../controllers/").glob("*.py"):
        if "appadmin" in controller.name:
            continue
        for line in controller.open():
            if paramless_def.match(line) and "NO_TEST_REDIRECT_ON" not in line:
                method_name = line.split()[1].split("(")[0]
                yield f"/{controller.name.removesuffix('.py')}/{method_name}"


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    password: str
    roles: list[str]

    def login(self, session: CookieEnrichedTestApp) -> CookieEnrichedTestApp:
        """Login as this user and return the session (TestApp) with the cookie set."""
        login_form = session.get("/user/login")
        login_form.form["email"] = self.email
        login_form.form["password"] = self.password
        response = login_form.form.submit().follow()
        return session

    def create_on_server(
        self, session: CookieEnrichedTestApp, jwt: jwt_encoder
    ) -> webtest.TestApp:
        """Create this user on the server and return the session (TestApp) with the cookie set."""

        create_form = session.get("/user/register?_next=/user/logout")
        create_form.form["first_name"] = self.first_name
        create_form.form["last_name"] = self.last_name
        create_form.form["email"] = self.email
        create_form.form["password"] = self.password
        create_form.form["password_two"] = self.password
        create_form.form.submit().follow()
        # make sure the session is updated with the cookie received on login
        self.login(session)

        resp = session.get(
            "/webtest_support/assign_roles_to_user",
            extra_environ=jwt_extra(jwt, email=self.email, roles=self.roles),
        )
        return session

    def delete_from_server(self, session: CookieEnrichedTestApp, jwt: jwt_encoder):
        "Delete the user using /webtest_support/remove_user_from_db"
        session.get(
            "/webtest_support/remove_user_from_db",
            extra_environ=jwt_extra(jwt, email=self.email),
        )


admin_user = User("Admin", "User", "admin@roc.nl", "test", ["admin"])
edwh_user = User(
    "Pietje", "Puk", "p.puk@roc.nl", "supersecret", ["education_warehouse"]
)


@pytest.fixture()
def anonymous_session(request, jwt) -> CookieEnrichedTestApp:
    return new_session(jwt)


@pytest.fixture(params=[admin_user], scope="module")
def admin_session(request, jwt: jwt_encoder) -> CookieEnrichedTestApp:
    session = new_session(jwt, request.param)
    try:
        yield session.user.create_on_server(session, jwt)
    finally:
        session.user.delete_from_server(session, jwt)


@pytest.fixture(params=[edwh_user], scope="module")
def edwh_session(request, jwt: jwt_encoder) -> CookieEnrichedTestApp:
    session = new_session(jwt, request.param)
    try:
        yield session.user.create_on_server(session, jwt)
    finally:
        session.user.delete_from_server(session, jwt)


@pytest.fixture()
def temp_item(edwh_session, jwt: jwt_encoder) -> tuple[gid_str, webtest.TestResponse]:
    new_item_name = f"test item({random.randint(0,10000000)})"
    quick_edit = edwh_session.get("/default/quick_create")
    quick_edit.form["name"] = new_item_name
    quick_edit = quick_edit.form.submit().follow()
    quick_edit.mustcontain(new_item_name)
    item_gid = quick_edit.pyquery("#item_gid__row PRE").text()
    try:
        yield item_gid, quick_edit
    finally:
        edwh_session.post(
            "/webtest_support/remove_item_from_db",
            extra_environ=jwt_extra(jwt, item_gid=item_gid),
        )
