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

    def permute(self, block: int) -> int:
        result = 0
        for index, position in enumerate(self.permutation):
            bit = self.bit_computing_service.get_by_position(
                position=position,
                source=block,
                source_length=self.input_bit_size
            )
            result = self.bit_computing_service.set_at_position(
                position=index + 1,
                bit=bit,
                destination=result,
                destination_bit_length=self.output_bit_size,
            )
        return result

    def reverse_permutation(self, block: int):
        permutation = self.__calculate_unique_permutation()
        result = 0
        for index, position in enumerate(permutation):
            bit = self.bit_computing_service.get_by_position(
                position=index + 1,
                source=block,
                source_length=self.output_bit_size,
            )
            result = self.bit_computing_service.set_at_position(
                position=position,
                bit=bit,
                destination=result,
                destination_bit_length=self.input_bit_size,
            )
        return result

    def __calculate_unique_permutation(self):
        return list(OrderedDict.fromkeys(self.permutation).keys())
