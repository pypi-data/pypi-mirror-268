from typing import List, Tuple

from rapidfuzz import fuzz
from rapidfuzz.process import extract

from vokab import Strs
from . import AbstractFuzz


class DefaultFuzz(AbstractFuzz):
    @property
    def scorer(self):
        return getattr(fuzz, self.collection.config.fuzz.scorer)

    def fuzz(
        self, term: str, choices: Strs, limit: int
    ) -> List[Tuple[float, int]]:
        matches = []

        results = extract(
            query=term,
            choices=choices,
            scorer=self.scorer,
            limit=limit,
        )

        for text, score, index in results:
            matches.append((100 - score, index))

        return matches
