import click

from vokab import Collection
from vokab.cli import app


@app.command  # type: ignore[attr-defined]
@click.argument("params", nargs=-1)
@click.pass_context
def init(ctx, params):
    """Initialize a new collection."""
    collection: Collection = ctx.obj["collection"]
    kw = dict([param.split("=", maxsplit=1) for param in params])
    collection.update(**kw)
    collection.database.initialize()
    click.echo(f"Collection initialized: {collection.path}")
