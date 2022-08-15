class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in range(len(matrix)):
            for j in col:
                matrix[i][j] = 0