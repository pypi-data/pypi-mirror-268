from typing import ClassVar, List, Optional

import pyarrow as pa

from vokab import Entity, Strs, EntitiesAdapter
from . import Table
from .. import AbstractDatabase


class EntitiesTable(Table):
    name: ClassVar = "entities"

    def upsert(self, entities: List[Entity]):
        as_dicts = self.database.to_entity_dicts(entities)
        super(EntitiesTable, self).add(as_dicts)

    def get(self, slug: str) -> Optional[Entity]:
        query = f"slug == '{slug}'"
        data = self.table.search().where(query).to_list()
        return Entity(**data[0]) if data else None

    def fetch(self, slugs: Strs) -> List[Entity]:
        data = []

        if slugs:
            slugs = map(lambda s: s.replace("'", ""), slugs)
            slugs = map(lambda s: f"'{s}'", slugs)
            slugs = ", ".join(slugs)
            query = f"slug in ({slugs})"
            count = len(slugs)
            data = self.table.search().where(query).limit(count).to_list()

        return EntitiesAdapter.validate_python(data)

    @classmethod
    def columns(cls, database: AbstractDatabase) -> List[pa.Field]:
        columns = [
            pa.field("slug", pa.string()),
            pa.field("name", pa.string()),
            pa.field("label", pa.string()),
            pa.field("prevalence", pa.int64()),
            pa.field("meta", pa.string()),
            pa.field("aliases", pa.string()),
        ]
        return columns
