"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = [[root, 0]]
        ans = []
        while queue:
            node, lvl = queue.pop(0)
            if len(ans) < lvl+1:
                ans.append([])
            ans[lvl].append(node.val)
            if node.children:
                for neighbour in node.children:
                    queue.append([neighbour, lvl+1])
        return ans