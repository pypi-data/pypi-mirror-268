import os.path
from typing import List, Optional

from lancedb import LanceDBConnection, connect

from vokab import Entity, Labels, Limit, Results, Strs, Vec, Entities
from . import EntitiesTable, TermsTable
from .. import AbstractDatabase


class LanceDBDatabase(AbstractDatabase):
    name = "lancedb"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._conn = None
        self._terms = None
        self._entities = None

    @property
    def conn(self) -> LanceDBConnection:
        if self._conn is None:
            db_url = self.config.database.url or "db"
            if not os.path.isabs(db_url):
                db_url = str(self.collection.path / db_url)
            self._conn = connect(uri=db_url)
        return self._conn

    @property
    def entities(self) -> EntitiesTable:
        if self._entities is None:
            self._entities = EntitiesTable.connect(self, self.conn)
        return self._entities

    @property
    def terms(self) -> TermsTable:
        if self._terms is None:
            self._terms = TermsTable.connect(self, self.conn)
        return self._terms

    def reindex(self):
        self.entities.reindex()
        self.terms.reindex()

    def stats(self) -> dict:
        return {
            "entities": self.entities.count(),
            "terms": self.terms.count(),
        }

    def upsert(self, entities: List[Entity]):
        self.entities.upsert(entities)
        self.terms.upsert(entities)

    def exact(self, term: str, labels: Labels, limit: Limit) -> Results:
        return self.terms.exact(term, labels, limit)

    def vss(self, vector: Vec, labels: Labels, limit: Limit) -> Results:
        return self.terms.vss(vector, labels, limit)

    def fts(self, term: str, labels: Labels, limit: Limit) -> Results:
        return self.terms.fts(term, labels, limit)

    def get(self, slug: str) -> Optional[Entity]:
        return self.entities.get(slug)

    def fetch(self, slugs: Strs) -> Entities:
        return self.entities.fetch(slugs)
