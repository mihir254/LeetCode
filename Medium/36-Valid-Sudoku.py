from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = {}, {}, {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                number = int(board[i][j])
                if i not in row:
                    row[i] = set()
                if j not in col:
                    col[j] = set()
                if str(i//3)+str(j//3) not in box:
                    box[str(i//3)+str(j//3)] = set()
                if number in row[i] or number in col[j] or number in box[str(i//3)+str(j//3)]:
                    return False
                row[i].add(number)
                col[j].add(number)
                box[str(i//3)+str(j//3)].add(number)
        return True