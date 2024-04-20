from typing import List
from pydantic import TypeAdapter
from vokab import Entity, loader


def test_from_csv(data_path):
    entities = list(loader.from_file(data_path / "emojis.csv"))
    assert len(entities) == 4
    assert entities[0] == {
        "name": "happy",
        "aliases": ["😀"],
        "prevalence": "1",
    }


def test_from_tsv(data_path):
    entities = list(loader.from_file(data_path / "myths.tsv"))
    assert len(entities) == 10
    assert entities[-1] == {
        "aliases": ["Jupiter", "Jove"],
        "label": "DEITY",
        "meta": {
            "definition": "King of the Olympian gods",
            "dominion": "Power",
            "gender": "Male",
        },
        "name": "Zeus",
    }
    adapter = TypeAdapter(List[Entity])
    validated = adapter.validate_python(entities)
    assert len(validated) == 10
    assert isinstance(validated[0], Entity)


def test_from_txt(data_path):
    entities = list(loader.from_file(data_path / "emotions.txt"))
    assert len(entities) == 12
    assert entities[-1] == {
        "name": "Serenity",
    }


def test_from_jsonl(data_path):
    entities = list(loader.from_file(data_path / "mixed.jsonl"))
    assert len(entities) == 6
    assert entities[0] == {
        "name": "Dog",
        "aliases": ["Canine", "Hound"],
        "label": "animal",
    }
