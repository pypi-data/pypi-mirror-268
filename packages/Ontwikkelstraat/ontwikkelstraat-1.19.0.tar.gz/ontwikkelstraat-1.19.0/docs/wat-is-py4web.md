# Wat is py4web

# py4web-debug-tools

~~(I am absolutely crazy - indeed...)~~

[py4web debug tools](https://pypi.org/project/py4web-debug-tools)  bevat code die een 'debug mode' check doet (PY4WEB_DEBUG_MODE = 1),
en een `tools.enable` functie bevat. Voer deze functie uit in een controller om de standaard py4web error page uit te
breiden met een traceback van de error.

### dd()

de patch bevat ook een dd (dump and die) helper, die een specifieke error throwt, waardoor de value die je meegeeft aan
dd via een custom JSON encoder (explicieter voor sets en named tuples) als een soort error scherm weergegeven wordt in
de browser.
Het voordeel hiervan is dat het diep in een model gebruikt kan worden, waar je normaal alleen vanaf controllers data kan
weergeven/returnen.
