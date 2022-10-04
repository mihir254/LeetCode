class Solution:
    def findLonelyPixel(self, picture):
        row_set, col_set = set(), set()
        checked_row, checked_col = set(), set()
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B" and i not in row_set and i not in checked_row:
                    row_set.add(i)
                elif picture[i][j] == "B" and i in row_set:
                    row_set.remove(i)
                    checked_row.add(i)
                if picture[i][j] == "B" and j not in col_set and j not in checked_col:
                    col_set.add(j)
                elif picture[i][j] == "B" and j in col_set:
                    col_set.remove(j)
                    checked_col.add(j)
        if not row_set or not col_set:
            return 0
        count = 0
        for row in row_set:
            for col in col_set:
                if picture[row][col] == "B":
                    count += 1
        return count