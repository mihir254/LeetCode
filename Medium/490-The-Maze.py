class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        visited = set()
        return self.dfs(maze, start, destination, visited)
        
    def dfs(self, mat, cur, tar, visit):
        if (cur[0],cur[1]) in visit:
            return False
        visit.add((cur[0],cur[1]))
        if cur == tar:
            return True
        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]
        for neighbour in neighbours:
            tempx, tempy = cur[0], cur[1]
            while 0 <= tempx+neighbour[0] < len(mat) and 0 <= tempy+neighbour[1] < len(mat[0]) and mat[tempx+neighbour[0]][tempy+neighbour[1]] != 1:
                tempx += neighbour[0]
                tempy += neighbour[1]
            if self.dfs(mat, [tempx, tempy], tar, visit):
                return True
        return False