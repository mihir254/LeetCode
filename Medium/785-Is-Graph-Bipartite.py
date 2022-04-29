class Solution:
    def isBipartite(self, graph) -> bool:
        color = [-1]*len(graph)
        for i in range(len(graph)):
            if color[i] == -1:
                stack = [i]
                color[i] = 0
                while stack:
                    node = stack.pop()
                    neighbours = graph[node]
                    for neighbour in neighbours:
                        if color[neighbour] == -1:
                            stack.append(neighbour)
                            color[neighbour] = color[node]^1
                        elif color[neighbour] == color[node]:
                            return False
        return True