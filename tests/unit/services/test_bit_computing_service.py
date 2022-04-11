from services import BitComputingService


class TestBitComputingService:
    def setup(self):
        self.service = BitComputingService()

    def test_get_slice_case_1(self):
        source = 0b0011_1100_0101
        bit_slice = self.service.get_slice(
            source=source,
            source_length=12,
            start=3,
            end=7,
        )
        assert bit_slice == 0b1111

    def test_get_slice_case_2(self):
        source = 0b0000_1111_1111
        bit_slice = self.service.get_slice(
            source=source,
            source_length=12,
            start=1,
            end=4,
        )
        assert bit_slice == 0b0000

    def test_get_slice_case_3(self):
        source = 0b1111_0000_1010
        bit_slice = self.service.get_slice(
            source=source,
            source_length=12,
            start=9,
            end=13,
        )
        assert bit_slice == 0b1010

    def test_get_bit_by_position_one(self):
        sources = [
            0b1000_0000, 0b0100_0000, 0b0010_0000, 0b0001_0000,
            0b0000_1000, 0b0000_0100, 0b0000_0010, 0b0000_0001,
        ]

        bit_length = 8
        for index, source in enumerate(sources):
            position = index + 1
            result = self.service.get_by_position(
                position=position,
                source=source,
                source_length=bit_length,
            )
            assert result == 1

    def test_get_bit_by_position_zero(self):
        sources = [
            0b0111_1111, 0b1011_1111, 0b1101_1111, 0b1110_1111,
            0b1111_0111, 0b1111_1011, 0b1111_1101, 0b1111_1110,
        ]
        bit_length = 8
        for index, source in enumerate(sources):
            position = index + 1
            result = self.service.get_by_position(
                position=position,
                source=source,
                source_length=bit_length,
            )
            assert result == 0

    def test_get_bit_by_position_bit_size_12(self):
        result = self.service.get_by_position(
            position=12,
            source=0b0000_0000_0001,
            source_length=12
        )
        assert result == 1

    def test_create_continuous_bit_mask(self):
        expected_bitmasks = [
            0b0000_0000, 0b0000_0001, 0b0000_0011,
            0b0000_0111, 0b0000_1111, 0b0001_1111,
            0b0011_1111, 0b0111_1111, 0b1111_1111,

        ]
        for length, expected_mask in enumerate(expected_bitmasks):
            assert self.service.create_continuous_mask(length) == expected_mask

    def test_calculate_ones_mask_with_zero_bit_at_position(self):
        expected_bitmasks = [
            0b0111_1111, 0b1011_1111, 0b1101_1111, 0b1110_1111,
            0b1111_0111, 0b1111_1011, 0b1111_1101, 0b1111_1110,
        ]

        for index, expected_bitmask in enumerate(expected_bitmasks):
            position = index + 1
            result = self.service.calculate_ones_mask_with_bit_at_position(
                position=position,
                bit=0,
                bit_length=8
            )
            assert result == expected_bitmask

    def test_calculate_ones_mask_with_one_bit_at_position(self):
        result = [
            self.service.calculate_ones_mask_with_bit_at_position(
                position=position,
                bit=1,
                bit_length=8
            )
            for position
            in range(1, 9)
        ]
        assert set(result) == {0b1111_1111}

    def test_calculate_zeros_mask_with_zero_bit_at_position(self):
        result = [
            self.service.calculate_zeros_mask_with_bit_at_position(
                position=position,
                bit=0,
                bit_length=8,
            )
            for position
            in range(1, 9)
        ]
        assert set(result) == {0b0000_0000}

    def test_calculate_zeros_mask_with_one_bit_at_position(self):
        expected_bitmasks = [
            0b1000_0000, 0b0100_0000, 0b0010_0000, 0b0001_0000,
            0b0000_1000, 0b0000_0100, 0b0000_0010, 0b0000_0001,
        ]
        for index, expected_bitmask in enumerate(expected_bitmasks):
            position = index + 1
            result = self.service.calculate_zeros_mask_with_bit_at_position(
                position=position,
                bit=1,
                bit_length=8,
            )
            assert result == expected_bitmask

    def test_set_one_bit_at_position(self):
        expected_bitmasks = [
            0b1000_0000, 0b0100_0000, 0b0010_0000, 0b0001_0000,
            0b0000_1000, 0b0000_0100, 0b0000_0010, 0b0000_0001,
        ]
        for index, expected_bitmask in enumerate(expected_bitmasks):
            position = index + 1
            result = self.service.set_at_position(
                position=position,
                bit=1,
                destination=0b0000_0000,
                destination_bit_length=8
            )
            assert result == expected_bitmask

    def test_set_zero_bit_at_position(self):
        expected_bitmasks = [
            0b0111_1111, 0b1011_1111, 0b1101_1111, 0b1110_1111,
            0b1111_0111, 0b1111_1011, 0b1111_1101, 0b1111_1110,
        ]
        for index, expected_bitmask in enumerate(expected_bitmasks):
            position = index + 1
            result = self.service.set_at_position(
                position=position,
                bit=0,
                destination=0b1111_1111,
                destination_bit_length=8,
            )
            assert result == expected_bitmask

    def test_merge_nums(self):
        first = 0b1111
        second = 0b0000
        third = 0b0011
        result = self.service.merge_nums(4, nums=[first, second, third])
        assert result == 0b1111_0000_0011
