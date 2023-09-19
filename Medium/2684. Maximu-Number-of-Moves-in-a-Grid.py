from typing import List
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        store = {}
        answer = 0
        for i in range(len(grid)):
            store[i] = []
            for j in range(len(grid[0])):
                store[i].append(-1)
        for i in range(len(grid)):
            ans = self.recursion(i, 0, grid, store, answer)
            if ans == len(grid[0])-1:
                return ans
            answer = max(answer, ans)
        return answer
    def recursion(self, position, steps, matrix, store, answer):
        if position in store:
            if store[position][steps] > -1:
                return store[position][steps]
        if steps == len(matrix[0])-1:
            store[position][steps] = 0
            return 0
        possibleRoutes = [-1, 0, 1]
        best = 0
        for route in possibleRoutes:
            newPos = position+route
            if newPos >= 0 and newPos < len(matrix) and matrix[newPos][steps+1] > matrix[position][steps]:
                ans = 1 + self.recursion(newPos, steps+1, matrix, store, answer)
                best = max(best, ans)
        store[position][steps] = best
        return store[position][steps]