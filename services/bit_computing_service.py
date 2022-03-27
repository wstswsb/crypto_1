from exceptions import InvalidBitPositionException


class BitComputingService:
    def get_bit_by_position(self, position: int, source: int, source_bit_length: int) -> int:
        self.validate_position(position, source_bit_length)

        result = source >> (source_bit_length - position) & 1
        return result

    def create_continuous_bitmask(self, bit_length: int) -> int:
        result = 0
        for i in range(bit_length):
            result |= 2 ** i
        return result

    def calculate_ones_mask_with_bit_at_position(
            self,
            position: int,
            bit: int,
            bit_length: int) -> int:
        self.validate_position(position, bit_length)

        result_bitmask = self.create_continuous_bitmask(bit_length)
        if bit == 1:
            return result_bitmask

        return (result_bitmask ^ (1 << (bit_length - position))) & result_bitmask

    def calculate_zeros_mask_with_bit_at_position(
            self,
            position: int,
            bit: int,
            bit_length: int) -> int:

        self.validate_position(position, bit_length)
        if bit == 0:
            return 0
        return 1 << (bit_length - position)

    def set_bit_at_position(
            self,
            position: int,
            bit: int,
            destination: int,
            destination_bit_length: int) -> int:

        result_bitmask = self.create_continuous_bitmask(destination_bit_length)
        if bit == 0:
            position_mask = self.calculate_ones_mask_with_bit_at_position(
                position,
                bit,
                destination_bit_length,
            )
            return destination & position_mask & result_bitmask

        if bit == 1:
            position_mask = self.calculate_zeros_mask_with_bit_at_position(
                position,
                bit,
                destination_bit_length,
            )
            return (destination | position_mask) & result_bitmask

    def validate_position(self, position: int, position_length_constraint: int):
        if position < 1 or position > position_length_constraint:
            error = f"{position = }\n{position_length_constraint = }"
            raise InvalidBitPositionException(error)
