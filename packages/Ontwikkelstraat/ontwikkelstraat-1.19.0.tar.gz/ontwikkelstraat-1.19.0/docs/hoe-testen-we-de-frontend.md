# Front-end Testing with Pytest, Playwright, Request & Beautifulsoup

/!\ gebruikt de requests library op het moment dat je een post wil doen naar de webserver en alleen het antwoord wil parsen. 
(eventueel met beautifulsoup)

/!\ gebruikt de playwright library voor het aansturen van een browser wanneer je UI elementen wilt testen, integraties wilt testen en alles wilt testen dat enigsinds met javasript te maken heeft. 

## Inleiding

Alle tests zijn onderverdeeld in categorieën, deze categorieën hebben dezelfde naamgeving als een pytest mark
(@pytest.mark.categorie_naam). Alles wordt getest op zowel een ingelogde roc gebruiker als een anonieme gebruiker.  
**LET OP:** De door een roc gebruiker aangemaakte items mogen **NIET** zichtbaar zijn, dit wordt ook getest maar is
momenteel minder relevant.  
Als een test/functionaliteit **NIET** door een anonieme gebruiker uitgevoerd kan worden, dan wordt er getest op een
foutmelding.

### CAT0: componenten
Eventueel een aparte pagina voor maken om te testen. combinatie van playwright, requests. 

 * de engine voor het laden van componenten
   * parameters meegeven, werkt dit?
   * wordt de javascript uitgevoerd die we meegeven vanaf de front-end
   * worden template variabelen gebruikt? 
   * werkt het inloggen van een gebruiker? 
   * krijgt de gebruiker niet telkens een nieuwe session code? 
   * krijg je een nieuwe session code als je bent ingelogd? (/front_end/debug)
   * werkt het meesturen van de informatie van de gebruikte browser en hardware? 
   * worden wachtwoorden plaintext of bcrypted verstuurd? 
   * werkt de terug-knop met history ? 
   * URL parsing naar state enz
   * State naar reload 
  * caching van componenten, en cache-headers? 
   * ... 


### Cat1: zoekbalk
#### Tests:

* Test of het verwachte resultaat naar voren komt zodra hierop wordt gezocht.
* Test of niet meer dan het verwachte resultaat naar voren komt zodra hierop wordt gezocht 
* Gezochte tekst blijft staan na reloaden/verzenden #statemachine
* zoekterm werkt met ?q=%s  #statemachine
* Test of tegels die gemaakt zijn door een @roc gebruiker (admin), zichtbaar zijn voor een roc gebruiker #roc-gebruiker
* Filters blijven actief binnen searches #statemachine
* Quickfilter blijft actief binnen searches #statemachine
* Bij een nieuwe zoekopdracht wilt je naar pagina 1 
* Bij een wijziging van een filter binnen een gezochte set wil je weer naar pagina 1 van de zoekresultaten   
* Test of de foutmelding "Geen zoekresultaten" wordt weergegeven, zodra er naar een niet-bestaand item wordt gezocht.
* Test of het verwachte resultaat verandert zodra er na het zoeken op een quickfilter wordt geklikt. (Omdat je dan
  binnen een quickfilter zoekt.)
* zoekbalken moeten werken van verschillende pagina's 
  * hoofdpagina/item/auteur


### Cat2: quickfilter
#### Tests:
 * quick-filter gebruikt fselector vanuit URL (/quickfilter/slimfit)
 * quick-filter zonder selector levert default quickfilter  (/quickfilter)
 * quick-filter opbouw html #component_api (classes, onclick, enz enz)
 * quick-filter en back-button: wordt het bijgwerkt #statemachine
 * geselecteerde filter moet actief zijn na een reload/state-change #statemachine  
 * geselecteerde class terugvinden #component_api 
 * verschillende selecties (via filter en quick-filter), niet meerdere - oude delen.meteddie.nl functionaliteit nabouwen
* Test of de verwachte tegels worden weergegeven zodra er op een quickfilter wordt geklikt.
* Test of de verwachte tegels worden weergegeven zodra er op meerdere quickfilters achter elkaar wordt geklikt.


### Cat3: filters
#### Tests:

* Test of een enkele filter goed werkt.
* Test of enkele filters na elkaar goed werken.
* Test of meerdere filters tegelijk goed werken.
* Test of de "Geen zoekresultaten" foutmelding wordt weergegeven zodra er een niet bestaande combinatie van filters
  wordt uitgevoerd.
* Test of het bladeren door de tegels werkt bij het selecteren van één of meerdere filters.
* Test of een filter werkt bij het gebruiken van een quickfilter.
* test de integratie tussen filters en quickfilters
* test de integratie tussen filters en zoektermen 

=====================================================================
TODO: Overleg nog over de onderstaande categorieën!
=====================================================================

### Cat4: item
#### Tests:

### Cat4.1: item/tegel weergave

#### Tests:
* search 
  - q=?
  - tags=[]
* sort order aan de hand van de knop
* html-fragment structuur #component_api 
* Test of de tegels laden/zichtbaar zijn.
   - Test of alle informatie op de tegel staat (titel, auteur, beschrijving, leestijd, likes, reacties/berichten).
* Test of een tegel wordt geopend zodra er op de titel/afbeelding wordt geklikt.
* Test of de tags van een tegel zichtbaar zijn zodra er op deze tegel wordt geklikt.
* Test of de categorieën van een tegel zichtbaar zijn zodra er op deze tegel wordt geklikt.
* Test of er een bericht verstuurd kan worden zodra er op een tegel is geklikt.
* Test of de documenten zichtbaar zijn zodra er op een tegel wordt geklikt.
* Test of de "standaard navigatie" werkt, en de tegels worden getoond. (Door van pagina te wisselen op de home-pagina).
### Cat 4.2: item/item-pagina weergave
### Cat 4.3: item/item aanmaken 
### Cat 4.4: item/item opvragen


### Cat5: profiel

#### Tests:

* Test of je eigen profiel overeenkomt met je verwachting (naam, biografie)
* Test of het profiel van een ander overeenkomt met je verwachting (naam, biografie)
* Test of de items zichtbaar zijn op je eigen profiel.
* Test of de items zichtbaar zijn op het profiel van een andere gebruiker.
* Test of je je eigen profiel kunt aanpassen (edit knop).
* Test of je het profiel van iemand anders kunt aanpassen (edit knop).
* Test of de verzamelingen zichtbaar zijn op je eigen profiel.
* Test of de verzamelingen zichtbaar zijn op het profiel van een andere gebruiker.
* Test of er een verzameling aangemaakt kan worden op je eigen profiel.
* Test of er een verzameling aangemaakt kan worden op het profiel van een andere gebruiker.
* Test of je kunt zoeken tussen de items van je eigen profiel (zoekbalk, quickfilter, filters, pagina selectie).
* Test of je kunt zoeken tussen de items van het profiel van een andere gebruiker (zoekbalk, quickfilter, filters,
  pagina selectie).
* Test of de tellers naast Post, Reacties en Boards werken op je eigen profiel.
* Test of de tellers naast Post, Reacties en Boards werken op het profiel van een andere gebruiker.


### Cat6: inloggen

#### Tests:

* Test of er ingelogd kan worden met correcte gegevens.
* Test of er een foutmelding verschijnt bij het inloggen met incorrecte gegevens (correcte gebruikersnaam, incorrect
  wachtwoord. incorrecte gebruikersnaam, correct wachtwoord. incorrecte gebruikersnaam, incorrect wachtwoord.)

### Cat7: bericht sturen

#### Tests:

* Test

### Cat8: likes (thumbs/hearts) maken

#### Tests:

* Test

### Cat9: notificaties

#### Tests:

* Test

### Cat 10: favoriet 
 * een lijst kan gedeel worden met meerdere mensen, en daarom wordt 

### Cat 11: (gedeelde) lijsten
 * 

### Cat 12: wachtwoord resetten 

### Cat 13: integratie met workbench 

## Emulatie apparaten

Dit komt mogelijk later nog...
