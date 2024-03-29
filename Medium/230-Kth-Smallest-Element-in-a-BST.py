from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inorder(root, res)
        return res[k-1]
    def inorder(self, node, res):
        if not node:
            return None
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)