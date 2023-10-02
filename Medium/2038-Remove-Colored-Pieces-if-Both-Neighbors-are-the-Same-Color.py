class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, b = 0, 0
        running_a, running_b = 0, 0
        for i in range(len(colors)):
            if colors[i] == 'A':
                running_a += 1
                running_b = 0
                if running_a >= 3:
                    a += 1
            else:
                running_a = 0
                running_b += 1
                if running_b >= 3:
                    b += 1
        return a > b