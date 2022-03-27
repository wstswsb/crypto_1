from s_block import SBlock
from .bit_computing_service import BitComputingService
from repositories import AInputsOutputsCRepository, ProbabilityACRepository
from models import AInputsOutputsC, ProbabilityAC


class SBlockAnalyticsService:
    def __init__(
            self,
            s_block: SBlock,
            bit_computing_service: BitComputingService,
            a_inputs_outputs_c_repository: AInputsOutputsCRepository,
            probability_a_c_repository: ProbabilityACRepository):
        self.s_block = s_block
        self.bit_computing_service = bit_computing_service
        self.a_in_out_c_repository = a_inputs_outputs_c_repository
        self.probability_a_c_repository = probability_a_c_repository

        self.max_input = bit_computing_service.create_continuous_bitmask(s_block.input_bit_size)
        self.max_output = bit_computing_service.create_continuous_bitmask(s_block.output_bit_size)

    def analyze_s_block(self) -> ProbabilityAC:
        self.build_a_inputs_outputs_table()
        self.build_a_c_table()
        return self.find_most_probabilistic()

    def build_a_inputs_outputs_table(self):
        models = [
            self.generate_a_in_out_c(a, input_1)
            for a in range(self.max_input + 1)
            for input_1 in range(self.max_input + 1)
        ]
        self.a_in_out_c_repository.insert_many(models)

    def generate_a_in_out_c(self, a: int, input_1: int) -> AInputsOutputsC:
        input_2 = a ^ input_1
        output_1 = self.s_block.substitute(input_1)
        output_2 = self.s_block.substitute(input_2)
        c = output_1 ^ output_2
        return AInputsOutputsC(a, input_1, input_2, output_1, output_2, c)

    def build_a_c_table(self):
        for a in range(self.max_input + 1):
            probabilities_a_c = self.generate_probabilities_a_c(a)
            self.probability_a_c_repository.insert_many(probabilities_a_c)

    def generate_probabilities_a_c(self, a: int) -> list[ProbabilityAC]:
        models = self.a_in_out_c_repository.find_by_a(a)
        c_count = self.count_c(models)

        result = [
            ProbabilityAC(a, c, probability=c_count[c] / len(models))
            for c in range(self.max_output + 1)
        ]

        return result

    def count_c(self, models: list[AInputsOutputsC]) -> dict[int, int]:
        c_count = {c: 0 for c in range(self.max_output + 1)}
        for model in models:
            c_count[model.c] += 1
        return c_count

    def find_most_probabilistic(self) -> ProbabilityAC:
        items = self.probability_a_c_repository.find_four_most_probability()

        if items[0].probability == 1.0:
            items = items[1:]

        self.check_uniqueness_probability(items)
        return items[0]

    def check_uniqueness_probability(self, models: list[ProbabilityAC]):
        if len(models) < 2:
            return
        if models[0].probability == models[1].probability:
            print(models)
            raise Exception("Probability is not unique")
