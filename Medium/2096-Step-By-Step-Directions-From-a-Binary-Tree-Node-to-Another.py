# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        startPath, endPath = [], []
        self.findNode(root, startValue, startPath)
        self.findNode(root, destValue, endPath)
        while startPath and endPath and startPath[-1] == endPath[-1]:
            startPath.pop()
            endPath.pop()
        return ("U"*len(startPath)) + "".join(endPath[::-1])
        
    def findNode(self, node, target, path):
        if node.val == target:
            return True
        if node.left and self.findNode(node.left, target, path):
            path += ["L"]
        elif node.right and self.findNode(node.right, target, path):
            path += ["R"]
        return path