class Solution:
    def generateMatrix(self, n: int):
        mat = [[0]*n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            mat[i][j] = k + 1
            if mat[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return mat