# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        lst = []
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            lst.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return min(lst[i]-lst[i-1] for i in range(1, len(lst)))