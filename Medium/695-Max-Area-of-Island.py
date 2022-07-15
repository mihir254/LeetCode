class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        count, n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = max(count, self.dfs(grid, (i, j), n, m))
        return count
    
    def dfs(self, mat, box, r, c):
        if box[0] < 0 or box[0] >= r or box[1] < 0 or box[1] >= c:
            return 0
        if mat[box[0]][box[1]] != 1:
            return 0
        mat[box[0]][box[1]] = -1
        neighbours = [(box[0]-1, box[1]), (box[0], box[1]-1), (box[0], box[1]+1), (box[0]+1, box[1])]
        cnt = 1
        for neighbour in neighbours:
            cnt += self.dfs(mat, neighbour, r, c)
        return cnt