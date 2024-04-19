# Hoe werken verschillende applicatie versies

!!! warning
    De volgende content deels achterhaald!


## Versiebeheer en hosting
Vanuit de behoefte van mogelijke gebruikers moeten we verschillende versies  
van applicaties een tijdje aan blijven bieden.  
Dit geldt met name voor:
 * front-end (als py4web applicatie, per `major.minor` versie)
 * graphql (als microservice, per `major` versie)

Omdat de versies kunnen verschillen vanwege een ander 'onderstel', zoals libraries,
graphql versie, hulp dingen, py4web versie enzovoorts zetten we elke `major.minor`
versie beschikbaar.  Bij de front-end applicatie is dat per `major.minor` omdat de
 templates sneller kunnen verschillen en daarmee "lichtelijk" backward incompatible
 kunnen zijn.  
Bij de Graphql mag dat alleen per `major` versie gebeuren.

De hosting is geregeld via traefik en deze ondersteund helaas geen URL
rewriting vanuit de HTML die hij terug ontvangt. Dat kan Nginx schijnbaar
wel, en web2py kon dat zelf vanuit de routing... dus, we moeten om wat
uitdagingen heen werken.

Binnen treafik wordt dit opgelost met routers en middlewares.  
Een middleware is iets dat een bewerking kan uitvoeren op de requests zoals
deze binnenkomen of weer vertrekken. Middleware wordt gedelcareerd op het
niveau van de provider, bij ons docker, en mag dus maar 1 keer gedeclareerd
worden. Eenmalig gebruikte middleware wordt daarom gedeclareerd binnen de
labels van traefik zelf, bij ons de `reverse-proxy`.

```yaml
services:
  reverse-proxy:
    image: traefik:v2.4
    # ... 
    labels:
      - "traefik.http.middlewares.strip-front-end-version.stripprefixregex.regex=^/(dev|[0-9.]+)/"
```
De hierboven getoonde `stripprefixregex` kan dus op meerdere plekken benut worden.

De middleware wordt gekoppeld aan een router, en de router geef je per service op.  
Als een service via verschillende URLs benaderbaar is, zijn er verschillende
routers aangemaakt voor de service.

Een versie van een py4web heeft namelijk verschillende manieren nodig om
benaderd te worden. `_dashboard` werkt namelijk *erg* slechts met alleen
een versie prefix, maar we willen onze gebruikers niet met heel gekke
domein namen laten werken. We kunnen deze gekke domeinnamen echter wel zelf
gebruiken om bijvoorbeeld bij `/_dashboard` te komen. Daarom hebben we 2 routers:

 * `py4web-v0-9-dns-prefixed`: door de combinatie van applicatienaam en het versie nummer  is elke docker container terug te vinden  
   ⚠ vereist een dns record met `*.` in argeweb.
 * `py4web-v0-9-path-prefixed`: ghost.cms installaties/templates van Mike moeten gebruik maken van de front-end applicatie met een gepinde versie. Dit omdat we niet willen dat een wijziging in de code een oude template van Mike zou breken. Deze urls worden daarom geprefixt met een versienumer.

Bijvoorbeeld:

> * **dns-prefixed**: `http://py4web-v0.9.robin.edwh.nl/front_end`
> * **path-prefixed**: `http://localhost/0.9/front_end`

Dit wordt op de volgende manier gerealiseerd:
```yaml
  py4web-v0.9:
    labels:
      - "traefik.enable=true" # 1
      - "traefik.http.middlewares.add_0-9-version_header.headers.customrequestheaders.X-EDWH-VER=0.9" # 2
      - "traefik.http.services.py4web-v0-9.loadbalancer.server.port=8000" # 3
      - "traefik.http.routers.py4web-v0-9-dns-prefixed.rule=HostRegexp(`py4web.v0.9.{anydomain:.*}`)" # 4
      - "traefik.http.routers.py4web-v0-9-path-prefixed.rule=PathPrefix(`/0.9/`)" # 5 
      - "traefik.http.routers.py4web-v0-9-path-prefixed.middlewares=strip-front-end-version , add_0-9-version_header" # 6
```
De labels:
1. enable treafik voor deze container
2. maak een nieuwe middleware aan voor deze specifieke versie, om een header mee te kunnen geven naar de docker-container. De versienummer uit het pad wordt namelijk verwijderd, maar zo kun je deze wel weer toevoegen in een URL vanuit de achterliggende webserver.
3. geeft aan op welke poort deze container draait
4. de DNS-Prefix rule werkt voor de `...dns-prefixed` router op basis van en expliciete applicatie en versie, maar niet domein specifiek
5. de `path-prefixed` router is een nieuwe router, die op basis van versienummer het URL herkent. Hier wordt dus geen domein aan gekoppeld, alleen een pad.
6. aan dezelfde router als bij stap 5 worden ook de midlewares toegevoegd om 1) het pad te verwijderen uit de url en 2) het verwijderde pad via een header beschikbaar te stellen

De taak van de achterliggende (py4web) webserver is om bij **uitgaande** urls die via de  `path-prefixed` router binnenkomen de header weer toe te voegen!
De applicatie wordt misschien wel gehost onder `/X` maar de uitgaande URL moet naar `/0.9/X`...


### Miro weergave:
![versiebeheer-miro-bord](versiebeheer-miro-bord.png "Miro bord")