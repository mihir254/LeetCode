from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # maxi = 0
        # queue = [[root, []]]
        # while queue:
        #     node, ancestors = queue.pop(0)
        #     for ancestor in ancestors:
        #         maxi = max(maxi, abs(ancestor-node.val))
        #     if node.left:
        #         queue.append([node.left, ancestors+[node.val]])
        #     if node.right:
        #         queue.append([node.right, ancestors+[node.val]])
        # return maxi

        maxi = 0
        queue = [[root, -1, -1]]
        while queue:
            node, maxAncestor, minAncestor = queue.pop(0)
            if maxAncestor != -1 and minAncestor != -1:
                maxi = max(maxi, abs(maxAncestor-node.val), abs(node.val-minAncestor))
            newMax = node.val if maxAncestor == -1 else max(maxAncestor, node.val)
            newMin = node.val if minAncestor == -1 else min(minAncestor, node.val)
            if node.left:
                queue.append([node.left, newMax, newMin])
            if node.right:
                queue.append([node.right, newMax, newMin])
        return maxi