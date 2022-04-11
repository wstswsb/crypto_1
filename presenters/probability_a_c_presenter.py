import json

from models import ProbabilityAC


class ProbabilityACPresenter:
    def present(self, model: ProbabilityAC) -> str:
        return json.dumps({
            "delta_a": f"{model.a:>04b}",
            "delta_c": f"{model.c:>04b}",
            "probability": model.probability,
        }, indent=4)
