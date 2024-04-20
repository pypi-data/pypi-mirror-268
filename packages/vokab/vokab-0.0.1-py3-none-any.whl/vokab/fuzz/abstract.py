from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from vokab import Collection, Request, Results, Strs, lazy


class AbstractFuzz(ABC):
    type_mapping = {
        "default": "vokab.fuzz.DefaultFuzz",
    }

    def __init__(self, collection: Collection, **_):
        self.collection = collection
        self.request_keys = set(Request.model_fields.keys())

    @classmethod
    def construct(
        cls,
        collection: Collection,
        class_type: Optional[str] = None,
    ) -> "AbstractFuzz":
        class_type = class_type or collection.config.fuzz.type
        class_type = AbstractFuzz.type_mapping.get(class_type, class_type)
        return lazy.create(AbstractFuzz, class_type, collection=collection)

    def __call__(self, term: str, results: Results, limit: int) -> Results:
        # Group results by slug and term
        grouped_results = {}
        for result in results:
            key = (result.slug, result.term)
            if (
                key not in grouped_results
                or result.is_alias < grouped_results[key].is_alias
            ):
                grouped_results[key] = result

        # Sort the grouped results by alias (preferred first) then prevalence
        sorted_results = sorted(
            grouped_results.values(),
            key=lambda r: (r.is_alias, -1 * r.prevalence),
        )
        choices = [r.term for r in sorted_results]

        # Get matches (distance, index)
        matches = self.fuzz(term=term, choices=choices, limit=limit)

        # Sort matches by lowest distance then by preferred term/prevalence
        matches = sorted(matches)

        # Collect out results with fuzz type, distance, and rank applied
        out_results = []
        for rank, (distance, index) in enumerate(matches, start=1):
            update = dict(type="fuzz", distance=distance, rank=rank)
            in_result = sorted_results[index]
            out_result = in_result.model_copy(update=update)
            out_results.append(out_result)

        return out_results

    @abstractmethod
    def fuzz(
        self, term: str, choices: Strs, limit: int
    ) -> List[Tuple[float, int]]:
        pass
