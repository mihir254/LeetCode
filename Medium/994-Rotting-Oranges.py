class Solution:
    def orangesRotting(self, grid) -> int:
        minute, rotten = 0, 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten += 1
                    queue.append([i, j, minute])
        while queue:
            rotten_pos_x, rotten_pos_y, time = queue.pop(0)
            neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            minute = max(minute, time)
            for neighbour in neighbours:
                if rotten_pos_x+neighbour[0] >= 0 and rotten_pos_x+neighbour[0] < len(grid) and rotten_pos_y+neighbour[1] >= 0 and rotten_pos_y+neighbour[1] < len(grid[0]) and grid[rotten_pos_x+neighbour[0]][rotten_pos_y+neighbour[1]] == 1:
                    grid[rotten_pos_x+neighbour[0]][rotten_pos_y+neighbour[1]] = 2
                    queue.append([rotten_pos_x+neighbour[0], rotten_pos_y+neighbour[1], time+1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minute