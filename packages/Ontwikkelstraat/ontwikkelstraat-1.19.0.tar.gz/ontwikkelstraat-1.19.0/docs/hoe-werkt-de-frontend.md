# Hoe werkt de front-end
# HTMX/_hyperscript

## Message bus

Events worden verstuurd naar een `.edwh-messagebus` element. Body bevat deze class, dus de events komen altijd ergens
terecht. Mocht je meerdere states tegelijk nodig hebben, dan kan je de class ook aan andere html elementen toevoegen:

```html

<div class=".edwh-messagebus">
    <!-- luister naar events met hx-trigger="ew:voorbeeld from closest .edwh-messagebus" -->
    <!-- verstuur events met _="send ew:voorbeeld to closest .edwh-messagebus" -->
</div>
```

Als je met `hx-trigger` en hyperscript vervolgens `closest .edwh-messagebus` gebruikt, dan zijn al je events
'scoped' binnen dat html element.

## Componenten
Dankzij HTMX zijn de componenten modulair toe te voegen. 
Bijvoorbeeld een pagina met (alleen) een filterbalk en tiles:
```html
<div 
    id="filters"
    hx-post="filter"
    _="install Filters"
></div>

<div 
    id="tiles"
    hx-post="tiles"
></div>
```

Deze `hx-post` komen overeen met routes in de `fragmentx` controllers.
We hebben de volgende componenten in gebruik:

- `quick-filter`: bevat de quickfilter balk. Kan gebruikt worden met `on htmx:afterSettle call initial_qf(closest .edwh-state)` om de juiste knop is-active te maken op basis van de state.
- `filter` en `filter-with-active`: bevat de sorteren en filter knoppen. De versie met `-with-active` laat ook zien welke filters momenteel geselecteerd zijn. 
Met `install Filters` wordt de UI-functionaliteit aangezet
- `tiles`: laadt de item tiles. `install StateToURL` - sla de state op in de URL, zodat die geladen kan worden na een reload/bookmark etc.
- `modals`: wordt gebruikt door het loginscherm om login/registratie/etc. modals te tonen
- ... verder is er nog een aantal kleinere functionaliteiten die niet altijd gebruikt worden.

Zie [Joplin](https://joplin.edwh.nl/shares/INGbv5yR7BRXdcsJzqgHuV5U0iKoYkCx) voor een stappenplan van implementatie.

## State
State leeft als een formulier waarvan de input's gezamenlijk met de HTMX vals opgestuurd worden richting de fragmentsx
web applicatie. Dit formulier moet de class 'edwh-state' hebben, 
zodat onderdelen binnen het formulier met  _hyperscript `closest .edwh-state` kunnen aanroepen om bijvoorbeeld andere informatie op te halen.
Als er maar één state op de pagina bestaat, kan die de id `#state` krijgen. Als er meerdere states op dezelfde pagina staan, mag deze id niet bestaan.

State wijzigingen vinden plaats door 3 verwerkingen:

1. Een pagina wordt geladen. Vanuit de HTML wordt een 'cleane' state afgegeven. De `url_to_state` bouwt state op, op
   basis van het URL. Deze functie wordt getriggerd vanuit state tag middels een `init block`; hierna wordt
   een `ew:state_changed` verzonden, zodat de UI zich hierop kan afstemmen.
2. Gebruiker voert middels user interface elementen wijzigingen door. Er zijn soms aparte handlers voor de verschillende
   wijzigingen, deze brengen uiteindelijk een wijziging aan in state waarna een `ew:state_changed` wordt verzonden. De
   wijziging benodigd voor de UI wordt gedaan in de `ew:state_changed` handlers, en niet in de event handler die
   geinitieerd wordt vanuit het UI element. (dus niet in de `on click`)
    1. Zoekopdracht
    2. Bladeren
    3. Filteren
    4. Quickfilters
    5. Sorteren
3. Gebruiker bladert terug door de history. via `window.onpopstate` wordt dit opgevangen, de te herstellen state wordt
   uit het popstate event gehaald en in het state formulier ingevuld waarna een `ew:state_changed` wordt afgevuurd,
   zodat de juiste tiles geladen worden en UI zich aanpast.

## Behaviors

Behaviors staan gedefinieerd in behaviors._hs. Sommigen bevatten veel complexe logica en andere behaviors zijn klein en
simpel, maar toch handig voor hergebruik. De volgende herbruikbare behaviors zijn beschikbaar:

- `Auth`: Laat het login scherm zien on-click.
- `LikeButton(item_id: UUID)`: like/hartje functionaliteit zoals te zien bij tiles en items. `item_id` geeft aan over
  welk item de like gaat.
- `StateMachine(stickers: string)`: Logica die bij de tiles hoort, ook te gebruiken op bijv. de user pagina met embedded
  tiles. `stickers` kan 'same', 'new' of 'none' zijn en wordt gebruikt om aan te geven wat er moet gebeuren als er op
  een sticker wordt geklikt.
- `CloseModal`: kan gebruikt worden op knoppen die een 'Cancel'/'Annuleren' of 'X' (kruisje) functionaliteit hebben: om
  de huidige modal te verlaten
- `Sticker(id: UUID)`: kan gebruikt worden voor search_by_sticker, in combinatie met de `StateMachine` die de sticker
  dan op de juiste plek opent.
- `PasswordConfirm(password_feedback_element: HTMLElement, not_required: bool)`: logica voor 'wachtwoord
  herhalen'. `password_feedback_element` wordt gebruikt om feedback te tonen, `not_required` is `true` bij edit: je
  hoeft je wachtwoord niet aan te passen. Bij register is dit wel required.
- `FileUpload`: logica voor drag-and-drop en het omzetten van de geuploade afbeelding naar base64
- `KvK`: logica voor het invullen van het verborgen Kamer van Koophandel veld (`#input-kvk`) vanuit scholen-list.
- `StateToURL`: bij elke `ew:state_changed` wordt `state_to_url()` aangeroepen. Deze behavior kan worden weggelaten als
  de state (bijv filters) NIET in de URL moeten worden opgeslagen
- `Search`: verander de state indien op de home page, anders redirect naar de homepage. Wordt gebruikt door het zoekveld
  in de header. LET OP: `install Search()` moet met haakjes `()` worden uitgevoerd, omdat deze een (optionele)
  optie `default` verwacht. Zonder haakjes gaat hyperscript dus lopen zeuren.
- `SearchInput`: voeg deze behavior toe aan een q input om zoekfunctionaliteit toe te voegen aan de tiles.
  Gebruik: `<input name="q" type="hidden" _="install SearchInput" />`
  (zoals bijv. op een scholenoverzichtspagina)
- `QuickFilterInput`: voeg deze toe aan een qf input om quickfilter functionaliteit toe te voegen.
  Gebruik: `<input name="qf" type="hidden" value="" _="install QuickFilterInput" />`
- `OrderInput`: voeg deze toe aan een order input om sorteren toe te voegen.
  Gebruik: `<input name="order" type="hidden" value="" _="install OrderInput" />`
- `TriggerCheck`: behavior voor Tiles om zeker te weten dat de tiles geladen worden (indien de HX-trigger om een of
  andere reden niet afgaat, zorgt deze behavior er voor dat dit vanzelf opgelost wordt en de user geen lege pagina te
  zien krijgt)

## Event naamgeving

1. `werkwoord_zelfstandignaamwoord`
    * Als dit verstuurd wordt, is het verzoek dat een handler de gevraagde wijziging uitvoert. Zo
      initieert `change_state` een wijziging op state, die een handler moet uitvoeren.
    * Meestal komt dit vanuit een UI-element of history handler.
2. `zelfstandignaamwoord_werkwoordverledentijd[_extra]`
    * als dit verstuurd wordt, is het een notificatie voor UI elementen om zich aan de nieuwe waarheid van state  
      aan te passen. Zo verzoekt `filters_changed` dat filter knoppen zich aanpassen aan de nieuwe geselecteerde
      filter-gids.
    * `_extra` kan bijv. `_for_q` zijn in `history_recovered_for_q` om aan te geven dat het om de history van een
      specifieke variabele gaat
3. verder worden `ew:warning`, `ew:danger`, `ew:success` gebruikt, zie [non-messagebus](#non-messagebus)

We hebben de volgende events:

### edwh-messagebus

- `ew:change_state(page: int, search: str, tag: gid, tags: list[gids], quick_filter: gid, order: str)`: laat de handler
  de state wijzigen welke weer een `ew:state_changed` verstuurt. Gebruik `tag` om één tag aan of uit te zetten (toggle)
  en gebruik `tags` om de set met tags te vervangen.
- `ew:state_changed`*: wordt verzonden nadat state gewijzigd is, bedoeld dat de UI de weergave kan aanpassen n.a.v. de
  nieuwe state. Triggert ook de reload van de tiles content.
- `ew:change_order`*: als de order moet worden aangepast, state wordt hierdoor aangepast
- `ew:order_changed`*: als de order is aangepast, UI wordt hierdoor aangepast. Dit gebeurt vlak na `ew:change_order`
- `ew:filters_changed`*: als de filters aangepast zijn, UI moet nog worden aangepast
- `ew:search_entered`*: als de query aangepast is
- `ew:change_qf`*: als de quickfilter aangepast moet worden (-> tags, qf input en UI)
- `ew:load_form(form: str, ...data)`: Wordt gebruikt om verschillende auth forms in te laden
- `ew:history_recovered_for_${key}`: geeft per URL parameter aan dat de state er voor is ingeladen

_*_ Deze events worden afgevuurd als je gebruik maakt van `change_state`, je hoeft ze dus niet zelf te sturen.
Er op luisteren is wel mogelijk.

### non-messagebus:

- `ew:success`: als een POST goed gelukt is, wordt dit event afgevuurd (door `return SUCCESS(...)` te gebruiken)
- `ew:warning`: als een POST gelukt is met waarschuwing, wordt dit event afgevuurd  (door `return WARNING(...)` te
  gebruiken)
- `ew:danger`: als een POST niet goed gelukt is, wordt dit event afgevuurd  (door `return DANGER(...)` te gebruiken)
  Deze events worden NIET naar de messagebus gestuurd, omdat we deze events niet door iedereen willen laten opvangen,
  maar alleen door het element dat de request verstuurd heeft (of een parent daarvan). Dus hiermee kan je bijvoorbeeld
  een `on ew:success call location.reload()` toevoegen aan een login formulier om de pagina te verversen na login. Als
  je `on ew:success from closest .edwh-messagebus call location.reload()` zou doen, dan zou dit ook triggeren bij
  ongerelateerde success-events, en dat willen we niet.
- `ew:submit`: vervanging van `submit`, die je (soms) niet handmatig mag triggeren

### history_recovered_for_...

- `history_recovered_for_q`

## Cookies
Standaard blokkeert HTMX het setten van cookies (in elk geval cross origin, wat wij vaak gebruiken).
Als dit voor problemen zorgt, kan de volgende meta tag als setting worden toegevoegd in de `<head>`:
```html
<meta name="htmx-config" content='{"withCredentials":true}'>
```

## Troubleshooting?

```js
monitorEvents(htmx.find(".edwh-messagebus"));

debug(); // logt alle custom events
```