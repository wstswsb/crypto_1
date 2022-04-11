from .s_block_analytics_service import SBlockAnalyticsService
from .bit_permutation_service import BitPermutationService
from .bit_computing_service import BitComputingService


class FAnalyticsService:
    def __init__(
            self,
            s_input_bit_length: int,
            s_1_analytics_service: SBlockAnalyticsService,
            s_2_analytics_service: SBlockAnalyticsService,
            s_3_analytics_service: SBlockAnalyticsService,
            permutation_service: BitPermutationService,
            computing_service: BitComputingService):
        self.s_input_bit_length = s_input_bit_length
        self.s_1_analytics_service = s_1_analytics_service
        self.s_2_analytics_service = s_2_analytics_service
        self.s_3_analytics_service = s_3_analytics_service
        self.permutation_service = permutation_service
        self.computing_service = computing_service

    def find_delta_x_right(self):
        most_probables = [
            self.s_1_analytics_service.compute_most_probabilistic()[0],
            self.s_2_analytics_service.compute_most_probabilistic()[0],
            self.s_3_analytics_service.compute_most_probabilistic()[0],
        ]
        expanded_x = self.computing_service.merge_nums(
            num_bit_length=self.s_input_bit_length,
            nums=[mp.a for mp in most_probables]
        )
        print(f"{expanded_x = :>012b}")
        delta_x = self.permutation_service.reverse_permutation(expanded_x)
        return delta_x
