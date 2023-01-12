class Solution:
    def countSubTrees(self, n, edges, labels):
        graph = self.makeGraph(edges)
        answer = [0]*n
        visited = set()
        self.dfs(graph, visited, 0, labels, answer)
        return answer
    def dfs(self, graph, visited, node, labels, answer):
        visited.add(node)
        letter = labels[node]
        neighbours = graph.get(node)
        store = {letter: 1}
        for neighbour in neighbours:
            if neighbour not in visited:
                child_store = self.dfs(graph, visited, neighbour, labels, answer)
                for k, v in child_store.items():
                    if k not in store:
                        store[k] = 0
                    store[k] += v
        answer[node] = store[letter]
        return store
    def makeGraph(self, edges):
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