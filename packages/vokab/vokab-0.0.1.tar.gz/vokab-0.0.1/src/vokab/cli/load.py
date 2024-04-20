from pathlib import Path
from typing import Iterable, List

import click
from pydantic import TypeAdapter
from tqdm import tqdm

from vokab import Collection, Entity, databases, loader
from vokab.cli import app


class Target:
    def __init__(self, database: databases.AbstractDatabase, batch_size: int):
        self.database = database
        self.batch_size = batch_size

    def __call__(self, rows: Iterable[dict]) -> int:
        adapter = TypeAdapter(List[Entity])
        batch = []
        total_count = 0

        for row in rows:
            total_count += 1
            batch.append(row)

            if len(batch) >= self.batch_size:
                entities = adapter.validate_python(batch)
                self.database.upsert(entities)
                batch = []

        if batch:
            entities = adapter.validate_python(batch)
            self.database.upsert(entities)

        self.database.reindex()

        return total_count


@app.command  # type: ignore[attr-defined]
@click.argument("filename", type=click.Path(exists=True))
@click.option(
    "--mv-splitter",
    default="|",
    help="Multi-value splitter used for parsing aliases (default: '|')",
)
@click.option(
    "--batch-size",
    type=int,
    default=1000,
    help="Batch sizes for loading data to the database.",
)
@click.pass_context
def load(ctx, filename, mv_splitter, batch_size):
    """Load entities from a file."""
    collection: Collection = ctx.obj["collection"]

    path = Path(filename)
    with path.open() as file:
        total_lines = sum(1 for _ in file)

    source = loader.from_file(path, mv_splitter=mv_splitter)
    target = Target(database=collection.database, batch_size=batch_size)
    with tqdm(source, total=total_lines, unit="entities") as progress:
        count = target(progress)

    click.echo(f"Loaded {count} entities from {path}")
