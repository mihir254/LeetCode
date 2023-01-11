class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        hashset = set([vertex for vertex in range(len(hasApple)) if hasApple[vertex]])
        graph = self.createGraph(edges)
        visited = set()
        answer = self.helper(graph, hashset, visited, 0, 0)
        return answer
    def helper(self, graph, hashset, visited, time_to_reach, node):
        visited.add(node)
        neighbours = graph.get(node)
        time_from_children = 0
        for neighbour in neighbours:
            if neighbour not in visited:
                time_from_children += self.helper(graph, hashset, visited, 2, neighbour)
        return (time_to_reach + time_from_children) if (node in hashset or time_from_children > 0) else 0
    def createGraph(self, edges):
        graph = {}
        for edge in edges:
            v1, v2 = edge
            if v1 not in graph:
                graph[v1] = []
            if v2 not in graph:
                graph[v2] = []
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph