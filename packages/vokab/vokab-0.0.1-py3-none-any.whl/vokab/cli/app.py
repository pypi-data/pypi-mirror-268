import logging

import click

from vokab import Collection, const


@click.group()
@click.option(
    "--path",
    "-p",
    type=click.Path(),
    help="Path to vokab collection.",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Increase verbosity. Use multiple times for more verbosity.",
)
@click.option(
    "-q",
    "--quiet",
    is_flag=True,
    help="Suppress all output except errors.",
)
@click.pass_context
def app(ctx, path: str, verbose: int, quiet: bool):
    from vokab.logging import logger

    if quiet:
        logger.setLevel(logging.ERROR)
    elif verbose == 1:
        logger.setLevel(logging.INFO)
    elif verbose >= 2:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)

    ctx.ensure_object(dict)
    path = path or const.DEFAULT_VOKAB_HOME
    if path is None:
        msg = "You must specify a project path (--path or VOKAB_HOME)."
        raise click.UsageError(msg)
    collection = Collection.load(path)
    ctx.obj["collection"] = collection
