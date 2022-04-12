class Solution:
    def gameOfLife(self, board) -> None:
        temp = []
        for i in range(len(board)):
            temp.append([])
            for j in range(len(board[0])):
                score = self.checker(i-1, j-1, board) + self.checker(i-1, j, board) + self.checker(i-1, j+1, board) + self.checker(i, j-1, board) + self.checker(i, j+1, board) + self.checker(i+1, j-1, board) + self.checker(i+1, j, board) + self.checker(i+1, j+1, board)
                if board[i][j] == 1:
                    if score < 2 or score > 3:
                        temp[i].append(0)
                    else:
                        temp[i].append(1)
                else:
                    if score == 3:
                        temp[i].append(1)
                    else:
                        temp[i].append(0)
        board[:] = temp[:]
        
        
    def checker(self, row, column, board):
        if row<0 or row>len(board)-1 or column<0 or column>len(board[0])-1 or board[row][column]==0:
            return 0
        return 1