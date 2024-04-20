import click
from vokab import Collection, logger
from vokab.cli import app


@app.command  # type: ignore[attr-defined]
@click.pass_context
def reindex(ctx):
    """Reindex the database."""
    collection: Collection = ctx.obj["collection"]
    logger.info("Database reindexing...")
    collection.database.reindex()
    logger.info("Database reindexed.")
