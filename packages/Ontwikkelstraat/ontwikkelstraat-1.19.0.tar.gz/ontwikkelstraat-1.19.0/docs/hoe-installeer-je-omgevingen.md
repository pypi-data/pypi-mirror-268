# Hoe installeer je omgevingen

Om een [omgeving](wat-is-een-omgeving.md) voor te bereiden

## Development host

### Voorbereidingen

De development host is de machine waar de ontwikkelaar rechtstreeks op werkt. Uitgaande van een
linux machine of
compatible.

De development host heeft doorgaan nodig:

1. IDE: pycharm
2. python3 (3.10, 3.11?): `sudo apt install python3.10 python3.10-venv `
3. pipx: `pip install pipx`
4. invoke: `pipx install invoke`
5. een aantal libraries die invoke gebruikt:  `pipx inject invoke httpx tabulate pyyaml humanize`
6. zelfde geld voor fabric:  `pipx install fabric; pipx inject fabric httpx tabulate pyyaml
   humanize`
7. git: `sudo apt install git`
8. multipass (voor lokale ontwikkeling): `sudo snap install multipass`

## clone de server_provisioning

```bash
git clone git@github.com?educationwarehouse/server_provisioning
```

## Installeer multipass

```bash
cd server_provisioning
inv mp.install 
```

## start een docker-ready VM

```bash 
multipass launch docker --name dockers # of delen, fica, etc.
```

## prepare multipass

Multipass benaderbaar maken met SSH door een eigen sleutel toe te voegen.

```bash 
invoke mp.prepare dockers
```

## prepare generic server

```bash 
multipass list 
# copy IPv4 
fab -H ubuntu@<ipadres> prepare-generic-server
```

Werkt dit niet omdat je authentication errors krijgt, dan moet je voortaan `-i ~/.ssh/multipass.key`
toevoegen
aan je commandline:

```bash
fab -H ubuntu@<ipadres> -i ~/.ssh/multipass.key prepare-generic-server  
```

# Voor multipass:

git clone de repository voor de reverse_proxy en de ontwikkelstraat.
Log in met de github cli voor het grootste gemak om private repo's te klonen.

```bash 
git clone ... 
multipass mount <reverse_proxy foldernaam>  dockers:/home/ubuntu/proxy
multipass mount <ontwikkelstraat foldernaam>  dockers:/home/ubuntu/omgeving
```

Login op de multipass middels `multipass shell dockers`
Configureer de reverse proxy: `cd proxy; invoke setup`  
Voer de gegevens in waar het script om vraagt en start de proxy om de netwerken te
maken: `invoke up`
Configureer de omgeving middels `cd omgeving; invoke setup`  
Login op docker middels `dockers login`, met gebruiker `educationwarehouse` en wachtwoord uit de
wachtwoord kluis.
Download de images via `docker-compose pull`, na enige tijd is het klaar en zijn de images
beschikbaar.

### download de backup

De backup staat onder meer in teams waar je toegang hebt, sla de file op in de omgeving directory
in `./migrate/data` als
`database_to_recover.sql`, of `database_to_recover.sql.gz`, of als `database_to_recover.sql.xz`.

### configureer de hostnames om lokaal benaderbaar te zijn

in de multipass, in de omgeving directory: `docker-compose config | grep Host`.  
Filter de hostnames en gebruik deze om via `mp.fix-host` op te geven op de host machine:

```bash
inv mp.fix-dns dockers -h delen.dockers.local -h py4web.dockers.local -h web2py.dockers.local -h .... 
```

### installeer de database

`invoke whipe-db`
Dit schoont de omgeving (wat nog leeg is), en maakt vervolgens

###  

Start de omgeving middels `invoke up`

# Voor een remote server:

## installeer de reverse proxy

```bash
fab -e -H ubuntu@fica.meteddie.nl install-omgeving -c educationwarehouse/reverse_proxy  -i -o reverse_proxy 
```

## installeer de omgeving

```bash
fab -e -H ubuntu@fica.meteddie.nl install-omgeving -c educationwarehouse/ontwikkelstraat  -i -o fica.productie --branch feature_omgeving
```

## via SSHFS lokaal en remote werken

!!! tip
    Zie ook [Hoe werken we met sshfs](hoe-werken-we-met-ssh.md#sshfs)


1. installeer sshfs (`sudo apt install sshfs` op ubuntu, voor Mac: vraag [Mike naar zijn ervaring](https://www.petergirnus.com/blog/how-to-use-sshfs-on-macos))
2. er van uitgaande dat je een keyagent gebruikt (zoals KeepassXC, pageant of vergelijkbaar op 
   Mac) hoef je geen keyfile te regelen, als je die wel nodig hebt, zorg er voor dat de file 
   gereed staat. Mike gebruikte dit, op linux werken we meestal met een keeagent. 
3. Zorg er voor dat je een group hebt met groupid `1050` (remote wordt deze aangemaakt tijdens 
   het [provisionen van de server](hoe-wordt-een-server-geprovisioned.md) als `Microservice`, en 
   van sommige bestanden wordt het ownership ingesteld door `inv setup` ingesteld op 
   `microservice:mircoservice`. Deze files zouden niet schrijfbaar zijn voor jouw gebruiker, als 
   je geen lid bent van de groep `1050`. 
4. Maak jezelf lid van boven genoemde groep
5. Log op nieuw in of herstart, want meestal is dat nodig voor groeplidmaatschapwijzigingen.
6. maak een lege directory die als 'mount-point' geldt voor de remote files, bijvoorbeeld 
   `~/PycharmProjects/prd2.meteddie.nl_live`
7. Mount met SSHFS het remote filesystem:
   ```bash
   sshfs ubuntu@prd2.meteddie.nl:/home/ubuntu/omgeving prd2.meteddie.nl_live/ -o auto_unmount
   ```
8. Werk in pycharm vanuit deze file. Mocht je een server gebruiken die al [ingespoeld](hoe-wordt-een-server-geprovisioned.md) is, 
   dan is de `remote` ingesteld op een lokaal niet bestaand adres. Dat zit in de ssh config file.  
   Vanuit Pycharm kun je een nieuwe remote toevoegen (menu: `git`, `manage remotes...`).  
   ⚠️Tijdens het committen van code kies je ipv `origin` dan je nieuwe naam van de remote uit.  



# Gaat het niet goed?

* controleer dat je keys niet conflicteren, bijvoorbeeld omdat je mp.prepare teveel hebt uitegevoerd
* log eens in met SSH rechtstreks op het ipadres met gebruiker ubuntu om te zien of de key wel of
  niet gebruikt wordt. 