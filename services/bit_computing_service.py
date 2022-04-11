from exceptions import InvalidBitPositionException


class BitComputingService:
    def get_slice(
            self,
            source: int,
            source_length: int,
            start: int,
            end: int) -> int:
        # min start = 1
        right_shift = source_length - end + 1
        mask = self.create_continuous_mask(end - start)
        return (source >> right_shift) & mask

    def get_by_position(
            self,
            position: int,
            source: int,
            source_length: int) -> int:

        self.validate_position(position, source_length)
        result = source >> (source_length - position) & 1
        return result

    def create_continuous_mask(self, length: int) -> int:
        result = 0
        for i in range(length):
            result |= 2 ** i
        return result

    def calculate_ones_mask_with_bit_at_position(
            self,
            position: int,
            bit: int,
            bit_length: int) -> int:
        self.validate_position(position, bit_length)

        mask = self.create_continuous_mask(bit_length)
        if bit == 1:
            return mask

        return (mask ^ (1 << (bit_length - position))) & mask

    def calculate_zeros_mask_with_bit_at_position(
            self,
            position: int,
            bit: int,
            bit_length: int) -> int:

        self.validate_position(position, bit_length)
        if bit == 0:
            return 0
        return 1 << (bit_length - position)

    def set_at_position(
            self,
            position: int,
            bit: int,
            destination: int,
            destination_bit_length: int) -> int:

        result_bitmask = self.create_continuous_mask(destination_bit_length)
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

    def validate_position(
            self,
            position: int,
            length_constraint: int) -> None:

        if position < 1 or position > length_constraint:
            error = f"{position = }\n{length_constraint = }"
            raise InvalidBitPositionException(error)

    def merge_nums(self, num_bit_length: int, nums: list[int]):
        result = 0
        for index, num in enumerate(nums):
            correction = index + 1
            result |= (num << (num_bit_length * (len(nums) - correction)))
        return result

    def merge_c(self, c_1: int, c_2: int, c_3: int):
        result = c_1 << 5
        result |= c_2 << 2
        result |= c_3
        return result
