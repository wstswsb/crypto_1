from abc import ABC, abstractmethod


class SBlock(ABC):
    @property
    @abstractmethod
    def input_length(self) -> int:
        pass

    @property
    @abstractmethod
    def output_length(self) -> int:
        pass

    @property
    @abstractmethod
    def matrix(self) -> list[list[int]]:
        pass

    @property
    def number_of_columns(self) -> int:
        return len(self.matrix[0])

    @property
    def number_of_rows(self) -> int:
        return len(self.matrix)

    def substitute(self, replacement_block: int) -> int:
        row_index = self.calculate_row_index(replacement_block)
        column_index = self.calculate_column_index(replacement_block)
        return self.matrix[row_index][column_index]

    @abstractmethod
    def calculate_row_index(self, block: int) -> int:
        pass

    @abstractmethod
    def calculate_column_index(self, block: int) -> int:
        pass


class SBlock2Rows8Columns(SBlock):
    def __init__(self, matrix: list[list[int]]):
        self.__matrix = matrix
        self.__input_bit_size = 4
        self.__output_bit_size = 3

    @property
    def input_length(self) -> int:
        return self.__input_bit_size

    @property
    def output_length(self) -> int:
        return self.__output_bit_size

    @property
    def matrix(self):
        return self.__matrix

    def calculate_row_index(self, block: int) -> int:
        return (block >> 3) & 0b1

    def calculate_column_index(self, block: int) -> int:
        return block & 0b111


class SBlock4Rows4Columns(SBlock):
    def __init__(self, matrix: list[list[int]]):
        self.__matrix = matrix
        self.__input_bit_size = 4
        self.__output_bit_size = 2

    @property
    def input_length(self) -> int:
        return self.__input_bit_size

    @property
    def output_length(self) -> int:
        return self.__output_bit_size

    @property
    def matrix(self):
        return self.__matrix

    def calculate_row_index(self, block: int) -> int:
        return ((block & 0b1000) >> 2) | (block & 0b1)

    def calculate_column_index(self, block: int) -> int:
        return (block & 0b0110) >> 1
