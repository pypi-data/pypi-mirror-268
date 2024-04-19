# Wat is docker-compose

Docker-compose is een python programma bedoeld om makkelijker met Docker te kunnen werken. 
Waar Docker gericht is op de verschillende individuele mogelijkheden van docker (een image, een 
instance, een netwerk, een volume) is docker-compose gericht op de gezamenlijkheid. 

Een docker-compose file is een [yaml](https://en.wikipedia.org/wiki/YAML) file. Yaml is bedoeld 
om eenvoudig te verwerken voor zowel mens als machine. 

De yaml file is opgedeeld in een aantal verschillende onderdelen, op hoofdniveau kom je onder 
meer tegen: 

 * de versie van de docker-file (wat onder meer impact heeft op wat er mogelijk is in die 
   docker-file, los van de versie van docker-compose en docker zelf)
 * service: een docker container wordt een service genoemd, en je kunt meerdere services hebben 
   voor een oplossing. Denk aan [postgres, redis, web2py, py4web, migrate, celery workers](wat-is-een-omgeving.md) 
   enz. Een service is een beschrijving van hoe een docker container gestart wordt, maar kan wel 
   over meerdere draaiende containers gaan. Dit komt omdat je van een service meerdere 
   containers kunt starten. Denk bij een service daarom aan de blauwdruk, en een container aan 
   een instance.  
   Per service worden meerdere dingen beschreven, waaronder: 
    * welke image gebruikt wordt, als het niet zelf gebuild wordt 
    * welke Dockerfile gebruikt wordt voor het builden, mits een service gebuild moet worden
    * welke poorten open gezet moeten worden richting de host 
    * welke poorten beschikbaar zijn voor bijvoorbeeld traefik als reverse proxy
    * welke volumes en directories gemount moeten worden 
    * welke labels er toegevoegd zijn. labels worden bij ons vooral gebruikt vooor het aansturen 
      van treafik, zodat die weet welke hostname gebruikt wordt bij een service (dus 1 of meer 
      containers)
 * volumes die lange tijd opgeslagen moeten worden (zoals die van de database) of die gedeeld 
   zijnd oor meerdere services (bij ons nu niet gebruikt)
 * Netwerken die (mogelijk gedeeld worden) 