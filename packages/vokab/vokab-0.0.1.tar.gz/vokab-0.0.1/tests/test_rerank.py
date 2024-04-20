from pytest import approx
from vokab import Collection, ResultsAdapter, rerankers


def test_rrf_reranker(collection: Collection):
    term = "herekles"

    vector = collection.encoder(term)
    vss_results = collection.database.vss(vector, labels=[], limit=20)
    fuzz_results = collection.fuzz(term=term, results=vss_results, limit=20)

    assert isinstance(collection.reranker, rerankers.RRFRanker)
    ranked = collection.reranker(
        result_sets=[vss_results, fuzz_results], limit=4
    )

    assert ResultsAdapter.dump_python(ranked) == [
        {
            "distance": approx(0.46875),
            "is_alias": False,
            "label": "HERO",
            "prevalence": 0,
            "rank": 1,
            "slug": "hero/hercules",
            "term": "hercules",
            "type": "rerank",
        },
        {
            "distance": approx(0.46875),
            "is_alias": True,
            "label": "CREATURE",
            "prevalence": 0,
            "rank": 2,
            "slug": "creature/minotaur",
            "term": "asterion",
            "type": "rerank",
        },
        {
            "distance": approx(0.5833333333333334),
            "is_alias": True,
            "label": "HERO",
            "prevalence": 0,
            "rank": 3,
            "slug": "hero/hercules",
            "term": "heracles",
            "type": "rerank",
        },
        {
            "distance": approx(0.7166666666666667),
            "is_alias": False,
            "label": "HERO",
            "prevalence": 0,
            "rank": 4,
            "slug": "hero/odysseus",
            "term": "odysseus",
            "type": "rerank",
        },
    ]
