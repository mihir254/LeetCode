class Solution:
    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [4, 2],
    }
    store = {}
    def knightDialer(self, n: int) -> int:
        answer = 0
        for i in range(10):
            x = self.path(i, n-1)
            answer += x
        return answer % (10**9 + 7)
    def path(self, position, stepsLeft):
        if (position, stepsLeft) in self.store:
            return self.store[(position, stepsLeft)]
        if stepsLeft == 0:
            return 1
        nextPositions = self.moves[position]
        paths = 0
        for pos in nextPositions:
            paths += self.path(pos, stepsLeft-1)
        self.store[(position, stepsLeft)] = paths
        return paths