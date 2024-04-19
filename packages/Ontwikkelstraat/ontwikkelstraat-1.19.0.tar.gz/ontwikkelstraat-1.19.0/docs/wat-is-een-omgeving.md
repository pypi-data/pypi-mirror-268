# Wat is een Omgeving

Een omgeving bestaat uit een paar samenwerkende delen:

1. het is een [git](wat-is-git.md) repository (meestal op https://github.com/educationwarehouse/... )
1. het bevat een [invoke](wat-is-invoke.md) `tasks.py` met:
    * een `def setup(ctx,...)` functie welke de vereiste instellingen voor in [de omgevingsvariabelen](wat-is-dotenv.md)
      opslaat in
      de [`.env`](wat-is-dotenv.md) file
    * `up` ,`stop`, `build`, `ps` en andere functies om de omgeving te beheren
1. het bevat een [`.env`](wat-is-dotenv.md) file (die **nooit** in git mag komen), beheerd door
   bovengenoemde [`tasks.py`](wat-is-invoke.md)
1. het bevat een [`docker-compose.yaml`](wat-is-docker-compose.md) die de diensten van deze omgeving beschrijft

```plantuml
package Omgeving {
   file "tasks.py" as tasks
   file ".env" as dotenv
   file "docker-compose.yaml" as dc
   tasks -> dotenv: beheer van \nomgevings nvariabelen
   folder "files onder ./" as fs 
   tasks -down-> fs: beheer van \nownership en\npermissions
   node "docker instance(s)" as docker1 #lightblue
   dc -down-> docker1: declareert
}
```

## Standaard: 1 reverse proxy met meerdere omgevingen
```plantuml
cloud internet 
package "reverse proxy" {
   node traefik #lightblue 
   file ".env" as dotenv0 
   file "tasks.py" as tasks0 
   file "docker-compose.yaml" as dc0
}
package "eerste omgeving" {
   node database as database1 #lightblue
   node utils as utils1 #lightblue
   node webserver as webserver1 #lightblue
   file "tasks.py" as tasks1 
   file ".env" as dotenv1 
   file "docker-compose.yaml" as dc1

}
package "tweede omgeving" {
   node webserver as webserver2 #lightblue
   node database as db2 #lightblue
   node utils as utils2 #lightblue
   file "tasks.py" as tasks2 
   file ".env" as dotenv2
   file "docker-compose.yaml" as dc2

}
[traefik] -down-> [webserver1]
[traefik] -down-> [webserver2]
internet -down-> traefik 
```
Dit kan omdat elke container via labels geconfigureerd wordt om op bepaalde hostnames te 
luisteren. Deze zijn doorgaans weer bepaald op basis van omgevingsvariabelen. 

```yaml
  jupyterlab:
    labels:
      - "traefik.http.routers.jupyterlab-${PROJECT}-secure.rule=Host(`lab.${HOSTINGDOMAIN}`)" # 1
      - "traefik.http.routers.jupyterlab-${PROJECT}-secure.tls=true"  # 2
      - "traefik.http.routers.jupyterlab-${PROJECT}-secure.tls.certresolver=${CERTRESOLVER}" # 3
      - "traefik.docker.network=broker" # 4
      - "traefik.enable=true" # 5
    ... 
```
Om de verschillende labels even bijlangs te lopen: 

   1. deze instance is gekoppeld aa `$PROJECT` en `$HOSTINGDOMAIN`, zodat deze instance 
      bijvoorbeeld luistert naar `https://lab.docker.local`. De koppeling met $PROJECT is dat 
      verschillende omgevingen verschillende project namen hebben, en daarmee overschrijf je niet 
      de "centrale" sleutels via "concurerende" service labels. 
   2. TLS wordt verplicht, https is enabled. 
   3. Deze instance wordt gekoppeld aan een `$CERTRESOLVER`, meestal `letsencrypt` voor 
      internet-facing 
      services, of `default` voor lokale ontwikkeling
   4. Deze instance moet benaderbaar zijn voor de reverse proxy, en dat vereist `broker` toegang. 
   5. traefik geven we expliciet op dat de service gebruikt moet worden, om per ongeluk open zetten 
      te voorkomen. 

## Omgeving: Reverse proxy

De reverse proxy is een specifieke omgeving die een [`treafik`](wat-is-treafik.md) instance host, bedoeld om http(s)
verkeer om te leiden
naar de [docker](wat-is-docker.md) services in andere omgevingen. De configuratie van deze diensten staat altijd in de
omgeving van die
diensten zelf, nooit bij de revere proxy. De reverse proxy is onafhankelijk, maar bied een traefik
virtueel [netwerk](architectuur-vanuit-netwerk-perspectief.md) waarop diensten uit
andere omgevingen zichzelf beschikbaar maken.

## Omgeving: Feature-omgeving

```plantuml
file ".env" as dotenv
file "tasks.py" as tasks
file "docker-compose.yaml" as compose

node py4web #lightblue {
   folder cmsx
   folder c 
   folder fragmentx
   folder "shared-code" as shared_p4wb #lightgreen
}
node web2py #lightblue {
   folder workbench
   folder "shared-code" as shared_w2p #lightgreen
}
node celery-worker as cw #lightblue {
   file tasks.py as cwtasks
   folder "shared-code" as shared_cw #lightgreen
}

node "celery-beat" as cb #lightblue {
   file tasks.py as cbtasks
}

node migrate #lightblue {
   folder "shared-code" as shared_migrate #lightgreen
}

node jupyterlab #lightblue {
   folder "shared-code" as shared_jupyterlab #lightgreen
}

node "redis-master\nRW" as redis #lightblue 
node "redis-slave\nRO" as redis2 #lightblue 
database pgpool #lightblue 
database "pg-0" as pg0 #lightblue 
database "pg-1" as pg1 #lightblue 
pgpool -down-> pg0 
pgpool -down-> pg1 
pg0  -> pg1 : replication
fragmentx -down-> redis: session-storage\n& celery-jobs
cb -right-> redis: timers
redis -down-> cw: jobs
redis -down-> redis2: replica

fragmentx -down-> pgpool 
c -down-> pgpool 
workbench -down-> pgpool 
migrate -down-> pgpool 
cwtasks -down-> pgpool 
jupyterlab -down-> pgpool 

folder shared-code as shared #lightgreen {
   folder "edwh/core/backend" as backend
}
```

Zo heet het in ieder geval nu. Het is de omgeving waarin een frontend ([cmsx](wat-is-cmsx.md)
via [py4web](wat-is-py4web.md), [redis](wat-is-redis.md)), backend
([fragmentx](wat-is-fragmentx.md) via [py4web](wat-is-py4web.md), [workbench](wat-is-de-workbench.md)
via [web2py](wat-is-web2py.md),  [edwh.core libraries](wat-zijn-de-core-libraries.md), [celery](wat-is-celery.md) jobs,
[postgres](wat-is-postgres.md) en wat maar nodig is) te hosten
voor een complete omgeving van https://delen.meteddie.nl.

Dit zijn onze "basis" omgevingen. Een afgeleide omgeving is bijvoorbeeld [Fica]('fica-omgeving.md'), wat een fork is
van (of branch is binnen)
de [feature-omgeving](feature-omgeving.md).

## Installatie

## Dependencies
!!! tip
    Heb je iets in een requirements.in aangepast? Run `invoke pip.comile <map>` waarbij map het 
    pad is naar de aangepaste .in file, bijv. `py4web`

Voor onze python dependencies gebruiken we een `requirements.in` en een `requirements.txt` file per Dockerfile (
bijv. `web2py`, `py4web` etc.). De .in files beschrijven welke dependencies nodig zijn, met of zonder
versie-specificatie (==3.0.0, ~3.0.0, >3.0.0, etc.).
Vervolgens wordt de package [`pip-tools`](https://pypi.org/project/pip-tools/) gebruikt om 
compatible versies te pinnen in de `.txt`. Hierdoor werk je altijd
met dezelfde versie van packages totdat [pip.compile](wat-is-pip-compile.md) opnieuw wordt uitgevoerd.

Mocht je zelf builden, dan wordt er voor elke `invoke build` gekeken of de `requirements.txt` 
bestaat en ouder is dan de `requirements.in`, zo niet dan wordt je gevraagd of je de `.in` wil 
pip.compilen. 

## Static Files

!!! tip
    TLDR: is het design of de functionaliteit van je omgeving stuk? 
    Probeer eerst `invoke bundle.build`

Veel omgevingen hebben ook static files (Javascript en CSS) met dependencies nodig.
Om deze samen te voegen en remote dependencies er bij in te verwerken, is de [bundler](wat-is-de-bundler.md) gemaakt.
