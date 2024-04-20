import re
from typing import ClassVar, List

import pyarrow as pa

from vokab import Entity, Labels, Limit, Results, ResultsAdapter, Vec, logger
from . import Table
from .. import AbstractDatabase


class TermsTable(Table):
    name: ClassVar = "terms"
    column_names: ClassVar = [
        "slug",
        "label",
        "term",
        "is_alias",
        "prevalence",
    ]

    def upsert(self, entities: List[Entity]):
        as_dicts = self.database.to_term_dicts(entities)
        super(TermsTable, self).add(as_dicts)

    def exact(self, term: str, labels: Labels, limit: Limit) -> Results:
        query = clean_query(term)
        qb = self.table.search()
        qb = qb.select(self.column_names)

        # LanceDB support a single WHERE clause
        clause = f"(term == '{query}')"
        if labels:
            subclauses = [f'label == "{label}"' for label in labels]
            clause += "AND (" + " OR ".join(subclauses) + ")"
        qb = qb.where(clause, prefilter=True)

        data = qb.limit(limit).to_list()
        sorted(data, key=lambda d: d["is_alias"])
        for rank, record in enumerate(data, start=1):
            record["type"] = "exact"
            record["rank"] = rank
            record["distance"] = int(record["is_alias"])

        return ResultsAdapter.validate_python(data)

    def vss(self, vector: Vec, labels: Labels, limit: Limit) -> Results:
        kw = {"query_type": "vector", "vector_column_name": "vector"}
        qb = self.table.search(query=vector, **kw)
        qb = qb.select(self.column_names)
        if labels:
            subclauses = [f'label == "{label}"' for label in labels]
            clause = " OR ".join(subclauses)
            qb.where(clause, prefilter=True)
        data = qb.limit(limit).to_list()
        for vss_rank, record in enumerate(data, start=1):
            record["type"] = "vss"
            record["rank"] = vss_rank
            record["distance"] = record.pop("_distance")
        return ResultsAdapter.validate_python(data)

    def fts(self, name: str, labels: Labels, limit: Limit) -> Results:
        query = clean_query(name)
        qb = self.table.search(query, query_type="fts")
        qb = qb.select(self.column_names)
        if labels:
            subclauses = [f'label == "{label}"' for label in labels]
            clause = " OR ".join(subclauses)
            qb.where(clause, prefilter=True)
        data = qb.limit(limit).to_list()
        for fts_rank, record in enumerate(data, start=1):
            record["type"] = "fts"
            record["rank"] = fts_rank
            record["distance"] = record.pop("score")
        return ResultsAdapter.validate_python(data)

    def reindex(self):
        num_records = self.table.count_rows()

        logger.info(f"Indexing FTS: {num_records}")
        self.table.create_fts_index(["term"], replace=True)

        if num_records > 256:  # pragma: no cover
            num_partitions = min(num_records, 256)
            num_sub_vectors = min(num_records, 96)
            index_cache_size = min(num_records, 256)
            device = None
            if self.database.config.encoder.device in {"cuda", "mps"}:
                device = self.database.config.encoder.device

            logger.info(f"Indexing VSS: {num_records} ({device or 'CPU'})")
            self.table.create_index(
                metric="cosine",
                num_partitions=num_partitions,
                num_sub_vectors=num_sub_vectors,
                vector_column_name="vector",
                replace=True,
                index_cache_size=index_cache_size,
                accelerator=device,
            )
        logger.info("Terms Table: Indexing complete.")

    @classmethod
    def columns(cls, database: AbstractDatabase) -> List[pa.Field]:
        columns = [
            pa.field("slug", pa.string()),
            pa.field("label", pa.string()),
            pa.field("term", pa.string()),
            pa.field("is_alias", pa.bool_()),
            pa.field("prevalence", pa.int64()),
        ]
        if database.config.encoder.enabled:
            columns.append(
                pa.field(
                    "vector",
                    pa.list_(
                        pa.float32(),
                        database.config.encoder.dimensions,
                    ),
                )
            )
        return columns


alphanum_re = re.compile(r"[^a-zA-Z0-9\s]")


def clean_query(query):
    return alphanum_re.sub("", query).lower()
