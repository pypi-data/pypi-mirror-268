from vokab import Collection, Request, ResultsAdapter, fuzz


def test_default_fuzz(collection: Collection):
    assert isinstance(collection.fuzz, fuzz.DefaultFuzz)
    assert collection.config.fuzz.scorer == "WRatio"

    term = "herekles"
    vector = collection.encoder(term)
    vss_results = collection.database.vss(vector, labels=[], limit=20)

    fuzz_results = collection.fuzz(term=term, results=vss_results, limit=3)
    assert ResultsAdapter.dump_python(fuzz_results) == [
        {
            "distance": 25.0,
            "is_alias": False,
            "label": "HERO",
            "prevalence": 0,
            "rank": 1,
            "slug": "hero/hercules",
            "term": "hercules",
            "type": "fuzz",
        },
        {
            "distance": 25.0,
            "is_alias": True,
            "label": "HERO",
            "prevalence": 0,
            "rank": 2,
            "slug": "hero/hercules",
            "term": "heracles",
            "type": "fuzz",
        },
        {
            "distance": 28.57142857142857,
            "is_alias": True,
            "label": "DEITY",
            "prevalence": 0,
            "rank": 3,
            "slug": "deity/mercury",
            "term": "hermes",
            "type": "fuzz",
        },
    ]
