class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}
        self.graphBuilder(equations, values, graph)
        answer = []
        for query in queries:
            visited = set()
            ans = self.dfs(query[0], query[1], graph, visited, 1.0)
            answer.append(ans)
        return answer
    def graphBuilder(self, eqs, vals, grp):
        for i in range(len(eqs)):
            if eqs[i][0] not in grp:
                grp[eqs[i][0]] = []
            grp[eqs[i][0]].append((eqs[i][1], vals[i]))
            if eqs[i][1] not in grp:
                grp[eqs[i][1]] = []
            grp[eqs[i][1]].append((eqs[i][0], 1/vals[i]))
    def dfs(self, src, tgt, graph, visited, val):
        if src not in graph or tgt not in graph or src in visited:
            return -1
        if src == tgt:
            return val
        visited.add(src)
        neighbours = graph.get(src)
        for neighbour in neighbours:
            product = self.dfs(neighbour[0], tgt, graph, visited, val*neighbour[1])
            if product != -1:
                return product
        return -1
