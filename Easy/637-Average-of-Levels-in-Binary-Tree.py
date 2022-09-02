# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        stack = [[root, 0]]
        answer = []
        while stack:
            node, level = stack.pop()
            if len(answer) < level+1:
                answer.append([0, 0])
            answer[level][0] += node.val
            answer[level][1] += 1
            if node.right:
                stack.append([node.right, level+1])
            if node.left:
                stack.append([node.left, level+1])
        result = [i[0]/i[1] for i in answer]
        return result