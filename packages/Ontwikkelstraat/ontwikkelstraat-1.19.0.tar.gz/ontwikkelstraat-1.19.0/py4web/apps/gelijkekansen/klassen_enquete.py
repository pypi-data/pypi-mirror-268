import typing
from dataclasses import dataclass
from enum import Enum, auto


class ThemaSchoolleider(Enum):
    Basis = auto()
    Ouderbetrokkenheid = auto()
    # Moeilijk_te_bereik_ouder = auto()
    # Helikopterouder = auto()
    Taalontwikkeling = auto()
    Armoede = auto()
    Sociaal_en_cultureel_kapitaal = auto()
    Identiteit = auto()
    Verwachtingen = auto()
    De_kracht_van_het_team = auto()
    Burgerschap = auto()

    @property
    def human_name(self):
        return self.name.replace("_", " ")

    @property
    def ghost_id(self):
        return {
            "Verwachtingen": "verwachtingen-schoolleidersversie",
            "Taalontwikkeling": "taal-schoolleiderversie",
            "Armoede": "armoede-schoolleidersversie",
            "Sociaal_en_cultureel_kapitaal": "cultureel-en-sociaal-kapitaal-schoolleidersversie",
            "Identiteit": "identiteit-schoolleiderversie",
            "Ouderbetrokkenheid": "ouderbetrokkenheid-schoolleidersversie",
            "Burgerschap": "burgerschap-schoolleidersversie",
            "De kracht van het team": "de-kracht-van-het-team-schoolleidersversie",
        }.get(self.name, self.name)


class ThemaDocent(Enum):
    Basis = auto()
    Ouderbetrokkenheid = auto()
    # Moeilijk_te_bereik_ouder = auto()
    # Helikopterouder = auto()
    Taalontwikkeling = auto()
    Armoede = auto()
    Sociaal_en_cultureel_kapitaal = auto()
    Identiteit = auto()
    Verwachtingen = auto()
    De_kracht_van_het_team = auto()
    Burgerschap = auto()

    @property
    def human_name(self):
        return self.name.replace("_", " ")

    @property
    def ghost_id(self):
        return {
            "Verwachtingen": "verwachtingen",
            "Taalontwikkeling": "taal",
            "Armoede": "armoede",
            "Sociaal_en_cultureel_kapitaal": "cultureel-en-sociaal-kapitaal",
            "Identiteit": "identiteit",
            "Ouderbetrokkenheid": "ouderbetrokkenheid",
            "Burgerschap": "burgerschap",
            "De kracht van het team": "de-kracht-van-het-team",
        }.get(self.name, self.name)


# enum kan niet inherited worden dus vandaar de kopie voor beide versies.


@dataclass
class Antwoord:
    antwoord: str
    optie: str
    punten: int | float


## Vraag template:
# class VraagN:
#     vraag = ""
#     thema: Thema.
#     antwoorden = [
#         Antwoord(
#             "label",
#             "optie",
#             3,
#         ),
#         Antwoord(
#             "label",
#             "optie",
#             2,
#         ),
#         Antwoord(
#             "label",
#             "optie",
#             1,
#         ),
#     ]


# Deel 1
# Werk je voornamelijk met leerlingen in het basis- of het middelbaar onderwijs?
# Deze vraag heeft twee opties:
# 1. Basisonderwijs
# 2. Middelbaar onderwijs


class BasisStap:
    """
    Het class systeem zit nu als volgt in elkaar:
    - Basis Stap: elke vraag inherit hier van, zodat er altijd een (lege) berekeningfunctie en vraag property is
    - - VraagMetAntwoord: elke vraag die beantwoord kan worden (dus geen tekstpagina of uitslag)
    - - - StandaardVraag: keuze uit 1 optie
    - - - - VraagN: de vragen
    - - - - NietBestaandeVraag: placeholder
    - - - StapelVraag: keuze uit n opties (stapel = n)
    - - - - StapelN: de stapelvragen
    - - Uitleg: tekstpagina
    - - Uitslag: resultatenpagina

    """

    # abstracte basis
    vraag: str

    @classmethod
    def berekening(cls, gegeven_antwoord, score_per_thema):
        """
        Inheritable class om 'score_per_thema' te updaten op basis van 'gegeven_antwoord'
        Deze class method is per type vraag (VraagMetAntwoord, StandaardVraag, oid) te wijzigen
        of per vraag zelf (bijv. Vraag0, StapelVraag1)

        :param gegeven_antwoord keuze(s) gemaakt bij de vraag
        :type gegeven_antwoord dict
        :param score_per_thema: huidige score dict om te updaten
        :type score_per_thema dict

        :rtype None
        """
        pass


class VraagMetAntwoord(BasisStap):
    vraag: str


class StandaardVraag(VraagMetAntwoord):
    vraag: str
    thema: Enum  # ThemaDocent | ThemaSchoolleider
    antwoorden: list

    template = "vraag"

    @classmethod
    def berekening(cls, gegeven_antwoord, score_per_thema):
        # berekening voor standaard vragen: tel de punten bijbehorend bij het antwoord op bij het gegeven thema
        for antwoord in cls.antwoorden:
            if antwoord.optie == gegeven_antwoord[0]:
                score_per_thema[cls.thema] += antwoord.punten
                break


class StapelVraag(VraagMetAntwoord):
    vraag: str
    themas: list  # of Thema
    stapel: int  # hoeveelheid mogelijke antwoorden

    template = "stapel"

    @classmethod
    def berekening(cls, gegeven_antwoord, score_per_thema):
        # berekening voor stapels: tel 2 punten op bij de geselecteerde themas
        for thema in cls.themas:
            if thema.name in gegeven_antwoord:
                score_per_thema[thema] += 2


class Docent_Vraag0(StandaardVraag):
    vraag = (
        "Werk je voornamelijk met leerlingen in het basis- of het middelbaar onderwijs?"
    )
    thema = ThemaDocent.Basis
    antwoorden = [
        Antwoord("Basis", "PO", 0),
        Antwoord("Middelbaar onderwijs", "VO", 0),
    ]


KIES_STELLING = "Kies de stelling die het meest van toepassing is op wat jij in je dagelijkse praktijk ziet/meemaakt:"


# Ouderbetrokkenheid (2x):
# Moeilijk te bereiken ouder
#
#
# Vraag 1 van 9
# Ik vind het lastig om de ouders van de kinderen waarmee ik werk te bereiken (3p)
#
# Verschillen in achtergrond (cultureel, sociaal, economisch) en taalbarrières staan soms het contact met ouders in de weg (2p)
#
# Ik heb, uitzonderingen daar gelaten, relatief weinig moeite met het contact met ouders (1p)


class Docent_Vraag1(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaDocent.Ouderbetrokkenheid
    antwoorden = [
        Antwoord(
            "Ik vind het lastig om de ouders van de kinderen waarmee ik werk te bereiken.",
            "Lastig",
            1.5,
        ),
        Antwoord(
            "Verschillen in achtergrond (cultureel, sociaal, economisch) en taalbarrières staan soms het contact met ouders in de weg.",
            "Soms",
            1,
        ),
        Antwoord(
            "Ik heb, uitzonderingen daar gelaten, relatief weinig moeite met het contact met ouders.",
            "Weinig",
            0.5,
        ),
    ]


# Vraag 2 van 9
class Docent_Vraag2(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaDocent.Ouderbetrokkenheid
    antwoorden = [
        Antwoord(
            "Ik heb vaak het idee dat de verwachtingen van ouders groter zijn dan wat wij als schoolteam kunnen waarmaken.",
            "Groter",
            1.5,
        ),
        Antwoord(
            "Ik vind dat de ouders van leerlingen uit mijn klas te veel nadruk leggen op het halen van hoge cijfers en/of een bepaald schoolniveau.",
            "Nadruk",
            1,
        ),
        Antwoord(
            "Door middel van goed contact met ouders en leerlingen zorg ik ervoor dat de druk op mijn leerlingen niet te hoog wordt.",
            "Niet",
            0.5,
        ),
    ]


# Verschillende soorten taal
#
# Vraag 3 van 9
# Ik vind het soms lastig om in te schatten welke verschillende talen kinderen beheersen en op welk niveau ze dit doen, en om vervolgens gebruik te maken van alle talen die ze beheersen (3p)
#
# Het kost me veel energie om om te gaan met alle verschillende taalniveaus van kinderen uit de klas (2
#
# Ik weet goed hoe ik meertaligheid effectief kan gebruiken in de klas en op school (1p)
class Docent_Vraag3(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaDocent.Taalontwikkeling
    antwoorden = [
        Antwoord(
            "Ik vind het soms lastig om in te schatten welke verschillende talen kinderen beheersen en op welk niveau ze dit doen, en om vervolgens gebruik te maken van alle talen die ze beheersen.",
            "lastig",
            3,
        ),
        Antwoord(
            "Het kost me veel energie om om te gaan met alle verschillende taalniveaus van kinderen uit de klas.",
            "energie",
            2,
        ),
        Antwoord(
            "Ik weet goed hoe ik meertaligheid effectief kan gebruiken in de klas en op school.",
            "effectief",
            1,
        ),
    ]


# Armoede
#
# Vraag 4 van 9
# Ik heb veel kinderen in de klas/ik werk met veel kinderen die op of onder de armoedegrens leven (1p)
#
# Ik blijf het moeilijk vinden om in te schatten hoeveel geld er beschikbaar is voor kinderen thuis (2p)
#
# In mijn dagelijkse realiteit kom ik, volgens mij, zelden in aanraking met kinderen die in armoede opgroeien (3p)
#
# Sociaal en cultureel kapitaal
#
class Docent_Vraag4(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaDocent.Armoede
    antwoorden = [
        Antwoord(
            "Ik heb veel kinderen in de klas/ik werk met veel kinderen die op of onder de armoedegrens leven.",
            "Veel",
            1,
        ),
        Antwoord(
            "Ik blijf het moeilijk vinden om in te schatten hoeveel geld er beschikbaar is voor kinderen thuis.",
            "Moeilijk",
            2,
        ),
        Antwoord(
            "In mijn dagelijkse realiteit kom ik, volgens mij, zelden in aanraking met kinderen die in armoede opgroeien.",
            "Zelden",
            3,
        ),
    ]


# Vraag 5 van 9
# Ik heb het idee dat ik uit een hele andere wereld kom/van een heel andere achtergrond ben dan de kinderen die ik les geef, maar dit staat het contact tussen mij en mijn leerlingen niet in de weg (2p)
#
# Het grote verschil in achtergrond tussen mij en mijn leerlingen bemoeilijkt het contact tussen mij en hen en maakt het in sommige gevallen moeilijk om een goede relatie op te bouwen (3p)
#
# Over het algemeen heb ik het idee dat mijn leerlingen zich goed in mij kunnen herkennen en denk ik dat ik goed zicht heb op waar ze vandaan komen (en hoe dit zich tegenover mijn afkomst/achtergrond verhoudt). (1p)
#


class Docent_Vraag5(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaDocent.Sociaal_en_cultureel_kapitaal
    antwoorden = [
        Antwoord(
            "Ik heb het idee dat ik uit een hele andere wereld kom/van een heel andere achtergrond ben dan de kinderen die ik les geef, maar dit staat het contact tussen mij en mijn leerlingen niet in de weg.",
            "Redelijk",
            2,
        ),
        Antwoord(
            "Het grote verschil in achtergrond tussen mij en mijn leerlingen bemoeilijkt het contact tussen mij en hen en maakt het in sommige gevallen moeilijk om een goede relatie op te bouwen.",
            "Moeilijk",
            3,
        ),
        Antwoord(
            "Over het algemeen heb ik het idee dat mijn leerlingen zich goed in mij kunnen herkennen en denk ik dat ik goed zicht heb op waar ze vandaan komen (en hoe dit zich tegenover mijn afkomst/achtergrond verhoudt).",
            "Goed",
            1,
        ),
    ]


#
# Identiteit
#
# Vraag 6 van 9
# Ik merk regelmatig dat mijn leerlingen verward zijn over hun identiteit, mede omdat de regels op school zo sterk verschillen van de regels op straat en thuis en dit zorgt voor moeilijkheden. (3p)
#
# Mijn leerlingen zijn duidelijk in het proces van het ontwikkelen van hun eigen identiteit en ik weet niet altijd hoe ik ze in dit proces bij kan staan. (2p)
#
# Ik zie dat sommige leerlingen moeite hebben met de verschillen tussen de werelden waarin ze leven, maar weet tegelijkertijd ook hoe ik hier mee om moet gaan. (1p)
#


class Docent_Vraag6(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaDocent.Identiteit
    antwoorden = [
        Antwoord(
            "Ik merk regelmatig dat mijn leerlingen verward zijn over hun identiteit, mede omdat de regels op school zo sterk verschillen van de regels op straat en thuis en dit zorgt voor moeilijkheden.",
            "Verward",
            3,
        ),
        Antwoord(
            "Mijn leerlingen zijn duidelijk in het proces van het ontwikkelen van hun eigen identiteit en ik weet niet altijd hoe ik ze in dit proces bij kan staan.",
            "ondersteuningsvraagstuk",
            2,
        ),
        Antwoord(
            "Ik zie dat sommige leerlingen moeite hebben met de verschillen tussen de werelden waarin ze leven, maar weet tegelijkertijd ook hoe ik hier mee om moet gaan.",
            "weiniguitdaging",
            1,
        ),
    ]


#
# Verwachtingen
#
# Vraag 7 van 9
# Ik heb veel kinderen in mijn klas die ongemotiveerd zijn of lijken en ik vind het lastig om te bedenken wat ik daarmee moet. (3p)
#
# Ik ben me bewust van de invloed van mijn verwachtingen op leerlingen, maar weet niet altijd hoe ik deze goed over kan brengen (2p)
#
# Ik zie ongemotiveerde leerlingen als een uitdaging, er is altijd iets wat een leerling prikkelt. (0p)
#
class Docent_Vraag7(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaDocent.Verwachtingen
    antwoorden = [
        Antwoord(
            "Ik heb veel kinderen in mijn klas die ongemotiveerd zijn of lijken en ik vind het lastig om te bedenken wat ik daarmee moet.",
            "Lastig",
            3,
        ),
        Antwoord(
            "Ik ben me bewust van de invloed van mijn verwachtingen op leerlingen, maar weet niet altijd hoe ik deze goed over kan brengen.",
            "Soms",
            2,
        ),
        Antwoord(
            "Ik zie ongemotiveerde leerlingen als een uitdaging, er is altijd iets wat een leerling prikkelt.",
            "Uitdaging",
            1,
        ),
    ]


#
# De kracht van het team
#
# Vraag 8 van 9
# Ik wil graag aan gelijkere kansen werken, maar krijg soms het idee dat ik de enige ben in het schoolteam (3p)
#
# Het gaat bij ons op school veel over gelijke kansen, maar woorden worden lang niet altijd omgezet naar daden (2p)
#
# Binnen onze school werken we actief aan het creëeren van gelijkere kansen, individueel maar vooral als team (1p)
#


class Docent_Vraag8(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaDocent.De_kracht_van_het_team
    antwoorden = [
        Antwoord(
            "Ik wil graag aan gelijkere kansen werken, maar krijg soms het idee dat ik de enige ben in het schoolteam.",
            "lonely",
            3,
        ),
        Antwoord(
            "Het gaat bij ons op school veel over gelijke kansen, maar woorden worden lang niet altijd omgezet naar daden.",
            "zucht_daadkracht",
            2,
        ),
        Antwoord(
            "Binnen onze school werken we actief aan het creëeren van gelijkere kansen, individueel maar vooral als team.",
            "team_effort",
            1,
        ),
    ]


#
# Burgerschap
#
# Vraag 9 van 9
# Het komt meerdere keren per jaar voor dat ik schrik van de opmerkingen die een leerling maakt over een gevoelig onderwerp en ik vervolgens niet weet hoe ik hier mee om moet gaan. (3p)
#
# In mijn klas is er altijd ruimte voor discussie en debat, ook als het gaat over onderwerpen die bij een deel van de leerlingen gevoelig liggen. (1)
#
# Af en toe vermijd ik onderwerpen in mijn lessen omdat ik niet weet hoe ik het moet behandelen. (2p)
#
# HIERTUSSEN KRIJGT DE BEZOEKER IETS MEER OVER DE THEMA’S TE LEZEN. ZIE ANDERE BESTAND.
#
class Docent_Vraag9(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaDocent.Burgerschap
    antwoorden = [
        Antwoord(
            "Het komt meerdere keren per jaar voor dat ik schrik van de opmerkingen die een leerling maakt over een gevoelig onderwerp en ik vervolgens niet weet hoe ik hier mee om moet gaan.",
            "verward",
            3,
        ),
        Antwoord(
            "In mijn klas is er altijd ruimte voor discussie en debat, ook als het gaat over onderwerpen die bij een deel van de leerlingen gevoelig liggen.",
            "debat",
            1,
        ),
        Antwoord(
            "Af en toe vermijd ik onderwerpen in mijn lessen omdat ik niet weet hoe ik het moet behandelen.",
            "detour",
            2,
        ),
    ]


class Schoolleider_Vraag0(StandaardVraag):
    vraag = (
        "Werk je voornamelijk met leerlingen in het basis- of het middelbaar onderwijs?"
    )
    thema = ThemaSchoolleider.Basis
    antwoorden = [
        Antwoord("Basis", "PO", 0),
        Antwoord("Middelbaar onderwijs", "VO", 0),
    ]


class Schoolleider_Vraag1(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaSchoolleider.Ouderbetrokkenheid
    antwoorden = [
        Antwoord(
            "Bij mij op school is het vaak lastig om ouders van kinderen actief te betrekken.",
            "Lastig",
            1.5,
        ),
        Antwoord(
            "Ik zie dat verschillen in achtergrond (cultureel, sociaal, economisch) en taalbarrières soms het contact tussen school en ouders in de weg staan.",
            "Soms",
            1,
        ),
        Antwoord(
            "Mijn team en ik hebben, uitzonderingen daargelaten, relatief weinig moeite met het contact met ouders.",
            "Weinig",
            0.5,
        ),
    ]


# Vraag 2 van 9
class Schoolleider_Vraag2(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaSchoolleider.Ouderbetrokkenheid
    antwoorden = [
        Antwoord(
            "Ik heb vaak het idee dat de verwachtingen van ouders groter zijn dan wat wij als schoolteam kunnen waarmaken.",
            "Groter",
            1.5,
        ),
        Antwoord(
            "Ik vind dat ouders van leerlingen bij mij op school te veel nadruk leggen op het halen van hoge cijfers en/of een bepaald schoolniveau.",
            "Nadruk",
            1,
        ),
        Antwoord(
            "Als team slagen wij er door goed contact met ouders te onderhouden in de werkdruk te verminderen.",
            "Niet",
            0.5,
        ),
    ]


# Verschillende soorten taal
#
# Vraag 3 van 9
# Ik vind het soms lastig om in te schatten welke verschillende talen kinderen beheersen en op welk niveau ze dit doen, en om vervolgens gebruik te maken van alle talen die ze beheersen (3p)
#
# Het kost me veel energie om om te gaan met alle verschillende taalniveaus van kinderen uit de klas (2
#
# Ik weet goed hoe ik meertaligheid effectief kan gebruiken in de klas en op school (1p)
class Schoolleider_Vraag3(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaSchoolleider.Taalontwikkeling
    antwoorden = [
        Antwoord(
            "Docenten bij mij op school lijken vaak moeite te hebben met het inschatten welke verschillende talen leerlingen spreken en op welk niveau ze dit precies doen.",
            "lastig",
            3,
        ),
        Antwoord(
            "Het kost leden van het schoolteam veel energie om te gaan met alle verschillende taalniveaus binnen één klas.",
            "energie",
            2,
        ),
        Antwoord(
            "Mijn team weet goed hoe meertaligheid effectief ingezet kan geworden in de klas en op school.",
            "effectief",
            1,
        ),
    ]


# Armoede
#
# Vraag 4 van 9
# Ik heb veel kinderen in de klas/ik werk met veel kinderen die op of onder de armoedegrens leven (1p)
#
# Ik blijf het moeilijk vinden om in te schatten hoeveel geld er beschikbaar is voor kinderen thuis (2p)
#
# In mijn dagelijkse realiteit kom ik, volgens mij, zelden in aanraking met kinderen die in armoede opgroeien (3p)
#
# Sociaal en cultureel kapitaal
#
class Schoolleider_Vraag4(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaSchoolleider.Armoede
    antwoorden = [
        Antwoord(
            "Er zijn veel kinderen die op of onder de armoedegrens leven bij ons op school.",
            "Veel",
            1,
        ),
        Antwoord(
            "Ik blijf het moeilijk vinden om in te schatten hoeveel geld er beschikbaar is voor kinderen thuis.",
            "Moeilijk",
            2,
        ),
        Antwoord(
            "In mijn dagelijkse realiteit kom ik, volgens mij, zelden in aanraking met kinderen die in armoede opgroeien.",
            "Zelden",
            3,
        ),
    ]


# Vraag 5 van 9
# Ik heb het idee dat ik uit een hele andere wereld kom/van een heel andere achtergrond ben dan de kinderen die ik les geef, maar dit staat het contact tussen mij en mijn leerlingen niet in de weg (2p)
#
# Het grote verschil in achtergrond tussen mij en mijn leerlingen bemoeilijkt het contact tussen mij en hen en maakt het in sommige gevallen moeilijk om een goede relatie op te bouwen (3p)
#
# Over het algemeen heb ik het idee dat mijn leerlingen zich goed in mij kunnen herkennen en denk ik dat ik goed zicht heb op waar ze vandaan komen (en hoe dit zich tegenover mijn afkomst/achtergrond verhoudt). (1p)
#


class Schoolleider_Vraag5(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaSchoolleider.Sociaal_en_cultureel_kapitaal
    antwoorden = [
        Antwoord(
            "Ik heb het idee dat ik uit een hele andere wereld kom dan de meeste kinderen op school, maar dat staat het contact tussen mij en leerlingen niet in de weg.",
            "Redelijk",
            2,
        ),
        Antwoord(
            "Het grote verschil in achtergrond tussen mij en leerlingen bemoeilijkt het contact en maakt het in sommige gevallen moeilijk om een goede relatie op te bouwen",
            "Moeilijk",
            3,
        ),
        Antwoord(
            "Over het algemeen heb ik het idee dat mijn leerlingen zich goed in mij kunnen herkennen en denk ik dat ik goed zicht heb op waar ze vandaan komen (en hoe dit zich tegenover mijn afkomst/achtergrond verhoudt).",
            "Goed",
            1,
        ),
    ]


#
# Identiteit
#
# Vraag 6 van 9
# Ik merk regelmatig dat mijn leerlingen verward zijn over hun identiteit, mede omdat de regels op school zo sterk verschillen van de regels op straat en thuis en dit zorgt voor moeilijkheden. (3p)
#
# Mijn leerlingen zijn duidelijk in het proces van het ontwikkelen van hun eigen identiteit en ik weet niet altijd hoe ik ze in dit proces bij kan staan. (2p)
#
# Ik zie dat sommige leerlingen moeite hebben met de verschillen tussen de werelden waarin ze leven, maar weet tegelijkertijd ook hoe ik hier mee om moet gaan. (1p)
#


class Schoolleider_Vraag6(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaSchoolleider.Identiteit
    antwoorden = [
        Antwoord(
            "Ik merk regelmatig dat leerlingen verward zijn over hun identiteit en dat dit zorgt voor (orde)problemen in de klas en op school.",
            "Verward",
            3,
        ),
        Antwoord(
            "Zowel mijn team als ik hebben soms zichtbaar moeite met het bijstaan van leerlingen in hun identiteitsontwikkeling.",
            "ondersteuningsvraagstuk",
            2,
        ),
        Antwoord(
            "Wij als team zien dat sommige leerlingen moeite hebben met de verschillende werelden waarin ze leven, maar weten vrij goed hoe hiermee om te gaan.",
            "weiniguitdaging",
            1,
        ),
    ]


#
# Verwachtingen
#
# Vraag 7 van 9
# Ik heb veel kinderen in mijn klas die ongemotiveerd zijn of lijken en ik vind het lastig om te bedenken wat ik daarmee moet. (3p)
#
# Ik ben me bewust van de invloed van mijn verwachtingen op leerlingen, maar weet niet altijd hoe ik deze goed over kan brengen (2p)
#
# Ik zie ongemotiveerde leerlingen als een uitdaging, er is altijd iets wat een leerling prikkelt. (0p)
#
class Schoolleider_Vraag7(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaSchoolleider.Verwachtingen
    antwoorden = [
        Antwoord(
            "Docenten geven vaak aan dat ze niet weten wat ze moeten doen met het grote aantal kinderen in de klas dat ongemotiveerd lijkt te zijn.",
            "Lastig",
            3,
        ),
        Antwoord(
            "k ben me bewust dat mijn verwachtingen vormend zijn voor hoe het schoolteam functioneert, maar weet niet altijd hoe ik de juiste verwachtingen over kan brengen.",
            "Soms",
            2,
        ),
        Antwoord(
            "Ik zie een lage motivatie bij zowel leden van het schoolteam als leerlingen als een uitdaging. Er is altijd een manier om iemand te motiveren.",
            "Uitdaging",
            1,
        ),
    ]


#
# De kracht van het team
#
# Vraag 8 van 9
# Ik wil graag aan gelijkere kansen werken, maar krijg soms het idee dat ik de enige ben in het schoolteam (3p)
#
# Het gaat bij ons op school veel over gelijke kansen, maar woorden worden lang niet altijd omgezet naar daden (2p)
#
# Binnen onze school werken we actief aan het creëeren van gelijkere kansen, individueel maar vooral als team (1p)
#


class Schoolleider_Vraag8(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaSchoolleider.De_kracht_van_het_team
    antwoorden = [
        Antwoord(
            "Ik zie gelijke kansen als een speerpunt van het schoolbeleid, maar heb het idee dat dit niet gedragen wordt binnen de rest van het team.",
            "lonely",
            3,
        ),
        Antwoord(
            "Het gaat bij ons op school veel over gelijke kansen, maar woorden worden lang niet altijd omgezet naar daden.",
            "zucht_daadkracht",
            2,
        ),
        Antwoord(
            "Bij ons op school werken we actief aan het creëren van gelijkere kansen, individueel maar vooral als team.",
            "team_effort",
            1,
        ),
    ]


#
# Burgerschap
#
# Vraag 9 van 9
# Het komt meerdere keren per jaar voor dat ik schrik van de opmerkingen die een leerling maakt over een gevoelig onderwerp en ik vervolgens niet weet hoe ik hier mee om moet gaan. (3p)
#
# In mijn klas is er altijd ruimte voor discussie en debat, ook als het gaat over onderwerpen die bij een deel van de leerlingen gevoelig liggen. (1)
#
# Af en toe vermijd ik onderwerpen in mijn lessen omdat ik niet weet hoe ik het moet behandelen. (2p)
#
# HIERTUSSEN KRIJGT DE BEZOEKER IETS MEER OVER DE THEMA’S TE LEZEN. ZIE ANDERE BESTAND.
#
class Schoolleider_Vraag9(StandaardVraag):
    vraag = KIES_STELLING
    thema = ThemaSchoolleider.Burgerschap
    antwoorden = [
        Antwoord(
            "Het komt meerdere keren per jaar voor dat een leerling opmerkingen maakt over een gevoelig onderwerp en wij vervolgens als team niet goed weten hoe we hiermee om moeten gaan.",
            "verward",
            3,
        ),
        Antwoord(
            "Docenten laten over het algemeen voldoende ruimte voor discussie en debat, ook als het gaat over onderwerpen die bij een deel van de leerlingen gevoelig liggen.",
            "debat",
            1,
        ),
        Antwoord(
            "Ik krijg de indruk dat er regelmatig onderwerpen vermeden worden omdat docenten niet weten hoe ze het moeten behandelen.",
            "detour",
            2,
        ),
    ]


# LEES OVER THEMAS
class Docent_Uitleg(BasisStap):
    vraag = ""
    thema = ThemaDocent.Basis
    antwoorden = []

    template = "uitleg"


class Schoolleider_Uitleg(BasisStap):
    vraag = ""
    thema = ThemaSchoolleider.Basis
    antwoorden = []

    template = "uitleg_schoolleider"


class Uitslag(BasisStap):
    vraag = ""
    template = "uitslag"


class Docent_Stapel1(StapelVraag):
    vraag = "Welke drie thema's spreken je het meest aan?"
    themas = [
        ThemaDocent.Burgerschap,
        ThemaDocent.Sociaal_en_cultureel_kapitaal,
        ThemaDocent.Taalontwikkeling,
        ThemaDocent.Ouderbetrokkenheid,
        ThemaDocent.Verwachtingen,
        ThemaDocent.De_kracht_van_het_team,
        ThemaDocent.Identiteit,
        ThemaDocent.Armoede,
        # Prestatiedruk -> helicopter?
    ]
    stapel = 3


class Docent_Stapel2(StapelVraag):
    vraag = "Van welke drie thema's weet je het minst?"
    themas = [
        ThemaDocent.Burgerschap,
        ThemaDocent.Sociaal_en_cultureel_kapitaal,
        ThemaDocent.Taalontwikkeling,
        ThemaDocent.Ouderbetrokkenheid,
        # de kracht van verwachtingen ??
        ThemaDocent.Verwachtingen,
        ThemaDocent.De_kracht_van_het_team,
        ThemaDocent.Identiteit,
        ThemaDocent.Armoede,
        # Prestatiedruk -> helicopter?
    ]
    stapel = 3


class Schoolleider_Stapel1(StapelVraag):
    vraag = "Welke drie thema's spreken je het meest aan?"
    themas = [
        ThemaSchoolleider.Burgerschap,
        ThemaSchoolleider.Sociaal_en_cultureel_kapitaal,
        ThemaSchoolleider.Taalontwikkeling,
        ThemaSchoolleider.Ouderbetrokkenheid,
        ThemaSchoolleider.Verwachtingen,
        # ThemaSchoolleider.De_kracht_van_het_team,
        ThemaSchoolleider.Identiteit,
        ThemaSchoolleider.Armoede,
        # Prestatiedruk -> helicopter?
    ]
    stapel = 3


class Schoolleider_Stapel2(StapelVraag):
    vraag = "Van welke drie thema's weet je het minst?"
    themas = [
        ThemaSchoolleider.Burgerschap,
        ThemaSchoolleider.Sociaal_en_cultureel_kapitaal,
        ThemaSchoolleider.Taalontwikkeling,
        ThemaSchoolleider.Ouderbetrokkenheid,
        # de kracht van verwachtingen ??
        ThemaSchoolleider.Verwachtingen,
        # ThemaSchoolleider.De_kracht_van_het_team,
        ThemaSchoolleider.Identiteit,
        ThemaSchoolleider.Armoede,
        # Prestatiedruk -> helicopter?
    ]
    stapel = 3


# Deel 3
#
# Welke drie thema’s spreken je het meest aan?
# Burgerschap, sociaal en cultureel kapitaal, taalontwikkeling, ouderbetrokkenheid, verwachtingen, de kracht van het team, identiteit, armoede, prestatiedruk
#
# (Elk thema in deze top drie krijgt 2 punten)
#
# Van welke drie thema’s weet je het minst?
# Burgerschap, sociaal en cultureel kapitaal, taalontwikkeling, ouderbetrokkenheid, de kracht van verwachtingen, identiteit, armoede, prestatiedruk
#
# (Elk thema in deze top drie krijgt 3 punten)


## /EINDE VRAGEN


class Versie:
    VRAGEN: list
    MAX_VRAGEN: int
    MAX_ANTWOORDEN: int
    HOMEPAGE: str
    THEMA: Enum

    def __init__(self):
        self.MAX_VRAGEN = len(self.VRAGEN)
        self.MAX_ANTWOORDEN = sum(
            [1 for v in self.VRAGEN if issubclass(v, VraagMetAntwoord)]
        )


class DocentVersie(Versie):
    VRAGEN = [
        Docent_Vraag0,
        Docent_Vraag1,
        Docent_Vraag2,
        Docent_Vraag3,
        Docent_Vraag4,
        Docent_Vraag5,
        Docent_Vraag6,
        Docent_Vraag7,
        Docent_Vraag8,
        Docent_Vraag9,
        Docent_Uitleg,
        Docent_Stapel1,
        Docent_Stapel2,
        Uitslag,
    ]

    HOMEPAGE = "docenten"
    THEMA = ThemaDocent


class SchoolleiderVersie(Versie):
    VRAGEN = [
        Schoolleider_Vraag0,
        Schoolleider_Vraag1,
        Schoolleider_Vraag2,
        Schoolleider_Vraag3,
        Schoolleider_Vraag4,
        Schoolleider_Vraag5,
        Schoolleider_Vraag6,
        Schoolleider_Vraag7,
        # Schoolleider_Vraag8, # todo: vraag 8 hoort bij het thema De_kracht_van_het_team maar dat hoofdstuk bestaat niet op de schoolleidersversie
        Schoolleider_Vraag9,
        Schoolleider_Uitleg,
        Schoolleider_Stapel1,
        Schoolleider_Stapel2,
        Uitslag,
    ]

    HOMEPAGE = "schoolleiders"
    THEMA = ThemaSchoolleider


VERSIES = {
    "schoolleiders": SchoolleiderVersie(),
    "docenten": DocentVersie(),
}


class BerekenResultaat(typing.NamedTuple):
    compleet: bool
    scores: typing.Optional[dict[str, int]]
    top_themas: list[dict]


def bereken(antwoorden: dict, versie: Versie) -> BerekenResultaat:
    if not (len(antwoorden) >= versie.MAX_ANTWOORDEN):
        return BerekenResultaat(False, None, [])

    score_per_thema = {thema: 0.0 for thema in versie.THEMA}
    for idx, vraag in enumerate(versie.VRAGEN):
        vraag.berekening(antwoorden.get("q" + str(idx)), score_per_thema)

    themas_naar_belangrijkheid = sorted(
        score_per_thema.keys(), key=lambda thema: score_per_thema[thema], reverse=True
    )

    top_themas = []
    while (
        len(top_themas) < 3
        or score_per_thema[top_themas[-1]]
        == score_per_thema[themas_naar_belangrijkheid[0]]
    ):
        top_themas.append(themas_naar_belangrijkheid.pop(0))

    # todo: statistieken?

    return BerekenResultaat(
        True,
        {thema.name: score for thema, score in score_per_thema.items()},
        [
            dict(
                idx=idx,
                thema=thema.human_name,
                score=score_per_thema[thema],
                ghost_id=thema.ghost_id,
            )
            for idx, thema in enumerate(top_themas)
        ],
    )
