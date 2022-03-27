import json

from s_block import SBlock2Rows8Columns, SBlock4Rows4Columns
from exceptions import InvalidSBlockFileException


class SBlockReader:
    def __init__(self, path_resources: str):
        self.path_resources = path_resources

    def read(self, filename: str):
        matrix = self.read_matrix(filename)
        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])

        if number_of_rows == 2 and number_of_columns == 8:
            return SBlock2Rows8Columns(matrix)

        if number_of_rows == number_of_columns == 4:
            return SBlock4Rows4Columns(matrix)

        raise InvalidSBlockFileException()

    def read_matrix(self, filename: str) -> list[list[int]]:
        with open(f"{self.path_resources}/{filename}", "r") as file:
            matrix = json.load(file)
        return matrix
