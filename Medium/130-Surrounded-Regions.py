from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            self.dfs(i, 0, board, visited)
            self.dfs(i, n-1, board, visited)
        for i in range(n):
            self.dfs(0, i, board, visited)
            self.dfs(m-1, i, board, visited)
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"
    
    def dfs(self, x, y, mat, visited):
        if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]) or (x, y) in visited or mat[x][y] != "O":
            return
        visited.add((x, y))
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        mat[x][y] = ""
        for dx, dy in neighbours:
            self.dfs(x+dx, y+dy, mat, visited)
        mat[x][y] = "O"