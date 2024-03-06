from typing import List
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        vertices = len(edges)+1
        graph = {}
        ans = [0]*vertices
        for i, j, k in edges:
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []
            graph[i].append([j, k])
            graph[j].append([i, k])
        for i in range(vertices):
            answer = []
            if i in graph and len(graph[i]) > 1:
                visited = set()
                visited.add(i)
                for j, k in graph[i]:
                    x = self.dfs(j, k, graph, signalSpeed, visited)
                    answer.append(x)
            if answer:
                mul = 0
                for x in range(len(answer)-1):
                    for y in range(x+1, len(answer)):
                        mul += answer[x]*answer[y]
                ans[i] = mul
        return ans
    def dfs(self, node, wt, graph, speed, visited):
        total = 0
        if wt % speed == 0:
            total += 1
        visited.add(node)
        nei = graph.get(node)
        if nei:
            for j, k in nei:
                if j not in visited:
                    total += self.dfs(j, k+wt, graph, speed, visited)
        return total