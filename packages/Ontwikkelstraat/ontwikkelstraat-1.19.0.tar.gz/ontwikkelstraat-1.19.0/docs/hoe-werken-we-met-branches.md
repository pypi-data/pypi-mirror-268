## Branch naamgeving en samenwerking 

De workflow is vereenvoudigd weergegeven als:
```plantuml
entity "feature" as feature
entity "staging" as staging
entity "prd" as prd
note over feature
    Ontwikkeling vind hier plaats, lokaal
    op de machine van de ontwikkelaar 
    of in een specifieke machine. 

    branchname:
    [omgeving]/feature/[feature_#taigaid]/[ontwikkelaar]
end note 
feature -> staging: productie geschikte code
note over staging
    De staging is voor het klaarzetten van 
    wijzigingen die productie in mogen. 
    
    branchname:
    [omgeving]/staging 
end note 
staging -> prd: in productie brengen
note over prd: branchname:\n[omgeving]/prd
``` 

## releasen ziet er zo uit: 

```plantuml
entity "staging" as staging
entity "prd" as prd
participant "Host" as prd_host
staging -> prd: pull request && merge
prd -> prd_host: pull
prd_host -> prd_host: ew setup
prd_host -> prd_host: ew up 
```

Uitgaande van wat er op ontwikkel is gebeurd:
 - builden van nieuwe images (`docker compose build`)
 - pushen van de images naar docker hub (`docker compose push`)
 - testen van de wijzigingen in de feature branches
 - merge van de geaccepteerde features naar de staging branch
 - testen van de staging branch 
 - pull-request maken van de staging branch naar de prd branch
 - validatie van de pull-request
 - merge van de pull-request

Uitvoeren op productie: 
```
docker compose pull 
git pull 
ew setup 
ew up logs -s migrate -s py4web -s web2py 
```

## Van feature tot release: 
```plantuml
entity "feature/remco" as feature
participant "pull request" as pr
entity "staging" as staging
activate staging 
participant "pull request" as pr2
entity "prd" as prd
activate prd 
participant productie_host as prd_host
activate prd_host
== ontwikkeling nieuwe feature ==
create feature 
staging -> feature: clone
loop tot pull request akkoord
    staging -> feature ++: regelmatig:\npull & merge om bij te blijven\nbij de staging, om zo uitgebreide\nmerges te voorkomen.
    note over feature: ontwikkeling in\ndeze branch
    staging -> feature: pull & merge ...
    note over feature
        Functionele tests
        met gebruikers. 
        Omdat de staging 
        heel vaak wordt 
        gepulled en 
        gemerged zijn er 
        geen grote ver-
        rassingen.
    end note 

    create pr 
    feature -> pr++: pull request
    note over pr: beoordeling
    pr -> staging: merge
    destroy pr  
end 
== testen ==
note over staging
    Integratie test.
    Dit zou geen gekke 
    dingen mogen opleveren, 
    omdat de combinatie al 
    getest is in de laatste 
    feature. 
end note  
create pr2 
staging -> pr2++: pull request
note over pr2: beoordeling
pr2 -> prd --: merge
destroy pr2
== releasen ==
prd -> prd_host: pull
note over prd_host
    $ edwh setup
    $ edwh up
    
    Dit moet o.a. de 
    migrate uitvoeren 
    waardoor schema-
    wijzigingen aan-
    komen
end note 

== afwachten == 
note over feature
    Als er geen fouten 
    gemeld worden kan
    na verloop van tijd 
    de feature branch 
    opgedoekt worden. 
end note  
feature -> feature: delete
destroy feature
```

# Samenwerken voor een feature
```plantuml
entity "feature/remco" as fremco
entity "feature/mike" as fmike
entity "feature/staging" as feature
participant "pull request" as pr
entity "staging" as staging
entity "prd" as prd
participant productie_host as prd_host
activate prd 
activate staging 
== ontwikkeling nieuwe feature ==
create feature 
staging -> feature: clone
activate feature
note over feature
    Zie schema hierboven over het 
    ontstaan van de feature branch
end note 

== samen doorontwikkelen aan feature ==
create fremco
feature -> fremco ++: clone
note over fremco: ontwikkeling 
create fmike 
feature -> fmike ++: clone 

note over fmike: ontwikkeling 
loop tot pull request akkoord
    loop doorontwikkelen
        staging -> feature: pull & merge: om bij te blijven
        note over feature
            Door te mergen
            in de feature/staging 
            branch hebben zowel 
            Mike als Remco baat
            bij het merge-werk. 
        end note
        fmike <- feature: pull & merge 
        note over fmike
            (door)ontwikkeling
            in actueel gehouden code
        end note 
        fmike -> feature: push
        feature -> fremco: pull & merge 
        note over fremco
            (door)ontwikkeling
            in actueel gehouden code
        end note 
        feature <- fremco: push
        note over fmike
            Functionele tests met gebruikers in de branch
            waar er gewerkt wordt. Danwel in de feature 
            branch, waar de gebruiker zowel de wijzigen 
            van Remco en Mike in 1x kan testen.  
        end note 
    end 
    note over feature
        Geen ontwikkeling 
        in deze branch, tenzij
        minimale patches. De
        rest van de ontwikkeling
        zit in de ./remco en ./mike
        subbranches. 
    end note
    create pr 
    feature -> pr++: pull request
    note over pr: beoordeling
    pr -> staging: merge
    destroy pr  
end 
== releasen ==
prd -> prd_host: pull
prd_host -> prd_host: ew setup
prd_host -> prd_host: ew up 
== afwachten == 
note over fmike: wachten tot geen foutmeldingen en of gewenste door-\nontwikkelingen zijn aangeven zijn van gebruikers. 
fremco -> fremco: delete
fmike -> fmike: delete
feature -> feature: delete
destroy fremco
destroy fmike
destroy feature
```


De branch naamgeving is als volgt:

* `{platform}/prd` is de productie branch, bedoeld wat de productie machine draait
* `{platform}/staging` is de staging branch waar alles wat richting productie gaat moet komen te staan. Je mag hiervan
  verwachten dat het productie waardige code is. 
* `{platform}/feature/{feature_#taigaid}[/{developer}]` zijn development branches waarin ontwikkelaars werken. Mocht je
  met meer mensen aan een feature werken, dan is de `/{developer}` toevoeging noodzakelijk, en geldt de `feature_#taigaid` 
  branch als staging branch voor deze feature. 
* `main` heeft geen functie meer

