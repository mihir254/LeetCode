# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ''
        left = '(' + self.tree2str(root.left) + ')' if root.left or root.right else ''
        right = '(' + self.tree2str(root.right) + ')' if root.right else ''
        return str(root.val)+left+right