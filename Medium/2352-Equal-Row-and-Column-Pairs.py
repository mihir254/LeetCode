class Solution:
    def equalPairs(self, grid) -> int:
        colMap = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j not in colMap:
                    colMap[j] = []
                colMap[j].append(grid[i][j])
        cols = colMap.values()
        rows = [x for x in grid]
        count = 0
        for col in cols:
            for row in rows:
                if col == row:
                    count += 1
        return count