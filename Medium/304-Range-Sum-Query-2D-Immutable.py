class NumMatrix:

    def __init__(self, matrix):
        row, col = len(matrix), len(matrix[0])
        self.matrix = [[0]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    self.matrix[0][0] = matrix[0][0]
                elif i == 0 and j >= 1:
                    self.matrix[i][j] = matrix[i][j] + self.matrix[i][j-1]
                elif i >= 1 and j == 0:
                    self.matrix[i][j] = matrix[i][j] + self.matrix[i-1][j]
                else:
                    self.matrix[i][j] = matrix[i][j] + self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]
        if row > 1 and col > 1:
            self.matrix[row-1][col-1] = matrix[row-1][col-1] + self.matrix[row-2][col-1] + self.matrix[row-1][col-2] - self.matrix[row-2][col-2]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 >= 1 and col1 >= 1:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1] - self.matrix[row1-1][col2] + self.matrix[row1-1][col1-1]
        elif row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0 and col1 >= 1:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        elif row1 >= 1 and col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]