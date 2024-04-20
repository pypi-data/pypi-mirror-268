from pytest import approx

from vokab import (
    Collection,
    Request,
    databases,
    encoders,
    fuzz,
    linkers,
)


def test_default_collection(collection: Collection):
    assert collection.config_path.name.endswith("terms.json")
    assert collection.config_path.exists()
    assert isinstance(collection.encoder, encoders.SBertEncoder)
    assert isinstance(collection.database, databases.AbstractDatabase)
    assert isinstance(collection.fuzz, fuzz.DefaultFuzz)
    assert isinstance(collection.linker, linkers.DefaultLinker)


def test_fail_collection_load(mocker):
    try:
        assert Collection.load("/#") is None  # invalid path
        assert False, "Didn't throw exception."
    except OSError:
        pass


def test_call_linker_exact_match(collection):
    response = collection(q="athena")
    assert response.is_exact
    assert str(response) == "Athena"
    assert response.model_dump(exclude_none=True) == {
        "candidates": [
            {
                "distances": {"exact": 0.0, "rerank": 0.0},
                "entity": {
                    "aliases": ["Minerva", "Pallas"],
                    "label": "DEITY",
                    "meta": {
                        "definition": "Goddess of wisdom, war, " "and crafts",
                        "dominion": "Wisdom",
                        "gender": "Female",
                    },
                    "name": "Athena",
                    "prevalence": 0,
                    "slug": "deity/athena",
                },
                "is_alias": False,
                "ranks": {"exact": 1, "rerank": 1},
                "term": "athena",
            }
        ],
        "match": {
            "aliases": ["Minerva", "Pallas"],
            "label": "DEITY",
            "meta": {
                "definition": "Goddess of wisdom, war, and crafts",
                "dominion": "Wisdom",
                "gender": "Female",
            },
            "name": "Athena",
            "prevalence": 0,
            "slug": "deity/athena",
        },
        "request": {"linker": "default", "term": "athena"},
    }


def test_call_linker_semantic_lexical(collection):
    request = Request(term="herekles", limit=2)
    term = "herekles"
    response = collection(q=request)
    assert not response.is_exact
    assert str(response) == "Odysseus"
    assert response.model_dump(exclude_none=True) == {
        "candidates": [
            {
                "distances": {
                    "fuzz": 75.0,
                    "rerank": 0.25,
                    "vss": approx(72.650146484375),
                },
                "entity": {
                    "aliases": ["Ulysses"],
                    "label": "HERO",
                    "meta": {
                        "definition": "Legendary Greek king of " "Ithaca",
                        "dominion": "Cunning",
                        "gender": "Male",
                    },
                    "name": "Odysseus",
                    "prevalence": 0,
                    "slug": "hero/odysseus",
                },
                "is_alias": False,
                "ranks": {"fuzz": 1, "rerank": 1, "vss": 2},
                "term": "odysseus",
            },
            {
                "distances": {
                    "fuzz": 75.0,
                    "rerank": 0.25,
                    "vss": approx(66.16249084472656),
                },
                "entity": {
                    "aliases": ["Asterion"],
                    "label": "CREATURE",
                    "meta": {
                        "definition": "Half-man, half-bull " "monster",
                        "dominion": "Strength",
                        "gender": "Male",
                    },
                    "name": "Minotaur",
                    "prevalence": 0,
                    "slug": "creature/minotaur",
                },
                "is_alias": True,
                "ranks": {"fuzz": 2, "rerank": 2, "vss": 1},
                "term": "asterion",
            },
        ],
        "match": {
            "aliases": ["Ulysses"],
            "label": "HERO",
            "meta": {
                "definition": "Legendary Greek king of Ithaca",
                "dominion": "Cunning",
                "gender": "Male",
            },
            "name": "Odysseus",
            "prevalence": 0,
            "slug": "hero/odysseus",
        },
        "request": {
            "limit": 2,
            "linker": "default",
            "term": "herekles",
        },
    }
