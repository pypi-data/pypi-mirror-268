# Base imports.
import hashlib
import json
import os

# Add this import to use pytest decorators.
import random
import string
import time
from contextlib import contextmanager

import pytest

# Add this import to use autotype within PyCharm.
import requests
from bs4 import BeautifulSoup
from filelock import FileLock
from playwright.sync_api import BrowserContext, Page, sync_playwright

# Get the environment variables.
HOME_URL = os.getenv("home_url")
FRONT_END_URL = os.getenv("front_end_url", HOME_URL.replace("/ghost", "/front_end"))
REGULAR_EMAIL = os.getenv("regular_email")
REGULAR_PASSWORD = os.getenv("regular_password")
REGULAR_USER_GID = os.getenv("regular_user_gid")
ROC_EMAIL = os.getenv("roc_email")
ROC_PASSWORD = os.getenv("roc_password")
ROC_USER_GID = os.getenv("roc_user_gid")
NORMAL_ITEM_GID = os.getenv("normal_item_gid")
ROC_ITEM_GID = os.getenv("roc_item_gid")
EMAIL_VALIDATION_SEED = os.getenv("email_validation_seed")
TIME_WHEN_TESTING = os.getenv("static_datetime")


# The standard "session_data" is being used for regular authenticated users.
@pytest.fixture(scope="session")
def session_data(tmp_path_factory, worker_id):
    if worker_id == "master":
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return setup_login(as_roc=False)

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    # Save the authenticated cookies from a regular user in a .json, this is a temporary file.
    fn = root_tmp_dir / "regular_authenticated_cookie.json"
    # The file is locked until one worker has unlocked it, then all the other workers will use this file.
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = setup_login(as_roc=False)
            fn.write_text(json.dumps(data))
    return data


# The admin "roc_session_data" is being used for roc (admin) authenticated users.
@pytest.fixture(scope="session")
def roc_session_data(tmp_path_factory, worker_id):
    if worker_id == "master":
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return setup_login(as_roc=True)

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    # Save the authenticated cookies from a roc (admin) user in a .json, this is a temporary file.
    fn = root_tmp_dir / "roc_authenticated_cookie.json"
    # The file is locked until one worker has unlocked it, then all the other workers will use this file.
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = setup_login(as_roc=True)
            fn.write_text(json.dumps(data))
    return data


def generate_email_validation_code(email: str, seed: str) -> int:
    """Returns a 6 digit email validation code based on the email adres.

    This code should be hard to guess, so using some hashmagic with an arbitrary seed.
    Seed should come from the config file, so the test suite can be fed the same config
    seed and calculate the numbers. This is to be able to test the login logic.
    """
    h = hashlib.sha3_512()
    h.update(seed.encode())
    h.update(email.strip().lower().encode())
    return str(int(h.hexdigest(), 16))[-6:]


def setup_login(as_roc):
    email, password = (
        (ROC_EMAIL, ROC_PASSWORD) if as_roc else (REGULAR_EMAIL, REGULAR_PASSWORD)
    )
    cookies_name = "roc" if as_roc else "regular"
    # Check if cookies already exist in json files.
    if not os.path.exists(f"{cookies_name}_cookies.json"):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context()
            page = context.new_page()
            # Go to the page.
            page.goto(HOME_URL, wait_until="networkidle", timeout=0)

            # Click span:has-text("Login")
            page.click('span:has-text("Inloggen")')
            # Fill [placeholder="Email input"]
            page.fill("#field-email", email)
            # Fill [placeholder="Password input"]
            page.fill("#field-password", password)
            # Submit the credentials and login.
            page.click("#submit-credentials")
            # Manually wait for the page to load, so the verification has time to pop up.
            time.sleep(5)

            # Verification
            if page.query_selector("#submit-verification"):
                if as_roc:
                    verification_code = generate_email_validation_code(
                        ROC_EMAIL, EMAIL_VALIDATION_SEED
                    )
                    page.click("#verify-code")
                    page.fill("#verify-code", f"{verification_code}")
                    page.click("#submit-verification")
                    time.sleep(5)
                else:
                    verification_code = generate_email_validation_code(
                        REGULAR_EMAIL, EMAIL_VALIDATION_SEED
                    )
                    page.click("#verify-code")
                    page.fill("#verify-code", f"{verification_code}")
                    page.click("#submit-verification")
                    time.sleep(5)

            # Check if logged in properly.
            if as_roc:
                # Click #edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a
                page.click(
                    "#edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a"
                )

                # Click a:has-text("Mijn Profiel")
                page.click('a:has-text("Mijn Profiel")')
                assert (
                    "/user/a2f28371-72fe-4962-ab28-6c72624e3282"
                    or "/user/603df027-5636-4096-aa98-d7c30e8bcddb" in page.url
                ), f"De gebruiker is niet succesvol ingelogd!"

            # Get cookies from website.
            cookies = context.cookies()
            # Store cookies in json file.
            with open(f"{cookies_name}_cookies.json", "w") as f:
                f.write(json.dumps(cookies))
    else:
        with open(f"{cookies_name}_cookies.json", "r") as f:
            cookies = json.load(f)
    return cookies


# The following fixtures make using the Context fixture easier.
# You can now use an unauthenticated_context, regular_authenticated_context and a roc_authenticated_context.
# This makes it easier to see which context is being used/can be used.
def context_manager_factory(scope: str, context: BrowserContext, add_these_cookies):
    @contextmanager
    def save_alter_recover_cookies():
        ori_cookies = context.cookies()
        context.add_cookies(add_these_cookies)
        # edwh authentication scope. (unauthenticated, regular, roc)
        context.scope = scope
        try:
            yield context
        finally:
            context.clear_cookies()
            context.add_cookies(ori_cookies)
            del context.scope

    return save_alter_recover_cookies


# Use all three contexts:
# def test_single_searchbar_result(
#     self, page: Page, browser_name, screenshot, browser_context_managers
# ):
#     for switch_user in browser_context_managers:
#         with switch_user() as context:
#             page.goto(...)
@pytest.fixture
def browser_context_managers(
    context: BrowserContext,
    session_data,
    roc_session_data,
):
    # Levert een lijst van context handlers om session data te activeren
    # er is geen mogelijkheid om session_data te verwijderen, alleen totaal
    # te clearen. basis is de normale sessie. hiervan een kopie maken om later
    # te filteren wat er bijgekomen is en dat te verwijderen.
    return (
        context_manager_factory("unauthenticated", context, []),  # unauthenticated
        context_manager_factory("regular", context, session_data),  # regular
        context_manager_factory("roc", context, roc_session_data),  # roc
    )


# Use a single context:
# def test_searchbar_result(
#     self, page: Page, browser_name, screenshot, roc_authenticated
# ):
#     with roc_authenticated() as context:
#         page.goto(...)
@pytest.fixture
def unauthenticated(context: BrowserContext):
    return context_manager_factory("unauthenticated", context, [])  # unauthenticated


@pytest.fixture
def regular_authenticated(context: BrowserContext, session_data):
    return context_manager_factory("regular", context, session_data)  # regular


@pytest.fixture
def roc_authenticated(context: BrowserContext, roc_session_data):
    return context_manager_factory("roc", context, roc_session_data)  # roc


@pytest.fixture
def request_session():
    return requests.session()


# Make a screenshot directory, based on the stored current time (time_when_testing) and the browser name.
def create_screenshot_directory(browser_name):
    browser_dir = os.path.join("screenshots", "static_ghost", browser_name)

    # Check if the directory already exists.
    if not os.path.exists(browser_dir):
        os.mkdir(browser_dir)

    screenshot_dir = os.path.join(browser_dir, TIME_WHEN_TESTING)
    if not os.path.exists(screenshot_dir):
        os.mkdir(screenshot_dir)
    return screenshot_dir


def take_screenshot(screenshot, page, browser_name, scroll_selector, screenshot_name):
    if screenshot == "take_screenshot":
        if scroll_selector is not None:
            # Scroll down for better screenshots.
            handle = page.query_selector(scroll_selector)
            handle.scroll_into_view_if_needed()
        page.wait_for_load_state("networkidle")
        page.screenshot(
            path=f"{create_screenshot_directory(browser_name)}/{screenshot_name}.png"
        )


@pytest.mark.authenticatie
class TestAuthentication:
    @staticmethod
    def core_login(page: Page, unauthenticated, email, password):
        with unauthenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)

            # Click span:has-text("Login")
            page.click('span:has-text("Inloggen")')
            # Fill [placeholder="Email input"]
            page.fill("#field-email", email)
            # Fill [placeholder="Password input"]
            page.fill("#field-password", password)
            # Submit the credentials and login.
            page.click("#submit-credentials")

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_regular_authenticated_login(
        self, page: Page, browser_name, screenshot, unauthenticated
    ):
        email = REGULAR_EMAIL
        password = REGULAR_PASSWORD
        self.core_login(page, unauthenticated, email=email, password=password)
        # Check if logged in properly

        # Click #edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a
        page.click(
            "#edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a"
        )
        # Click a:has-text("Mijn Profiel")
        page.click('a:has-text("Mijn Profiel")')
        assert (
            REGULAR_USER_GID in page.url
        ), f"De gebruiker is niet succesvol ingelogd met {unauthenticated.scope}@{browser_name}."

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_roc_authenticated_login(
        self, page: Page, browser_name, screenshot, unauthenticated
    ):
        email = ROC_EMAIL
        password = ROC_PASSWORD
        self.core_login(page, unauthenticated, email=email, password=password)
        # Check if logged in properly
        # Click #edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a
        page.click(
            "#edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a"
        )

        # Click a:has-text("Mijn Profiel")
        page.click('a:has-text("Mijn Profiel")')
        assert (
            ROC_USER_GID in page.url
        ), f"De gebruiker is niet succesvol ingelogd met {unauthenticated.scope}@{browser_name}."

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_false_email_login(
        self, page: Page, browser_name, screenshot, unauthenticated
    ):
        email = "FALSE_EMAIL@FalseEmail.nl"
        password = ROC_PASSWORD
        self.core_login(page, unauthenticated, email=email, password=password)
        # Check if the error message appears.
        assert page.wait_for_selector(
            "#feedback >> text=Gebruikersnaam of wachtwoord onbekend, probeer een andere combinatie."
        ), f"De error message is niet verschenen met {unauthenticated.scope}@{browser_name}."

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_false_password_login(
        self, page: Page, browser_name, screenshot, unauthenticated
    ):
        email = ROC_EMAIL
        password = "FALSE_PASSWORD"
        self.core_login(page, unauthenticated, email=email, password=password)
        # Check if the error message appears.
        assert page.wait_for_selector(
            "#feedback >> text=Gebruikersnaam of wachtwoord onbekend, probeer een andere combinatie."
        ), f"De error message is niet verschenen met {unauthenticated.scope}@{browser_name}."

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_false_email_and_password_login(
        self, page: Page, browser_name, screenshot, unauthenticated
    ):
        email = "FALSE_EMAIL@FalseEmail.nl"
        password = "FALSE_PASSWORD"
        self.core_login(page, unauthenticated, email=email, password=password)
        # Check if the error message appears.
        assert page.wait_for_selector(
            "#feedback >> text=Gebruikersnaam of wachtwoord onbekend, probeer een andere combinatie."
        ), f"De error message is niet verschenen met {unauthenticated.scope}@{browser_name}."

    @staticmethod
    def core_registration(page: Page, unauthenticated, email, password):
        with unauthenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)

            # Click span:has-text("Login")
            page.click('span:has-text("Inloggen")')
            # Click Registeren
            page.click(
                "#login-modal > div.modal-content > form > div.field.is-grouped > div:nth-child(1) > div > button:nth-child(2)"
            )
            # Fill Locatie
            page.fill("#signup-locatie", "Assen")
            # Fill School
            page.fill("#signup-school", "Drenthe College")
            numbers = string.digits
            # Fill Voornaam
            page.fill(
                "#signup-voornaam",
                "TestVoornaam" + "".join(random.choice(numbers) for i in range(16)),
            )
            # Fill Achternaam
            page.fill(
                "#signup-achternaam",
                "TestAchternaam" + "".join(random.choice(numbers) for i in range(16)),
            )
            # Fill Rol
            page.fill("#signup-rol", "Student")
            # Click Volgende
            page.click(
                "div.field:nth-child(6) > div:nth-child(1) > button:nth-child(1)"
            )

            # Fill Email
            page.fill("#signup-email", email)
            # Fill Wachtwoord
            page.fill("#signup-password", password)
            # Fill Wachtwoord herhalen
            page.fill("#signup-password2", password)
            # Click TOS
            page.click("#signup-conditions")
            # Click Verzenden
            page.click(
                "#signup-2 > div.field.is-grouped > div > button.button.is-primary.is-rounded.mx-1.control"
            )

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    @pytest.mark.accept_database_clutter
    def test_creating_regular_account(
        self, page: Page, browser_name, screenshot, unauthenticated
    ):
        numbers = string.digits
        email = (
            "CorrectEmail"
            + "".join(random.choice(numbers) for i in range(16))
            + "@educationwarehouse.nl"
        )
        password = "CorrectPassword"
        self.core_registration(page, unauthenticated, email=email, password=password)

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    @pytest.mark.accept_database_clutter
    def test_creating_roc_account(
        self, page, browser_name, screenshot, unauthenticated
    ):
        numbers = string.digits
        email = (
            "CorrectEmail"
            + "".join(random.choice(numbers) for i in range(16))
            + "@roc.nl"
        )
        password = "CorrectPassword"
        self.core_registration(page, unauthenticated, email=email, password=password)

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_creating_account_with_incorrect_email(
        self, page: Page, browser_name, screenshot, unauthenticated
    ):
        numbers = string.digits
        email = (
            "FALSE_EMAIL"
            + "".join(random.choice(numbers) for i in range(16))
            + "@FalseEmail.nl"
        )
        password = "CorrectPassword"
        self.core_registration(page, unauthenticated, email=email, password=password)
        # Check if the error message appears.
        assert page.wait_for_selector(
            '#generic-feedback >> text=403: unknown domain "falseemail.nl"'
        ), f"De error message is niet verschenen met {unauthenticated.scope}@{browser_name}."

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_creating_account_with_incorrect_password(
        self, page: Page, browser_name, screenshot, unauthenticated
    ):
        numbers = string.digits
        email = (
            "CorrectEmail"
            + "".join(random.choice(numbers) for i in range(16))
            + "@roc.nl"
        )
        password = "12345"
        self.core_registration(page, unauthenticated, email=email, password=password)
        # Try to login, this shouldn't be possible since the account isn't created.
        page.goto(HOME_URL, wait_until="networkidle", timeout=30000)

        # Click span:has-text("Login")
        page.click('span:has-text("Inloggen")')
        # Fill [placeholder="Email input"]
        page.fill("#field-email", email)
        # Fill [placeholder="Password input"]
        page.fill("#field-password", "12345")
        # Submit the credentials and login.
        page.click("#submit-credentials")

        # Check if the error message appears.
        assert page.wait_for_selector(
            "#feedback >> text=Gebruikersnaam of wachtwoord onbekend, probeer een andere combinatie."
        ), f"De error message is niet verschenen met {unauthenticated.scope}@{browser_name}."

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_regular_account_logout(
        self, page: Page, browser_name, screenshot, regular_authenticated
    ):
        with regular_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)

            # Click #edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a
            page.click(
                "#edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a"
            )
            # Click a:has-text("Uitloggen")
            page.click('a:has-text("Uitloggen")')

            assert page.wait_for_selector(
                "#login-btn > span:nth-child(2)"
            ), f"De 'inloggen' knop is niet zichtbaar, dus er is niet succesvol uitgelogd met {context.scope}@{browser_name}."

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_roc_account_logout(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)

            # Click #edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a
            page.click(
                "#edwh-loaded-menu > div.navbar-item.bd-navbar-item.bd-navbar-item-base.has-dropdown > a"
            )
            # Click a:has-text("Uitloggen")
            page.click('a:has-text("Uitloggen")')

            assert page.wait_for_selector(
                "#login-btn > span:nth-child(2)"
            ), f"De 'inloggen' knop is niet zichtbaar, dus er is niet succesvol uitgelogd met {context.scope}@{browser_name}."


@pytest.mark.zoekbalk
class TestSearchbar:
    @pytest.mark.skipif(
        os.getenv("skip_statemachine") == "True",
        reason="Statemachine tests don't work well with xdist, so these are skipped if xdist is being used.",
    )
    @pytest.mark.statemachine
    def test_searchbar_result(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)
            # Search for a single tile (the entire tile title).
            search_term = "Migrate test item namenamename"
            page.fill("#qform_q", search_term)
            page.click("#qform > div > div:nth-child(1) > button")

            # Check if the inner_text from the tile is equal to the search_term.
            assert (
                page.inner_text(
                    "#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p"
                )
                == search_term
            ), f"Het gezochte item is niet gevonden met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p",
                screenshot_name=f"zoekbalk@test_searchbar_result=visible",
            )

            # Check if the search exists in the url (statemachine), single tile no tags.
            assert (
                "?q=Migrate%20test%20item%20namenamename" in page.url
            ), f"De URL komt niet overeen met de statemachine met {context.scope}@{browser_name}."

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_single_searchbar_result(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)
            # Search for a single tile (the entire tile title).
            search_term = "Migrate test item namenamename"
            page.fill("#qform_q", search_term)
            page.click("#qform > div > div:nth-child(1) > button")

            # Waiting for the network to be idle, before getting the text from a tile title.
            page.wait_for_load_state("networkidle")
            # Check if the inner_text from the tile is equal to the search_term.
            assert (
                page.inner_text(
                    "#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p"
                )
                == search_term
            ), f"Het gezochte item is niet gevonden met {context.scope}@{browser_name}."

            # Waiting for the network to be idle, due to selectors not being fully loaded after searching.
            page.wait_for_load_state("networkidle")

            # Check if there are additional items/tiles, there shouldn't be any.
            hrefs_of_page = page.eval_on_selector_all(
                "a[href^='/item/']",
                "elements => elements.map(element => element.href)",
            )
            assert (
                len(hrefs_of_page) < 3
            ), f"Er zijn meerdere items/tegels gevonden met {context.scope}@{browser_name}."

            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p",
                screenshot_name=f"zoekbalk@test_single_searchbar_result=visible",
            )

    @pytest.mark.skip(reason="No way of currently testing this.")
    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_searchbar_error_message(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)
            # Search for a random non-existing tile.
            letters = string.ascii_letters
            search_term = "".join(random.choice(letters) for i in range(16))
            page.fill("#qform_q", search_term)
            page.click("#qform > div > div:nth-child(1) > button")
            # Check if the error message exists.
            assert (
                page.inner_text(
                    "#tiles > div > div.column.has-text-centered > div.title"
                )
                == "Sorry, we konden niets vinden!"
            )

    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_searchbar_text_visible(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)
            # Search for a single tile (the entire tile title).
            search_term = "Migrate test item namenamename"
            page.fill("#qform_q", search_term)
            with page.expect_navigation():
                page.click("#qform > div > div:nth-child(1) > button")

            # Check if the text is still visible after searching.
            assert (
                page.eval_on_selector("#qform_q", "(element) => element.value")
                == search_term
            ), f"De text in de zoekbalk is verdwenen/gewijzigd met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#qform_q",
                screenshot_name=f"zoekbalk@test_searchbar_text_visible=search_without_quickfilter",
            )

            # Click on a quickfilter for more navigation.
            page.click("#qf-btn-1")
            # Check if the text is still visible after having clicked on the quickfilter.
            assert (
                page.eval_on_selector("#qform_q", "(element) => element.value")
                == search_term
            ), f"De text in de zoekbalk is verdwenen/gewijzigd met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#qform_q",
                screenshot_name=f"zoekbalk@test_searchbar_text_visible=search_with_quickfilter",
            )

            # Check if the text is still visible after reloading the page.
            assert (
                page.eval_on_selector("#qform_q", "(element) => element.value")
                == search_term
            ), f"De text in de zoekbalk is verdwenen/gewijzigd met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#qform_q",
                screenshot_name=f"zoekbalk@test_searchbar_text_visible=reloaded_page",
            )

    @pytest.mark.skipif(
        os.getenv("skip_statemachine") == "True",
        reason="Statemachine tests don't work well with xdist, so these are skipped if xdist is being used.",
    )
    @pytest.mark.statemachine
    def test_searchbar_with_filter(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)
            # Search for a general subject.
            search_term = "leren"
            page.fill("#qform_q", search_term)
            page.click("#qform > div > div:nth-child(1) > button")

            # Waiting for the network to be idle, before getting the text from a tile title.
            page.wait_for_load_state("networkidle")
            # Get the title from the first tile (without using the filter).
            title_without_filter = page.inner_text(
                "#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p"
            )
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p",
                screenshot_name=f"zoekbalk@test_searchbar_with_filter=visible_without_filter",
            )

            # Click on the filter dropdown.
            page.click("#filtermenu-open", delay=250)

            # Select a filter.
            page.click(
                "#filtermenu > div > div:nth-child(1) > ul > li:nth-child(1) > a",
                delay=250,
            )
            # Close the filter dropdown.
            page.click("#filtermenu-open", delay=250)

            # Waiting for the network to be idle, before getting the text from a tile title.
            page.wait_for_load_state("networkidle")
            # Get the title from the first tile (while using a filter).
            title_with_filter = page.inner_text(
                "#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p"
            )
            # Check if the tiles are different, by comparing the titles.
            assert (
                title_without_filter != title_with_filter
            ), f"De tegels zijn identiek met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p",
                screenshot_name=f"zoekbalk@test_searchbar_with_filter=visible_with_filter",
            )

            # Check if the filter exists in the URl (statemachine).
            assert (
                "?q=leren&tags=%5B%229b349ed2-b3d0-491f-99ea-53c31f6ae702%22%5D"
                in page.url
            ), f"De URL (statemachine) komt niet overeen met dat wat verwacht wordt met {context.scope}@{browser_name}"
            # Check if the page number is equal to one, by not having it specified in the URL (statemachine).
            assert (
                "&page=" not in page.url
            ), f"Het pagina nummer staat waarschijnlijk niet op 1, omdat '&page=' voorkomt in de url met {context.scope}@{browser_name}"

    @pytest.mark.skipif(
        os.getenv("skip_statemachine") == "True",
        reason="Statemachine tests don't work well with xdist, so these are skipped if xdist is being used.",
    )
    @pytest.mark.statemachine
    def test_searchbar_with_quickfilter(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)
            # Search for a general subject.
            search_term = "leren"
            page.fill("#qform_q", search_term)
            page.click("#qform > div > div:nth-child(1) > button")

            page.wait_for_load_state("networkidle")
            # Get the title from the first tile (without using the quickfilter).
            title_without_quickfilter = page.inner_text(
                "#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p"
            )
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p",
                screenshot_name=f"zoekbalk@test_searchbar_with_quickfilter=visible_without_quickfilter",
            )

            # Click on a quickfilter.
            page.click("#qf-btn-4")
            page.wait_for_load_state("networkidle")
            # Get the title from the first tile (while using a quickfilter).
            title_with_quickfilter = page.inner_text(
                "#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p"
            )
            # Check if the tiles are different, by comparing the titles.
            assert (
                title_without_quickfilter != title_with_quickfilter
            ), f"De tegels met en zonder quickfilter zijn identiek met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p",
                screenshot_name=f"zoekbalk@test_searchbar_with_quickfilter=visible_with_quickfilter",
            )

            # Check if the quickfilter exists in the URl (statemachine).
            assert (
                "?q=leren&qf=82c567e7-0ee5-442b-b9c6-289447f5ec4d" in page.url
            ), f"De URL (statemachine) komt niet overeen met dat wat vewacht wordt met {context.scope}@{browser_name}."
            # Check if the page number is equal to one, by not having it specified in the URL (statemachine).
            assert (
                "&page=" not in page.url
            ), f"Het pagina nummer staat waarschijnlijk niet op 1, omdat '&page=' voorkomt in de url met {context.scope}@{browser_name}."

            # Change the quickfilter again, from another quickfilter.
            page.click("#qf-btn-5")
            page.wait_for_load_state("networkidle")
            # Get the title from the first tile (while using a quickfilter).
            title_with_second_quickfilter = page.inner_text(
                "#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p"
            )

            # Test if the tiles are unique when switching quickfilter.
            assert (
                title_with_quickfilter != title_with_second_quickfilter
            ), f"De tegels met verschillende quickfilters zijn identiek met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p",
                screenshot_name=f"zoekbalk@test_searchbar_with_quickfilter=visible_with_second_quickfilter",
            )

            # Check if the quickfilter exists in the URl (statemachine).
            assert (
                "?q=leren&qf=e70d6a29-b026-4664-9ae0-7673c94af664" in page.url
            ), f"De URL (statemachine) komt niet overeen met dat wat vewacht wordt met {context.scope}@{browser_name}."
            # Check if the page number is equal to one, by not having it specified in the URL (statemachine).
            assert (
                "&page=" not in page.url
            ), f"Het pagina nummer staat waarschijnlijk niet op 1, omdat '&page=' voorkomt in de url met {context.scope}@{browser_name}."

    @pytest.mark.skipif(
        os.getenv("skip_statemachine") == "True",
        reason="Statemachine tests don't work well with xdist, so these are skipped if xdist is being used.",
    )
    @pytest.mark.statemachine
    def test_searchbar_item_and_author(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            # Go to the item page.
            page.goto(
                f"{HOME_URL}/item/{ROC_ITEM_GID}",
                wait_until="networkidle",
                timeout=30000,
            )
            # Search for a term.
            search_term = "leren"
            page.fill("#qform_q", search_term)
            page.click("#qform > div > div:nth-child(1) > button")
            # Check if the search has been executed within the URL.
            assert (
                "?q=leren" in page.url
            ), f"De zoekopdracht is niet succesvol uitgevoerd met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector=None,
                screenshot_name=f"zoekbalk@test_searchbar_item_and_author=item_search_visible",
            )

            # Go to the author page.
            page.goto(
                f"{HOME_URL}/user/{ROC_USER_GID}",
                wait_until="networkidle",
                timeout=30000,
            )
            # Search for a term.
            search_term = "leren"
            page.fill("#qform_q", search_term)
            page.click("#qform > div > div:nth-child(1) > button")
            # Check if the search has been executed within the URL.
            assert (
                "?q=leren" in page.url
            ), f"De zoekopdracht is niet succesvol uitgevoerd met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector=None,
                screenshot_name=f"zoekbalk@test_searchbar_item_and_author=author_search_visible",
            )


@pytest.mark.quickfilter
class TestQuickfilter:
    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_request_quickfilter(self, request_session):
        # All quickfilter urls
        quickfilter_urls = [
            FRONT_END_URL + "/quick-filter",
            FRONT_END_URL + "/quick-filter/slimfit",
            FRONT_END_URL + "/quick-filter/testing",
        ]

        # All quickfilter tag data
        default_quickfilter_data = [
            "56428ab5-78db-47dd-897b-a540284c7fc3",
            "bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7",
            "7afe35b0-881b-41bf-88ec-7e1d3fc774e3",
            "82c567e7-0ee5-442b-b9c6-289447f5ec4d",
            "e70d6a29-b026-4664-9ae0-7673c94af664",
            "3ce22256-df83-42f1-a8f8-34621066693e",
            "0e8c1ced-742c-40e0-8321-1d6fe5342345",
            "on_quick_filter_select(this,'Alles%20Tonen',null)",
            "on_quick_filter_select(this,'Coronavirus','56428ab5-78db-47dd-897b-a540284c7fc3')",
            "on_quick_filter_select(this,'Professionalisering','bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7')",
            "on_quick_filter_select(this,'Anders%20organiseren','7afe35b0-881b-41bf-88ec-7e1d3fc774e3')",
            "on_quick_filter_select(this,'Differentiatie','82c567e7-0ee5-442b-b9c6-289447f5ec4d')",
            "on_quick_filter_select(this,'School%20en%20samenleving','e70d6a29-b026-4664-9ae0-7673c94af664')",
            "on_quick_filter_select(this,'Het%20volgen%20van%20leerlingen','3ce22256-df83-42f1-a8f8-34621066693e')",
            "on_quick_filter_select(this,'21ste%20Eeuwse%20vaardigheden','0e8c1ced-742c-40e0-8321-1d6fe5342345')",
        ]
        slimfit_quickfilter_data = [
            "on_quick_filter_select(this,'Alles%20Tonen',null)",
        ]
        testing_quickfilter_data = [
            "0fc58d00-d187-4fd5-adbd-3980f901f2a9",
            "60107ed0-50ad-451b-971c-6d583832471a",
            "on_quick_filter_select(this,'Alles%20Tonen',null)",
            "on_quick_filter_select(this,'niet%20bestaand%201','0fc58d00-d187-4fd5-adbd-3980f901f2a9')",
            "on_quick_filter_select(this,'niet%20bestaand%202','60107ed0-50ad-451b-971c-6d583832471a')",
        ]

        def check_tag_data_and_onclick_data(url, obtainable_data):
            # Get all the tags from the quickfilters, and check if these exist within the quickfilter data.
            data_list = []
            for data in soup.find_all("button"):
                # Get the obtainable data and store it in _data.
                _data = data.get(obtainable_data)
                # Check if the data exists in button
                # (otherwise this code won't be ran due to the first <button> not having this data).
                if _data:
                    data_list.append(_data)
                    if url == FRONT_END_URL + "/quick-filter":
                        assert (
                            _data in default_quickfilter_data
                        ), f"De tag_data komt niet overeen met {url}."
                    if url == FRONT_END_URL + "/quick-filter/slimfit":
                        assert (
                            _data in slimfit_quickfilter_data
                        ), f"De tag_data komt niet overeen met {url}."
                    if url == FRONT_END_URL + "/quick-filter/testing":
                        assert (
                            _data in testing_quickfilter_data
                        ), f"De tag_data komt niet overeen met {url}."
                # Check if the data is unique..
                assert len(data_list) == len(set(data_list))

        # Go through urls, and check for proper response status code.
        for url in quickfilter_urls:
            response = request_session.get(url)
            assert (
                response.status_code == 200
            ), f"Er is geen 200 response status code met {url}"
            soup = BeautifulSoup(response.text, features="html.parser")

            check_tag_data_and_onclick_data(url=url, obtainable_data="data-tag-gid")
            check_tag_data_and_onclick_data(url=url, obtainable_data="onclick")

    @pytest.mark.skipif(
        os.getenv("skip_statemachine") == "True",
        reason="Statemachine tests don't work well with xdist, so these are skipped if xdist is being used.",
    )
    @pytest.mark.statemachine
    def test_quickfilter_back_and_forward_button_navigation(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)
            # Click on a quickfilter ("Professionalisering").
            page.click("#qf-btn-2")
            # Check if the URL contains the quickfilter (statemachine)
            assert (
                "qf=bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7" in page.url
            ), f"De quickfilter is niet te zien in de pagina URL met {context.scope}@{browser_name}."

            # Click on the other quickfilter ("Differentiatie").
            page.click("#qf-btn-4")
            # Check if the URL contains the quickfilter (statemachine)
            assert (
                "qf=82c567e7-0ee5-442b-b9c6-289447f5ec4d" in page.url
            ), f"De quickfilter is niet te zien in de pagina URL met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector=None,
                screenshot_name=f"quickfilter@test_quickfilter_back_and_forward_button_navigation=last_quickfilter_visible",
            )

            # Navigate using the back and forward button, and check if this is working.
            # Back button.
            page.go_back()
            # Check if the navigation is working properly.
            assert (
                "qf=bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7" in page.url
            ), f"De quickfilter is niet te zien in de pagina URL met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector=None,
                screenshot_name=f"quickfilter@test_quickfilter_back_and_forward_button_navigation=first_quickfilter_visible",
            )

            # Forward button.
            page.go_forward()
            # Check if the navigation is working properly.
            assert (
                "qf=82c567e7-0ee5-442b-b9c6-289447f5ec4d" in page.url
            ), f"De quickfilter is niet te zien in de pagina URL met {context.scope}@{browser_name}."

            # Back button twice, to go to the homepage.
            page.go_back()
            page.go_back()
            # Check if the navigation is working properly.
            assert (
                page.url == HOME_URL + "/"
            ), f"De pagina is niet succesvol teruggegaan naar de homepage met {context.scope}@{browser_name}."
            # Take a screenshot if the CLI argument --screenshot is given.
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector=None,
                screenshot_name=f"quickfilter@test_quickfilter_back_and_forward_button_navigation=homepage_visible",
            )

    @pytest.mark.skipif(
        os.getenv("skip_statemachine") == "True",
        reason="Statemachine tests don't work well with xdist, so these are skipped if xdist is being used.",
    )
    @pytest.mark.statemachine
    def test_selected_quickfilter_active_and_traceable_after_state_change(
        self,
        page: Page,
        browser_name,
        screenshot,
        roc_authenticated,
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)
            # Click on a quickfilter ("Professionalisering").
            page.click("#qf-btn-2")
            # Check if the URL contains the quickfilter (statemachine)
            assert (
                "qf=bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7" in page.url
            ), f"De quickfilter is niet te zien in de pagina URL met {context.scope}@{browser_name}."
            quickfilter_url = page.url

            # Check if the quickfilter remains consistent after a state change (reload).
            page.reload()
            assert (
                "qf=bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7" in page.url
            ), f"De quickfilter is niet te zien in de pagina URL met {context.scope}@{browser_name}."
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector=None,
                screenshot_name=f"quickfilter@test_selected_quickfilter_active_after_state_change=quickfilter_visible",
            )

            # Go to the quickfilter page.
            page.goto(quickfilter_url)
            # Check if the URL contains the quickfilter (statemachine)
            assert (
                "qf=bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7" in page.url
            ), f"De quickfilter is niet te zien in de pagina URL met {context.scope}@{browser_name}."
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector=None,
                screenshot_name=f"quickfilter@test_selected_quickfilter_active_after_state_change=quickfilter_traceable",
            )

    @pytest.mark.skipif(
        os.getenv("skip_statemachine") == "True",
        reason="Statemachine tests don't work well with xdist, so these are skipped if xdist is being used.",
    )
    @pytest.mark.statemachine
    def test_different_quickfilter_and_filter_selections(
        self, page: Page, browser_name, screenshot, roc_authenticated
    ):
        with roc_authenticated() as context:
            page.goto(HOME_URL, wait_until="networkidle", timeout=30000)
            # Check if there are enough tiles without using filters.
            hrefs_of_page = page.eval_on_selector_all(
                "a[href^='/item/']",
                "elements => elements.map(element => element.href)",
            )
            assert (
                len(hrefs_of_page) > 8
            ), f"Er te weinig tegels gevonden zonder filters met {context.scope}@{browser_name}."
            # Click on a quickfilter ("Professionalisering").
            page.click("#qf-btn-2")
            # Check if the URL contains the quickfilter (statemachine)
            assert (
                "qf=bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7" in page.url
            ), f"De quickfilter is niet te zien in de pagina URL met {context.scope}@{browser_name}."

            # Open the filter dropdown
            page.click("#filtermenu-open")
            # Click on all the filters (14 t/m 18 jaar (bovenbouw VO), personeel, ICT ontwikekling, Primair onderwijs (po))
            page.click("text=14 t/m 18 jaar (bovenbouw VO)", delay=500)
            page.click("text=Personeel", delay=500)
            page.click("text=ICT ontwikkeling", delay=500)
            page.click("text=Primair onderwijs (po)", delay=500)
            # Close the filter dropdown
            page.click("#filtermenu-open", delay=500)

            page.wait_for_load_state("networkidle")
            # Check tiles..
            assert (
                page.inner_text(
                    "#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p"
                )
                == "Migrate test item namenamename"
            ), f"Het gezochte item is niet gevonden met {context.scope}@{browser_name}."
            # Take screenshot
            take_screenshot(
                screenshot,
                page,
                browser_name,
                scroll_selector="#tiles > div > div.edwh-column-card > article > div > div.edwh-card-heading > a > p",
                screenshot_name=f"quickfilter@test_different_quickfilter_and_filter_selections=expected_tile_visible",
            )

    # Future tests:
    @pytest.mark.skip(
        reason="The roc tile still has to be made using the insert statement in the migrate."
    )
    @pytest.mark.skipif(
        os.getenv("skip_regular") == "True",
        reason="Regular tests shouldn't be ran when running statemachine without xdist.",
    )
    def test_roc_tiles_visibility(self):
        return
