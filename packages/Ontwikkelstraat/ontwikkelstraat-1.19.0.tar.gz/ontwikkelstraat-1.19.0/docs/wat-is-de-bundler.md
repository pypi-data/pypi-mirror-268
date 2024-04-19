# Wat is de bundler
Veel omgevingen hebben ook static files (Javascript en CSS) met dependencies nodig.
Om deze samen te voegen en remote dependencies er bij in te verwerken, is de bundler gemaakt.

## bundle.yaml

Het makkelijkst is om een bundle.yaml te gebruiken om de static file dependencies van een proejct te beheren.
In theorie zou alles ook via de commandline moeten kunnen, maar dat is een stuk minder handig om te gebruiken.
De yaml bevat de volgende top-level keys:

- js: heeft als value een lijst van dependencies voor de javascript. Dit kan bestaan uit:
    - een URL van een remote dependency (bijv. htmx)
    - een pad naar een lokale JS file
    - een pad naar een lokale HTML file - die zal aan het einde van de body worden toegevoegd (handig voor bijv. modals)
    - inline javascript: moet beginnen met een comment (/* ... */) om herkend te worden
    - inline hyperscript: moet gewrapd worden in _() of _hyperscript() om herkend te worden
- css: heeft als value een lisjt van dependencies voor de javascript. Dit kan bestaan uit:
    - een URL van een remote dependency (bijv. bulma)
    - een pad naar een lokale CSS file
    - een pad naar een lokale SCSS/sass file, deze zal naar css worden omgezet
    - een dictionary met de volgende keys:
        - file: een pad/url naar CSS/SASS
        - scope: een class of ID die om voor classes wordt gezet (handig voor de LTS versie, waar onze CSS niet mag
          conflicteren met de normale CSS van een site)
        - minify: 0 of 1, of het stukje CSS geminified moet worden
- config: dit bevat de overige settings. Elk van deze settings kan ook als variabele gebruikt worden in de rest van de
  yaml, door een $ voor de key te zetten.
    - minify: moet de JS/CSS geminified worden?
    - output_css: waar wordt de output CSS naartoe geschreven? (1 file)
    - output_js: waar wordt de output JS naartoe geschreven? (1 file)
    - (en eigen keys die je als variabelen verder in de config wil gebruiken)

## Alle Omgevingen

### bundle.build

`bundle.build --cache=0/1 --version=... --input=... --minify=0/1 --output-js=... --output-css=...`

- cache (default: 1): use local cache for remote dependencies
- version (default: latest): specify bundle version (available as $version in the yaml)
- input (default: bundle.yaml): specify config yaml location
- output-js (default: output_js): overwrite config yaml setting
- output-css (default: output_css): overwrite config yaml setting

### bundle.build-js

Lijkt op bundle.build maar doet alleen de JS files

### bundle.build-css

Lijkt op bundle.build maar doet alleen de CSS files

## LTS

Voor de [LTS app](wat-is-lts.md) wordt bijgehouden welke versies van de bundel zijn uitgegeven (met changelog). Hiervoor zijn wat
specifieke commando's:

### bundle.list

Laat alle versies zien die de LTS database kent

### bundle.publish
`invoke bundle.publish --no-css --no-js --filename --major/--minor/--patch`

- (no)-css/js: publish slechts voor één van de twee een nieuwe versie
- filename: overschrijf bundle.yaml lokatie
- --major/--minor/--patch/--version: bump semantische versie (MAJ.MIN.PAT) of publiceer specifieke --version; indien niet opgegeven, wordt het nieuwe versienummer gevraagd

Compile en publiceer een nieuwe versie van de bundles.

### bundle.reset

Verwijder alle versies van de bundles uit de LTS database