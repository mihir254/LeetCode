# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root) -> int:
        levelSum = []
        queue = [[root, 1]]
        while queue:
            node, level = queue.pop(0)
            if len(levelSum) < level:
                levelSum.append(0)
            levelSum[level-1] += node.val
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        maxi = max(levelSum)
        return levelSum.index(maxi) + 1