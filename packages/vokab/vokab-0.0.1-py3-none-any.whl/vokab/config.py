import json
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field

from vokab import const


class DatabaseConfig(BaseModel):
    type: str = "lancedb"
    url: Optional[str] = None


class EncoderConfig(BaseModel):
    type: str = "sbert"
    enabled: bool = True
    batch: int = 1000
    device: const.DeviceType = "cpu"
    model: str = "sentence-transformers/paraphrase-MiniLM-L6-v2"
    dimensions: int = 384
    precision: const.PrecisionType = "float32"


class FuzzConfig(BaseModel):
    type: str = "default"
    scorer: const.FuzzScorerType = "WRatio"


class LinkerConfig(BaseModel):
    type: str = "default"


class RerankerConfig(BaseModel):
    type: str = "rrf"


class Config(BaseModel):
    path: Optional[Path] = Field(None, exclude=True)
    database: DatabaseConfig = Field(..., default_factory=DatabaseConfig)
    encoder: EncoderConfig = Field(..., default_factory=EncoderConfig)
    fuzz: FuzzConfig = Field(..., default_factory=FuzzConfig)
    linker: LinkerConfig = Field(..., default_factory=LinkerConfig)
    reranker: RerankerConfig = Field(..., default_factory=RerankerConfig)

    def apply(self, **updates) -> "Config":
        current = self.model_dump()
        nested = self.make_nested(updates)
        merged = self.merge_nested(current, nested)
        return Config(path=self.path, **merged)

    def save(self):
        assert self.path, "Config path not set."
        output = self.model_dump()
        json.dump(output, self.path.open("w"), indent=4)

    @classmethod
    def load(cls, path: Path) -> "Config":
        if path.exists():
            data = path.read_text()
            config = Config.model_validate_json(data)
        else:
            config = Config(path=path)
            config.save()
        return config

    @classmethod
    def merge_nested(cls, d1, d2):
        """
        Merge two nested dictionaries, prioritizing values from the second dictionary.
        Keys unique to the first dictionary are retained.

        :param d1: Existing nested dictionary
        :param d2: Updates dictionary
        :return: Merged dictionary where updates overwrite existing values,
                 and keys unique to the first dictionary are retained.
        """
        merged = d1.copy()

        for k, v in d2.items():
            if k in d1 and isinstance(d1[k], dict) and isinstance(v, dict):
                # Recursively merge nested dictionaries
                merged[k] = cls.merge_nested(d1[k], v)
            else:
                # Overwrite or add value from d2
                merged[k] = v

        return merged

    @classmethod
    def make_nested(cls, updates: dict) -> dict:
        """
        :param updates: Dict of updates with nested keys delimited by "__".
        :return: Nested dict with keys expanded.
        """
        updates_nested_dict: dict = {}
        for k, v in updates.items():
            if v is not None:
                if "__" in k:
                    keys = k.split("__")
                    nested_dict = updates_nested_dict
                    for key in keys[:-1]:
                        nested_dict = nested_dict.setdefault(key, {})
                    nested_dict[keys[-1]] = v
                else:
                    updates_nested_dict[k] = v  # pragma: no cover
        return updates_nested_dict
