class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        fin_row, fin_col = len(grid)-1, len(grid[0])-1
        if grid[fin_row][fin_col] == 1 or grid[0][0] == 1:
            return -1
        queue = [(0,0,1)]
        while queue:
            row, col, length = queue.pop(0)
            if row == fin_row and col == fin_col:
                return length
            for x,y in ((row-1,col-1),(row-1,col),(row-1,col+1),(row,col-1),(row,col+1),(row+1,col-1),(row+1,col),(row+1,col+1)):
                if 0<=x<=fin_row and 0<=y<=fin_col and grid[x][y]!=1:
                    grid[x][y] = 1
                    queue.append((x, y, length+1))
        return -1