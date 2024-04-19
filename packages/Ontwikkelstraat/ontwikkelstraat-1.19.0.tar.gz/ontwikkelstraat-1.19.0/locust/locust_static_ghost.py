import os
import random
import time

from bs4 import BeautifulSoup

from locust import HttpUser, between, tag, task

# Get environment variables.
ROC_EMAIL = os.getenv("roc_email")
ROC_PASSWORD = os.getenv("roc_password")

data = {
    "FRONT_END_BASE": "/front_end/",
    "GHOST_BASE": "/ghost/",
    "item_uri_template": "/ghost/item/{}",
    "likes": [],
    "limit": 9,
    "login_url": "/front_end/login",
    "order": "",
    "page": 1,
    "q": "",
    "qf": "",
    "tags": [],
    "user_uri_template": "/ghost/user/{}",
}

collected_gids = []


def random_gid():
    return random.choice(collected_gids)


def discovered_gid(gid):
    if gid not in collected_gids:
        collected_gids.append(gid)


class StaticGhostSpeedTest(HttpUser):
    wait_time = between(1, 3)

    @tag("request_tiles")
    @task
    def request_tiles(self):
        # create a copy of the dictionary to give each 'user' their own data
        _data = data.copy()
        while True:
            response = self.client.post("/front_end/tiles", json=_data, name="tiles")
            soepje = BeautifulSoup(response.text, features="html.parser")
            for article in soepje.find_all("article"):
                discovered_gid(article.a["href"].split("/")[-1])
            pagination_next = soepje.find_all("a", attrs={"class": "pagination-next"})
            next_button = pagination_next[0] if pagination_next else []
            if not next_button:
                break
            if random.randint(1, 5) == 1:
                break
            _data["page"] += 1
            time.sleep(random.randint(3, 10))

    @tag("request_quick_filter")
    def request_quick_filter(self):
        _data = data.copy()
        quick_filter_data = [
            "56428ab5-78db-47dd-897b-a540284c7fc3",
            "bd8a4db1-33e2-4ed1-b0e6-fe0998295aa7",
            "7afe35b0-881b-41bf-88ec-7e1d3fc774e3",
            "82c567e7-0ee5-442b-b9c6-289447f5ec4d",
            "e70d6a29-b026-4664-9ae0-7673c94af664",
            "3ce22256-df83-42f1-a8f8-34621066693e",
            "0e8c1ced-742c-40e0-8321-1d6fe5342345",
        ]
        _data["qf"] = "".join(random.choice(quick_filter_data))
        # List with quick-filter URl's.
        self.client.post("/front_end/tiles", json=_data, name="quick-filter")

    @tag("request_filter")
    def request_filter(self):
        # create a copy of the dictionary to give each 'user' their own data
        _data = data.copy()
        filter_data = [
            '["%229b349ed2-b3d0-491f-99ea-53c31f6ae702%22"]',
            '["%22c1add226-83a0-4f33-8e6d-f6918189ade4%22"]',
            '["%22c85461ed-d24e-4a0c-912d-8eca4f68293e%22"]',
            '["%2203ba8cb4-a58d-4ba9-9862-a08144511c13%22"]',
            '["%228856b32d-dcfd-4a29-baa7-679888418938%22"]',
            '["%2254b0f0ca-5edc-4e6c-ae55-6be94316ab3a%22"]',
            '["%22146214d3-6091-4aff-bfdf-3f50d41d2e8a%22"]',
            '["%222d700548-3e70-445b-8952-cad416e8f076%22"]',
            '["%22ba3686a9-bc1e-4387-8cfc-e2737f07bc62%22"]',
            '["%2258892b54-e349-4579-984e-c68c7ee084be%22"]',
            '["%2265866c5a-5cb9-4dbd-8e9a-79515fe43aba%22"]',
            '["%22c1add226-83a0-4f33-8e6d-f6918189ade4%22","%2254b0f0ca-5edc-4e6c-ae55-6be94316ab3a%22","%2222615965-b307-4d39-b4ea-871e6baa6854%22"]',
            '["%229b349ed2-b3d0-491f-99ea-53c31f6ae702%22","%228856b32d-dcfd-4a29-baa7-679888418938%22","%228dbaad22-638d-46bd-8471-69181176fad6%22","%22a155acde-4ad8-4b8c-9693-a2eecef3c4c2%22","%22ed8d8d22-3578-435d-b943-3584fe853792%22"]',
            '["c85461ed-d24e-4a0c-912d-8eca4f68293e","146214d3-6091-4aff-bfdf-3f50d41d2e8a","684af7bc-9db2-4f1d-b66f-04e307f39809","4225d914-d4c8-4f89-85c5-11e26f853afa","54b0f0ca-5edc-4e6c-ae55-6be94316ab3a","a7d16fab-be3a-4f85-a04c-f985131c00f3","ba3686a9-bc1e-4387-8cfc-e2737f07bc62"]',
        ]
        _data["tags"] = "".join(random.choice(filter_data))
        self.client.post("/front_end/tiles", json=_data, name="filter")

    @tag("request_menu")
    def request_menu(self):
        # create a copy of the dictionary to give each 'user' their own data
        secret_data = {"hardware": {}, "password": ROC_PASSWORD, "username": ROC_EMAIL}
        self.client.post("/front_end/menu", json=secret_data, name="menu")

    @tag("request_items")
    @task
    def request_item(self):
        # Open an item
        self.request_menu()
        self.client.get(str("/front_end/item/" + random_gid()), timeout=15, name="item")

    def on_start(self):
        self.client.get("/ghost", name="homepage")
        self.request_filter()
        self.request_menu()
        self.request_quick_filter()
