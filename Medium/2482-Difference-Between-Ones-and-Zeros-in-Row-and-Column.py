from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if i == len(rows):
                    rows.append(0)
                if j == len(cols):
                    cols.append(0)
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = 2*rows[i] + 2*cols[j] - m - n
        return ans