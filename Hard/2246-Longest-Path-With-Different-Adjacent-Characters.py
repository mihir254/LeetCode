class Solution:
    def longestPath(self, parent, s: str) -> int:
        graph = {}
        for i, v in enumerate(parent):
            if i not in graph:
                graph[i] = []
            if v not in graph and v != -1:
                graph[v] = []
            if v != -1:
                graph[i].append(v)
                graph[v].append(i)
        visited = set()
        ans = 1
        def dfs(node):
            nonlocal ans
            visited.add(node)
            length = 1
            neighbours = graph.get(node)
            for neighbour in neighbours:
                if neighbour not in visited:
                    x = dfs(neighbour)
                    if s[node] != s[neighbour]:
                        ans = max(ans, length + x)
                        length = max(length, x + 1)
            return length
        answer = dfs(0)
        return ans
        
    # def dfs(self, visited, node, previous, graph, s, answer):
    #     visited.add(node)
    #     length, continuous = 1, True
    #     if s[node] == previous:
    #         continuous = False
    #     returns = []
    #     neighbours = graph.get(node)
    #     for neighbour in neighbours:
    #         if neighbour not in visited:
    #             l, c = self.dfs(visited, neighbour, s[node], graph, s, answer)
    #             if c:
    #                 returns.append(l)
    #     returns.sort(reverse=True)
    #     for i in range(len(returns)):
    #         if i >= 2:
    #             break
    #         length += returns[i]
    #     return [length, continuous]