class Solution:
    def removeStones(self, stones: int) -> int:
        visited = set()
        count = 0
        for stone in stones:
            if tuple(stone) not in visited:
                self.dfs(stone, stones, visited)
                count += 1
        return len(stones)-count
    def dfs(self, node, graph, visited):
        visited.add(tuple(node))
        neighbours = []
        for point in graph:
            if tuple(point) not in visited and (point[0] == node[0] or point[1] == node[1]):
                neighbours.append(point)
        for neighbour in neighbours:
            self.dfs(neighbour, graph, visited)