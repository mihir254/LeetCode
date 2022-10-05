# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if level == depth-1:
                new_left_node = TreeNode(val)
                new_right_node = TreeNode(val)
                new_left_node.left = node.left
                new_right_node.right = node.right
                node.left = new_left_node
                node.right = new_right_node
            else:
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
        return root