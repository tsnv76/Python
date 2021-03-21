class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'Наша матрица {self.matrix}'

    def __add__(self, other):
        return Matrix([[cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
                       for row_1, row_2 in zip(self.matrix, other.matrix)])


matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
mt1 = Matrix(matrix_1)
mt2 = Matrix(matrix_2)
print(mt1)
print(mt2)
print(mt1 + mt2)
