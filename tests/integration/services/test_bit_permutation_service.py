from structure import (
    bit_permutation_service_expand,
    bit_permutation_service,
)


class TestBitPermutationService:
    def setup(self):
        self.permutation = [8, 7, 3, 2, 5, 4, 1, 6]
        self.block_bit_size = 8

        self.service = bit_permutation_service
        self.service.permutation = self.permutation
        self.service.block_bit_size = self.block_bit_size

    def test_do_bit_permutation_zeros_block(self):
        block = 0b0000_0000
        assert self.service.do_bit_permutation(block) == 0

    def test_do_bit_permutation_ones_block(self):
        block = 0b1111_1111
        assert self.service.do_bit_permutation(block) == 0b1111_1111

    def test_do_bit_permutation_case_1(self):
        block = 0b0000_1111
        assert self.service.do_bit_permutation(block) == 0b1100_1001

    def test_do_bit_permutation_case_2(self):
        block = 0b1111_0000
        assert self.service.do_bit_permutation(block) == 0b0011_0110

    def test_do_bit_permutation_case_3(self):
        block = 0b0101_0101
        assert self.service.do_bit_permutation(block) == 0b1001_0101

    def test_do_bit_permutation_case_4(self):
        block = 0b1010_1010
        assert self.service.do_bit_permutation(block) == 0b0110_1010


class TestBitPermutationWithExpansionService:
    def setup(self):
        self.permutation = [7, 6, 3, 8, 4, 5, 1, 2, 4, 7, 6, 1]
        self.source_block_bit_size = 8
        self.result_block_bit_size = 12

        self.service = bit_permutation_service_expand
        self.service.permutation = self.permutation
        self.service.block_bit_size = self.source_block_bit_size

    def test_do_bit_permutation_ones_block(self):
        block = 0b1111_1111
        assert self.service.do_bit_permutation(block) == 0b1111_1111_1111

    def test_do_bit_permutation_zeros_block(self):
        block = 0b0000_0000
        assert self.service.do_bit_permutation(block) == 0

    def test_do_bit_permutation_case_1(self):
        block = 0b1010_1010
        assert self.service.do_bit_permutation(block) == 0b1010_0110_0101

    def test_do_bit_permutation_case_2(self):
        block = 0b1111_0000
        assert self.service.do_bit_permutation(block) == 0b0010_1011_1001

    def test_do_bit_permutation_case_3(self):
        block = 0b0111_1110
        assert self.service.do_bit_permutation(block) == 0b1110_1101_1110

    def test_reverse_bit_permutation_case_1(self):
        block = 0b1010_0110_0101
        assert self.service.reverse_bit_permutation(block) == 0b1010_1010

    def test_reverse_bit_permutation_case_2(self):
        block = 0b0010_1011_1001
        assert self.service.reverse_bit_permutation(block) == 0b1111_0000

    def test_reverse_bit_permutation_case_3(self):
        block = 0b1110_1101_1110
        assert self.service.reverse_bit_permutation(block) == 0b0111_1110
