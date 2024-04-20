import os.path
from pathlib import Path
from typing import Union, Optional

from pydantic import BaseModel, Field

from vokab import Config, Request, Response


class Collection(BaseModel):
    path: Path
    config: Config = Field(..., default_factory=Config)

    _admin = None
    _database = None
    _encoder = None
    _fuzz = None
    _linker = None
    _reranker = None

    def __call__(self, q: Union[Request, str], **kwargs) -> Response:
        if isinstance(q, str):
            request = Request(term=q, **kwargs)
        else:
            request = q.model_copy(update=kwargs)

        request.linker = request.linker or self.config.linker.type
        linker = self.get_linker(class_type=request.linker)
        return linker(request)

    def update(self, **updates):
        self.config = self.config.apply(**updates)
        self.config.save()

    @classmethod
    def load(cls, path: Union[str, Path]) -> "Collection":
        full_path = Path(os.path.expanduser(path))
        full_path.mkdir(parents=True, exist_ok=True)

        collection = Collection(path=full_path)
        collection.config = Config.load(collection.config_path)
        return collection

    @property
    def config_path(self):
        return self.path / "terms.json"

    @property
    def encoder(self):
        if self._encoder is None:
            from .encoders import AbstractEncoder

            self._encoder = AbstractEncoder.construct(self)
        return self._encoder

    @property
    def database(self):
        if self._database is None:
            from .databases import AbstractDatabase

            self._database = AbstractDatabase.construct(self)
        return self._database

    @property
    def fuzz(self):
        if self._fuzz is None:
            from .fuzz import AbstractFuzz

            self._fuzz = AbstractFuzz.construct(self)
        return self._fuzz

    @property
    def reranker(self):
        if self._reranker is None:
            from .rerankers import AbstractReranker

            self._reranker = AbstractReranker.construct(self)
        return self._reranker

    @property
    def linker(self):
        if self._linker is None:
            self._linker = self.get_linker()
        return self._linker

    def get_linker(self, class_type: Optional[str] = None):
        from .linkers import AbstractLinker

        return AbstractLinker.construct(self, class_type=class_type)
