import math
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, TypeAdapter

from vokab import Confidence, Entity, Labels, const


class Request(BaseModel):
    """Search Request submitted to Searcher with no optional values."""

    # term being searched for in collection
    term: str

    # allowed label, used for pre-filtering when set
    labels: Labels = None

    # switch default linker
    linker: Optional[str] = None

    # override default limit
    limit: Optional[int] = None


class Result(BaseModel):
    slug: str
    term: str

    label: str = Field(default="ENTITY")
    is_alias: bool = Field(default=False)
    prevalence: int = Field(
        default=0,
        description="Higher value means more likely. Used for disambiguation.",
    )

    # result type
    type: const.ResultType
    rank: int = Field(default=math.inf)
    distance: float = Field(default=math.inf)


Results = List[Result]
ResultsAdapter = TypeAdapter(Results)


class Candidate(BaseModel):
    term: str
    is_alias: bool
    entity: Entity
    ranks: Dict[const.ResultType, int]
    distances: Dict[const.ResultType, float]

    @property
    def is_exact(self):
        return "exact" in self.ranks


Candidates = List[Candidate]
CandidatesAdapter = TypeAdapter(Candidates)


class Response(BaseModel):
    request: Request
    candidates: Candidates = Field(default_factory=list)
    match: Optional[Entity] = Field(default=None)

    def __str__(self):
        return self.match.name if self.match else "-"

    @property
    def is_exact(self):
        return self.candidates and self.candidates[0].is_exact
