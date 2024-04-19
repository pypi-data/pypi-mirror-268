"""
This file defines the database models
"""
import json
import os

from ombott import HTTPError
from pydal.validators import *

from py4web import HTTP

from .common import Field, cache, db

db.define_table(
    "dna",
    Field("uitslag", "string", length=6),
    Field("cell", "integer"),
    Field("opmerking", "string", length=4096),
)


def read_dna_csv():
    with open(
        os.path.join(os.path.dirname(__file__), "databases", "dna.csv"), "r"
    ) as f:
        table = [line.split("|") for line in f.read().split("\n") if line]
        return table


def _line_to_dict(line):
    _idx, uitslag, cell, opmerking = line
    return dict(uitslag=uitslag, cell=cell, opmerking=opmerking)


def read_dna_csv_as_dicts():
    with open(
        os.path.join(os.path.dirname(__file__), "databases", "dna.csv"), "r"
    ) as f:
        table = [
            _line_to_dict(line.split("|")) for line in f.read().split("\n") if line
        ]
        return table


def fill_dna_table():
    table = read_dna_csv_as_dicts()
    db.dna.truncate()

    db.dna.bulk_insert(table)
    return True


slimfit_route_map = {
    "Starten met slimfit": {
        0: {
            1: "https://slimfit.meteddie.nl/start-naar-1/",
            2: "https://slimfit.meteddie.nl/start-naar-2/",
            3: "https://slimfit.meteddie.nl/start-naar-3/",
        },
    },
    "Route 1-4-7": {
        1: {4: "https://slimfit.meteddie.nl/1-naar-4/"},
        4: {7: "https://slimfit.meteddie.nl/4-naar-7/"},
    },
    "Route 2-5-8": {
        2: {5: "https://slimfit.meteddie.nl/2-naar-5/"},
        5: {8: "https://slimfit.meteddie.nl/5-naar-8/"},
    },
    "Route 3-6-9": {
        3: {6: "https://slimfit.meteddie.nl/3-naar-6/"},
        6: {9: "https://slimfit.meteddie.nl/6-naar-9/"},
    },
    "Route 2-5-6-9": {
        2: {5: "https://slimfit.meteddie.nl/2-naar-5/"},
        5: {6: "https://slimfit.meteddie.nl/5-naar-6/"},
        6: {9: "https://slimfit.meteddie.nl/6-naar-9/"},
    },
    "Route 1-3-6-9": {
        1: {3: "https://slimfit.meteddie.nl/1-naar-3/"},
        3: {6: "https://slimfit.meteddie.nl/3-naar-6/"},
        6: {9: "https://slimfit.meteddie.nl/6-naar-9/"},
    },
    "Route 1-4-6-9": {
        1: {4: "https://slimfit.meteddie.nl/1-naar-4/"},
        4: {6: "https://slimfit.meteddie.nl/4-naar-6/"},
        6: {9: "https://slimfit.meteddie.nl/6-naar-9/"},
    },
}

slimfit_route_url_map = {
    "Starten met slimfit": {},
    "Route 1-4-7": {"url": "https://slimfit.meteddie.nl/route147"},
    "Route 2-5-8": {"url": "https://slimfit.meteddie.nl/route258"},
    "Route 3-6-9": {"url": "https://slimfit.meteddie.nl/route369"},
    "Route 2-5-6-9": {"url": "https://slimfit.meteddie.nl/route2569"},
    "Route 1-3-6-9": {"url": "https://slimfit.meteddie.nl/route1369"},
    "Route 1-4-6-9": {"url": "https://slimfit.meteddie.nl/route1469"},
}

VRAGEN = {
    1: {
        "vraag": "Op welke wijze wordt er aan de basisvakken (taal, lezen, rekenen,) gewerkt?",
        "antwoorden": [
            {"label": "De lessen uit de methode worden gevolgd", "value": "a"},
            {
                "label": "Er worden korte instructies gepland (m.b.v. methode)",
                "value": "b",
            },
            {
                "label": "Er wordt met leer- en ontwikkelingslijnen gewerkt voor alle leerlingen <br>(de methode is één van de bronnen). <br/>Kinderen hebben mede inzicht in de leer- en ontwikkelingslijnen",
                "value": "c",
            },
        ],
    },
    2: {
        "vraag": "Op welke wijze wordt er aan de wereld oriënterende en creatieve vakken gewerkt?",
        "antwoorden": [
            {
                "label": "We volgen de methode voor de wereld oriënterende en creatieve vakken en zoeken hierin naar mogelijkheden om groepsoverstijgende activiteiten plaats te laten vinden",
                "value": "a",
            },
            {
                "label": "We werken projectmatig of thematisch aan WO en de creatieve vakken, waarbij we groepsoverstijgend werken ",
                "value": "b",
            },
        ],
    },
    3: {
        "vraag": "Hoe worden ruimten gebruikt?",
        "antwoorden": [
            {
                "label": "De leeractiviteiten vinden voornamelijk plaats in het eigen klaslokaal ",
                "value": "a",
            },
            {
                "label": "Er zijn meerdere hoeken en ruimten waar kinderen kunnen werken ",
                "value": "b",
            },
            {
                "label": "Kinderen werken in alle ruimten van het gebouw en daarbuiten",
                "value": "c",
            },
        ],
    },
    4: {
        "vraag": "Hoe zijn de leerlingen gegroepeerd?",
        "antwoorden": [
            {"label": "In leerstofjaarklassen of combinaties daarvan", "value": "a"},
            {
                "label": "In horizontale units (grote scholen; bijv. meerdere parallelgroepen werken samen in een unit)",
                "value": "b",
            },
            {
                "label": "In verticale, heterogene units (groep 1-2/ groep 3-5, groep 6-8 etc.)",
                "value": "c",
            },
        ],
    },
    5: {
        "vraag": "Welke omschrijving treft uw school het beste als het gaat om inzet van functionarissen, het onderscheiden van rollen, en het dragen van gezamenlijke verantwoordelijkheid?",
        "antwoorden": [
            {
                "label": "Op onze school werken er voornamelijk leerkrachten die verantwoordelijk zijn voor hun eigen klas",
                "value": "a",
            },
            {
                "label": "Naast functiedifferentiatie (leerkracht, onderwijsassistent) vindt er op onze school ook roldifferentiatie plaats ( leerkracht als instructeur, begeleider, coach, observator). We werken voornamelijk in teamverband en zijn gezamenlijk verantwoordelijk voor de planning en uitvoering van het onderwijs",
                "value": "b",
            },
        ],
    },
}


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)


def dd(*data):
    raise HTTPError(status=418, body=json.dumps(data, indent=2, cls=SetEncoder))
