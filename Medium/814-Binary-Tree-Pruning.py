# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root):
        def dfs(node):
            if not node.left and not node.right:
                if node.val == 0:
                    return False
                else:
                    return True
            if node.left:
                checkLeft = dfs(node.left)
                if not checkLeft:
                    node.left = None
            if node.right:
                checkRight = dfs(node.right)
                if not checkRight:
                    node.right = None
            if not node.right and not node.left and node.val == 0:
                return False
            else:
                return True
        dfs(root)
        if not root.left and not root.right and root.val == 0:
            return None
        return root