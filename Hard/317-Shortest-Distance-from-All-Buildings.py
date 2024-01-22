from typing import List
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        store = {}
        buildings = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    buildings.append((i, j))
        distance = -1
        for bx, by in buildings:
            visited = set()
            queue = [[(bx,by), 0]]
            while queue:
                node, dist = queue.pop(0)
                if node in visited:
                    continue
                if grid[node[0]][node[1]] == 0:
                    if node not in store:
                        store[node] = [0, 0]
                    store[node][1] += dist
                    store[node][0] += 1
                visited.add(node)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newX, newY = node[0]+dx, node[1]+dy
                    if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) and ((newX, newY) not in visited) and (grid[newX][newY] == 0):
                        queue.append([(newX, newY), dist+1])
        for k,v in store.items():
            if v[0] == len(buildings):
                if distance == -1:
                    distance = v[1]
                else:
                    distance = min(distance, v[1])
        return distance