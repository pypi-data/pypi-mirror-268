import math
from pytest import fixture
from vokab import Results, Result, ResultsAdapter


@fixture(scope="session")
def db(collection):
    return collection.database


def pop(results: Results):
    distances = []
    modified = []
    r: Result
    for r in results:
        distances.append(r.distance)
        modified.append(r.model_copy(update=dict(distance=math.inf)))
    assert distances == sorted(distances)
    return modified


def test_get_entity(db):
    entity = db.get(slug="deity/zeus")
    assert entity.model_dump() == {
        "aliases": ["Jupiter", "Jove"],
        "label": "DEITY",
        "meta": {
            "definition": "King of the Olympian gods",
            "dominion": "Power",
            "gender": "Male",
        },
        "name": "Zeus",
        "prevalence": 0,
        "slug": "deity/zeus",
    }


def test_fetch_entities(db):
    entities = db.fetch(slugs=["deity/zeus", "hero/odysseus"])
    names = sorted([e.name for e in entities])
    assert names == ["Odysseus", "Zeus"]


def test_vss_search(collection, db):
    vector = collection.encoder("herekles")
    results = pop(db.vss(vector, labels=[], limit=3))
    assert ResultsAdapter.dump_python(results) == [
        {
            "distance": math.inf,
            "is_alias": True,
            "label": "CREATURE",
            "prevalence": 0,
            "rank": 1,
            "slug": "creature/minotaur",
            "term": "asterion",
            "type": "vss",
        },
        {
            "distance": math.inf,
            "is_alias": False,
            "label": "HERO",
            "prevalence": 0,
            "rank": 2,
            "slug": "hero/odysseus",
            "term": "odysseus",
            "type": "vss",
        },
        {
            "distance": math.inf,
            "is_alias": True,
            "label": "HERO",
            "prevalence": 0,
            "rank": 3,
            "slug": "hero/hercules",
            "term": "heracles",
            "type": "vss",
        },
    ]

    r2 = pop(db.vss(vector, labels=["CREATURE", "HERO"], limit=3))
    assert r2 == results

    heroes = pop(db.vss(vector, labels=["HERO"], limit=1))
    assert ResultsAdapter.dump_python(heroes) == [
        {
            "distance": math.inf,
            "is_alias": False,
            "label": "HERO",
            "prevalence": 0,
            "rank": 1,
            "slug": "hero/odysseus",
            "term": "odysseus",
            "type": "vss",
        },
    ]

    assert pop(db.vss(vector, labels=["HERO2"], limit=1)) == []


def test_fts_search(db):
    results = pop(db.fts("athena", labels=[], limit=3))
    assert ResultsAdapter.dump_python(results) == [
        {
            "distance": math.inf,
            "is_alias": False,
            "label": "DEITY",
            "prevalence": 0,
            "rank": 1,
            "slug": "deity/athena",
            "term": "athena",
            "type": "fts",
        }
    ]
    assert pop(db.fts("athena", labels=["DEITY"], limit=3)) == results
    assert pop(db.fts("athena", labels=["DEITY", "HERO"], limit=3)) == results
    assert pop(db.fts("athena", labels=["HERO"], limit=3)) == []
    assert pop(db.fts("athena", labels=["DEITY2"], limit=3)) == []


def test_exact_search(db):
    results = pop(db.exact("ATHENA", [], 3))
    assert ResultsAdapter.dump_python(results) == [
        {
            "distance": math.inf,
            "is_alias": False,
            "label": "DEITY",
            "prevalence": 0,
            "rank": 1,
            "slug": "deity/athena",
            "term": "athena",
            "type": "exact",
        }
    ]
    assert pop(db.exact("athena", ["DEITY"], 3)) == results
    assert pop(db.exact("athena", ["DEITY", "HERO"], 3)) == results
    assert pop(db.exact("athena", ["HERO"], 3)) == []
    assert pop(db.exact("athena", ["DEITY2"], 3)) == []


def test_stats(db):
    assert db.stats() == {
        "entities": 10,
        "terms": 21,
    }
