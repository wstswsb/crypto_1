from .bit_permutation_service import BitPermutationService
from .bit_computing_service import BitComputingService
from models import XlXrYlYr, AInputsOutputsC
from repositories import (
    AInputsOutputsCRepository,
    K_1_X_Repository,
)


class KeySearchService:
    def __init__(
            self,
            a_start_position: int,
            a_end_position: int,
            permutation_service: BitPermutationService,
            permutation_with_expand_service: BitPermutationService,
            bit_computing_service: BitComputingService,
            a_in_out_repository: AInputsOutputsCRepository,
            key_repository: K_1_X_Repository):
        self.a_start_position = a_start_position
        self.a_end_position = a_end_position
        self.permutation_service = permutation_service
        self.permutation_with_expand_service = permutation_with_expand_service
        self.bit_computing_service = bit_computing_service

        self.a_in_out_repository = a_in_out_repository
        self.key_repository = key_repository

    def find_last_keys(
            self,
            xy_1: XlXrYlYr,
            xy_2: XlXrYlYr,
            c_start_position: int,
            c_end_position: int):
        fulL_c = self.permutation_service.reverse_permutation(xy_1.yl ^ xy_2.yl)
        c = self.bit_computing_service.get_slice(
            source=fulL_c,
            source_length=8,
            start=c_start_position,
            end=c_end_position,
        )
        self.find_keys(xy_1.yr, xy_2.yr, c)

    def find_keys(
            self,
            num_1: int,
            num_2: int,
            c: int) -> None:
        expanded_num_1 = self.permutation_with_expand_service.permute(num_1)
        expanded_num_2 = self.permutation_with_expand_service.permute(num_2)
        self.find_s_block_keys(expanded_num_1, expanded_num_2, c)

    def find_s_block_keys(
            self,
            expanded_xr_1: int,
            expanded_xr_2: int,
            c: int) -> None:
        a_1 = self.bit_computing_service.get_slice(
            source=expanded_xr_1,
            source_length=12,
            start=self.a_start_position,
            end=self.a_end_position,
        )
        a_2 = self.bit_computing_service.get_slice(
            source=expanded_xr_2,
            source_length=12,
            start=self.a_start_position,
            end=self.a_end_position,
        )
        delta_a = a_1 ^ a_2
        a_in_out_c_list = self.a_in_out_repository \
            .find_by_a_and_c(delta_a, c)
        keys = self.generate_keys(a_1, a_2, a_in_out_c_list)
        self.key_repository.insert_many(keys)

    def generate_keys(
            self,
            a_1: int,
            a_2: int,
            a_in_out_c_list: list[AInputsOutputsC]) -> list[int]:
        keys: list[int] = []
        for a_in_out_c in a_in_out_c_list:
            keys.append(a_1 ^ a_in_out_c.input_1)
        return keys

    def _get_s_block_a(self, expanded_xr: int) -> int:
        return self.bit_computing_service.get_slice(
            source=expanded_xr,
            source_length=12,
            start=0,
            end=4,
        )
