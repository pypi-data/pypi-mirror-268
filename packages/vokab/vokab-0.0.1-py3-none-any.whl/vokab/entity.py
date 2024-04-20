import json
from typing import Any, Optional, ClassVar, Union, List
from unicodedata import normalize

from pydantic import (
    BaseModel,
    Field,
    TypeAdapter,
    computed_field,
    field_validator,
    field_serializer,
)


def slugify(name: str) -> str:
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    text = (
        normalize("NFKD", name)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    return "".join(char if char.isalnum() else "-" for char in text)


class Entity(BaseModel):
    NULL_LABEL: ClassVar = "ENTITY"

    name: str = Field(
        ...,
        description="Entity's preferred term.",
    )
    aliases: list[str] = Field(
        ...,
        description="Entity's alias terms.",
        default_factory=list,
    )
    label: str = Field(
        default=NULL_LABEL,
        description="Entity concept type such as PERSON, ORG, or GPE.",
    )
    meta: dict = Field(
        ...,
        description="Additional entity attribute fields.",
        default_factory=dict,
    )
    prevalence: int = Field(
        default=0,
        description="Higher value means more likely. Used for disambiguation.",
    )

    @computed_field(alias="slug")  # type: ignore[misc]
    @property
    def slug(self) -> str:
        return self.to_slug(self.name, self.label)

    @classmethod
    def to_slug(cls, name: str, label: Optional[str] = None) -> str:
        label = label or cls.NULL_LABEL
        return f"{label.lower()}/{slugify(name)}"

    def __eq__(self, other: Any):
        other = getattr(other, "slug", other)
        return self.slug == other

    def __getattr__(self, key: str) -> Any:
        # Check if the key exists in the meta dictionary
        if self.meta is not None and key in self.meta:
            return self.meta[key]
        # Attribute not found; raise AttributeError
        raise AttributeError(
            f"{self.__class__.__name__!r} object has no attribute {key!r}"
        )

    def __setattr__(self, key: str, name: Any):
        # Check if the key is a predefined field in the BaseModel
        if key in self.model_fields:
            super().__setattr__(key, name)
        else:
            self.meta = self.meta or {}
            self.meta[key] = name

    def iter_terms(self):
        yield self.name
        yield from self.aliases

    # noinspection PyMethodParameters
    @field_validator("meta", "aliases", mode="before")
    def json_loads(cls, value: Union[list, dict, str]) -> Union[list, dict]:
        if isinstance(value, str):
            data = json.loads(value)
        else:
            data = value
        return data


Entities = List[Entity]
EntitiesAdapter = TypeAdapter(Entities)


class EntityFlattened(Entity):
    """
    Serialize the Entity class as a flat dictionary.
    Replaces meta and alias fields with a JSON string.
    """

    @field_serializer("meta", "aliases")
    def serialize_as_json(self, value: Union[list, dict]) -> str:
        return json.dumps(value)


EntityFlatListAdapter = TypeAdapter(List[EntityFlattened])
