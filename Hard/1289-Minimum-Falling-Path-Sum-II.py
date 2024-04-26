from typing import List
class Solution:
    # def minFallingPathSum(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     dp = {}
    #     mini = float('inf')
    #     for col in range(n):
    #         mini = min(mini, self.dfs(grid, 0, col, dp))
    #     return mini
    
    # def dfs(self, grid, x, y, dp):
    #     if x == len(grid)-1:
    #         return grid[x][y]
    #     if (x, y) in dp:
    #         return dp[(x, y)]
    #     mini = float('inf')
    #     for col in range(len(grid[0])):
    #         if col != y:
    #             mini = min(mini, self.dfs(grid, x+1, col, dp))
    #     dp[(x, y)] = mini + grid[x][y]
    #     return dp[(x, y)]

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[n-1][i] = grid[n-1][i]
        for i in range(n-2, -1, -1):
            for j in range(n):
                mini = float('inf')
                for k in range(n):
                    if k != j:
                        mini = min(mini, dp[i+1][k])
                dp[i][j] = mini + grid[i][j]
        return min(dp[0])