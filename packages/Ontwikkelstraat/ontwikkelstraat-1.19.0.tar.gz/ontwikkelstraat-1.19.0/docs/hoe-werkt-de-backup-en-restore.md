# Hoe werkt de backup en restore

```
(invoke) config-backup:

Maakt een repository aan via restic waar de verschillende backups (snapshots) kunnen worden opgeslagen, bij het aanmaken van de repositories, wordt er gevraagd om wachtwoorden aan te maken.
Bij het gebruik van local wordt de repository in de huidige werkdirectory opgeslagen. SFTP maakt gebruik van een SSH config file die vooraf ingesteld moet worden.
Bij Swift en B2 moeten er verbindingsgevens worden ingevoerd om verbinding te maken met het bijbehorende netwerk tijdens de config, deze kunnen opgevraagd worden bij de awesome beheerder(s) of eindbaas Remco.

Opties:
-c : connectie keuze, maak een keuze op welke manier er een repository moet worden aangemaakt: local, SFTP, Swift, B2.                                                                             

(invoke) backup:

Maakt een backup van huidige omgeving of een backup van een stream. Deze worden via de connectie keuze opgeslagen op bijbehorende manier. 
Let op: om deze functie werkend te krijgen is het verplicht om de config-backup uit te voeren.

Opties:
-c : connectie keuze, maak een keuze op welke manier er een repository moet worden benaderd: local, SFTP, Swift, B2. 
-s : stream, kies ervoor om van een (data)stream een backup te maken. 
-f : files, kies ervoor om een backup van de files te maken. 
-m : geef een bericht mee aan restic om weer te geven bij het opvragen van de backups. 

(invoke) snapshots: 
Geeft een overzicht weer van welke backups(snapshots) zijn gemaakt en welk ID hieraan gekoppeld is.
Let op: om deze functie werkend te krijgen is het verplicht om de config-backup uit te voeren.

Opties:
-c : connectie keuze, maak een keuze op welke manier er een repository moet worden benaderd: local, SFTP, Swift, B2.
-t : geef hierbij eventueel de tag stream of files op, snapshots scheid de backups dan op tag.
-n : mocht je hier een nummer opgeven, zorgt snapshots ervoor dat alleen de laatste zoveel snapshots worden laten zien.

(invoke) restore:
Pakt een bestaande snapshot uit een repository en plaatst deze op het opgegegeven pad. Ook kan met deze optie een data stream worden opgehaald en gekoppeld aan sql.
Let op: om deze functie werkend te krijgen is het verplicht om de config-backup uit te voeren.

Opties: 
-c : connectie keuze, maak een keuze op welke manier er een repository moet worden benaderd: local, SFTP, Swift, B2.
-f : restore file snaphot, automatisch wordt hierbij de laatste file snapshot gebruikt. 
-r : restore een stream, automatisch wordt hierbij de laatste stream snapshot gebruikt. 
-s : geef handmatig een snapshot op die gerestored moet worden, de ID hiervan kan via de optie 'snapshots' worden bekeken.
-t : geef een pad op waarin de restore moet worden neergezet.

(invoke) check: 
Controleerd de integriteit van de repositories (in de code staat extra functionaliteit beschreven voor het ook willen controleren van opgeslagen data).
Let op: om deze functie werkend te krijgen is het verplicht om de config-backup uit te voeren.

Opties:
-c : connectie keuze, maak een keuze op welke manier er een repository moet worden benaderd: local, SFTP, Swift, B2.
```
