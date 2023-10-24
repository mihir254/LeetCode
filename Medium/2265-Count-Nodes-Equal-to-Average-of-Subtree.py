from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[2]
    def dfs(self, node):
        if not node:
            return [0, 0, 0]
        leftSum, leftCount, leftTreeAnswers = self.dfs(node.left)
        rightSum, rightCount, rightTreeAnswers = self.dfs(node.right)
        thisSum = leftSum + rightSum + node.val
        thisCount = leftCount + rightCount + 1
        average = thisSum // thisCount
        totalAnswers = leftTreeAnswers + rightTreeAnswers
        if average == node.val:
            totalAnswers += 1
        return [thisSum, thisCount, totalAnswers]