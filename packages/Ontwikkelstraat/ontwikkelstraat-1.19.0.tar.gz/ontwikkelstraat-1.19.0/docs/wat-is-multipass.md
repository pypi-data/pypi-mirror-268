# Wat is multipass

Multipass is een tool om snel en eenvoudig virtuele machines te maken en te beheren. Het is
ontwikkeld door Canonical, de ontwikkelaars van Ubuntu. Multipass werkt op Windows, macOS en
Linux. Elk van de besturingsystemen heeft eigen voorkeur virtualizers. Op Windows wordt
Hyper-V gebruikt, op macOS wordt VirtualBox gebruikt en op Linux wordt KVM gebruikt.

Multipass helpt om met al deze verschillende virtualizers te werken door één cli te gebruiken die
met alle virtualizers werkt. Je hoeft dus niet elk van de virtualizers te installeren en te leren
gebruiken. Je kunt gewoon de cli van Multipass gebruiken.

## Ondersteuning vanuit `server_provisioning`

Sommige specifieke commando's (zoals het mappen van `dockers.local` in je hosts file) en een
geautomatiseerde installatie voor linux zijn te
vinden [in het invoke script](https://github.com/educationwarehouse/server_provisioning/blob/master/tasks.py)
van de [provision-sever repository](https://github.com/educationwarehouse/server_provisioning).

```
 Available tasks:
  mp.fix-host (mp.fix-dns)
  mp.install
  mp.prepare
```

### Installeer Multipass

Je kunt Multipass installeren door
de [installatie instructies](https://multipass.run/docs/installing-on-linux)
te volgen, of bovenstaand script te gebruiken. Voor windows en macOS kun je de installatie
uitvoeren door de installatie instructies te volgen op de [Multipass website](https://multipass.
run/).

## Multipass cli

De cli heet `multipass` maar wordt vaak gealiased naar `mp`.

De cli heeft een aantal subcommands. De meest gebruikte subcommands zijn `launch`, `list`, `exec`
en `delete`. Elke virtual machine heeft een naam. De naam van de virtual machine wordt gebruikt
als argument voor de subcommands. Als je geen naam opgeeft, wordt de naam `primary` gebruikt.
Wij gebruiker doorgaans de naam `dockers`. Bijvoorbeeld:

* `mp launch dockers` om een virtual machine te starten
* `mp exec dockers -- ls -la` om een commando uit te voeren op de virtual machine
* `mp delete dockers` om de virtual machine te verwijderen
* `mp list` om een lijst van de virtual machines te zien
* `mp info dockers` om informatie over de virtual machine te zien (waaronder het IP adres en
  eventuele mounts)

## Mounts

Je kunt een map op je host machine mounten op de virtual machine. Dit is handig als je bestanden
van je host machine wilt gebruiken in de virtual machine. Bijvoorbeeld:

* `mp mount ~/projects:/home/ubuntu/projects dockers` om de map `~/projects` op je host machine
  te mounten op de map `/home/ubuntu/projects` in de virtual machine

Handig voor het remounten is onder andere:

* `mp mount --list` om een lijst van de mounts te zien
* `mp mount --forget dockers` om alle mounts van de virtual machine te verwijderen

Enkele veel gebruikte shell commando's in een invoke script:

```python
from invoke import task


@task
def mp_up(ctx, omgeving, mp_name='dockers'):
    ctx.run(f'multipass exec {mp_name} -d {omgeving} ../.local/bin/invoke up', echo=True)


@task
def mp_remount(ctx, mp_name='dockers'):
    '''Remounts the reverse_proxy and omgeving folders, starting the reverse_proxy container. 
    '''
    if mp_name == 'dockers':
        ctx.run(f'multipass unmount {mp_name}:', echo=True)
        ctx.run(f'multipass mount reverse_proxy {mp_name}:reverse_proxy', echo=True)
        ctx.run(f'multipass mount omgeving {mp_name}:omgeving', echo=True)
        ctx.run(f'multipass info {mp_name}', echo=True)
        ctx.run(f'multipass exec {mp_name} -d reverse_proxy ../.local/bin/invoke up', echo=True)


@task
def shell(ctx, mp_name='dockers'):
    ctx.run(f'multipass shell {mp_name}')
```


