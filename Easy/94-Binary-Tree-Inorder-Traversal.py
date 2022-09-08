# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> int:
        ans = []
        self.inorder(root, ans)
        return ans
    def inorder(self, node, ans):
        if not node:
            return
        self.inorder(node.left, ans)
        ans.append(node.val)
        self.inorder(node.right, ans)