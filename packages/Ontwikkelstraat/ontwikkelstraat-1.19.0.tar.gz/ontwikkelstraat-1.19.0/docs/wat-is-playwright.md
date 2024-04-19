# Wat is playwright
## Voer Playwright tests uit m.b.v. PyTest & Xdist
**LET OP: Voer pytest commando's ALTIJD uit vanuit de root folder!**
**Dit heeft invloed op de uitvoering van bepaalde tests!**

##Stap 0: Installeer Playwright, Pytest & Xdist
Playwright, PyTest & Xdist zijn m.b.v. requirements.txt al automatisch geïnstalleerd.
Als dit niet het geval is, installeer dan Playwright, PyTest & Xdist met de volgende commands:
```
pip install pytest-playwright
pip install pytest-xdist
```

##Stap 0.5: Installeer Playwright browsers
Installeer hiermee de browsers die Playwright gebruikt (Chromium, FireFox & Safari):

Voor Windows 10:  
`playwright install`

Voor Ubuntu 18.04+:  
https://github.com/microsoft/playwright/blob/master/utils/docker/Dockerfile.bionic
```
~/.local/bin/playwright install
~/.local/bin/playwright install-deps
```

##Stap 1: Maak een standaard test, als deze nog niet bestaat.
De reden dat overal test_ voor of achter staat heeft te maken met het gebruik van PyTest
Directory: test_example_tests | example_tests_test  
Filename: test_example.py | example_test.py
```
from playwright.sync_api import sync_playwright
import pytest


def test_playwright_with_pytest():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        print(page.title())
        assert page.title() == "Fast and reliable end-to-end testing for modern web apps | Playwright"
        browser.close()
```

##Stap 2: Command Line Interface
**LET OP: Voer pytest commando's ALTIJD uit vanuit de root folder!**
**Dit heeft invloed op de uitvoering van bepaalde tests!**

Met behulp van "invoke" worden pytest commando's uitgevoerd. Het optimale pytest commando
is:  
`pytest -v -n auto --browser chromium --browser firefox --browser webkit`

Dit commando wordt met behulp van invoke zo uitgevoerd:  
`invoke pytest`

Om Screenshots te maken voeg je --screenshot toe:  
`invoke pytest --screenshot`

Om screenshots te maken én de eerder gemaakte screenshots te verwijderen voeg je --screenshot en --clean-screenshots toe:  
`invoke pytest --screenshot --clean-screenshots`  
LET OP: Dit werkt niet onder virtualbox!

Om warnings te kunnen zien (die standaard uit staan), voeg je --disable-warnings toe:  
`invoke pytest --disable-warnings`

Om headed de tests te kunnen zien (visuele browser), voeg je --headed toe:  
`invoke pytest --headed`  
LET OP: Dit werkt alleen als er een visuele verbinding is met vagrant. (X Port-Forwarding)

##Stap 3: Bekijk error messages.
Via Terminal:
![img.png](playwright_img.png)