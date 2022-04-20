# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        self.inorderTraversal(root, inorder)
        node = TreeNode(inorder[0])
        temp = node
        for i in inorder[1:]:
            temp.right = TreeNode(i)
            temp = temp.right
        return node
        
    def inorderTraversal(self, node, inorder):
        if not node:
            return
        self.inorderTraversal(node.left, inorder)
        inorder.append(node.val)
        self.inorderTraversal(node.right, inorder)