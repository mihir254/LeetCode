# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [[root, root.val]]
        ans = 0
        while stack:
            node, high = stack.pop()
            if node.val >= high:
                high = node.val
                ans += 1
            if node.right:
                stack.append([node.right, high])
            if node.left:
                stack.append([node.left, high])
        return ans