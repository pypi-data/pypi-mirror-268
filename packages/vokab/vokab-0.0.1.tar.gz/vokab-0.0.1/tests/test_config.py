from pathlib import Path
from tempfile import TemporaryDirectory

from vokab.config import Config, FuzzConfig


def test_search_config_invalid_fuzzer():
    try:
        FuzzConfig(scorer="InvalidScorer")
        assert False, "Expected ValueError for invalid fuzzer"
    except ValueError:
        pass


def test_config_defaults():
    config = Config()

    assert config.database.type == "lancedb"
    assert config.database.url is None

    assert config.encoder.type == "sbert"
    assert config.encoder.device == "cpu"
    assert (
        config.encoder.model == "sentence-transformers/paraphrase-MiniLM-L6-v2"
    )
    assert config.encoder.dimensions == 384
    assert config.encoder.precision == "float32"

    assert config.linker.type == "default"
    assert config.fuzz.scorer == "WRatio"


def test_config_save_load():
    with TemporaryDirectory() as temp_dir:
        config_path = Path(temp_dir) / "test_config.json"
        config = Config(path=config_path)
        config = config.apply(fuzz__scorer="QRatio")
        config.save()

        loaded_config = Config.load(config_path)
        assert loaded_config.linker.type == "default"  # default
        assert loaded_config.fuzz.scorer == "QRatio"  # nested override
