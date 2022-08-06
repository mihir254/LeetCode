# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: TreeNode):
        res = []
        self.dfs(res, root)
        return res
    def dfs(self, ans, node):
        if not node:
            return -1
        level = 1 + max(self.dfs(ans, node.left), self.dfs(ans, node.right))
        if len(ans) <= level:
            ans.append([])
        ans[level].append(node.val)
        return level