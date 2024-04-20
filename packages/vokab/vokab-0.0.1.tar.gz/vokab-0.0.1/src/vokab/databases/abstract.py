from abc import ABC, abstractmethod
from typing import Optional, List

from vokab import (
    Collection,
    Config,
    Dicts,
    Entity,
    EntityFlatListAdapter,
    Labels,
    Limit,
    Strs,
    Results,
    Vec,
    encoders,
    lazy,
    Entities,
)


class AbstractDatabase(ABC):
    type_mapping = {
        "sqlite": "vokab.databases.SQLiteDatabase",
        "lancedb": "vokab.databases.LanceDBDatabase",
    }

    def __init__(self, collection: Collection):
        self.collection: "Collection" = collection
        self.config: Config = collection.config
        self.encoder: "encoders.AbstractEncoder" = collection.encoder

    def initialize(self):
        pass  # pragma: no cover

    def reindex(self):
        pass

    @abstractmethod
    def stats(self) -> dict:
        pass

    @abstractmethod
    def upsert(self, entities: List[Entity]):
        pass

    @abstractmethod
    def get(self, slug: str) -> Optional[Entity]:
        pass

    @abstractmethod
    def fetch(self, slugs: Strs) -> Entities:
        pass

    @abstractmethod
    def exact(self, term: str, labels: Labels, limit: Limit) -> Results:
        pass

    @abstractmethod
    def vss(self, vector: Vec, labels: Labels, limit: Limit) -> Results:
        pass

    @abstractmethod
    def fts(self, term: str, labels: Labels, limit: Limit) -> Results:
        pass

    @classmethod
    def construct(cls, collection: Collection) -> "AbstractDatabase":
        class_type = collection.config.database.type
        class_type = AbstractDatabase.type_mapping.get(class_type, class_type)
        return lazy.create(AbstractDatabase, class_type, collection=collection)

    @classmethod
    def to_entity_dicts(cls, entities: List[Entity]) -> Dicts:
        return EntityFlatListAdapter.dump_python(entities, mode="json")

    def to_term_dicts(self, entities: List[Entity]) -> Dicts:
        terms = []
        as_dicts = []

        for entity in entities:
            is_alias = False
            seen = set()
            for term in entity.iter_terms():
                lower = term.lower()
                if lower not in seen:
                    terms.append(term)
                    seen.add(lower)
                    as_dicts.append(
                        {
                            "slug": entity.slug,
                            "label": entity.label,
                            "term": lower,
                            "is_alias": is_alias,
                            "prevalence": entity.prevalence,
                        }
                    )
                    is_alias = True

        if self.config.encoder.enabled:
            vectors = self.encoder(terms)
            for d, v in zip(as_dicts, vectors):
                d["vector"] = v

        return as_dicts
