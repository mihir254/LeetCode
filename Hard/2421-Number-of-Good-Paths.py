class Solution:
    def numberOfGoodPaths(self, vals, edges) -> int:
        graph = {}
        for edge in edges:
            v1, v2 = edge
            if v1 not in graph:
                graph[v1] = []
            if v2 not in graph:
                graph[v2] = []
            graph[v1].append(v2)
            graph[v2].append(v1)
        if edges:
            answer = 0
            completed = set()
            for i in range(len(vals)):
                visited = set()
                answer += self.dfs(i, i, visited, graph, vals, completed)
            return answer
        else:
            return 1
    def dfs(self, node, start, visited, graph, vals, completed):
        visited.add(node)
        result = 0
        if vals[node] == vals[start] and (node, start) not in completed and (start, node) not in completed:
            completed.add((start, node))
            result += 1
        neighbours = graph.get(node)
        for neighbour in neighbours:
            if neighbour not in visited and vals[node] <= vals[start]:
                result += self.dfs(neighbour, start, visited, graph, vals, completed)
        return result