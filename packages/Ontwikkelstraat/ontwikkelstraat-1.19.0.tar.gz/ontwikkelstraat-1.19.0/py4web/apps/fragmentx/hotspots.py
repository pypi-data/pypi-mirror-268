import re
from dataclasses import dataclass

import ghost
import yaml


@dataclass
class Hotspot:
    top: float
    left: float
    tooltip: str
    position: str


# Example:
"""
---
top: 25
left: 9.6
position: right down
---
<p>We hergebruiken oude content, zoals websites, rapporten en verslagen. We halen daar de relevante
praktijkervaringen uit en leggen contact met de educatieteams erachter om die praktijkervaringen samen
met hen te actualiseren en te delen.</p>
<p>Dat doen we bijvoorbeeld met content van <a href="https://www.schoolaanzet.nl">School aan zet</a>, <a
    href="https://www.innovatieimpulsonderwijs.nl">Innovatieimpuls Onderwijs</a>, <a
    href="https://pactvoorkindcentra.nl">PACT voor Kindcentra</a> en <a
    href="https://www.lerarenontwikkelfonds.nl">Lerarenontwikkelfonds</a>.</p>
<p>Zo bouwen we voort op de kennis en ervaring die eerder is opgedaan en verduurzamen we het effect van deze
projecten.</p>
"""

# <hr/> ≈ --- ≈ —
RE_DELIMITER = re.compile(r"<hr/?>|-{3,5}|—{1,3}", re.MULTILINE)
RE_BR = re.compile(r"<br/?>|</p>")
RE_HTML = re.compile(r"<.+?>")


# @cache.memoize(3600)
def get_hotspots(endpoint, api_key):
    client = ghost.GhostContent(endpoint, api_key)

    filtered_posts: ghost.GhostResultSet = client.posts.get(
        tag=["hotspot"], order="title"
    )

    hotspots = [None]  # skip index 0 so the hotspot counter starts at 1
    for post in filtered_posts:
        content = post["html"]

        try:
            *_, yml, html = RE_DELIMITER.split(content, 2)

            yml = RE_BR.sub("\n", yml)
            yml = RE_HTML.sub("", yml)
            data = yaml.load(yml, yaml.Loader)

            hotspots.append(
                Hotspot(
                    data["top"],
                    data["left"],
                    html,
                    data.get("position", "right down"),
                )
            )

        except (ValueError, KeyError) as _:
            # incorrect frontmatter, skip!
            # print("!! Parsing failed!", _)
            continue

    return hotspots


_HOTSPOTS = [
    # 0
    Hotspot(0, 0, "", ""),  # hack voor @index die op 0 begint standaard
    # 1
    Hotspot(
        25,
        9.6,
        """<p>We hergebruiken oude content, zoals websites, rapporten en verslagen. We halen daar de relevante
               praktijkervaringen uit en leggen contact met de educatieteams erachter om die praktijkervaringen samen
               met hen te actualiseren en te delen.</p>
            <p>Dat doen we bijvoorbeeld met content van <a href="https://www.schoolaanzet.nl">School aan zet</a>, <a
                    href="https://www.innovatieimpulsonderwijs.nl">Innovatieimpuls Onderwijs</a>, <a
                    href="https://pactvoorkindcentra.nl">PACT voor Kindcentra</a> en <a
                    href="https://www.lerarenontwikkelfonds.nl">Lerarenontwikkelfonds</a>.</p>
            <p>Zo bouwen we voort op de kennis en ervaring die eerder is opgedaan en verduurzamen we het effect van deze
               projecten.</p>""",
        "right down",
    ),
    # 2
    Hotspot(
        45,
        9.6,
        """<p>We sluiten aan bij online en offline activiteiten waarbij kennis en ervaringen worden uitgewisseld, zoals
               bij congressen en webinars.</p>
            <p>Praktijkervaringen die daar worden uitgewisseld worden opgetekend en samen met de educatieteams erachter
               gedeeld.</p>
            <p>Zo creëren we praktijkgerichte verslagen en vergroten we het rendement van de activiteiten.</p>
""",
        "right down",
    ),
    # 3
    Hotspot(
        68.6,
        9.9,
        """<p>Via verschillende online formulieren halen we samen met partners specifieke praktijkervaringen 
            op.</p>""",
        "right down",
    ),
    # 4
    Hotspot(
        90,
        10.3,
        """<p>Regelmatig doen we actief onderzoek naar praktijkervaringen op een bepaald thema.</p>
            <p>Daarbij verbinden we de praktijk en bestaande wetenschappelijke kennis om de waarde van de ervaringen te
               vergroten. Wanneer er geen of weinig wetenschappelijke kennis aanwezig is over een bepaald thema, doen we
               zelf onderzoek en/of zoeken we contact met universiteiten en NRO.</p>
            <p>Zo dragen we bij aan <em>research based practice</em> en <em>practice based research</em>.</p>""",
        "right up",
    ),
    # 5
    Hotspot(
        # 52.5, 39.5,
        51.1,
        41,
        """<p>In ons <em>warehouse </em>– in goed Nederlands vertaald als magazijn – slaan we alle relevante informatie
           die we tegenkomen op, zodat deze gebruikt kan worden te inspiratie, maar ook voor onderzoek.</p>""",
        "left down",
    ),
]
