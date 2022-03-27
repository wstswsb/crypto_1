from s_block import SBlock2Rows8Columns, SBlock4Rows4Columns


class TestSBlock2Rows8Columns:
    def setup(self):
        self.matrix = [
            [0, 1, 2, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 2, 1, 0],
        ]
        self.s_block = SBlock2Rows8Columns(self.matrix)

    def test_substitute_zero_row(self):
        block = 0b0111
        assert self.s_block.substitute(block) == self.matrix[0][7]

    def test_substitute_first_row(self):
        block = 0b1001
        assert self.s_block.substitute(block) == self.matrix[1][1]

    def test_number_of_rows(self):
        assert self.s_block.number_of_rows == 2

    def test_number_of_columns(self):
        assert self.s_block.number_of_columns == 8

    def test_calculate_row_index_zero(self):
        assert self.s_block.calculate_row_index(0b0000) == 0

    def test_calculate_row_index_one(self):
        assert self.s_block.calculate_row_index(0b1000) == 1

    def test_calculate_column_index(self):
        assert self.s_block.calculate_column_index(0b0000) == 0b0
        assert self.s_block.calculate_column_index(0b0001) == 0b001
        assert self.s_block.calculate_column_index(0b0011) == 0b011
        assert self.s_block.calculate_column_index(0b0111) == 0b111


class TestSBlock4Rows4Columns:
    def setup(self):
        self.matrix = [
            [0, 1, 2, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 2, 1, 0],
        ]
        self.s_block = SBlock4Rows4Columns(self.matrix)

    def test_calculate_row_index_zero(self):
        assert self.s_block.calculate_row_index(0b0000) == 0

    def test_calculate_row_index_one(self):
        assert self.s_block.calculate_row_index(0b0001) == 1

    def test_calculate_row_index_two(self):
        assert self.s_block.calculate_row_index(0b1000) == 2

    def test_calculate_row_index_three(self):
        assert self.s_block.calculate_row_index(0b1001) == 3

    def test_calculate_column_index_zero(self):
        assert self.s_block.calculate_column_index(0b0000) == 0

    def test_calculate_column_index_one(self):
        assert self.s_block.calculate_column_index(0b0010) == 1

    def test_calculate_column_index_two(self):
        assert self.s_block.calculate_column_index(0b0100) == 2

    def test_calculate_column_index_three(self):
        assert self.s_block.calculate_column_index(0b0110) == 3
