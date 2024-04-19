# Wat is LTS

De LTS bevat een kopie van fragmentx, die minder vaak gewijzigd wordt en daarmee (in theorie) stabiel genoeg is voor
derde partijen om onze tiles op hun pagina's te includen.

De LTS werkt met een gebundelde CSS (voor onze tiles styles) en JS (voor onze tiles logica) die met `bundle.compile`
en `bundle.publish` gemaakt worden (zie [de bundler](wat-is-de-bundler.md)). De LTS app bevat naast de fragmentx
functionaliteit ook custom functionaliteit om
deze versies te kunnen beheren (bijv. `lts/docs` en `lts/manage`).

[Volledige documentatie (voor externen) hier.](https://fragments.meteddie.nl/lts/)
