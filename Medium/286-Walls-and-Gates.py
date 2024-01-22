from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gates = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gates.append((i, j))
        distance = 0
        while gates:
            distance += 1
            n = len(gates)
            for _ in range(n):
                x, y = gates.pop(0)
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    newX, newY = x+dx, y+dy
                    if newX >= 0 and newY >= 0 and newX < len(rooms) and newY < len(rooms[0]) and rooms[newX][newY] == 2147483647:
                        rooms[newX][newY] = distance
                        gates.append((newX, newY))