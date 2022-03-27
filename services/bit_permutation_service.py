from collections import OrderedDict

from .bit_computing_service import BitComputingService


class BitPermutationService:
    def __init__(
            self,
            permutation: list[int],
            bit_computing_service: BitComputingService,
            input_bit_size: int,
            output_bit_size: int):

        self.permutation = permutation
        self.bit_computing_service = bit_computing_service

        self.input_bit_size = input_bit_size
        self.output_bit_size = output_bit_size

    def do_bit_permutation(self, block: int) -> int:
        result = 0
        for index, position in enumerate(self.permutation):
            bit = self.bit_computing_service.get_bit_by_position(
                position=position,
                source=block,
                source_bit_length=self.input_bit_size
            )
            result = self.bit_computing_service.set_bit_at_position(
                position=index + 1,
                bit=bit,
                destination=result,
                destination_bit_length=self.output_bit_size,
            )
        return result

    def reverse_bit_permutation(self, block: int):
        unique_permutation = list(OrderedDict.fromkeys(self.permutation).keys())
        result = 0
        for index, position in enumerate(unique_permutation):
            bit = self.bit_computing_service.get_bit_by_position(
                position=index + 1,
                source=block,
                source_bit_length=self.output_bit_size,
            )
            result = self.bit_computing_service.set_bit_at_position(
                position=position,
                bit=bit,
                destination=result,
                destination_bit_length=self.input_bit_size,
            )
        return result
