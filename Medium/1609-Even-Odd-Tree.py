from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = -1
        while queue:
            level += 1
            n = len(queue)
            prev = 0 if level % 2 == 0 else float('inf')
            for _ in range(n):
                node = queue.pop(0)
                if (level % 2 == 0 and (node.val % 2 == 0 or prev >= node.val)) or (level % 2 == 1 and (node.val % 2 == 1 or prev <= node.val)):
                    return False
                prev = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return True