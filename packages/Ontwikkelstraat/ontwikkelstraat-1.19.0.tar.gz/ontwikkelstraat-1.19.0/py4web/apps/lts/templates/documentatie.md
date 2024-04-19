# Education Warehouse Tiles

## voor Externe Partijen

#### Implementatie

In de head:  
`<link rel="stylesheet" href="https://fragments.meteddie.nl/lts/cdn/1.0/css/bundled.css"/>`  
Aan het einde van de body:  
`<script src="https://fragments.meteddie.nl/lts/cdn/1.0/js/bundled.js"></script>`

Vervolgens kan er een `form` geplaatst worden op de plek waar de kaarten moeten verschijnen (zie voorbeelden verderop).

Deze static files kunnen naar wens op versie worden vastgezet.
`1.0` zoals in het voorbeeld hierboven wordt automatisch geupdate met fixes, maar niet met nieuwe functionaliteit.
Een semantische versie van drie nummers lang (bijv. `1.0.3`) zal helemaal niet worden geupdate.
Als er slechts één getal wordt opgegeven (bijv. `https://fragments.meteddie.nl/lts/cdn/2/js/bundle.js`) dan zal deze
geupdate worden met alle versies en nieuwe functionaliteit na 2.0.0 (dus 2.0.1, 2.1.0, 2.1.1 etc.) die geen breaking
veranderingen bevatten.
Updates die wel bestaande functionaliteit zouden kunnen breken worden in een nieuwe major versie gedaan (bijv. `3.0.0`)
en zullen handmatig moeten worden bijgewerkt en gecontroleerd op benodigde veranderingen aan uw kant.  
[De lijst van versies (met demo-pagina) is hier te bekijken.](/lts/versions)  
[De lijst van veranderingen (changelog) is hier te bekijken.](/lts/changelog)

#### Mogelijke gebruikersopties uitgelegd mbt functionaliteit (instelling → opties)

Opties kunnen worden meegegeven via hx-vals of input's. De hx-vals is bedoeld voor ‘statische’ opties en inputs zijn
voor dynamische opties, bijv door de user aan te passen via de UI.

**De opties die geaccepteerd worden bij de route `simple_tiles`:**

* limit: aantal te weergeven kaarten in 1 scherm (`int`)
* paginate: true / false (`bool`)
* change_url: true / false (`bool`): normaal wordt de state opgeslagen in de url, zodat een reload bijv. niet de tags of
  zoekterm reset.
  Indien dit gedrag ongewenst is, kan dit uitgezet worden met deze optie.
* page de huidige pagina (`int`), waarschijnlijk moet deze in een input om dynamisch te zijn, anders werkt paginate
  niet.
    * Echter wordt dit automatisch al geregeld als page weggelaten wordt uit de opties
* likes: enabled / disabled (`string`), wordt op dit moment niet actief gebruikt
* q: zoekterm (`string`)
* base\_tags: `array` met de verschillende tag gids (unieke identifier Education Warehouse content) waarop gefilterd
  moet worden.
    * `['1274163a-be86-4395-8eef-4af66d9b81ec', ‘HIER NOG EEN GID BIJVOORBEELD’]`
    * Het idee is dat een platform zijn eigen tag in de base tags stopt, zodat alle zoekresultaten in elk geval relevant
      zijn voor dat platform.
* tags (`array`): deze tags worden toegevoegd aan de base tags, waarschijnlijk ingevuld d.m.v. filterknoppen
* quickfilter (`boolean`, `string`): Indien `true`, wordt de standaard quickfilter balk boven de tiles getoond.
  Indien `false` (de standaard), wordt de quickfilter balk verborgen.
  Indien het een string is, wordt een specifieke quickfilter balk getoond (met de opgegeven naam).
* searchbar (`boolean`): Indien `true`, wordt er een zoekbalk toegevoegd die gebruikt kan worden om door de items te
  zoeken.  
  Als u een zoekbalk elders op de pagina wilt plaatsen en kundig bent in HTML, kan de volgende snippet gebruikt en
  aangepast worden:

```html
<form _="install Search">
    <input type="text" name="q" placeholder="Vul een zoekterm in" _="install SearchUI">
</form>
```

* filters (`boolean`, `"with-active"`, `"modal"`, `"modal-with-active""`): Indien `true`, wordt er een filter balk weergegeven.
  Indien `with-active`, wordt ook weergegeven welke filters door de gebruiker zijn geselecteerd.
  Indien `modal`, wordt de menu-style 'modal' gebruikt i.p.v. default. 

**Deze optie moet in een input aanwezig zijn zodat het script weet waar de request(s) naar toe moet:**

* `FRONT_END_BASE` (`string`): URL/path naar de juiste fragmentx server

Een minimale html snippet met default settings kan er dan als volgt uitzien (met de css bundle in de head en de JS
bundle aan het einde van de body):

```html

<form
        hx-post="simple_tiles"
        hx-trigger="load"
        hx-vals='{}'>
    <input type="hidden" name="FRONT_END_BASE" value="https://fragments.meteddie.nl/lts/">
</form>
```

Of een iets uitgebreidere met tags als dynamische en verder statische settings:

```html

<form>
    <!-- can be for example user-selected: -->
    <input type="hidden" name="tags" value="07df9e97-2c9d-457d-bd35-65a107dbc66d"/>
    <div
            hx-post="simple_tiles"
            hx-trigger="load"
            hx-vals='{
        "limit": 3,
        "paginate": true,
        "likes": "disabled",
        "base_tags": "4cc54bf2-b7c8-415d-8938-7a47d9207439,1274163a-be86-4395-8eef-4af66d9b81ec"
        }'>
        <input type="hidden" name="FRONT_END_BASE" value="https://fragments.meteddie.nl/lts">
    </div>
</form>
```

#### Mogelijke gebruikersopties uitgelegd mbt styling (welk doel → welke class)

* Achtergrondkleur aanpassen van de section waar de kaarten worden getoond → `.edwh-style`

_Voor alle onderstaande opties geld, altijd `.edwh-style` voor de class plaatsen._

* Afstand tussen verschillende kaarten vergroten → `.edwh-columns`
* Achtergrondkleur van de kaarten aanpassen → `.edwh-card`
* Afstand tussen titel + auteur en de teaser aanpassen → `.edwh-card-heading`
* Kleur, aantal regels en grootte van de titel aanpassen → `.edwh-card-title`
* Kleur en grootte van de auteur/leestijd aanpassen → `.edwh-card-subtitle`
* Kleur en grootte van de teaser aanpassen → `.edwh-card-teaser`
* Kleur en grootte van het hartje / de like button aanpassen → `.edwh-icon > path`
* Kleur en grootte van de counter naast het hartje aanpassen → `.edwh-like-count`
* Kleur pagination aanpassen → `.pagination-link`
* Kleur actieve pagination aanpassen → `.pagination-link.is-current`
* Kleur pijltjes pagination aanpassen → `.pagination path`

<div id="email-form" 
     hx-get="email_registration_form" 
     hx-trigger="load"
     hx-vals="js:{...Object.fromEntries(new URLSearchParams(location.search))}"
> ></div>
