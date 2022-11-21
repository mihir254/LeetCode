class Solution:
    def nearestExit(self, maze, entrance) -> int:
        queue = [[entrance, 0]]
        maze[entrance[0]][entrance[1]] = "+"
        while queue:
            node, level = queue.pop(0)
            x, y = node[0], node[1]
            if (x == 0 or y == 0 or x == len(maze)-1 or y == len(maze[0])-1) and level != 0:
                return level
            neighbours = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for dx, dy in neighbours:
                if x+dx >= 0 and y+dy >= 0 and x+dx < len(maze) and y+dy < len(maze[0]) and maze[x+dx][y+dy] == ".":
                    maze[x+dx][y+dy] = "+"
                    queue.append([[x+dx, y+dy], level+1])
        return -1