from abc import ABC, abstractmethod
from typing import List, Optional

from vokab import (
    Candidate,
    Candidates,
    Collection,
    Entity,
    Request,
    Response,
    Results,
    lazy,
)


class AbstractLinker(ABC):
    type_mapping = {
        "default": "vokab.linkers.DefaultLinker",
    }

    def __init__(self, collection: Collection, **_):
        self.collection = collection
        self.request_keys = set(Request.model_fields.keys())

    @property
    def encoder(self):
        return self.collection.encoder

    @property
    def database(self):
        return self.collection.database

    @classmethod
    def construct(
        cls,
        collection: Collection,
        class_type: Optional[str] = None,
    ) -> "AbstractLinker":
        class_type = class_type or collection.config.linker.type
        class_type = AbstractLinker.type_mapping.get(class_type, class_type)
        return lazy.create(AbstractLinker, class_type, collection=collection)

    def __call__(self, request: Request) -> Response:
        result_sets: List[Results] = self.search(request)
        ranked_results: Results = self.rerank(request, result_sets)
        candidates: Candidates = self.collect(
            request, ranked_results, result_sets
        )
        match: Optional[Entity] = self.select(request, candidates)
        return Response(
            request=request,
            candidates=candidates,
            match=match,
        )

    @abstractmethod
    def search(self, request: Request) -> List[Results]:
        """Use request to search database for initial results."""

    def collect(
        self,
        request: Request,
        ranked_results: Results,
        result_sets: List[Results],
    ) -> Candidates:
        slugs = [result.slug for result in ranked_results]
        entity_dict = dict((e.slug, e) for e in self.database.fetch(slugs))
        candidate_map = {}
        candidates = []

        for result in ranked_results:
            entity = entity_dict.get(result.slug)
            assert entity is not None, f"Cannot find entity: {result.slug}"

            candidate = Candidate(
                term=result.term,
                is_alias=result.is_alias,
                entity=entity_dict.get(result.slug),
                ranks={result.type: result.rank},
                distances={result.type: result.distance},
            )
            candidates.append(candidate)
            candidate_map[(result.slug, result.term)] = candidate

        for result_set in result_sets:
            for result in result_set:
                candidate = candidate_map.get((result.slug, result.term))
                if candidate:
                    candidate.ranks[result.type] = result.rank
                    candidate.distances[result.type] = result.distance

        return candidates

    def rerank(self, request: Request, result_sets: List[Results]) -> Results:
        """Rank input result sets and return a single ranked result set."""
        limit: int = request.limit or 10
        reranked: Results = self.collection.reranker(
            result_sets=result_sets,
            limit=limit,
        )

        return reranked

    @abstractmethod
    def select(
        self, request: Request, candidates: Candidates
    ) -> Optional[Entity]:
        """Select best result using selection strategy and resolve Entity."""
