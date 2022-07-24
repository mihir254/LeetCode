# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = float('-inf')
    def maxPathSum(self, root) -> int:
        self.recursion(root)
        return self.ans
    def recursion(self, node):
        if not node:
            return 0
        left = max(0, self.recursion(node.left))
        right = max(0, self.recursion(node.right))
        self.ans = max(self.ans, left+right+node.val)
        return max(left, right)+node.val