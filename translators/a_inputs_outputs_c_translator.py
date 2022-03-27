from models import AInputsOutputsC
from .base_translator import BaseTranslator


class AInputsOutputsCTranslator(BaseTranslator):
    def to_dict(self, model: AInputsOutputsC) -> dict[str, int]:
        return {
            "a": model.a,
            "input_1": model.input_1,
            "input_2": model.input_2,
            "output_1": model.output_1,
            "output_2": model.output_2,
            "c": model.c,
        }

    def from_db_tuple(self, db_tuple: tuple[int]) -> AInputsOutputsC:
        return AInputsOutputsC(*db_tuple)
