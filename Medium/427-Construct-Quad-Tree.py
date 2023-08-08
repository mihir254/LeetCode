from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.helper(grid)
    def helper(self, grid):
        if not grid:
            return None
        zeros, ones = False, False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and not ones:
                    zeros = True
                elif grid[i][j] == 1 and not zeros:
                    ones = True
                else:
                    zeros = False
                    ones = False
                    break
            if not zeros and not ones:
                break
        if zeros:
            return Node(0, True, None, None, None, None)
        if ones:
            return Node(1, True, None, None, None, None)
        half = len(grid) // 2
        first = [row[half:] for row in grid[:half]]
        second = [row[:half] for row in grid[:half]]
        third = [row[:half] for row in grid[half:]]
        fourth = [row[half:] for row in grid[half:]]
        topLeft = self.helper(second)
        topRight = self.helper(first)
        bottomLeft = self.helper(third)
        bottomRight = self.helper(fourth)
        return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)