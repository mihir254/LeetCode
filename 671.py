# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root) -> int:
        queue = [root]
        mini = []
        while queue:
            node = queue.pop(0)
            if node.val not in mini:
                mini.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        mini.sort()
        return -1 if len(mini)==1 else mini[1]