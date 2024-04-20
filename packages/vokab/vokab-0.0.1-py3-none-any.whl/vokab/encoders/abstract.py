from abc import ABC, abstractmethod
from typing import List

from vokab import Collection, Strs, Vec, lazy


class AbstractEncoder(ABC):
    type_mapping = {
        "sbert": "vokab.encoders.SBertEncoder",
    }

    def __init__(self, collection: Collection):
        self.collection = collection

    def __call__(self, sentences: Strs) -> List[Vec]:
        return self.encode(sentences=sentences)

    @abstractmethod
    def encode(self, sentences: Strs) -> List[Vec]:
        pass

    def encode_one(self, sentence) -> Vec:
        vectors = self.encode([sentence])
        return vectors[0]

    @classmethod
    def construct(cls, collection: Collection) -> "AbstractEncoder":
        class_type = collection.config.encoder.type
        class_type = AbstractEncoder.type_mapping.get(class_type, class_type)
        return lazy.create(AbstractEncoder, class_type, collection=collection)
