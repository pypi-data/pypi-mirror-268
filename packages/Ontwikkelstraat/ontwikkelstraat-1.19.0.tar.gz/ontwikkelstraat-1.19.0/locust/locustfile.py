import csv
import json
import random
import sys
import time
from pathlib import Path

import urllib3
from bs4 import BeautifulSoup

from locust import HttpUser, between, constant, tag, task

sys.path.append("../")
import datetime
import os

from tasks import read_dotenv

# schakelt de waarschuwingen uit voor wanneer de loadtest lokaal uitgetest wordt
urllib3.disable_warnings()


class SimulateUsers(HttpUser):
    # alle standaard informatie die nodig is om locust functioneel te laten lopen
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.random_word = ""
        self.random_qf = ""
        self.how_many_pages = None
        self.post_response = None
        self.get_response = None

    # de simulatie zelf, dus waar elke 'gebruiker' doorheen gaat
    @task
    def simulation(self):
        # bijhouden van het aantal requests om daar later een simulatie aan te koppelen
        count_the_requests_per_user = 0
        # kiest een random getal uit en dat later te vergelijken met het aantal requests per 'gebruiker'
        random_choosing = round(random.uniform(1, 11))
        os.system("rm locust_output.csv")
        # loopje omheen gezet om elke 'gebruiker' door het 100 pagina's te laten bladeren
        for browsing in range(1, 101):
            Stats.stats_to_csv_file(self)
            # elke 'gebruiker' 'checkt' ongeveer 3 seconde per pagina naar de tiles
            time.sleep(1)
            count_the_requests_per_user += 1
            print("counts per user: " + str(count_the_requests_per_user))
            # standaard informatie ophalen van de tiles etc, zodat het bij het lezen van de tiles niks verkeerd kan gaan
            self.post_response = self.client.post(
                "/fragmentx/tiles",
                json={
                    "qf": "",
                    "q": "",
                    "page": round(1, ThePages.how_many_pages(self)),
                    "tags": [],
                    "order": "",
                    "GHOST_BASE": "/",
                    "FRONT_END_BASE": "/fragmentx",
                    "limit": 9,
                    "paginate": True,
                    "item_uri_template": "/cmsx/item/{}",
                    "user_uri_template": "/cmsx/user/{}",
                    "login_url": "https://fragments.meteddie.nl/v1.0/front_end/login",
                },
                verify=False,
            )
            # controleert of het random getal en het aan requests per 'gebruiker' gelijk zijn
            # om daarvan een simulatie uit te laten kiezen
            if count_the_requests_per_user == random_choosing:
                which_simulation = round(random.uniform(1, 16))
                # zorgt ervoor dat de 'gebruiker' eerst een zoekopdracht uitvoert en daarna even doorheen scrolt
                if which_simulation < 6:
                    Search.search_simulation(self)
                    ThePages.how_many_pages(self)
                    ThePages.browsing_through_pages(self)
                    # zorgt ervoor dat de 'gebruiker' een quick filter uitvoert en daarna even doorheen scrolt
                if 6 <= which_simulation <= 11:
                    QuickFilter.quickfilter_simulation(self)
                    ThePages.how_many_pages(self)
                    ThePages.browsing_through_pages(self)
                # gaat de tile lezen
                ReadTiles.read_simulation(self)
                # gaat weer een random getal erbij optellen zodat die 'meegaat' met het aantal requests per 'gebruiker'
                random_choosing += round(random.uniform(1, 10))


# deze klasse gaat dus kijken hoeveel pagina's er in totaal zijn en bij de search en quickfilter etc
# daarna gaat die een random getal daar uit kiezen en zovaak weer random gaan browsen door bijv dezelfde search opdracht
class ThePages(SimulateUsers):
    def how_many_pages(self):
        # hierbij gebruikt die dus de gegevens die misschien eerder zijn aangeroepen dan deze functie
        # en anders gewoon de standaard die in de parent klasse staat
        self.post_response = self.client.post(
            "/fragmentx/tiles",
            json={
                "qf": self.random_qf,
                "q": self.random_word,
                "page": "1",
                "tags": [self.random_qf],
                "order": "",
                "GHOST_BASE": "/",
                "FRONT_END_BASE": "/fragmentx",
                "limit": 9,
                "paginate": True,
                "item_uri_template": "/cmsx/item/{}",
                "user_uri_template": "/cmsx/user/{}",
                "login_url": "https://fragments.meteddie.nl/v1.0/front_end/login",
            },
            verify=False,
        )
        # via de html parser van de library bs4 bekijkt die dus hoeveel pagina's er bij zitten
        soup = BeautifulSoup(self.post_response.text, "html.parser")
        # hierbij pakt die dus het laatste getal (alle pagina's)
        try:
            self.how_many_pages = soup.find_all(class_="pagination-link")[-1].get_text()
        except IndexError:
            self.how_many_pages = 1
        print("how many pages: " + str(self.how_many_pages))

    def browsing_through_pages(self):
        # bij deze gebruikt die de dezelfde gegevens als hierboven alleen dan gaat die nog naar random pagina's toe
        how_many_times_random = round(random.uniform(1, int(self.how_many_pages)))
        print(how_many_times_random)
        # de for loop is bepaald door het aantal pagina's en daar een random getal uit te gaan kiezen
        for browsing in range(1, how_many_times_random + 1):
            Stats.stats_to_csv_file(self)
            # de 'gebruiker' 'checkt' weer een paar seconde om de tiles te scannen
            time.sleep(3)
            # hiermee gaat die dus via de how_many_pages een random getal uitkiezen en daarna gaat die naar die pagina
            random_page = round(random.uniform(1, int(self.how_many_pages)))
            self.post_response = self.client.post(
                "/fragmentx/tiles",
                json={
                    "qf": self.random_qf,
                    "q": self.random_word,
                    "page": random_page,
                    "tags": [self.random_qf],
                    "order": "",
                    "GHOST_BASE": "/",
                    "FRONT_END_BASE": "/fragmentx",
                    "limit": 9,
                    "paginate": True,
                    "item_uri_template": "/cmsx/item/{}",
                    "user_uri_template": "/cmsx/user/{}",
                    "login_url": "https://fragments.meteddie.nl/v1.0/front_end/login",
                },
                verify=False,
            )
            print("random page: " + str(random_page))


# in deze klasse zit een hele woordenlijst achter van alle woorden die in alle tiles dus voorkomen
# (het is niet recent, dus er kunnen oudere woorden in zitten / de nieuwste woorden kunnen er ook NIET in zitten)
class Search(SimulateUsers):
    def search_simulation(self):
        print(f"SEARCH")
        # haalt de woordenlijst binnen
        hosting_domain = read_dotenv(Path("../.env")).get("HOSTINGDOMAIN")
        word_list = self.client.get(
            f"https://web2py.{hosting_domain}/init/default/word_freq", verify=False
        ).json()
        key_list = []
        # voegt elk woord toe en zet die in een lijst
        for key in word_list:
            key_list.append(key)
        # bekijkt wat de laatste index is om daarmee dus een random 1 uit te kiezen
        last_one = key_list[-1]
        how_many_words = key_list.index(last_one)
        random_number = random.uniform(1, int(how_many_words))
        self.random_word = key_list[round(random_number)]
        print("random word: " + self.random_word)


# deze klasse is voor alle quickfilters, hiermee gaat die dus random 1 van uit kiezen en klikt die dan op die qf
# en bezoekt die een paar pagina's daarvan
class QuickFilter(SimulateUsers):
    def quickfilter_simulation(self):
        print("QUICKFILTER")
        self.post_response = self.client.post(
            "/fragmentx/quick-filter",
            json={
                "qf": "",
                "q": "",
                "page": "1",
                "tags": [],
                "order": "",
                "GHOST_BASE": "/",
                "FRONT_END_BASE": "/fragmentx",
                "limit": 9,
                "paginate": True,
                "item_uri_template": "/cmsx/item/{}",
                "user_uri_template": "/cmsx/user/{}",
                "login_url": "https://fragments.meteddie.nl/v1.0/front_end/login",
            },
            verify=False,
        )
        # haalt alle quickfilters er uit via bs4
        soup = BeautifulSoup(self.post_response.text, "html.parser")
        quick_filters = soup.find_all(attrs={"data-tag-gid": True})
        # pakt alleen de quickfilter
        self.random_qf = quick_filters[random.randint(1, len(quick_filters))].attrs[
            "data-tag-gid"
        ]
        print("qf_simulation: " + self.random_qf)


# deze klasse is het 'lezen' van de tiles
class ReadTiles(SimulateUsers):
    def read_simulation(self):
        print("READING")
        # haalt als eerste een random tile op
        soup = BeautifulSoup(self.post_response.text, "html.parser")
        tiles_list = []
        tiles_list_without_none = []
        # hierbij gaat die dus bij elke a de inhoud ophalen
        for link in soup.find_all("a"):
            tiles_list.append(link.get("href"))
        # zorgt ervoor dat alle None's uit de lijst verwijderd wordt
        for without_none in tiles_list:
            if without_none is not None:
                tiles_list_without_none.append(without_none)
        tile = random.choice(tiles_list_without_none)
        # pakt alleen het achterste gedeelte, omdat je anders ook 'cmsx/item' erbij hebt staan
        tile = tile.split("/")[3]
        print(f"tile: {tile}")
        # gaat naar die tile toe die random is uitgekozen
        self.get_response = self.client.get(
            "/fragmentx/item?item_id=" + tile + "&GHOST_BASE=/&FRONT_END_BASE"
            "=/fragmentx&item_uri_template=/cmsx"
            "/item/{"
            "}&user_uri_template=/cmsx/user/{"
            "}&login_url=https://fragments"
            ".meteddie.nl/v1.0/front_end/login",
            verify=False,
        )
        # gaat het weer ontleden om alle tekst eruit te halen
        # om daarna het aantal woorden te delen door 5 / 11 (leestempo)
        get_soup = BeautifulSoup(self.get_response.text, "html.parser")
        read_text = get_soup.find("div", class_="content").getText(" ", strip=True)
        word_count = read_text.count(" ")
        time_to_read = word_count / round(random.uniform(5, 11))
        print(f"Time to read: {time_to_read}")
        # daarna 'leest/scant' de gebruiker dus door de tekst
        time.sleep(time_to_read)
        # time.sleep(2)
        # als laatste begint het hele proces weer opnieuw
        SimulateUsers.__init__(self, self.parent)


class Stats(SimulateUsers):
    def stats_to_csv_file(self):
        all_stats = self.client.get("http://0.0.0.0:8089/stats/requests")
        all_stats = all_stats.json()
        dict_stats = {}
        dict_stats.update({"date": datetime.datetime.now()})
        for key in all_stats.keys():
            if all_stats[key] is None:
                all_stats[key] = 0
            if key == "current_response_time_percentile_50":
                dict_stats.update({"median respone time 50": str(all_stats[key])})
            if key == "current_response_time_percentile_95":
                dict_stats.update({"median respone time 95": str(all_stats[key])})
            if key == "total_rps":
                dict_stats.update({"total rps": str(all_stats[key])})
        print(dict_stats)

        with open("locust_output.csv", "a") as file:
            file.write(json.dumps(dict_stats, default=str))


# import random
#
#
# class SamenhangendeComponentenTest(HttpUser):
#     wait_time = constant(1)
#
#     @tag("simple")
#     @task(10)
#     def simple(self):
#         # _from = 1 if random.randint(1, 100) < 60 else random.randint(1, 80)
#         self.client.get("/simple")
#
#     @tag("sleepy")
#     @task(1)
#     def met_sleep(self):
#         # _from = 1 if random.randint(1, 100) < 60 else random.randint(1, 80)
#         self.client.get("/sleep/10")
#
#     @tag("simple_request")
#     @task()
#     def met_simple_requests(self):
#         # _from = 1 if random.randint(1, 100) < 60 else random.randint(1, 80)
#         self.client.get("/request?url=http://graphql/simple")
#
#     @tag("sleepy_request")
#     @task()
#     def met_sleepy_requests(self):
#         # _from = 1 if random.randint(1, 100) < 60 else random.randint(1, 80)
#         self.client.get("/request?url=http://graphql/sleep/10")
