from sentence_transformers import SentenceTransformer

from . import AbstractEncoder


class SBertEncoder(AbstractEncoder):
    name = "sbert"

    def __init__(self, collection):
        super().__init__(collection)
        self._model = None

    @property
    def model(self):
        if self._model is None:
            self._model = SentenceTransformer(
                model_name_or_path=self.collection.config.encoder.model,
                device=self.collection.config.encoder.device,
            )
        return self._model

    def encode(self, sentences):
        return self.model.encode(
            sentences,
            device=self.collection.config.encoder.device,
            precision=self.collection.config.encoder.precision,
        )
