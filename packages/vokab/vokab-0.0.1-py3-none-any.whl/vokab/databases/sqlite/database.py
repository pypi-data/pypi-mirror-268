import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import List, Optional

import aiosql

from vokab import (
    Entity,
    Labels,
    Limit,
    Results,
    ResultsAdapter,
    Strs,
    Vec,
    lazy,
    Entities,
)
from .. import AbstractDatabase


class SQLiteDatabase(AbstractDatabase):
    name = "sqlite"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sql = aiosql.from_path(Path(__file__).parent / "sql", "sqlite3")

    def connect(self):
        db_url = self.config.database.url or "database.db"
        if not os.path.isabs(db_url):
            db_url = str(self.collection.path / db_url)
        conn = sqlite3.connect(db_url)

        conn.row_factory = lambda c, r: dict(
            [(col[0], r[idx]) for idx, col in enumerate(c.description)]
        )

        if self.config.encoder.enabled:
            sqlite_vss = lazy.lazy_import("sqlite_vss")
            conn.enable_load_extension(True)
            sqlite_vss.load(conn)

        return conn

    @contextmanager
    def acquire(self, existing_connection=None):
        conn = existing_connection

        if conn is None:
            conn = self.connect()

        try:
            yield conn

            if not existing_connection:
                conn.commit()

        except Exception as e:  # pragma: no cover
            conn.rollback()
            raise e

        finally:
            if not existing_connection:
                conn.close()

    def initialize(self):
        with self.acquire() as conn:
            self.sql.init_tables(conn)
            conn.execute(
                f"CREATE VIRTUAL TABLE IF NOT EXISTS vss_terms USING "
                f"vss0(vector({self.config.encoder.dimensions}))"
            )
            self.sql.init_triggers(conn)

    def stats(self) -> dict:
        with self.acquire() as conn:
            return dict(self.sql.stats(conn))

    def upsert(self, entities: List[Entity]):
        with self.acquire() as conn:
            entity_dicts = self.to_entity_dicts(entities)
            self.sql.upsert_entities(conn, entity_dicts)
            term_dicts = self.to_term_dicts(entities)
            self.sql.upsert_terms(conn, term_dicts)

    def exact(self, term: str, labels: Labels, limit: Limit) -> Results:
        with self.acquire() as conn:
            data = self.sql.exact_search(
                conn,
                term=term,
                labels=piped_or_null(labels),
                limit=limit,
            )
            return ResultsAdapter.validate_python(data)

    def vss(self, vector: Vec, labels: Labels, limit: Limit) -> Results:
        with self.acquire() as conn:
            if not labels:
                results = self.sql.vss_search(
                    conn,
                    vector=vector,
                    limit=limit,
                )
            else:
                results = self.sql.vss_search_by_label(
                    conn,
                    vector=vector,
                    labels=piped_or_null(labels),
                    limit=limit,
                )

            return ResultsAdapter.validate_python(results)

    def fts(self, term: str, labels: Labels, limit: Limit) -> Results:
        with self.acquire() as conn:
            data = self.sql.fts_search(
                conn,
                term=term,
                labels=piped_or_null(labels),
                limit=limit,
            )
            return ResultsAdapter.validate_python(data)

    def get(self, slug: str) -> Optional[Entity]:
        entity = None
        with self.acquire() as conn:
            data = self.sql.get_entity(conn, slug=slug)
            if data:
                entity = Entity(**data)
        return entity

    def fetch(self, slugs: Strs) -> Entities:
        placeholders = ",".join(["?"] * len(slugs))
        sql = f"SELECT * FROM entities WHERE slug IN ({placeholders})"
        with self.acquire() as conn:
            data = conn.execute(sql, slugs).fetchall()
            return [Entity(**record) for record in data]


def piped_or_null(vals: Labels):
    if vals:
        return "|" + "|".join(vals) + "|"
