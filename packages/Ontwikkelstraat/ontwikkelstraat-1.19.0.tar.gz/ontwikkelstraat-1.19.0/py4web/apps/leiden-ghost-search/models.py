"""
This file defines the database models
"""

import os
import sqlite3

from pydal.validators import *

from .common import Field, cache, db
from .ghost import GhostAdmin

SITE_CONFIG = {
    "url": "https://archief.meteddie.nl/",
    "adminAPIKey": os.getenv("GHOST_ADMIN_API_KEY"),  # _LEIDEN ?
    "contentAPIKey": os.getenv("GHOST_CONTENT_API_KEY"),  # _LEIDEN
}
g = GhostAdmin(**SITE_CONFIG)


class VirtualDb:
    fields = []
    in_mem_db = None
    cur = None

    def __init__(self):
        # self.setup_db()
        # self.fill_db()
        ...  # fixme: setup_db mot eerst werken

    def setup_db(self):
        in_mem_db = sqlite3.connect(":memory:")
        cur = in_mem_db.cursor()

        return  ###  FTS5 WERKT NIET IN ONZE DOCKER

        in_mem_db.enable_load_extension(True)
        in_mem_db.load_extension("ftstri")

        cur.execute(
            """
          create virtual table posts using FTS5(id unindexed, title, body, tokens, tokenize='trigram')
        """
        )

        self.fields = "id,title,body,tokens".split(",")
        self.in_mem_db = in_mem_db
        self.cur = cur

    def fill_db(self):
        cur = self.cur

        alle_posts = g.getAllPosts()

        cur.execute("DELETE FROM posts;")
        cur.executemany(
            """
          INSERT INTO posts VALUES (?, ?, ?, ?)
        """,
            [
                (
                    post["uuid"],
                    post["title"],
                    " ".join(BeautifulSoup(post["html"]).stripped_strings),
                    stemmed(" ".join(BeautifulSoup(post["html"]).stripped_strings)),
                )
                for post in alle_posts
            ],
        )
        cur.execute("commit")


mem_db = VirtualDb()
