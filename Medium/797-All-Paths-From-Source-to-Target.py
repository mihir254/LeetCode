class Solution:
    def allPathsSourceTarget(self, graph):
        ans = []
        self.dfs(0, len(graph)-1, graph, ans, [])
        return ans
    def dfs(self, src, dest, graph, ans, path):
        if src == dest:
            path.append(src)
            ans.append(path)
            return
        neighbours = graph[src]
        for neighbour in neighbours:
            self.dfs(neighbour, dest, graph, ans, path+[src])
        return