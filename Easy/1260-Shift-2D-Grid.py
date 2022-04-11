class Solution:
    def shiftGrid(self, grid, k: int):
        for _ in range(k):
            temp = grid[-1][-1]
            for i in range(len(grid)):
                x = grid[i][-1]
                grid[i][1:] = grid[i][:-1]
                grid[i][0] = temp
                temp = x
        return grid