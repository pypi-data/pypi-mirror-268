import os
from typing import (
    Annotated,
    Literal,
    List,
    Optional,
    Tuple,
    Set,
    Union,
    get_args,
)
import annotated_types

# Custom Types
Dicts = Union[List[dict], Tuple[dict, ...], Set[dict]]
Confidence = Annotated[float, annotated_types.Ge(0.0), annotated_types.Le(1.0)]
Strs = Union[List[str], Tuple[str, ...], Set[str]]
Labels = Optional[Union[List[str], Tuple[str, ...], Set[str]]]
Vec = List[float]
Limit = Annotated[int, annotated_types.Ge(0), annotated_types.Le(1000)]

# Default Vokab Home
DEFAULT_VOKAB_HOME = os.environ.get("VOKAB_HOME") or "~/.local/vokab"
DEFAULT_VOKAB_HOME = os.path.expanduser(DEFAULT_VOKAB_HOME)

# Device to use for generating semantic embeddings
# https://www.sbert.net/examples/applications/computing-embeddings/README.html
DeviceType = Literal["cpu", "cuda", "mps", "npu"]
DeviceChoices = get_args(DeviceType)
PrecisionType = Literal["float32", "int8", "uint8", "binary", "ubinary"]

# Results Types for searching, fuzzing, etc.
ResultType = Literal["exact", "vss", "fts", "fuzz", "rerank"]

# Response Decision type
# match = a single candidate identified with strong relative confidence.
# ambiguous = 2+ candidates were identified with no definitive confidence.
# novel = no candidates identified with any confidence.
DecisionType = Literal["match", "ambiguous", "novel"]

# Fuzz Scorers:
# https://rapidfuzz.github.io/RapidFuzz/Usage/fuzz.html
# ratio: Calculates Levenshtein Distance similarity ratio
# partial_ratio: Compares substrings, good for different length strings
# token_set_ratio: Compares unique words, allows different word order
# partial_token_set_ratio: Like token_set_ratio but compares substrings
# token_sort_ratio: Sorts words before compare, good when order is irrelevant
# partial_token_sort_ratio: Like token_sort_ratio but compares substrings
# token_ratio: Averages token_sort_ratio and token_set_ratio
# partial_token_ratio: Averages partial token sort and set ratios
# WRatio: Weighted combination of different ratios based on string lengths
# QRatio: Faster version of ratio, less accurate
FuzzScorerType = Literal[
    "ratio",
    "partial_ratio",
    "token_set_ratio",
    "partial_token_set_ratio",
    "token_sort_ratio",
    "partial_token_sort_ratio",
    "token_ratio",
    "partial_token_ratio",
    "WRatio",
    "QRatio",
]
