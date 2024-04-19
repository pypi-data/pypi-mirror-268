import os
from collections import defaultdict

# verdieping:
import ghost
import yarl
from bs4 import BeautifulSoup
from ycecream import y

from py4web import action, request

from .common import cache, session
from .handlebars import Handlebars, handlebars_helpers
from .helpers import ServerURL as URL

# enquete:
from .klassen_enquete import VERSIES, StandaardVraag, Versie, bereken

y.configure(enabled=os.getenv("ENABLE_ICECREAM"))


@action("index")
@action.uses(session, "klassen_index.html")
def index():
    return dict(
        server=request.urlparts.scheme + "://" + request.urlparts.netloc,
    )


vraag_hbs = Handlebars("kansen/vraag.hbs", helpers=handlebars_helpers)
uitleg_hbs = Handlebars("kansen/thema_uitleg.hbs", helpers=handlebars_helpers)
uitleg_schoolleider_hbs = Handlebars(
    "kansen/thema_uitleg_schoolleider.hbs", helpers=handlebars_helpers
)
stapel_hbs = Handlebars("kansen/stapel.hbs", helpers=handlebars_helpers)
uitslag_hbs = Handlebars("kansen/enquete_uitslag.hbs", helpers=handlebars_helpers)
verdieping_hbs = Handlebars("kansen/verdieping.hbs", helpers=handlebars_helpers)


class NietBestaandeVraag(StandaardVraag):
    vraag = ""


@action("cookie-check", method=["POST"])
@action.uses(session)
def cookie_check():
    post_url = URL("enquete", scheme="https") + "?restart"
    return f"<div hx-trigger='load' hx-post='{post_url}'>"


@action("enquete", method=["GET", "POST"])
@action("enquete/<vraag_nr:int>", method=["GET", "POST"])
@action.uses(session, vraag_hbs)
def enquete(vraag_nr=0):
    if not request.get_cookie(request.app_name + "_session"):
        # no cookie set! user is blocking our cookies 🥺
        # tijd om boos te worden 😡
        return """
            <div class="box">Het lijkt er op dat third party cookies geblokkeerd worden. 
            Sta deze toe om verder te gaan. Het kan vaak worden opgelost door de "Niet volgen" / "Do not track" instelling uit te schakelen. Hulp nodig? Bekijk de onderstaande bronnen.
             <div class="content">
              <ol>`
                <li>Microsoft: <a href="https://support.microsoft.com/nl-nl/windows/do-not-track-gebruiken-in-internet-explorer-11-ad61fa73-d533-ce96-3f64-2aa3a332e792">Do Not Track gebruiken in Internet Explorer 11</a></li>
                <li>Google: <a href="https://support.google.com/chrome/answer/2790761?hl=en&co=GENIE.Platform%3DAndroid&oco=0">'Niet bijhouden' in- of uitschakelen</a></li>
                <li>Apple (Mac): <a href="https://support.apple.com/nl-nl/guide/safari/sfri40732/mac">Voorkomen dat gekoppelde sites je volgen in Safari op de Mac</a><br>
                  </li>
                  <li>Apple (iOS): <a href="https://www.apple.com/nl/legal/privacy/data/nl/safari/">Safari en privacy</a><br>
                  </li>
              </ol>
             </div>
            </div>`
            """
    # versie:
    """
    hx-vals='js:{
                  "versie": sessionStorage.versie
                  }'
    """
    versie = request.forms.get("versie")

    if versie not in VERSIES:
        return (
            ""  # geen error want dat ziet de user als die nog geen versie gekozen heeft
        )
        # raise ValueError("Ongeldige Versie")

    versie: Versie = VERSIES[versie]

    vragen = versie.VRAGEN
    # ?restart betekent een reset van de antwoorden
    vraag_object = (
        vragen[vraag_nr] if vraag_nr < versie.MAX_VRAGEN else NietBestaandeVraag
    )

    antwoorden = {} if "restart" in request.query else session.get("antwoorden", {})
    volgende_vraag = vraag_nr + 1 if vraag_nr < versie.MAX_VRAGEN else None
    volgende_argument = vraag_nr + 1
    vorige_argument = vraag_nr - 1

    vraag_id = f"q{vraag_nr}"
    vorige_vraag_id = f"q{vorige_argument}"

    # https://bottlepy.org/docs/dev/api.html#bottle.MultiDict - request.params is afgeleide hiervan
    # daarom moeten we even voor list values hier omheen werken

    if gegeven_antwoord := request.params.get(vorige_vraag_id):
        antwoorden[vorige_vraag_id] = gegeven_antwoord

    resultaat = bereken(antwoorden, versie)
    compleet = resultaat.compleet
    scores = resultaat.scores
    top_themas_en_scores = resultaat.top_themas

    session["antwoorden"] = antwoorden
    template = {
        "uitleg": uitleg_hbs,
        "uitleg_schoolleider": uitleg_schoolleider_hbs,
        "stapel": stapel_hbs,
        "vraag": vraag_hbs,
        "uitslag": uitslag_hbs,
    }.get(vraag_object.template, vraag_hbs)

    base_url = (
        yarl.URL(request.headers.get("origin", "https://gelijkekansenindeklas.nl"))
        / versie.HOMEPAGE
    )
    for top_thema in top_themas_en_scores or []:
        #  href "/" wordt door htmx met https://delen.meteddie.nl/.... geprefixt,
        #  dus we moeten een absolute url opgeven!
        top_thema[
            "htmx_thema_div"
        ] = """
            <div _="on load log '{ghost_id}' then log '{base_url}'" ghost_id="{ghost_id}" hx-trigger="load" hx-get="{base_url}" hx-select="#{ghost_id}" hx-swap="outerHTML"></div>
        """.format(
            base_url=base_url, **top_thema
        )

    data = dict(
        context=dict(
            vraag=vraag_nr,
            vraag_object=vraag_object,
            volgende_vraag=volgende_vraag,
            volgende_argument=volgende_argument,
            vorige_argument=vorige_argument,
            first_question=vorige_argument < 0,
            beantwoord=range(vraag_nr),
            onbeantwoord=range(1, versie.MAX_VRAGEN - vraag_nr),
            vraag_id=vraag_id,
            antwoorden=antwoorden,
            compleet=compleet,
            score=scores,
            top_themas_en_scores=top_themas_en_scores,
            vorige_vraag_url=URL("enquete", vorige_argument, scheme="https"),
            volgende_vraag_url=URL("enquete", volgende_argument, scheme="https"),
            restart_url=URL("enquete", scheme="https") + "?restart",
        )
    )

    return template.transform(data)


@action("verdieping", method=["GET", "POST"])
@action.uses(verdieping_hbs)
@cache.memoize(3600)
def meer_verdieping():
    # elk block heeft:
    # - class: edwh-watcher
    # - data-type met 'aan de slag' of 'meer verdieping'
    # elke link heeft:
    # - data-type: bijv 'boek' oid
    ga = ghost.GhostAdmin(
        os.getenv("GHOST_URL_KANSEN"),
        os.getenv("GHOST_CONTENT_API_KEY_KANSEN"),
        os.getenv("GHOST_ADMIN_API_KEY_KANSEN"),
    )

    collection = defaultdict(set)

    versie = request.query.get("versie")

    if versie not in VERSIES:
        raise ValueError("Ongeldige Versie")

    for post in ga.posts(tag=["inleiding", "hoofdstuk"]):
        post: ghost.PostResource

        if versie not in post.tags:
            # irrelevant
            continue

        if "edwh-watcher" in post.html:
            doc = BeautifulSoup(post.html, features="html.parser")
            for block in doc.find_all("div", class_="edwh-watcher"):
                # block.data-type?
                for li in block.find_all("li"):
                    type = li.get("data-type", "overig").capitalize()
                    _li = str(li)
                    if _li:
                        collection[type].add(_li)

    return dict(types=collection)
