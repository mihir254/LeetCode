from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        self.placeNQueens(0, set(), set(), set(), [["."]*n for _ in range(n)], answer, n)
        return answer
        
    def placeNQueens(self, row, colSet, diag1Set, diag2Set, board, answer, n):
        if row >= n:
            answer.append(["".join(row) for row in board])
            return

        for col in range(n):
            if (col in colSet) or (row+col in diag1Set) or (row-col in diag2Set):
                continue

            colSet.add(col)
            diag1Set.add(row+col)
            diag2Set.add(row-col)
            board[row][col] = "Q"

            self.placeNQueens(row+1, colSet, diag1Set, diag2Set, board, answer, n)

            colSet.remove(col)
            diag1Set.remove(row+col)
            diag2Set.remove(row-col)
            board[row][col] = "."