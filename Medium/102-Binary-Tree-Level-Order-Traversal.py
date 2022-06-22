# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        else:
            res = []
            res.append([])
            queue = [(root, 0)]
            while queue:
                node, level = queue.pop(0)
                res[level].append(node.val)
                if node.left or node.right:
                    if len(res) <= level+1:
                        res.append([])
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
            return res