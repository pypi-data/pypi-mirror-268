import collections
import json
import re

import pybars
import requests
from yatl.helpers import A

from py4web import URL, abort, action, redirect, request, response

from .common import (
    T,
    auth,
    authenticated,
    cache,
    cacheheaders,
    db,
    flash,
    logger,
    session,
    unauthenticated,
)
from .handlebars import Handlebars, handlebars_helpers
from .models import VRAGEN, dd, fill_dna_table, slimfit_route_map, slimfit_route_url_map


def _absolute_URL_helper(
    this,
    *parts,
    vars=None,
    hash=None,
    signer=None,
    use_appname=None,
    static_version=None,
):
    """
    Vars werkt niet vanaf pybars, in zoverre dat je al een dictionary moet hebben, want die is niet aan te maken in handlebars.

    Lijkt op URL maar zet FRONT_END_BASE er voor ipv dat de URL helper gokt wat de prefix zou moeten zijn of een relatieve url

    Examples:
    URL('a','b',vars=dict(x=1),hash='y')       -> {FRONT_END_BASE}/{script_name?}/{app_name}/a/b?x=1#y
    URL('a','b',vars=dict(x=1),use_appname=False) -> {FRONT_END_BASE}/{script_name?}/a/b?x=1
    """

    return pybars.strlist(
        [
            # params = GET AND POST vars together
            request.params["FRONT_END_BASE"],
            URL(
                *parts,
                vars=vars,
                hash=hash,
                signer=signer,
                use_appname=use_appname,
                static_version=static_version,
            ),
        ]
    )


# add helper:
handlebars_helpers["absolute_url"] = _absolute_URL_helper


@action("vraag/<vraag_nr:int>", method=["POST"])
@action.uses(session, Handlebars("vraag.hbs", helpers=handlebars_helpers))
# you should NOT use cacheheaders, since you ought not to cache session!
def vraag_n(vraag_nr=1):
    if not request.get_cookie(request.app_name + "_session"):
        # no cookie set! user is blocking our cookies 🥺
        # tijd om boos te worden 😡
        return """
                <div class="box">Het lijkt er op dat third party cookies geblokkeerd worden. 
                Sta deze toe om verder te gaan. Het kan vaak worden opgelost door de "Niet volgen" / "Do not track" instelling uit te schakelen. Hulp nodig? Bekijk de onderstaande bronnen.
                <div class="content">
      <ol>
        <li>Microsoft: <a href="https://support.microsoft.com/nl-nl/windows/do-not-track-gebruiken-in-internet-explorer-11-ad61fa73-d533-ce96-3f64-2aa3a332e792">Do Not Track gebruiken in Internet Explorer 11</a></li>
        <li>Google: <a href="https://support.google.com/chrome/answer/2790761?hl=en&co=GENIE.Platform%3DAndroid&oco=0">'Niet bijhouden' in- of uitschakelen</a></li>
        <li>Apple (Mac): <a href="https://support.apple.com/nl-nl/guide/safari/sfri40732/mac">Voorkomen dat gekoppelde sites je volgen in Safari op de Mac</a><br>
          </li>
          <li>Apple (iOS): <a href="https://www.apple.com/nl/legal/privacy/data/nl/safari/">Safari en privacy</a><br>
          </li>
      </ol>
    </div>
        </div>
                """

    if antwoord := request.forms.get(f"vraag{vraag_nr - 1}"):
        if not session.get("antwoorden"):
            session["antwoorden"] = {}

        session["antwoorden"][f"vraag{vraag_nr - 1}"] = antwoord
        session.save()

    vraag = VRAGEN[vraag_nr]

    if vraag_nr == len(VRAGEN):
        volgende_vraag = "uitslag"
    else:
        volgende_vraag = vraag_nr + 1

    return dict(
        **vraag,
        laatste_uitslag=session.get("laatste_uitslag") or "",
        vraag_nr=vraag_nr,
        volgende_vraag=volgende_vraag,
        vorige_vraag=vraag_nr - 1,
        # gekoloniseerd van gelijkekansenindeklas:
        beantwoord=range(vraag_nr),
        onbeantwoord=range(0, len(VRAGEN) - vraag_nr),
    )


@action("cookie-check")
@action.uses(session)
def cookie_check():
    server = request.urlparts.scheme + "://" + request.urlparts.netloc + "/v1.0"

    vals = json.dumps(
        {
            "FRONT_END_BASE": server,
        }
    )

    return f"""<div 
    hx-trigger='load' 
    hx-post='{server}/slimfit-plaatsbepaling/vraag/1'
    
    hx-vals='{vals}'
    />"""


def _get(url):
    return requests.get(url).text


def _sort(d):
    return collections.OrderedDict(sorted(d.items()))


def _uitslag(uitslag):
    session["laatste_uitslag"] = uitslag
    session.save()

    # find the matching row
    _d = db(db.dna.uitslag == uitslag.lower()).select().first()
    if not _d:
        return dict(
            success=False,
            opmerking="Er kon geen uitslag worden gevonden, probeer het nog eens.",
        )

    d = _d.as_dict()
    d["success"] = True

    collected_urls = collections.defaultdict(set)

    for route, start_cell in slimfit_route_map.items():
        if d["cell"] in start_cell:
            collected_urls.update(start_cell[d["cell"]])

    d["collected_urls"] = _sort(collected_urls)

    return d


@action("plaatsbepaling", method=["GET"])
@action.uses(cacheheaders, Handlebars("uitslag.hbs", helpers=handlebars_helpers))
def plaatsbepaling_get():
    uitslag = request.query.get("uitslag")
    if not uitslag:
        return dict(
            uitslag=None,
            cell=None,
            opmerking="Niet alle antwoorden zijn gegeven, probeer het nog eens.",
            answered=True,
        )
    return _uitslag(uitslag)


@action("plaatsbepaling", method=["POST"])
@action.uses(cacheheaders, Handlebars("uitslag.hbs", helpers=handlebars_helpers))
@action.uses(session)
def plaatsbepaling_post():
    ordered_questions = ["vraag1", "vraag2", "vraag3", "vraag4", "vraag5"]
    # aggregate results, convert to key in dna table
    POST_vars = {**request.params}
    try:
        uitslag = "".join([POST_vars[key] for key in ordered_questions]).lower()
    except TypeError:
        # not all answers available, post_vars[key] returns none, which can't be joined
        return dict(
            uitslag=None,
            cell=None,
            opmerking="Niet alle antwoorden zijn gegeven, probeer het nog eens.",
            answered=True,
        )

    return _uitslag(uitslag)


@action("vraag/uitslag", method=["POST"])
@action.uses(cacheheaders, Handlebars("uitslag.hbs", helpers=handlebars_helpers))
@action.uses(session)
def uitslag():
    # modified copy of old plaatsbepaling_post

    ordered_questions = ["vraag1", "vraag2", "vraag3", "vraag4", "vraag5"]

    antwoorden = {**session["antwoorden"], "vraag5": request.forms.get("vraag5")}

    # aggregate results, convert to key in dna table
    try:
        uitslag = "".join([antwoorden[key] for key in ordered_questions]).lower()
    except TypeError:
        # not all answers available, post_vars[key] returns none, which can't be joined
        return dict(
            uitslag=None,
            cell=None,
            opmerking="Niet alle antwoorden zijn gegeven, probeer het nog eens.",
            answered=True,
        )

    return _uitslag(uitslag)


@action("admin/fill_db")
def admin_fill_db():
    return str(fill_dna_table())


RE_OG_DESCRIPTION = re.compile(
    r'<meta\W+property\W*=\W*"og:description"\W+content="(.*?)"'
)
RE_OG_IMAGE = re.compile(r'<meta\W+property\W*=\W*"og:image"\W+content="(.*?)"')
RE_ROUTETITLE = re.compile(r'id"*="routetitle".*?>(.*?)<')


@cache.memoize(3600)
def _card(url):
    text = _get(url).replace("\n", " ")

    description = RE_OG_DESCRIPTION.findall(text)[0]
    img = RE_OG_IMAGE.findall(text)[0]
    title = RE_ROUTETITLE.findall(text)[0]

    return dict(img=img, description=description, title=title)


@action("card", method=["GET"])
@action.uses(cacheheaders, Handlebars("card.hbs", helpers=handlebars_helpers))
def card():
    url = request.params["url"]
    return _card(url)


@action("ghost")
@action.uses(cacheheaders, Handlebars("ghost.hbs", helpers=handlebars_helpers))
def ghost():
    return {}
