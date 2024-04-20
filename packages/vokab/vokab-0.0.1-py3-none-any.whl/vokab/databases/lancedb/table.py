from abc import abstractmethod
from typing import ClassVar, List

import pyarrow as pa
from lancedb import LanceDBConnection
from lancedb.table import LanceTable

from vokab import Dicts, Entity
from .. import AbstractDatabase


class Table:
    name: ClassVar = None

    def __init__(self, database: AbstractDatabase, table: LanceTable):
        self.database = database
        self.table = table

    def add(self, data: Dicts):
        self.table.add(data)

    def count(self) -> int:
        return self.table.count_rows()

    def reindex(self):
        pass

    @abstractmethod
    def upsert(self, entities: List[Entity]):
        pass

    @classmethod
    def columns(cls, database: AbstractDatabase) -> List[pa.Field]:
        raise NotImplementedError

    @classmethod
    def connect(cls, database: AbstractDatabase, conn: LanceDBConnection):
        if cls.name not in conn.table_names():
            table = cls.construct(database, conn)
        else:
            table = conn.open_table(cls.name)
        return cls(database=database, table=table)

    @classmethod
    def construct(cls, database: AbstractDatabase, conn: LanceDBConnection):
        schema = pa.schema(cls.columns(database))
        return conn.create_table(name=cls.name, schema=schema, exist_ok=True)
