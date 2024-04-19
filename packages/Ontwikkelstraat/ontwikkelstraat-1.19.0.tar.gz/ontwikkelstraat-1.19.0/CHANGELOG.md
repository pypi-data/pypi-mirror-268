# Changelog

<!--next-version-placeholder-->

## v1.19.0 (2024-04-18)

### Feature

* Add address to coordinates conversion feature ([`4456593`](https://github.com/educationwarehouse/ontwikkelstraat/commit/4456593da89d1d41730714f4fafe378ac18a852f))

### Fix

* Pip.compile web2py requirements because geopy was added to .in + refactor `load_geo` code ([`83b8e5e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/83b8e5ecf2d80a203553bfd2719d6a35bde8fd83))
* Nominatim er weer uit gesloopt ([`6384a34`](https://github.com/educationwarehouse/ontwikkelstraat/commit/6384a34948fc90eb9ee6dad6aa4bc8f93ccad663))

## v1.18.6 (2024-04-11)

### Fix

* **tags:** Use request.args instead of request.vars ([`2d45532`](https://github.com/educationwarehouse/ontwikkelstraat/commit/2d455323d8627c2d8c5fb5963223cf07568d4935))

## v1.18.5 (2024-04-11)

### Fix

* **tag:** Workbench tag page should also work via args (instead of just vars) ([`c167de5`](https://github.com/educationwarehouse/ontwikkelstraat/commit/c167de549f4dd3fb78eeb54c8b63c9877dcbb6d8))

## v1.18.4 (2024-04-11)

### Fix

* **autotag:** Edit_tag/<gid> page does not exist, it should be workbench/tag/<gid> ([`babd5b7`](https://github.com/educationwarehouse/ontwikkelstraat/commit/babd5b788009b782df0886ca3949f0e59b09a033))

## v1.18.3 (2024-04-11)

### Fix

* '.name' still doesn't exist on None ([`e63c657`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e63c657bf7198bcabeb1eb99ac5b1d2860ebf0f6))

## v1.18.2 (2024-04-11)

### Fix

* Bump dependencies again because certbot found another ([`ad51550`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ad515504825501d7bfdc3bb239915ddc5b00ce5f))
* Additional fix for 'Tagged In Db' removed tags ([`0ec7d6d`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0ec7d6d63b8295c1825d0ecac198def544a98ee1))
* Auto tag for missing gid should not crash the whole autotag page ([`a5e54e9`](https://github.com/educationwarehouse/ontwikkelstraat/commit/a5e54e9e5e43431a430784a6ecc239238822c4cb))

### Performance

* Speed up docker builds by doing COPY as late as possible (-> can cache more steps) ([`dfd5c3a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/dfd5c3aa84d1f416d1732a649d6679c507094003))
* **docker:** Installeer eerst web2py en dan de andere dependencies. Dan is rebuild sneller (want w2p install is gecached) ([`0f5de90`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0f5de9000a289b2e2a04f9ee5a8fbdd61372692d))

## v1.18.1 (2024-03-21)

### Fix

* Bump dependencies (make dependabot happy) ([`21b9a27`](https://github.com/educationwarehouse/ontwikkelstraat/commit/21b9a2784d6b01c34efd73719bca0d8adec3248f))
* **sticker_link:** Added xml ([`d443b61`](https://github.com/educationwarehouse/ontwikkelstraat/commit/d443b61dbab4bda1e644567091579bef3c425758))
* **stickers:** Web2py sticker beheer - gebruik nieuwe htmx widget + cleanup code ([`70edf50`](https://github.com/educationwarehouse/ontwikkelstraat/commit/70edf50b63a617bfdc7526c96ac95a9a6ab6447f))

### Performance

* **docker:** Ook web2py met uv (waar mogelijk) ([`c989510`](https://github.com/educationwarehouse/ontwikkelstraat/commit/c989510b77614fecd6a3a444e05b292f68bb6f9a))
* **docker:** ✨ blazngly fast🚀 docker builds dankzij UV (behalve vor w2p) ([`1174c83`](https://github.com/educationwarehouse/ontwikkelstraat/commit/1174c83eaf4659cdb6cdabb7774acc3a223b7447))

## v1.18.0 (2024-03-15)
### Feature
* Add untag function and modify grid settings in controllers ([`ffa86eb`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ffa86eb77e77e1d3f8d67203107941f7b34e7c1f))
* Add recursive child search in tag search logic ([`e09ce7e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e09ce7e1d177d7c8e718e90b0e311f870e925aa5))
* Add work_auto_tags_magic task in backend tasks ([`f090858`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f09085802b89e1ccec599ce42eaa873dc44922a7))
* Create_auto_tag migration toegevoegd ([`f07af43`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f07af43dea7885e54394deac062ea8ff286a1998))
* Clean up sessions bij ew setup (benodigt unreleased versie van edwh!) ([`561a87e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/561a87e12ef387c0224ab808283b7cac18f334b4))

### Fix
* Clean up tasks - remove duplicate config loading at start (use edwh.TomlConfig instead when needed) ([`8ad5699`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8ad56997d601ae3ba8775ab5659c6aa83b577c28))
* Improve auto-tagging feature and refactor code ([`dfaa60d`](https://github.com/educationwarehouse/ontwikkelstraat/commit/dfaa60d1d7abf63be188e206539827e75eb3a186))
* Add 'invoke' to requirements, remove dependencies from 'typing-extensions' ([`62c639b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/62c639be84459fbe35c83caf19c8f94446359f60))
* Update command in docker-compose.yml ([`e831d87`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e831d87c94940e3d8c4d27c280bd5ef0575444c7))
* Edwh-migrate requirement fix, boost naar 0.7.5 ([`2c870f6`](https://github.com/educationwarehouse/ontwikkelstraat/commit/2c870f61d09643f862dc083f52c7e74f6d76494c))
* Update database queries in engine.py ([`bc5272b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/bc5272b36c4c993e9188cf56d90292620d0571f1))

## v1.17.0 (2024-03-14)

### Feature

* Basic tag lookup (note: CSS doesn't work on datalist for some reason) ([`e8bf7bc`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e8bf7bcccba431c6f84794ca8a991eb688abc7a9))
* Advanced search query opties van p4w overgenomen naar w2p workbench ([`63fecab`](https://github.com/educationwarehouse/ontwikkelstraat/commit/63fecab2a9f054a8d32c2e5aa782d09ee4190d42))

### Fix

* **tag_gid:** Show currently selected tag after choosing one ([`caec37b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/caec37b5afcacb18124d8849851f1be51f172f78))
* Actually use 'edwh_web2py_effdted_prio_grid' and deprecate local copy ([`6304db8`](https://github.com/educationwarehouse/ontwikkelstraat/commit/6304db86760e28de24c0b9bcfff38d9b4411f0c7))
* Datalist does not work well in all browsers, change to custom solution ([`99bdc60`](https://github.com/educationwarehouse/ontwikkelstraat/commit/99bdc60613b183ad303ea0ddd8b97c2828e7e009))
* **fragmentx:** Search by tags (#rekenen) ([`3855a75`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3855a75952f9fd48a01a9c9f58a9011ff7df83d3))
* Nieuwe organisatie aanmaken ging stuk want gid werd niet meegestuurd in de form ([`d1883eb`](https://github.com/educationwarehouse/ontwikkelstraat/commit/d1883eb4f94e5d07e8e9208a43e5515e6b37399e))
* **workbench.items:** Sorteren op "laatst gewijzigd" doet het nu iets beter ([`8915da4`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8915da4b023ff1dc3609b2a7406d4bfb570bb673))
* **filter:** Filter modal opent meteen en is niet te sluiten (Zoetermeer en Leiden) ([`3468e0b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3468e0b69173eba54f786e87e9999c062a16b4a7))
* Updated copyright to 2024 ([`323942d`](https://github.com/educationwarehouse/ontwikkelstraat/commit/323942d5b8124d086f1a4a1f4c8a3cb8a7b1ee5e))

### Documentation

* Explained that org tag must be a child of Organisations ([`760ccd4`](https://github.com/educationwarehouse/ontwikkelstraat/commit/760ccd46706aeff02d70b23601c44aadef094036))

## v1.16.0 (2024-03-14)



## v1.15.2 (2024-02-27)
### Fix
* **lts:** Also use LTS-specific base template settings in LTS controllers ([`c4695b1`](https://github.com/educationwarehouse/ontwikkelstraat/commit/c4695b1af378b0c3c1c888c0da50a1aa33d481c9))

## v1.15.1 (2024-02-27)
### Fix
* **lts:** Make .json extension output JSON again (for redash) #1980 ([`479a3a8`](https://github.com/educationwarehouse/ontwikkelstraat/commit/479a3a8a6c1ccd622701e7d11c44bd194386c73f))
* **tag:** Van tag naar item gaat nu iets beter: ([`4a184c1`](https://github.com/educationwarehouse/ontwikkelstraat/commit/4a184c1934ec505f7fd50f161ff632a3c6aac3b0))

## v1.15.0 (2024-02-26)
### Feature
* Add 'average' map center option to move map around (useful for placed at the edge of the map) ([`650b28a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/650b28aae145545f8c3d970fbe0290732a6461a8))
* Support custom map zoom and map center ([`ca03d37`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ca03d37ad4658aba3252cad9ef6090c53b484453))

### Fix
* **filter:** Include the rights import (which were added for LTS but missing for fragmentx + narrowcasting) ([`787875b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/787875bbf276247229af46e84beec3b2f2bb2368))
* Also show labels instead of just gids for applog changes in tags, authors ([`8a17bc5`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8a17bc5eaf853410c1666268c0423f140cd70b5a))
* Rename SMTP_FAKE sender to console@edwh.nl ([`3f12709`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3f12709ba457d16ca3ae78280bd4a65938a1dc40))
* Filter type (modal vs default) was incorrect gecached door p4w, dus nieuwe partial() logica ([`ce893ce`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ce893ce4495dc096fa27a155cfb3c6876701fd97))
* **lts.builder:** Tag selector was missing a Fixture ([`9983bd0`](https://github.com/educationwarehouse/ontwikkelstraat/commit/9983bd0658f446e2cd74034390a1095a1b6ac5b1))
* **lts:** Renamed confusing "go to" to "download" (next to "demo") ([`1767fcb`](https://github.com/educationwarehouse/ontwikkelstraat/commit/1767fcb794f54213a07d2074e4ad57c27a9d55de))
* Renamed `local.pip-upgrade-all` to `local.pip-bump-all` to make clear nothing (locally) is upgraded ([`c2ac7f9`](https://github.com/educationwarehouse/ontwikkelstraat/commit/c2ac7f9479d589d77851809c7b5660ba71f813d2))
* JWT: errors ipv tekst met todo (4xx) ([`7c69bf7`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7c69bf769d1da1d45794bdb01af1f52253b170a4))
* Allow setting w2p SMTP server or use fake logging 'client' (useful for password resets etc) ([`7e04195`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7e041952e213d6d60469d6879f3c8f9728d318d6))

### Documentation
* **pyproject:** Commentaar waarom web2py-gluon bij de dependencies staat ([`5b9c4c9`](https://github.com/educationwarehouse/ontwikkelstraat/commit/5b9c4c9ac426c74ff742dfbb4b20cb11888c7abb))

## v1.14.2 (2024-02-20)
### Fix
* **workbench:** Fix new_tag ([`fe1f44a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/fe1f44a9ce00f8bf7ff0d34a24933865079cb6e1))

## v1.14.1 (2024-02-20)
### Fix
* **overdragen:** Re-add 'new_password' import + rewrite * imports to specific ones to catch missing imports ([`e4b6abc`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e4b6abc15b431a37895096522641e1fb4cbcdb28))

## v1.14.0 (2024-02-20)
### Feature
* Moved shared logic between p4w and w2p to framework-independant shared class. ([`e1615a3`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e1615a3be42a19367ea354ea628bea687abf1ffe))
* **jwt:** Added p4w client ([`11c02b9`](https://github.com/educationwarehouse/ontwikkelstraat/commit/11c02b9762008caaf6c166eac8089c5f0078189d))
* **jwt:** Security features such as expiry of JWT and @auth.requires_still_exists() decorator ([`b00201b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/b00201bb6c064d578c626fafc8a093d4363d2f10))
* Implemented basic JWT Auth client + server ([`de9e13f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/de9e13fe12c44d847f5a526de3950758a63fc162))
* Added school location pin to map on item page ([`20df477`](https://github.com/educationwarehouse/ontwikkelstraat/commit/20df477aca3dabf7c0e0fd7b0dc5a7ffbb406430))
* **applog.read:** Added function to find top read items and readcount of specific item by gid ([`53c6084`](https://github.com/educationwarehouse/ontwikkelstraat/commit/53c6084acb461c794d415d428c04bed794dc281e))
* Applog filter van Remco gekoloniseerd ([`4a7b41a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/4a7b41a72d93cef1c8f73b1893834dcc144090f0))
* **applog.w2p:** Link between applog timeline pages ([`25e1215`](https://github.com/educationwarehouse/ontwikkelstraat/commit/25e12150a6c2381f3a455d0b457f7604405ad770))
* **applog.w2p:** Meer pagina's om applog changes te bekijken per item, per user, totaal ([`f169d18`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f169d18f79c5425f6961567d3816a5d07d482013))
* **applog.item:** ?full=1 to also show read actions ([`7b410ad`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7b410ad4d7d3c5ce2314859eed7dc412fa785e6b))
* **applog.item:** Change ui color based on applog action ([`c17e251`](https://github.com/educationwarehouse/ontwikkelstraat/commit/c17e251b97d91a1b60c78deac795b3a000fb432f))
* **applog.item:** Initiale basic UI voor applog history bekijken voor een item ([`00b5303`](https://github.com/educationwarehouse/ontwikkelstraat/commit/00b5303e6b58a30447bd15902bb5ec63c3717c42))
* Pydal definition for applog view ([`9053a06`](https://github.com/educationwarehouse/ontwikkelstraat/commit/9053a069879fde022704a6ff8d30ddc8148d225b))
* **applog:** Add (materialized) view to make working with update-item in applog easier ([`a53858b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/a53858b404b1f9e85b728d2be0c63eb6a0d756e9))
* **applog:** Store diff for change_item ([`7d41423`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7d414235c3ce5a3e897a7e088c06aba16a7378d6))
* Add more applog.update_item + refactor imports ([`43c0787`](https://github.com/educationwarehouse/ontwikkelstraat/commit/43c078754cb106ddcf141df4b98bb609a06760cc))
* Change_item now requires author email + changes, refactor imports ([`70f1f04`](https://github.com/educationwarehouse/ontwikkelstraat/commit/70f1f041df5b0903df2102282cafa82057fa5155))
* **lts:** Task om een LTS admin user aan te maken met docker-compose ([`ab75475`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ab75475cc72a5abab54b69623245cefb72e9dc98))
* **lts:** Up-to-date met staging en kleine fixes ([`6841dce`](https://github.com/educationwarehouse/ontwikkelstraat/commit/6841dced94fdafbaf5fa2c4e198c5614c9196a07))
* **lts:** Add search + filter to LTS builder and fix modal ([`ef64758`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ef647582894efe6b1010d7d3beddf62b26bc8b65))
* **lts.filter:** Menu style modal toegevoegd als optie ([`3d52a75`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3d52a75fb6c334a8fcf4e811212858b6537b7aaf))
* **lts:** Filters optie toegevoegd aan LTS ([`877790c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/877790cd426a8d3a7b2ea8f549d2440eb7ee2712))
* **lts:** Searchbar: true om een simpele zoekbalk toe te voegen aan de simple_tiles ([`0af8fe9`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0af8fe908eef9e1c428ba382627d33ce2dfc4647))

### Fix
* **item:** Re-added json import to prevent breaking ([`6d4615e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/6d4615e51aa92c9f89100a8b2aa80f1d908f8637))
* Removed EddieAuth.bind and use current.request instead of 'bound' request ([`8c19915`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8c1991528dceaa18c4ff3bfb7d8a3cb27704cfe6))
* Redirected 'retrieve password' to jwt endpoint ([`e6de55f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e6de55ff92263d0978de4176b3829e4a3ceb1edb))
* **lts.demo:** Search + tag example that actually return some results (nicer demo experience) ([`a323604`](https://github.com/educationwarehouse/ontwikkelstraat/commit/a3236041a04c71275e16301b97074ba07dfa2c6e))
* **applog.rights:** Only eddies can see history ([`5d90c94`](https://github.com/educationwarehouse/ontwikkelstraat/commit/5d90c94b3babc646e4bd07742564374947a5a5af))
* **applog.item:** UI improvements for viewing history ([`bfdde94`](https://github.com/educationwarehouse/ontwikkelstraat/commit/bfdde94e8cc789a7300b92d8d7a67da35b5dcc22))
* **applog.item:** Try replacing old item id with item gid in applogs ([`06db305`](https://github.com/educationwarehouse/ontwikkelstraat/commit/06db3055a7093fb15842ef6baca392ee947438dd))
* New base query for vw_item_applog since previous filter already exists in the new view ([`bfb6244`](https://github.com/educationwarehouse/ontwikkelstraat/commit/bfb6244ce9e0bf7ac03b4d8ed99f09cf6a584b05))
* **applog.item:** Remove refresh button since the new view is always up-to-date ([`8f9e1a6`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8f9e1a694d095c117005d2581136ed321a18734c))
* **applog.item:** Replaced slow material view with applog sqlite for item history ([`82e9bc4`](https://github.com/educationwarehouse/ontwikkelstraat/commit/82e9bc40622704537253ff03299bc8048150994c))
* **applog.item:** Make slightly more human readable ([`93a05d8`](https://github.com/educationwarehouse/ontwikkelstraat/commit/93a05d883ce31e075a563930864ceeac7cd87785))
* **applog.item:** Rename email to by_eddie_email for consistency ([`aa90696`](https://github.com/educationwarehouse/ontwikkelstraat/commit/aa906960f4f288753544d03699c87cf1bcc2d682))
* **applog.item:** Fire 'remove' event on delete ([`ff56316`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ff563169fb85af44a3959ee8629216a8d735465d))
* Change backend.applog.update_item calls to use fields before+after instead of old (empty) changes dict ([`999042f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/999042fdaa1a16cd04c07f5583bf2a4787ed6ccb))
* Missing import ([`233ec5e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/233ec5ee00dc0952608b26cd433e6fafae5934b6))
* **typo:** Dubbel aangemaakt in 'Daartoe hebben we een account aangemaakt voor u aangemaakt.' ([`47fc2cc`](https://github.com/educationwarehouse/ontwikkelstraat/commit/47fc2cc372149e9a914d92d1bc2df16b38b23931))
* **lts:** Klikken op de sorteer-knop zorgde voor een refresh - nu niet meer ([`0fad322`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0fad322f18778890883cc41ea832f96da6a8c2f6))
* **lts:** Cdn function now returns file extension in headers ([`a98e38b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/a98e38be5cf58874f1c384b02c846dafda528605))
* **reload:** Comment out uwsgi reload code ([`0dbdcf5`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0dbdcf50d3d6e1ad8a2106536bf6404cc2c56c23))
* **lts.search:** Include initial search query ([`453c23c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/453c23c55defed4df008b75ec13b7893c9a2b0e5))

### Documentation
* Added docstrings to more JWT auth functions and classes ([`0ffbca3`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0ffbca3e1214e0aeb55505a121e8602d8cbd5788))
* **jwt:** Added Eddie Auth docstrings ([`1578294`](https://github.com/educationwarehouse/ontwikkelstraat/commit/1578294b4260601215901ec272ccd1b9328ca952))
* Added docstrings + black reformat ([`e7121e7`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e7121e70043310d403181b6b2af91daa4238babb))
* **lts:** Font-awesome weer uit docs gehaald want dat zou meegebundeld moeten worden sinds bundle 1.1.0 ([`bd9000f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/bd9000fc0b803a4d272938970b4191f3470e54c6))
* **lts:** Uitleg over search bar met eigen HTML ([`bb01847`](https://github.com/educationwarehouse/ontwikkelstraat/commit/bb018473bc043b90bce0bc732083500f086e33e9))

### Performance
* **w2p.applog:** Read-item weer uit de view voor snellere queries voor create/update/delete applog ([`0a5baa5`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0a5baa586d2bca9ebc1e349f554880ff078befe4))
* 'if in' tuple -> set, 'for in' list -> tuple ([`82a3df3`](https://github.com/educationwarehouse/ontwikkelstraat/commit/82a3df31318954718427dabd22acc7019636c141))

## v1.13.0 (2024-02-08)
### Feature
* Sector toegevoegd bij het inserten (wanneer die BO is wordt die verandert naar po) ([`d3c4918`](https://github.com/educationwarehouse/ontwikkelstraat/commit/d3c4918dd64f29e94d5cfbd32543d705cd34cd01))
* Het werkt eindelijk!! morgen testen of het echt allemaal goed gaat ([`badb773`](https://github.com/educationwarehouse/ontwikkelstraat/commit/badb77377c74912fdbae86d4020837c3656c48a8))
* Zoekt de brinvests die meer dan 1 keer voor komen en laat daarvan nu alle gegevens zien. dit kan zometeen gebruikt worden om te gaan vergelijken met fuzz.ratio om daarmee te kijken welke het meest matched met welke al in de database staat ([`9d8c00e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/9d8c00eeb55deb5ca2e26c6c7d229d7c717f8788))
* Veilige jwt data overdracht van pytest naar web2py. ([`4dea27f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/4dea27f791f8f8d467de30176dbf80fbcf501cc8))
* Webtest toegevoegd om over HTTP gebruik te maken van https://dockers.local met eerste controle van alle functies van web2py die callable zijn. Uitzondering via `# NO_TEST_REDIRECT_ON` ([`450a8ad`](https://github.com/educationwarehouse/ontwikkelstraat/commit/450a8adcdf2bb3eb9758edb353d33e12148cdc1c))

### Fix
* **w2p:** Rogue tab ([`0213e32`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0213e32355aa19b3e9ca35b2d2430aaf2e5d2bf9))
* Scholen data inserten werkt weer, er zat nog een fout in dat die `pair` in `handled_values_for_duplicates_api` niet eruit filterde bij de laatste twee for loops ([`f621cfc`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f621cfc31c4844fb646608f06cf7e7cfd9cebc4e))
* Paar kleine foutjes en wat missende velden toegevoegd. ([`ca87aa6`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ca87aa60161b3613a7e7aebfb900915af218f08a))
* Source_orgs (json) heeft een key genaamd `adres`, de database heeft dat opgesplitst in `street` en `number`. met een recursive loop gaat die het nu goed "splitsen" ([`e03537c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e03537c72cb943aa6c918f5bc950a1bdc2acac27))
* Effdt toegevoegd aan de sql query ([`f6e6344`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f6e634444fe9726182f49108f0fd845e885e95ac))
* Controleert nu op postcode en huisnummer ipv straatnaam en huisnummer ([`a00d056`](https://github.com/educationwarehouse/ontwikkelstraat/commit/a00d056c13327904561791f7b682fb234063fc94))
*  requirements.txt bijgewerkt ([`dc75d32`](https://github.com/educationwarehouse/ontwikkelstraat/commit/dc75d32b4e481ed948b4144504be75b11957ecad))
* Data importer neemt nu minder tabellen over, en de uitedindelijke view in de views werkt nu na enkele DUO data importer run. ([`86bf243`](https://github.com/educationwarehouse/ontwikkelstraat/commit/86bf2439081a9a5b5d1268e4a9ff2821879c7c5b))
* `__init__edwh__new.ipynb` werkt weer zonder fouten bij een `%run`. De tags gaven nog wel een probleem, dus dat moet later nog bekeken worden. ([`18a40aa`](https://github.com/educationwarehouse/ontwikkelstraat/commit/18a40aafca7a0c59ca73f0c3d8d1181b4feab87f))
* Nieuwe materialized views gebruikt in uiteindelijk query. ([`3b12b6a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3b12b6a3846ff183afd582e41d7b629411977749))
* Requirements.txt is hard geupgrade, vooral de edwh[omgeving,plugins] had een versie die niet meewerkte. ([`68b17ed`](https://github.com/educationwarehouse/ontwikkelstraat/commit/68b17ed0539d310c23fce66eb69c8c080ecc1c02))
* Niet alleen nulls inserten, maar ook echte data. ([`b0f88df`](https://github.com/educationwarehouse/ontwikkelstraat/commit/b0f88dfda9454475c15a0cd2535c31a967abc462))
* Nog een minusucule aanpassing. en output geschoond. ([`7d3de94`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7d3de945699c475876c575b806ae59b97c892a6f))
* Downloaden werkt met de DUO data importer op basis van datadump! ([`90227c6`](https://github.com/educationwarehouse/ontwikkelstraat/commit/90227c612dfacdc5d0d188bb958f35ef340baa4b))
* Added `Visibility` as json-able field type for `edwh_asdict` ([`6225b6f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/6225b6ffc77ba0a39b6b5b10ac25c181a141156d))

## v1.12.0 (2024-02-05)
### Feature
* Add Uptime Robot auto add (domains via traefik) to setup task ([`7df1884`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7df188460609c8b01bbaa3b8374e3758317cf442))

### Fix
* **migrate:** Allow building migrate Docker even if B2 key is missing ([`3135761`](https://github.com/educationwarehouse/ontwikkelstraat/commit/31357616d22aa28c047d99084e865013b3beaad0))
* Don't crash if uptime plugin is not installed. + run `ew bundle.build` also in a 'loose' way ([`118ab9f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/118ab9fe74797c1fd02b0be10d14bf77ae8419ec))

## v1.11.1 (2024-02-05)
### Fix
* Besturen-search was kapot omdat w2p door een timestamp field zocht alsof het text was. ([`2567c6d`](https://github.com/educationwarehouse/ontwikkelstraat/commit/2567c6d46a649d1d305f390fa753732171a3c895))
* **thumbnail:** Use same logic in fragmentx; copy latest backend support ([`64eae44`](https://github.com/educationwarehouse/ontwikkelstraat/commit/64eae44b5787b6174fb7b6fd7f0b058d31bd3777))
* **thumbnail:** Progress gif wordt nu vervangen met letterplaatje ([`085ab05`](https://github.com/educationwarehouse/ontwikkelstraat/commit/085ab05214cd9ab955519fa703d1c9010c006eca))

## v1.11.0 (2024-01-10)
### Feature
* Ondersteuning itempagina binnen regioplatform ([`bf32fb3`](https://github.com/educationwarehouse/ontwikkelstraat/commit/bf32fb396f5056553e0bafcee6a4aa725db22137))
* Move simple analytics script to fragmentx via htmx so we can check if there is a logged in user ([`f997301`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f99730154fb880e27b04e2815dbb08db238848e4))

### Fix
* Docker compose (zonder -) heeft -qa nodig ipv -q voor inspect ([`479672c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/479672c385b81530ff00352a6db4d5b085969a50))
* **dc:** Set external: true instead of old deprecated syntax ([`4b5c0da`](https://github.com/educationwarehouse/ontwikkelstraat/commit/4b5c0da60b1b6d04c49accfac038dd366bdcd7d4))
* Security update to make dependabot happy ([`b07e667`](https://github.com/educationwarehouse/ontwikkelstraat/commit/b07e66746ff1f246a12c26f4aabed6cfd2e71112))
* Local up for og metadata + use DOCKER_COMPOSE instead of hardcoded docker-compose ([`f460c39`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f460c39cc74f0f1875540327066e8612ca43eda7))
* Copyright icons via PY4WEB_URL so it's absolute (from the hosting domain) ([`ccb4416`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ccb441622387fd929c25c1764be5b04d2cd6a735))
* **shared_applog:** Add jovyan user to microservices group so it can access/edit shared_applog etc. files ([`da73245`](https://github.com/educationwarehouse/ontwikkelstraat/commit/da73245d0c664ba071504e2cb55ee8d198695f7a))
* **docker:** Upgrade pip dependencies because docker wouldn't build anymore ([`83620ff`](https://github.com/educationwarehouse/ontwikkelstraat/commit/83620ff23da962b7b8e64e49862c54691a703875))
* Hide 'deprecated' tags from item page ([`b29c86e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/b29c86e260ad52884d4436c8279faae068985434))

### Documentation
* Added docs to local setup/up hooks and _py4web_url helper ([`dd203c8`](https://github.com/educationwarehouse/ontwikkelstraat/commit/dd203c8e8be1bc497f64c3dcff820d70e9138840))

## v1.10.2 (2023-11-16)
### Fix
* **letterplaatje:** Py4web's URL uses the HTTP ORIGIN header images were still pointing to the wrong domain ([`7f4eda9`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7f4eda9c86cb92436ec371b00347ddc0d0772de5))

## v1.10.1 (2023-11-16)
### Fix
* Letterplaatje url absolute ipv relative for 3rd party users ([`dab7392`](https://github.com/educationwarehouse/ontwikkelstraat/commit/dab73921adb26168df176162985a8adfacc87b52))
* __str__ did not return string and that crashed fragmentx+lts index ([`bf45f54`](https://github.com/educationwarehouse/ontwikkelstraat/commit/bf45f541541d2614ae9214f286e28a3edf25cfb6))

## v1.10.0 (2023-11-16)
### Feature
* Item_new_tab setting om te kiezen of een praktijkervaring in een ander tabblad geopend moet worden ([`40e89f7`](https://github.com/educationwarehouse/ontwikkelstraat/commit/40e89f7c78aed5631dfaae903238dd778ad99a35))
* Je krijgt nu een melding als je er geen cookie ingesteld kan worden ([`3781888`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3781888694083b4d232bcc2af7309fc5d1b4e1e9))
* **w2p:** Change document title to `Workbench ($controller)` for keepass autotype integration ([`dc653e3`](https://github.com/educationwarehouse/ontwikkelstraat/commit/dc653e3e8903fea778403d37fcc31dc5e7aaa2e3))
* **item:** Thumbnail 'letterplaatje' now looks at the first letter of normalized non-stopword in title. ([`181b911`](https://github.com/educationwarehouse/ontwikkelstraat/commit/181b911d53f6f4c8b33c5c3e4c3aaf41292f9616))

### Fix
* **lts:** Copy controllers.py from fragmentx since lts/tiles crashed ([`e392aed`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e392aedcf13950c81af4b5816413902a8ea0612a))
* **p4w:** Add debug tools requirement ([`0a3607a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0a3607ae8e4d7d8b1cc37a0cff61ae88f553d597))
* Don't crash if only stop words ([`501f60b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/501f60b805fdb4a639ea8790a5c9331b71096658))
* Copied backend support from fragmentx to narrowcasting and lts ([`4278c40`](https://github.com/educationwarehouse/ontwikkelstraat/commit/4278c401a234b2e1b5fde57fb796a96db0e6802d))

## v1.9.0 (2023-10-26)
### Feature
* `ew local.database-connections` al dan niet gepaard gaand met een `sput rmam` of `|width` (zie joplin). ([`ab174dc`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ab174dc7466662ddcd918762b3fd6af487c10a2b))

### Fix
* Update_materialized_view_mv__tag_arrays heeft nu docstrings; toont de tijd dat het geduurd heeft en heeft de `db.close` in een finally statement zitten. Het doel is dat de database verbinding vrijgegeven wordt, want dat blijkt onze connecties op te vreten in productie. Zie #1533 op taiga. ([`fdf297b`](https://github.com/educationwarehouse/ontwikkelstraat/commit/fdf297be8b208a6a0fffc8e43b52fac0262141ed))
* Defaults van lege dicts voor request.json of request.params ([`385587e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/385587e06f4fd96069b43662aa4861c159a85ca2))

### Documentation
* Celery worker backend_workers krijgt nu automatisch een herstart elke uur. Hierdoor worden dangling connecties hopelijk opgelost. Door `max_retries=0` wordt de herstart job niet continue gespawned en heb je niet een eeuwige restart loop. De celery-workers staan via docker-compose aangemerkt als `restart: always` dus docker slingert ze wel weer aan. ([`54496c8`](https://github.com/educationwarehouse/ontwikkelstraat/commit/54496c8f6f60e46c3b17bd2d64776eb426fd60d8))

## v1.8.3 (2023-10-26)
### Fix
* .json support voor alle urls: ([`be6cc2c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/be6cc2c4e52bf1d1981599f3e192f33ff8ed90e4))
* **lts:** Copied images from fragmentx ([`e8676bb`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e8676bb7e8f492fe7814e97b92fd6c48205436bf))

### Documentation
* Update van changelog ([`ec37413`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ec374134bd563a696be53f92133cd3dbcee834dd))

## v1.8.2 (2023-10-12)
### Fix
* gebruikt voor preview url nu een punt ipv met een slash... ([`f2acf76`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f2acf767de81cd800284ddf4bdaac0999e5ee054))
* 'openen op website' link houdt nu rekening met hostingdomain en application name 
### Documentation
* Update van changelog ([`05b808d`](https://github.com/educationwarehouse/ontwikkelstraat/commit/05b808dc1990865d8dec2fca18097e4a2ee1ad8b))

## v1.8.1 (2023-10-05)
 * landelijk/updates - security fixes
 * landelijk/feat_restart_via_query_arg/robin - restart?secret ipv restart/
 * landelijk/fix_item_visibility#1518/robin - deleted items zijn niet meer zichtbaar via de specifieke URL, maar preview items nog wel. 
 * landelijk/fix_duplicate_slug_error_msg#1503/robin - minder hoofdpijn voor Eddies als ze een naam 2x invoeren
 * landelijk/fix_filter_count_#1152/robin - visibility wordt nu meegenomen in de tellingen, dat was eerder niet zo (klad items werden meegeteld)
 * landelijk/fix_register_autofill_#1107/robin - KVK en plaatsnaam wordt weer aangevuld. :party: 

## v1.8.0 (2023-09-21)
### Feature
* **lts:** .json routes (met auth) voor gebruik in redash ([`a6127a1`](https://github.com/educationwarehouse/ontwikkelstraat/commit/a6127a1bab143f5314641f9fe9d3b9444505da54))
* Base tag toegevoegd ([`36d0151`](https://github.com/educationwarehouse/ontwikkelstraat/commit/36d01516b7a173f1ab68bc6ac25e75a2b69e5a6e))
* Iol-filter tag toevoegen in de iol rapportage ([`1a1d0b0`](https://github.com/educationwarehouse/ontwikkelstraat/commit/1a1d0b0728cfaf34e8ac208b67adf5db54e5db72))
* **tasks:** `save_backup_through_tunnel` toegevoegd ([`af32224`](https://github.com/educationwarehouse/ontwikkelstraat/commit/af32224038a2f6d56592c5771408974cb3a44fb1))
* **Docker:** Nieuwe images gebruikt ipv ubuntu. ([`9e1e237`](https://github.com/educationwarehouse/ontwikkelstraat/commit/9e1e237511d1e1af875d9197e0c58f5aa19fd11f))

### Fix
* Missing dependency pytz for fragmentx celery ([`db73d93`](https://github.com/educationwarehouse/ontwikkelstraat/commit/db73d93ab3a1c4bfcc26c9638dab951725443433))
* Missing dependency pytz for celeries ([`57fdab0`](https://github.com/educationwarehouse/ontwikkelstraat/commit/57fdab098782eee28b196c12d7024edca85f99be))
* Deze fixes doe ik steeds opnieuw maar for some reason komen ze maar niet mainstream terecht... ([`013cb51`](https://github.com/educationwarehouse/ontwikkelstraat/commit/013cb51914e1ec9f0033c959d0c4a231b25fd7c3))
* Re-compile jupyterlab requirements after merge ([`6311e55`](https://github.com/educationwarehouse/ontwikkelstraat/commit/6311e55531b28076b471b8db893c674b9ddd39d8))
* Quickfilter iolrapportage gid toegevoegd aan Voor scholen ([`48daa58`](https://github.com/educationwarehouse/ontwikkelstraat/commit/48daa58a07514342a7a7c1029a56e9d9d6b9f995))
* Style toegepast icm url's die horen bij iolrapportage. ([`c50ae9c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/c50ae9c9a53d712b40331eaf1546ee9a65abe619))
* **py4web:** Sqlite3 weer opgenomen als dependency voor LTS ([`3c3a083`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3c3a083fb51d08effed92f781c86ccdcde64bd2a))
* **tasks:** Sleep voor postgres verwijderd ([`de2aee4`](https://github.com/educationwarehouse/ontwikkelstraat/commit/de2aee4936d287bc841f0d18f51dc08b98c5fc63))
* **clicktracker:** Geen protocol in url laat het nu niet meer crashen ([`a63db4a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/a63db4a5d6149ccc4b5c0099133c3f40101081cb))
* **tasks:** Don't overwrite _default with a symlink if _default is set as DEFAULT_APP in .env ([`4c07e20`](https://github.com/educationwarehouse/ontwikkelstraat/commit/4c07e208263a1c9d2989640b337b42b0237a3afd))
* **modal:** Esc als er geen modal is deed funky. 'el in .class' -> 'el matches .class' is de goede hyperscript ([`feecf35`](https://github.com/educationwarehouse/ontwikkelstraat/commit/feecf3509ba1ce704518e62c1087dea750613e41))
* **update:** Web2py gaat slecht op urllib3 2.0 dus pin op <2 ([`9b1ffd4`](https://github.com/educationwarehouse/ontwikkelstraat/commit/9b1ffd49ab96cff147db72e820211c44ff221a85))

### Documentation
* Uitleg verbeterd zodat we geen `.../feature/xxx[/dev]` hebben, maar altijd `.../feature/xxx/[dev|staging]`. Toelichting op release proces. ([`8766033`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8766033a382e9dc85fe58ce4f4a4eeaa25f30b68))
* Releases gemarkeerd in cangelog + branch naamgeving ([`61831af`](https://github.com/educationwarehouse/ontwikkelstraat/commit/61831afa4186b87f6e1117c716190c57d0a450bb))

# Released on 2023-06-15

## v1.7.0 (2023-06-15)
### Feature
* Eddies zien verwijderde items niet langer in het item overzicht, maar admin gebruikers wel. Dit scheelt veel onoverzichtelijkheid, terwijl admins wel snel een item terug kunnen halen uit vergetelheid. ([`5293fc6`](https://github.com/educationwarehouse/ontwikkelstraat/commit/5293fc6faf187e78b094563f239d7d0bcaf875cb))
* Gewicht toevoegen aan akas en naam voor de tag_search, zo werkt deze net wat handiger. ([`1572eed`](https://github.com/educationwarehouse/ontwikkelstraat/commit/1572eeda554f1d40ca25910efa193cd6aa5473b4))
* Alleen met 'edit_tag_structure' recht mag je nu de verhoudingen tussen tags aanpassen. ([`78839e3`](https://github.com/educationwarehouse/ontwikkelstraat/commit/78839e38a4305055bc17b765af36b9bbd31020f4))
* **sticker:** Require is_admin or is_supereddie to remove a sticker tag ([`604b8aa`](https://github.com/educationwarehouse/ontwikkelstraat/commit/604b8aa7262a02dc80079ee0c4bccb504041c57a))
* Stickers kunnen nu ook verwijderd worden via een verwijder knop in het "sticker beheer" scherm. ([`e619f15`](https://github.com/educationwarehouse/ontwikkelstraat/commit/e619f1540ad1989be4f696a2de8194546bc38b39))
* `Tag` werkt nu zonder refresh en gaat tegen verwachting in nog steeds vrij snel. De `Tag` class werkt ook zonder de database verbinding bij te houden, waardoor de connecties niet meer ophopen (hopelijk). Updates van een kolom werken redelijk, de volgorde is aan te passen, er is te slepen van de ene kolom naar een andere. De search werkt, en parent-child relationships worden zo goed mogelijk gehonoreerd. ([`f2f5c69`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f2f5c697514ca333b8d923e3bb5c29d34d808d9c))
* **tags:** (EOD) bezig met een tags UI overhaul middels HTMX om een sortable tag tree te maken, die **hopelijk** kan samenwerken ([`0a43222`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0a43222ccb048f76c92ef2d70d8f2b3a53163895))
* **tags:** Tags code is nu naar `shared_code/edwh/core/tags.py` verhuist. /!\ VEREIST REBUILD ([`700c6ed`](https://github.com/educationwarehouse/ontwikkelstraat/commit/700c6edf9b87c6f240d1c68cb5f3d84fd57c520c))

### Fix
* Remove_stickers en edit_tag_structure rechten toegevoegd als roles, inclusief helpers. Verder black. Verwijderen ([`2643ae4`](https://github.com/educationwarehouse/ontwikkelstraat/commit/2643ae4474d9a3100967dc2a83bab01eb153da97))
* **jupyter:** Require newer version of edwh cli tool ([`59cc874`](https://github.com/educationwarehouse/ontwikkelstraat/commit/59cc874fa02d7f19c4b3b658389401a702dcd2ad))
* Tag.new() requires a db as first argument. ([`9c63268`](https://github.com/educationwarehouse/ontwikkelstraat/commit/9c63268fa079fc56b306a8c495f8a5b351295738))
* Deprecated tags worden niet meer weergegeven in de dropdown van de tag selectie bij "sticker beheer" ([`6652543`](https://github.com/educationwarehouse/ontwikkelstraat/commit/6652543cdf6bdb5e1750e1b2fa1c5696435330d2))
* In de html werd nog een "oude" aanroep naar Tag gedaan. ([`ff2432c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ff2432cdd470a7946c8edc7fb762e85c0059b320))
* `Tag` bijgewerkt in de migrations zodat deze werkt en `Tag.refresh()` verwijderd is. ([`dc11b41`](https://github.com/educationwarehouse/ontwikkelstraat/commit/dc11b4123b264137726febaf419eb42663a1d2a9))

### Documentation
* Releases gemarkeerd in cangelog. ([`0debcba`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0debcba6b57a1d65b6d07484594f6b25816ad17c))

### Performance
* **roles:** Added setup_roles_and_users to cache so it's not executed every pageload ([`bf7cf7e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/bf7cf7e2475c14d5365812129f81a4d9164063b9))

---
# Released on 2023-06-08

## v1.6.1 (2023-06-08)
### Fix
* De (0) achter de parent tags in de filterbalk zijn gewijzigd. ([`11ac82a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/11ac82ad09436a78af464f6b30256b781977c99a))

## v1.6.0 (2023-06-08)
### Feature
*  extra contactgegevens veld toegevoegd, met validators en alles voor web2py ([`15a9039`](https://github.com/educationwarehouse/ontwikkelstraat/commit/15a9039d100941d185a4c6f0c8558416866508e4))

### Fix
* Een default value via .get ipv ['tags'] levert minder foutmeldingen op, vooral bij nieuwe sessies. ([`ed6d106`](https://github.com/educationwarehouse/ontwikkelstraat/commit/ed6d106aacf1d9d5098504ea00c5f47eee8dcda5))
* Cache-keys worden als sleutel gebruikt in de cache tabel, en deze werden te lang. Opgelost door hashing toe te passen. ([`74eee3d`](https://github.com/educationwarehouse/ontwikkelstraat/commit/74eee3d290606c64510862370fe8a3e2bb0a61f0))

## v1.5.0 (2023-05-31)
### Feature
* **tasks:** Save generated py4web password to dotenv ([`f19373e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f19373eabf709ff4eb4d4094b8c676930cf6f0af))
* **tasks:** Don't hardcode default app to cmsx (useful for other forks + debugging) ([`dbc524c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/dbc524c4b8758ef446c2bcccc05e919c1c472c6d))

### Fix
* Items per tag in de weergave van de filterbalk werkt weer naar behoren. ([`9484e3f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/9484e3fa8e9cfd347f22d2c35e7a33b1543eb85c))
* Organisatie > hernoem tag werkt nu ook met komma's in de naam. Taiga:582 ([`5550f74`](https://github.com/educationwarehouse/ontwikkelstraat/commit/5550f74be022e818859f81434ab20671d6f68e6e))
* Oplossen van taiga:1322 - zoeken naar scholen werkt niet in de workbench. ([`c0ff682`](https://github.com/educationwarehouse/ontwikkelstraat/commit/c0ff682e70cae2112412f64b948642f42a106124))

## v1.4.1 (2023-05-29)
### Fix
* **names:** Eddie wil zelf de hoofdletters bepalen bij het invoeren van een nieuwe gebruikersnaam ([`8ccb35a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8ccb35a425fc624c5615a0df9c5501555ef11456))

### Documentation
* **changelog:** Add RELEASED ON for today's release ([`11ad8db`](https://github.com/educationwarehouse/ontwikkelstraat/commit/11ad8dba9dff591d7127343a1e2998e9825a58e1))

---
# Released on 2023-05-19

## v1.4.0 (2023-05-19)
### Feature
* **quickfilter:** Support for ;-separated tags for Zoetermeer ([`477aeaf`](https://github.com/educationwarehouse/ontwikkelstraat/commit/477aeaf313144e725c778d946ceb0b29ba311dd0))
* Quickfilter multitag support ([`0ccdfdc`](https://github.com/educationwarehouse/ontwikkelstraat/commit/0ccdfdcfc9df00c1187cb30e2ff7f5f872d34e6f))
* Backup en restore scripts toegevoegd ([`8ac680f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8ac680f165b5ec6d3292b553996b8635ed4ee9d0))

### Fix
* Letterplaatjes voor LTS en Narrowcasting die ook de thumbnail_url functie hebben ([`1739dfb`](https://github.com/educationwarehouse/ontwikkelstraat/commit/1739dfb3201aa9503c4134ab0b20775b4785c8b2))
*  docs (typo in changelog and release date was wrong) ([`bfe0c8a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/bfe0c8ace23db8662b90a43a384eaffc9e1434ae))

### Documentation
* Toevoegen release moment in de changelog ([`2ad2882`](https://github.com/educationwarehouse/ontwikkelstraat/commit/2ad2882bd335a7a7642187386e60b8e1a33bac28))

## v1.3.0 (2023-05-15)
### Feature
* **ioldb:** Custom role for users from specific email domains ([`1ccfd64`](https://github.com/educationwarehouse/ontwikkelstraat/commit/1ccfd64f2579199443fd7715ef559ff5b21357ff))

### Fix
* **ioldb:** Call .lower() to make sure the check matches even if email is not lowercase for some reason ([`013ac4e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/013ac4eb7f2bfa0da2c865e061b8dbec10e2db03))

---
# Released on 2023-05-11

## v1.2.1 (2023-05-11)
### Feature
* **backup:** Backup en restore scripts ([`7627d4c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7627d4c0529b5def68bbb6f8d22ce441aaaf0277))
* **tags:** Opruimen van de tags op basis van een kopie database van de excel. ([`1829681`](https://github.com/educationwarehouse/ontwikkelstraat/commit/182968120e9cb2f5babf6b45c93cfd2751830e5c))
* **tags:** Tag-search zoekt niet alleen in namen, maar ook in akas, descrioption, search_hints, definition, instructions en remarks. EN vereist dat een tag niet deprecated is. Dus deprecated tags zijn ALLEEN via GID in de adresbalk te openen, zoeken werkt ook niet meer. ([`41e38d1`](https://github.com/educationwarehouse/ontwikkelstraat/commit/41e38d17b1b199e9a6fc10a18b6661ed799c0656))
* **tags:** Deprecated tags niet meer tonen in de tag-tree ([`f212225`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f21222556a41aa268e16a1b2db9399c66b6dc68a))
* **tags:** Tag beschrijvingen bij mouseover tonen nu veel meer velden in de tag-tree ([`7a7cf01`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7a7cf01903c5fcb41fa92c2625f6254b10386c14))
* **postgres:** Gebruik slechts 1 postgres instance ipv twee! ([`9f1eda0`](https://github.com/educationwarehouse/ontwikkelstraat/commit/9f1eda008d1d95a609a9c3883e19fc319e638ea2))
* **tasks:** Edwh local.clean-jupyter to remove output of (specific) notebooks ([`48ed70e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/48ed70e085b2762e2f5484d3f88b0b8800f3ca87))
* **tasks:** Migrate overgedragen aan edwh-migrate zodat de migrate funcationaliteit in de library is te testen en te gebruiken en niet volledig onderdeel meer uitmaakt van de kern hier. Plus dat migrate op deze manier ook te gebruiken is met sqlite databases. ([`cd66ab1`](https://github.com/educationwarehouse/ontwikkelstraat/commit/cd66ab116c6fbe6366cf38295c0e5df1eea56b7f))
* **workbench:** License automatisch op "CC-BY-SA" staat in de dropdown voor nieuwe items ([`f7b7885`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f7b78854a02c2fe506831585046a277bf93ba2fd))
* **tags:** [#991](https://taiga.edwh.nl/project/remco-ewcore/us/991) aan het toevoegen. ([`d46cf0e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/d46cf0e95f133cb4e0a7c9a592304e0bec99ec65))

### Fix
* **auth:** 'unicode' was an alias for 'str' that was removed by yatl update ([`70917a1`](https://github.com/educationwarehouse/ontwikkelstraat/commit/70917a10c6f6c784e792ec1f67cfd530da0a74dd))
* **gitignore:** Adding captain-hooks folder to ignored because all that config should be local, not in the sourcecode repo. ([`b789f71`](https://github.com/educationwarehouse/ontwikkelstraat/commit/b789f71092a0c81c3a2c3a2779981a35f393faac))
* **tasks:** Fixing a rogue pycharm refactor ([`37e7e5f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/37e7e5f4701b023b2f87b0c1eeb632993ce0613b))
* **tasks:** `pipx` can now live at different places. ([`de52d2a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/de52d2a80600c7a7b520d984008df27bbf59b300))
* **update:** Attrs is a required dependency ([`3267913`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3267913dacf3611b5be4c22517fa40ed1d694df2))

### Documentation
* Verbeteren schema's ([`c825c0f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/c825c0f654fce85109e12077bcae462e072d297b))

## v1.2.0 (2023-05-11)
### Feature
* **backup:** Backup en restore scripts ([`7627d4c`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7627d4c0529b5def68bbb6f8d22ce441aaaf0277))
* **tags:** Opruimen van de tags op basis van een kopie database van de excel. ([`1829681`](https://github.com/educationwarehouse/ontwikkelstraat/commit/182968120e9cb2f5babf6b45c93cfd2751830e5c))
* **tags:** Tag-search zoekt niet alleen in namen, maar ook in akas, descrioption, search_hints, definition, instructions en remarks. EN vereist dat een tag niet deprecated is. Dus deprecated tags zijn ALLEEN via GID in de adresbalk te openen, zoeken werkt ook niet meer. ([`41e38d1`](https://github.com/educationwarehouse/ontwikkelstraat/commit/41e38d17b1b199e9a6fc10a18b6661ed799c0656))
* **tags:** Deprecated tags niet meer tonen in de tag-tree ([`f212225`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f21222556a41aa268e16a1b2db9399c66b6dc68a))
* **tags:** Tag beschrijvingen bij mouseover tonen nu veel meer velden in de tag-tree ([`7a7cf01`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7a7cf01903c5fcb41fa92c2625f6254b10386c14))
* **postgres:** Gebruik slechts 1 postgres instance ipv twee! ([`9f1eda0`](https://github.com/educationwarehouse/ontwikkelstraat/commit/9f1eda008d1d95a609a9c3883e19fc319e638ea2))
* **tasks:** Edwh local.clean-jupyter to remove output of (specific) notebooks ([`48ed70e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/48ed70e085b2762e2f5484d3f88b0b8800f3ca87))
* **tasks:** Migrate overgedragen aan edwh-migrate zodat de migrate funcationaliteit in de library is te testen en te gebruiken en niet volledig onderdeel meer uitmaakt van de kern hier. Plus dat migrate op deze manier ook te gebruiken is met sqlite databases. ([`cd66ab1`](https://github.com/educationwarehouse/ontwikkelstraat/commit/cd66ab116c6fbe6366cf38295c0e5df1eea56b7f))
* **workbench:** License automatisch op "CC-BY-SA" staat in de dropdown voor nieuwe items ([`f7b7885`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f7b78854a02c2fe506831585046a277bf93ba2fd))
* **tags:** [#991](https://taiga.edwh.nl/project/remco-ewcore/us/991) aan het toevoegen. ([`d46cf0e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/d46cf0e95f133cb4e0a7c9a592304e0bec99ec65))

### Fix
* **auth:** 'unicode' was an alias for 'str' that was removed by yatl update ([`70917a1`](https://github.com/educationwarehouse/ontwikkelstraat/commit/70917a10c6f6c784e792ec1f67cfd530da0a74dd))
* **gitignore:** Adding captain-hooks folder to ignored because all that config should be local, not in the sourcecode repo. ([`b789f71`](https://github.com/educationwarehouse/ontwikkelstraat/commit/b789f71092a0c81c3a2c3a2779981a35f393faac))
* **tasks:** Fixing a rogue pycharm refactor ([`37e7e5f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/37e7e5f4701b023b2f87b0c1eeb632993ce0613b))
* **tasks:** `pipx` can now live at different places. ([`de52d2a`](https://github.com/educationwarehouse/ontwikkelstraat/commit/de52d2a80600c7a7b520d984008df27bbf59b300))
* **update:** Attrs is a required dependency ([`3267913`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3267913dacf3611b5be4c22517fa40ed1d694df2))

### Documentation
* Verbeteren schema's ([`c825c0f`](https://github.com/educationwarehouse/ontwikkelstraat/commit/c825c0f654fce85109e12077bcae462e072d297b))

## v1.1.0 (2023-04-25)

### Feature
* **ioldb:** Gebruikt nu CAS voor authenticatie ([`91f0b27`](https://github.com/educationwarehouse/ontwikkelstraat/commit/91f0b27a33c0f17464f7eaf42bca56392ad57859))
* **ioldb:** Schermen voor sociale media en netwerken werkend gemaakt. ([`8c0ce79`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8c0ce791c24618fd1fd77463e48af6fda6f48828))
* **ioldb:** Negeer errors, sessions en uploads voor .git ([`8a0a015`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8a0a01515a7b4330c4bf5bd19d77101b84cdf833))
* **ioldb:** IOL database web2py applicatie toegevoegd ([`d2941c7`](https://github.com/educationwarehouse/ontwikkelstraat/commit/d2941c776be930318988c3fc1b57148ec7631755))
* **lts:** Automatische selectie letterplaatje voor tiles en items. ([`3d1ac5e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/3d1ac5eed1de37767077fcc374af0007eba7f418))
* **py4web:** Automatische selectie letterplaatje voor tiles en items. ([`1e0c090`](https://github.com/educationwarehouse/ontwikkelstraat/commit/1e0c0908c89923c47e7a0b56348f5a504a704081))

### Fix
* **item:** Item.html had een button die nog niet in productie mag. ([`667a12e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/667a12eb3f0b688914e4007a0aae4429d4408e47))
* **py4web:**  edwh-std-security middleware toegepast ([`2acdeb5`](https://github.com/educationwarehouse/ontwikkelstraat/commit/2acdeb5ccc265004eada4ef384d83f6f9772e158))
* **web2py:**  edwh-std-security middleware toegepast ([`a1974c0`](https://github.com/educationwarehouse/ontwikkelstraat/commit/a1974c07ae52d5d2898933672ba9fd0e5ccb5587))
* **ioldb:** SSL intern oplossen (docker.local levert selfsigned) ([`39e94e5`](https://github.com/educationwarehouse/ontwikkelstraat/commit/39e94e575e209a0c5bb00d013705a0b741e11ae5))
* **tasks:** Toml integratie liep niet lekker. is nu beter ([`449c63d`](https://github.com/educationwarehouse/ontwikkelstraat/commit/449c63d2a808c1a55dafc5f22f27fe051553a0ea))
* Config.toml er weer uit, hoort niet in de git repo ([`46d9bfa`](https://github.com/educationwarehouse/ontwikkelstraat/commit/46d9bfa02dd3a791cb9edf039ec796f800170d0a))
* **lts:** Item url terug gezet naar productie. ([`1339138`](https://github.com/educationwarehouse/ontwikkelstraat/commit/1339138bfc02b49de9b3c7a992728a28b695f703))
* **item:** Eerste regel was dubbel want 'body' bevat nog 'first_line' (en 'shorter_body' niet!) ([`b7b676e`](https://github.com/educationwarehouse/ontwikkelstraat/commit/b7b676e19e026ae737fd3ef9420ac52f41c0873c))

### Documentation
* **branches:** Meer uitleg over branches ([`28e7d77`](https://github.com/educationwarehouse/ontwikkelstraat/commit/28e7d7763c6e9b1a140119aead5d5c34dc9f6ed7))
* **branches:** Fix op schemas ([`869f5ae`](https://github.com/educationwarehouse/ontwikkelstraat/commit/869f5ae321f2abf92d90bf972c379a7561f7af13))
* **branches:**  werken met branches en releasen verder uitgelegd. ([`fd853f8`](https://github.com/educationwarehouse/ontwikkelstraat/commit/fd853f80d50ba8f03b44c10d0d288c094b116d9e))

## v1.0.1 (2023-04-10)
### Fix
* **tasks:** Alle backup gerelateerde code (die nu in edwh-backup-plugin ondergebracht is) verwijderd uit deze tasks.py; + config.toml + pyproject.toml ([`8723feb`](https://github.com/educationwarehouse/ontwikkelstraat/commit/8723feb5a266c8e34df5344544dd9475d5858e27))
* **tasks:** `service_names` now checks for typos ([`f7f7cca`](https://github.com/educationwarehouse/ontwikkelstraat/commit/f7f7ccac496509a35c9fa89fcdfb618b8ad0a0cf))
* **tasks:** Using config.toml for services or autodection ([`70d6dda`](https://github.com/educationwarehouse/ontwikkelstraat/commit/70d6ddafa22deabfb03f421d62002951889b12ad))
* **tasks:** Improved import warnings when using `invoke` or `edwh` ([`7f552ab`](https://github.com/educationwarehouse/ontwikkelstraat/commit/7f552abd382880ac5cd144b44a4f71190d17de7b))
