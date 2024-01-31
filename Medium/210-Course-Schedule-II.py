from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        completed = set()
        for s1, s2 in prerequisites:
            if s1 not in graph:
                graph[s1] = []
            graph[s1].append(s2)
        path = []
        for i in range(numCourses):
            if i not in graph:
                completed.add(i)
                path.append(i)
        cycle = False
        for i in range(numCourses):
            visited = set()
            x = self.dfs(i, graph, completed, visited, path)
            if not x:
                return []
        return path

    def dfs(self, node, graph, completed, visited, path):
        if node in completed:
            return True
        if node in visited:
            return False
        visited.add(node)
        nei = graph.get(node)
        if nei:
            repeated = False
            for n in nei:
                if n in completed:
                    continue
                x = self.dfs(n, graph, completed, visited, path)
                if not x:
                    return False
        completed.add(node)
        path.append(node)
        return True