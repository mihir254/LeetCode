# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.checker(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if not stack and subRoot:
            return False
        if not stack and not subRoot:
            return True
        return self.checker(stack.pop(), subRoot)
    
    def checker(self, p, q):
        if p and q:
            return p.val==q.val and self.checker(p.left, q.left) and self.checker(p.right, q.right)
        return p==q