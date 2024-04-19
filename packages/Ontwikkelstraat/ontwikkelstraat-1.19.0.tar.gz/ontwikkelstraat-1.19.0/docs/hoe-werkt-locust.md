# Hoe werkt locust 
***
**Documentatie:**
 * [Documentatie van locust](https://docs.locust.io/en/stable/)
 * [Installatie (pip install locust)](https://docs.locust.io/en/stable/installation.html)
 * Kunnen handige linkjes zijn om een beetje gevoel er in te krijgen:
   * https://www.blazemeter.com/blog/locust-python
   * https://medium.com/nerd-for-tech/load-testing-using-locust-io-f3e6e247c74e
***
**COMMAND LINE INTERFACE**
 * Wat wij het meest zullen gebruiken via de cli:
      * `-H`: geef meteen een hostname erbij bijv: https://www.google.com/
      * `-P`: geef hierbij een portnaam aan mee, standaard is het 8089 (dit gebruik je als je twee of meerdere locust testen op 1 server naast elkaar wil laten draaien. Voor uitleg kijk bij `Hoe draai je meerdere locust's naast elkaar?`)
      * `-u`: aantal gebruikers die je vooraf al mee kan geven
      * `--autostart`: start die automatisch meteen op, zonder een UI
      * `-f/--locustfile`: pakt die meerdere locustfiles tegelijk
      * wanneer de locust bezig is in de cli kan je deze opties gebruiken:
        * `w`: voor het random toevoegen van 1 tot 10 users
        * `s`: voor het random verwijderen van 1 tot 10 users
***
**Hoe werkt het?**
* Locustfile.py:
  * Als je begint met een Locust script te schrijven moet je natuurlijk als eerste de library importeren: `import locust`.
Maar je hebt ook `HttpUser` en `task` nodig, dat doe je door `from locust import HttpUser, task`. Je hebt ook
andere die je kan gebruiken, maar die staan wel in de [documentatie](https://docs.locust.io/en/stable/writing-a-locustfile.html) beschreven.
Daarna maak je een klasse aan maken met parameter `Httpuser`. Als je wil dat een functie uitgevoerd wordt
binnen een klasse moet je `@task` er boven zetten en in de functie als parameter `self` in zetten. Als je dat
hebt gedaan kan je beginnen met het maken van de simulaties.
* Op de webapplictatie:
  * Klik op `F12` en ga naar `Network`, reload dan nog wel een keertje. Om te kijken voor de Get & Post requests
  ga je de filters instellen op `XHR` en dan zie ook meteen of het een Get of een Post is. Bij Get kan je de 
  informatie halen uit de `Headers` & bij Post bij `Request` (als je daarbij op `Raw` klik krijg je JSON).

***
**Hoe draai je meerdere locust's naast elkaar?**
* Door dus `-P` mee te geven als argument in de cli met daarnaast bijvoorbeeld 8080.
* In het locustfile staat het wel hardcode erin, dus dat moet je dan zelf aanpassen. Dat doe je door:
  * Zet eerst de eerste aan.
  * Daarna ga je in de code een aantal dingen aanpassen (de lijnen kunnen misschien niet kloppen):
    * Lijn 37: schakel os.system('rm locust_output.csv') uit. Dit omdat die anders bij elke locust die je aan zet alle output van verwijdert wordt.
    * Lijn 209: verander de port: 8089 --> 8080
    * Lijn 224: verander de naam van het csv bestand.
  * Zodra je dit hebt gedaan kan je de volgende loucst aanzetten (met de juiste port natuurlijk)

***
**Foutmelding bij de search_simulation?**
* Dit kan gebeuren doordat je bijvoorbeeld op een andere server zit en niet lokaal zit.
* Ga naar het script toe en pas op lijn 129: {hosting_domain} --> de host waar je nu op zit. Dus als je bijvoorbeeld als host 'omgeving.romy.edwh.nl' zit, gebruik je de 'romy.edwh.nl'. De 'omgeving' sla je over aangezien 'web2py' daar moet staan.

***
**Wat is het verschil tussen Get en Post**
* Get die heeft de request parameter meteen in de URL string zitten en 
Post neem de request parameter mee in de message body
* Get is meer voor het inlezen (dus dat je informatie krijt) en Post is meer
voor het maken (dus informatie versturen).
  * Voorbeelden:
    * Get
    * ```python
      self.client.get('/fragmentx/item?item_id='
                      + tile + '&GHOST_BASE=/&FRONT_END_BASE'
                      '=/fragmentx&item_uri_template=/cmsx'
                      '/item/{}&user_uri_template=/cmsx/user/{'
                      '}&login_url=https://fragments'
                      '.meteddie.nl/v1.0/front_end/login')
      ```
    * Post
    * ```python
      self.client.post('/fragmentx/tiles',
                      json={"qf": self.random_qf, 
                            "q": self.random_word, "page": random_page,
                            "tags": [self.random_qf], "order": "", 
                            "GHOST_BASE": "/", 
                            "FRONT_END_BASE": "/fragmentx",
                            "limit": 9, "paginate": True, 
                            "item_uri_template": "/cmsx/item/{}",
                            "user_uri_template": "/cmsx/user/{}",
                            "login_url": "https://fragments.meteddie.nl/v1.0/front_end/login"}
      ```

***
**Andere HTTP methods**
* [Wat welke HTTP method is](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
* [Wat het verschil tussen de HTTP methods is](https://www.restapitutorial.com/lessons/httpmethods.html)
