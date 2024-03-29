from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        store = {}
        queue = [[root, 0]]
        lastLevel = -1
        while queue:
            node, level = queue.pop(0)
            lastLevel = max(level, lastLevel)
            if level not in store:
                store[level] = []
            store[level].append(node.val)
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        return store[lastLevel][0]