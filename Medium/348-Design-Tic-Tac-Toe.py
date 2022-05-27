class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for i in range(n)] for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if self.board[row] == [player]*len(self.board[0]):
            print("row")
            return player
        count = 0
        for i in range(len(self.board)):
            if self.board[i][col] == player:
                count += 1
        if count == len(self.board):
            print("col")
            return player
        count = 0
        if row+col==len(self.board)-1:
            for i in range(len(self.board)):
                if self.board[i][len(self.board)-1-i] == player:
                    count += 1
        if count == len(self.board):
            print("diag1")
            return player
        count = 0
        if row-col==0:
            for i in range(len(self.board)):
                if self.board[i][i] == player:
                    count += 1
        if count == len(self.board):
            print("diag2")
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)