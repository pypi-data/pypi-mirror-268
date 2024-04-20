from typing import List, Optional

from vokab import Entity, Request, Results, Candidates
from . import AbstractLinker


class DefaultLinker(AbstractLinker):
    def search(self, request: Request) -> List[Results]:
        limit: int = request.limit or 10

        exact: Results = self.database.exact(
            term=request.term,
            labels=request.labels,
            limit=limit,
        )

        result_set: List[Results]

        if exact:
            result_set = [exact]

        else:
            vss = self.database.vss(
                vector=self.encoder.encode_one(request.term),
                labels=request.labels,
                limit=limit,
            )

            fts = self.database.fts(
                term=request.term,
                labels=request.labels,
                limit=limit,
            )

            fuzz = self.collection.fuzz(
                term=request.term,
                results=vss + fts,
                limit=limit,
            )
            result_set = [vss, fuzz]

        return result_set

    def select(
        self, request: Request, candidates: Candidates
    ) -> Optional[Entity]:
        """Select best result using selection strategy and resolve Entity."""
        if candidates:
            return candidates[0].entity
