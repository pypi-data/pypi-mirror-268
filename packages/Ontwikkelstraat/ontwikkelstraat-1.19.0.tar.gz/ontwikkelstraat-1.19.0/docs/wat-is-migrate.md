# Wat is migrate

Migrate is een script dat er voor zorgt dat het database schema up to date is.  
Het ontleent zijn naam aan de term "migreren van de database", wat nodig is als er nieuwe schema 
of globale logica wijzingen zijn geweest. Denk aan: 

 * het toevoegen van nieuwe tabellen
 * het toevoegen, verwijderen of muteren van kolommen
 * de conversie van data om 1 kolom op te splitsen in 2 

Om bij te houden welke migraties wel en niet zijn uitgevoerd, wordt er in de tabel 
`ewh_implemented_features` bijgehouden welke functie met welk resultaat is bijgehouden. 

Functies in de `migrate.py` die zijn gedecoreerd met `@register` worden eenmalig per run 
uitgevoerd, tot ze succesvol zijn verlopen. Runs daarna worden ze over geslagen. Het is mogelijk 
om relaties tussen geregistreerde functies te hebben, maar meestal is de chronologische volgorde 
al voldoende. Dit betekent wel dat je niet zo maar de volgorde van de functies kunt aanpassen! 
Order-Matters&#8482;

## Een migratie ontleed
```py linenums="1"
@register
def add_license_to_item_2022_12_01_00(db: DAL):
    db.executesql(
        """
    alter table item
        add license varchar(15);
    """
    )
    db.commit()
    return True
```
<ol>
 <li> de decorator</li>
 <li> naamgeving is als volgt: functionaliteit in kleine letters, `_` gescheiden, 
      gevolgd door de datum en een volgnummer op die datum. Dit voorkomt dupliciteit.  </li>
 <li> De functie doet vervolgens iets met de database</li>
 <li value="9"> en commit de wijzigingen als het lukt. Mocht het niet lukken, dan moet de functie 
      proberen een rollback te doen. </li>
 <li value="10">
      Het resultaat moet de boolean `True` zijn voor een succesvolle migratie, of iets booleans 
      negatiefs waardoor de migratie niet als succesvol wordt gemarkeerd, en bij de volgende run 
      opnieuw wordt uitgevoerd.
</ol>
## Flag files
Als alle functies succesvol zijn uitgevoerd zet de `migrate.py` een flag bestand genaamd 
`/flags/migrate-{os.environ['SCHEMA_VERSION']}.complete`. De schema version wordt berekend in de 
`tasks.py` als de omgeving via `inv up` gestart wordt, of `inv setup` wordt uitgevoerd. Deze 
hash is op basis van **alle** code in de `shared_code` library, waardoor een code wijziging in 
de `migrate.py`, of in de `define_models.py` automatisch een andere hash oplevert. 

De flag files worden gebruikt door `dockerize` om te constateren of de migrate is voltooid, en 
afhankelijke services worden pas gestart wanneer de flag file bestaat.  
Dit gebeurd middels een gedeelde shared mount met alle docker omgevingen die `dockerize` draaien 
en daarmee zullen wachten op migrate. Ze mounten de omgevings-folder `./migrate/flags` meestal als 
`/flags`. 

Flag files worden verwijderd met een `inv whipe-db` of door een goed gemikte 
`rm migrate/flags/*.flag` opdracht. 

## Database recovery
Als het migrate script probeert zijn eigen tabel te benaderen, en constateren dat deze er niet 
is, gaat het er van uit dat we te maken hebben met een compleet lege database. Het zal in dat 
geval in de volgende volgorde kijken of er een bestand bestaat genaamd:
 
 1. `data/database_to_restore.sql`
 1. `data/database_to_restore.sql.gz`
 1. `data/database_to_restore.sql.xz`

(in de docker is de data directory te vinden als `/data`, in de omgeving directory is dit 
`migrate/data`)

# Veel voorkomende fout
 * Als je iets wijzigt en de services blijven hangen, dan wordt de migrate niet gedraait. 
   Vermogelijk gebruik je `inv up -s py4web`, die door wijzigingen in de code py4web laat 
   wachten tot migrate is gestart. Je kunt dit oplossen door `inv up` te draaien, zodat ook 
   migrate wordt uitgevoerd, inclusief andere containers, of je kunt het 'sneller' uitvoeren 
   door `inv up -s migrate -s py4web` te gebruiken. Dan voer je beide services snel uit, zonder 
   dat je er last van hebt. `inv logs -s migrate ` kan een grote vriend zijn bij het 
   troubleshooten.
