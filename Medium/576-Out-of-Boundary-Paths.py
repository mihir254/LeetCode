class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        grid = []
        for x in range(m):
            grid.append([])
            for y in range(n):
                grid[x].append([])
                for z in range(maxMove+1):
                    grid[x][y].append(-1)
        wez = self.recursion(grid, maxMove, startRow, startColumn)
        return wez % (10**9 + 7)
    
    def recursion(self, grid, moves, x, y):
        if moves < 0:
            return 0
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return 1
        if grid[x][y][moves] != -1:
            return grid[x][y][moves]
        ways = 0
        ways += self.recursion(grid, moves-1, x+1, y)
        ways += self.recursion(grid, moves-1, x-1, y)
        ways += self.recursion(grid, moves-1, x, y+1)
        ways += self.recursion(grid, moves-1, x, y-1)
        grid[x][y][moves] = ways
        return grid[x][y][moves]