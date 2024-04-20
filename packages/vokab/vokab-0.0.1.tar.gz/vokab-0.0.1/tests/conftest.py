from pathlib import Path
from tempfile import TemporaryDirectory

from click.testing import CliRunner
from pytest import fixture

from vokab import Collection, cli


@fixture(scope="session")
def data_path() -> Path:
    return Path(__file__).parent / "data"


@fixture(scope="session", params=["sqlite", "lancedb"])
def collection(request, data_path):
    with TemporaryDirectory(ignore_cleanup_errors=True) as dir_name:
        # initialize collection in temp directory using db_backend
        args = [
            "--path",
            dir_name,
            "init",
            f"database__type={request.param}",
        ]
        result = CliRunner().invoke(cli.app, args)
        assert result.exit_code == 0, f"Failed to init: {result.output}"

        # confirm db_backend set correctly
        collection = Collection.load(Path(dir_name))
        assert collection.config is not None
        assert collection.config.database.type == request.param

        # load myths.tsv file
        myths_tsv = str(data_path / "myths.tsv")
        args = ["--path", dir_name, "load", "--batch-size", "4", myths_tsv]
        CliRunner().invoke(cli.app, args)
        assert result.exit_code == 0, f"Failed to load: {result.output}"

        yield collection
