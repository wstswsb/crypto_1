from services import BitComputingService


class TestBitComputingService:
    def setup(self):
        self.service = BitComputingService()

    def test_get_bit_by_position_one(self):
        sources = [
            0b1000_0000, 0b0100_0000, 0b0010_0000, 0b0001_0000,
            0b0000_1000, 0b0000_0100, 0b0000_0010, 0b0000_0001,
        ]

        bit_length = 8
        for index, source in enumerate(sources):
            position = index + 1
            result = self.service.get_bit_by_position(
                position=position,
                source=source,
                source_bit_length=bit_length,
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
            result = self.service.get_bit_by_position(
                position=position,
                source=source,
                source_bit_length=bit_length,
            )
            assert result == 0

    def test_get_bit_by_position_bit_size_12(self):
        result = self.service.get_bit_by_position(
            position=12,
            source=0b0000_0000_0001,
            source_bit_length=12
        )
        assert result == 1

    def test_create_continuous_bit_mask(self):
        expected_bitmasks = [
            0b0000_0000, 0b0000_0001, 0b0000_0011,
            0b0000_0111, 0b0000_1111, 0b0001_1111,
            0b0011_1111, 0b0111_1111, 0b1111_1111,

        ]
        for bit_length, expected_bitmask in enumerate(expected_bitmasks):
            assert self.service.create_continuous_bitmask(bit_length) == expected_bitmask

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
            result = self.service.set_bit_at_position(
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
            result = self.service.set_bit_at_position(
                position=position,
                bit=0,
                destination=0b1111_1111,
                destination_bit_length=8,
            )
            assert result == expected_bitmask
