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
        node = TreeNode()
        temp, temp1 = node, node
        for i in inorder:
            temp.val = i
            temp.right = TreeNode()
            temp = temp.right
        for i in range(len(inorder)-1):
            temp1 = temp1.right
        temp1.right = None
        return node
        
    def inorderTraversal(self, node, inorder):
        if not node:
            return
        self.inorderTraversal(node.left, inorder)
        inorder.append(node.val)
        self.inorderTraversal(node.right, inorder)