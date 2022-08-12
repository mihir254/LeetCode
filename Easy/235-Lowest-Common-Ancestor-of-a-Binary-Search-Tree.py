# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack1, stack2 = [], []
        node1, node2 = root, root
        while node1 != p:
            stack1.append(node1)
            if p.val < node1.val:
                node1 = node1.left
            else:
                node1 = node1.right
        stack1.append(node1)
        while node2 != q:
            stack2.append(node2)
            if q.val < node2.val:
                node2 = node2.left
            else:
                node2 = node2.right
        stack2.append(node2)
        while len(stack1) > len(stack2):
            stack1.pop()
        while len(stack2) > len(stack1):
            stack2.pop()
        while stack1 and stack2:
            p1 = stack1.pop()
            p2 = stack2.pop()
            if p1 == p2:
                return p1