from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # balanced = True
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     self.helper(root)
    #     return self.balanced

    # def helper(self, node):
    #     if not self.balanced:
    #         return 0
    #     if not node:
    #         return 0
    #     lh, rh = self.helper(node.left), self.helper(node.right)
    #     if abs(lh - rh) > 1:
    #         self.balanced = False
    #     return 1 + max(lh, rh)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lh, rh = self.helper(root.left), self.helper(root.right)
        return abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def helper(self, node):
        if not node:
            return 0
        lh, rh = self.helper(node.left), self.helper(node.right)
        return 1 + max(lh, rh)