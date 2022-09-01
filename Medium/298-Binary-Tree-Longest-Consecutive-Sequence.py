# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        ans = 0
        stack = [[root, 0, 0]]
        while stack:
            node, prev, current = stack.pop()
            if current == 0 or node.val-1 == prev:
                current += 1
                ans = max(ans, current)
            else:
                current = 1
            prev = node.val
            if node.right:
                stack.append([node.right, prev, current])
            if node.left:
                stack.append([node.left, prev, current])
        return ans