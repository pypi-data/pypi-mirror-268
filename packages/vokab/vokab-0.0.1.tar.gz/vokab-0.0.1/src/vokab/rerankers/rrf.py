from typing import Dict, List, Tuple

from vokab import Candidates, Result, Results

from . import AbstractReranker


def sort_key(item: Tuple[Tuple[str, str], Tuple[Result, float]]) -> tuple:
    _, (result, rrf) = item
    return rrf, not result.is_alias, result.prevalence


class RRFRanker(AbstractReranker):
    def rerank(self, result_sets: List[Results], limit: int) -> Results:
        mapping: Dict[Tuple[str, str], Tuple[Result, float]] = {}
        num_result_sets = len(result_sets)

        for results in result_sets:
            for result in results:
                key = (result.slug, result.term)
                _, reciprocal = mapping.setdefault(key, (result, 0.0))
                reciprocal += 1 / result.rank
                mapping[key] = (result, reciprocal)

        sorted_results = sorted(mapping.items(), key=sort_key, reverse=True)
        sorted_results = sorted_results[:limit]

        reranked_results: Results = []
        for rank, (_, (result, rrf_score)) in enumerate(
            sorted_results, start=1
        ):
            distance = 1.0 - (rrf_score / num_result_sets)
            new_result = result.model_copy(
                update={
                    "type": "rerank",
                    "rank": rank,
                    "distance": distance,
                }
            )
            reranked_results.append(new_result)

        return reranked_results
