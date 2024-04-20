from vokab import Entity, EntityFlatListAdapter


def test_serialization_deserialization():
    entity = Entity(name="a", meta=dict(b=1, c=None), prevalence=10)
    assert entity.name == "a"
    assert entity.b == 1
    assert entity.c is None
    assert entity.prevalence == 10
    assert entity.model_dump(by_alias=True, mode="json") == {
        "name": "a",
        "label": "ENTITY",
        "aliases": [],
        "meta": {"b": 1, "c": None},
        "prevalence": 10,
        "slug": "entity/a",
    }

    data = EntityFlatListAdapter.dump_python([entity], mode="json")
    assert data == [
        {
            "name": "a",
            "label": "ENTITY",
            "aliases": "[]",
            "meta": '{"b": 1, "c": null}',
            "prevalence": 10,
            "slug": "entity/a",
        }
    ]

    entity_2 = EntityFlatListAdapter.validate_python(data)[0]
    assert entity_2.name == "a"
    assert entity_2.b == 1
    assert entity_2.c is None
    assert entity_2.prevalence == 10


def test_meta_edge_cases():
    entity = Entity(name="A B C")

    try:
        assert entity.unknown
        assert False, "Did not throw AttributeError exception."

    except AttributeError:
        pass

    entity.unknown = 123
    assert entity.unknown == 123

    assert entity.label == "ENTITY"
    assert entity == entity
    assert entity == "entity/a-b-c"
