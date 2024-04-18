from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self.dfs(i, j, grid, 0)
        return 0
    def dfs(self, x, y, grid, perimeter):
        grid[x][y] = -1
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] == 0:
                perimeter += 1
            elif grid[nx][ny] == 1:
                perimeter += self.dfs(nx, ny, grid, 0)
        return perimeter