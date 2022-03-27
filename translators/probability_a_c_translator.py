from typing import Union
from .base_translator import BaseTranslator
from models import ProbabilityAC


class ProbabilityACTranslator(BaseTranslator):
    def to_dict(self, model: ProbabilityAC) -> dict[str, Union[int, float]]:
        return {
            "a": model.a,
            "c": model.c,
            "probability": model.probability
        }

    def from_db_tuple(self, db_tuple: tuple[Union[int, float]]):
        return ProbabilityAC(*db_tuple)
