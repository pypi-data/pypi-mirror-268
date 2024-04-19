"""
This file defines the database models
"""
import json
import os
import pathlib
import warnings

import redis
import requests

from py4web import HTTP, response

from . import settings
from .common import Field, db, leidendb

db.define_table("gebruiker", Field("naam"))

db.define_table("rol", Field("naam"))

db.define_table(
    "gebruiker_rol",
    Field("gebruiker_id", "reference gebruiker"),
    Field("rol_id", "reference rol"),
)

db.commit()


class Plaatsen:
    def __init__(self):
        app_dir = pathlib.Path(__file__).parent.resolve()
        _plaatsfile = os.path.join(app_dir, "databases/slugified_plaatsen.json")

        with open(_plaatsfile) as plaatsfile:
            p = json.load(plaatsfile)
            self.plaatsen_exact = {p["plaats"]: p["plaats"] for key, p in p.items()}
            self.plaatsen_loose = {key: p["plaats"] for key, p in p.items()}

    def find_plaatsen(self, query):
        LIMIT = 10

        locations = list(
            {
                p
                for key, p in self.plaatsen_exact.items()
                if query.lower() in key.lower()
            }
        )
        limited_locations = locations[:LIMIT]
        if len(limited_locations) < LIMIT:
            more_locations = list(
                {
                    p
                    for key, p in self.plaatsen_loose.items()
                    if query.lower() in key.lower() and p not in locations
                }
            )
            locations += more_locations

        return sorted(locations[:LIMIT])


def setup_redis():
    host, port = settings.REDIS_SERVER.split(":")
    # for more options: https://github.com/andymccurdy/redis-py/blob/master/redis/client.py
    return redis.Redis(host=host, port=int(port))


redis_conn = setup_redis()


# todo: check?


class Scholen:
    _APIKEY = "56f37c57ba60eb4527caf417bb29fc9a353f1086abd7cf4d8959cad8073f63b2"  # todo: change
    _headers = {
        "ovio-api-key": _APIKEY,
    }

    def find_scholen(self, query):
        warnings.warn("Deprecated, please use your internal organisations table!")

        if cached := redis_conn.get(query.lower()):
            return json.loads(cached), "cached"

        url = (
            f"https://api.overheid.io/openkvk"
            f"?query={query}"
            f"&fields[]=plaats"
            f"&fields[]=handelsnaam"
            f"&fields[]=straat"
            f"&fields[]=huisnummer"
            f"&fields[]=postcode"
            f"&fields[]=sbi"
            f"&fields[]=statutairehandelsnaam"
            f"&queryfields[0]=plaats"
            f"&queryfields[1]=handelsnaam"
            f""
        )

        bedrijven = (
            requests.get(url, headers=self._headers)
            .json()
            .get("_embedded", {})
            .get("bedrijf", {})
        )
        answer = {
            b["handelsnaam"]: b["dossiernummer"]
            for b in bedrijven
            if any([str(sbi).startswith("85") for sbi in b.get("sbi", [])])
        }
        redis_conn.set(query.lower(), json.dumps(answer))
        return answer, "fresh"


plaatsen = Plaatsen()
scholen = Scholen()


def _calculate_star_average(
    results: list[int],
) -> tuple[int, int, list[dict[str, int | bool]]]:
    """
    Count the average star score of results
    results are an array of this structure:
    [amount of 1 star reviews, 2 stars, ..., 5 stars]
    """
    if not results:
        return 0, 0, []
    count = sum(results)

    total = 0
    details = []
    for ind, value in enumerate(results):
        stars = ind + 1

        frac = value / count if count else 0

        details.append(
            {
                "fraction": round(frac * 100),
                "stars": stars,
                "count": value,
                "singular": not stars - 1,  # true for 1
            }
        )
        total += stars * frac  # index + 1 = amount of stars given

    return count, total, details


leidendb.define_table(
    "ratings",
    Field("post_id"),
    Field("rating", "integer"),
    Field("session_id"),
    Field("platform"),
    # platform, bijv. leiden
)


def _set_header(key: str, value: str):
    response.headers[key] = value


# minder ambigue dan 303 (See Other)
def redirect_permanent(location: str):
    _set_header("Location", location)
    raise HTTP(301)


def redirect_temporary(location: str):
    _set_header("Location", location)
    raise HTTP(302)
