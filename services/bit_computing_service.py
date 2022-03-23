from exceptions import InvalidBitPositionException


class BitComputingService:
    def __init__(self, source_bit_length: int):
        self.source_bit_length = source_bit_length
        self.source_bit_mask = self.create_continuous_bitmask(self.source_bit_length)

    def get_bit_by_position(self, position: int, source: int) -> int:

        if position > self.source_bit_length:
            raise InvalidBitPositionException()
        bitmask = self.calculate_zeros_mask_with_bit_at_position(position, 1)
        return 1 if source & bitmask else 0

    def create_continuous_bitmask(self, bit_length: int) -> int:
        result = 0
        for i in range(bit_length):
            result |= 2 ** i
        return result

    def calculate_ones_mask_with_bit_at_position(self, position: int, bit: int) -> int:
        result = self.create_continuous_bitmask(self.source_bit_length)
        if bit == 0:
            result ^= (1 << (self.source_bit_length - position))
        return result & self.source_bit_mask

    def calculate_zeros_mask_with_bit_at_position(self, position: int, bit: int) -> int:
        result = self.create_continuous_bitmask(self.source_bit_length)
        if bit == 0:
            return 0
        xor_addend = self.calculate_ones_mask_with_bit_at_position(position, 0)
        return (result ^ xor_addend) & self.source_bit_mask

    def set_bit_at_position(
            self,
            position: int,
            bit: int,
            source: int) -> int:

        position_mask = self.calculate_ones_mask_with_bit_at_position(position, bit)
        return source & position_mask & self.source_bit_mask
