import json

from models import ProbabilityAC


class ProbabilityACPresenter:
    def present(self, model: ProbabilityAC) -> str:
        return json.dumps({
            "delta_a": model.a,
            "delta_c": model.c,
            "probability": model.probability,
        }, indent=4)
