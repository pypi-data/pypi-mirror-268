# Wat is docker

Docker is een programma dat isolerende containers maakt voor programma's om in te draaien.
Het is geen virtualisatie van de volledige hardware, maar gebruikt wel virtualisatie van
netwerken, schijven enz. Omdat de applicatie op native host hardware draait worden programma's
sneller uitgevoerd dan in een virtuele machine. Omdat ze toch gescheiden uitgevoerd worden krijgen
we de voordelen die virtualisatie doorgaans biedt.

!!! note
    Docker werkt enkel met een CLI.  
    [docker-compose](wat-is-docker-compose.md) werkt met een yaml file.  
    Gezien het [principe dat we zo veel mogelijk willen automatiseren](het-automation-principe.md),
    gebruiken we docker
    **vrijwel nooit** rechtstreeks op de commandline. Zeker niet binnen onze omgevingen.

## Images & Volumes

Docker werkt met images. Een image is de eerste virtualisatie van de harde schijf. Images zijn
read-only voor het proces dat ze uitvoert. Stel je een ISO bestand voor (of een CDROM voor wie
dat nog kan herinneren). Alle wijzigingen die je toe wilt passen moet je ergens kwijt, en dat
gebeurd doorgaans in een volume. Een volume is dus read-writable, en bevat doorgaans alleen de
verschillen tussen "eindresultaat op schijf" en "het oorspronkelijke image". Voeg je 5 bestanden
toe: dan worden deze bijgeschreven in het volume. verwijder je hiervan weer 2, dan blijven er 3
bestanden over in het volume. Delete je bestanden die al bestonden in de image, dan wordt deze
wijziging *toegevoegd aan het volume*. Ofwel, het volume bevat alle wijzigingen tov de image
door uitvoer van applicaties.

```plantuml
node "'virtuale schijf'" as disk {
node "volume (rw)" as volume {
    component deltas 
    note right: alle wijzingen tijdens het uitvoeren\nvan de applicatie gaan hierin. 
}
node "image (ro)" as image {
    component "layer-03" as l3
        note right: geinstalleerde applicaties en vereiste bestanden.
    component "layer-02" as l2
        note right: Geinstalleerde updates
    node "layer-01" as l1
        note right: Base OS layer\n(meestal vanuit een andere image)
    l3 -down-> l2 #transparent
    l2 -down-> l1 #transparent
}
volume -down-> image #transparent

}

note as uitleg
 Samen zijn het volume en image een geheel, en zien ze eruit
 als schijf voor het proces dat er in draait. 
 Docker gebruikt nooit deze term, maar voor het concept is 
 het wel makkelijk te begrijpen.
endnote 

uitleg .up- disk 
```

### Builden

Docker gebruikt een `Buildfile` met instructies voor het bouwen van een image.  
Tijdens het builden wordt dit stap voor stap uitgevoerd. Elke instructie levert een verschil op
met de toestand daarvoor, en zo worden verschillende layers van wijzigingen boven op elkaar
gestapeld. De kijkrichting vanuit een applicatie is "top down" in het schema hierboven. Het
meest recente staat bovenaan.

Docker cached de lagen tijdens het builden. Zodra een rebuild gepleegd wordt, kijkt of er iets
gewijzigd is in de commando's, en zo niet, pakt het de cache van de vorige keer. Dat maakt het
builden aanzienlijk sneller, maar je moet er wel rekening mee houden dat de meest specifieke
wijzigingen *onderaan* het bestand staan. Na het eerste verschil (tov de vorige build) worden
alle instructies *erna* opnieuw uitgevoerd: "Order Matters"&#8482;

### Pullen vanaf docker-hub

Als alle layers opgestapeld zijn tot een definitieve image, kan deze definitie image opgeslagen
worden op docker-hub: het pushen. Stel dat iemand dat al gedaan heeft (wat vaker voorkomt dan
dat je zelf iets pusht), dan kun je een image eenvoudig pullen. Docker heeft hiervoor
ondersteuning in de cli, maar wij gebruiken dit in de omgevingen nooit direct. Altijd via
een [docker-compose](wat-is-docker-compose.md) file.

### Pushen naar docker-hub

Remco heeft een `remcoboerma` account waar een abonnement op zit, daarmee kunnen we private
repositories aan. Daarnaast hebben we een gedeeld `educationwarehouse` account (zonder
abonnement) maar met de rechten op de private repositories. Deze contstructie gebruiken we op
dit moment om na te gaan wat onze behoeften zijn voor we investeren in een team constructie, die
vermoedelijk 10x zo veel gaat kosten.

Zowel het `remcoboerma` als het `educationwarehouse` account hebben de rechten om te pullen en
te pushen. Dat betekent dat een lokale build (op een zo snel mogelijke machine)
gepusht wordt, en alle anderen de build alleen maar hoeven te pullen. Dit voorkomt lang wachten,
en promoot het hergebruik van al geïnvesteerde klokcycli: een dubbele winst.

Het pushen doen we doorgaan vanuit [docker-compose](wat-is-docker-compose.md), omdat de
configuratie dan het gemakkelijkst is via de `docker-compose.yaml` i.p.v. cryptische `docker`
commandlines. 

