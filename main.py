class SBlock:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
