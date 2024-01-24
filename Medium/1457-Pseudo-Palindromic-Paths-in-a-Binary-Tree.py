# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root, set())
        return self.count

    def dfs(self, node, store):
        if not node:
            return
        if node.val in store:
            store.remove(node.val)
        else:
            store.add(node.val)
        if not node.left and not node.right:
            if len(store) <= 1:
                self.count += 1
            return
        self.dfs(node.left, set(store))
        self.dfs(node.right, set(store))