from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from vokab import Candidates, Collection, Request, Results, Strs, lazy


class AbstractReranker(ABC):
    type_mapping = {
        "default": "vokab.rerankers.RRFRanker",
        "rrf": "vokab.rerankers.RRFRanker",
    }

    def __init__(self, collection: Collection, **_):
        self.collection = collection
        self.request_keys = set(Request.model_fields.keys())

    @classmethod
    def construct(
        cls,
        collection: Collection,
        class_type: Optional[str] = None,
    ) -> "AbstractReranker":
        class_type = class_type or collection.config.reranker.type
        class_type = AbstractReranker.type_mapping.get(class_type, class_type)
        return lazy.create(AbstractReranker, class_type, collection=collection)

    def __call__(self, result_sets: List[Results], limit: int) -> Results:
        return self.rerank(result_sets=result_sets, limit=limit)

    @abstractmethod
    def rerank(self, result_sets: List[Results], limit: int) -> Results:
        pass
