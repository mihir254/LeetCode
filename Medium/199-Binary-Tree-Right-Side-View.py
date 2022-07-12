# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        store = {}
        queue = [(root, 0)]
        while queue:
            node, lvl = queue.pop(0)
            if lvl not in store:
                store[lvl] = []
            store[lvl].append(node.val)
            if node.left:
                queue.append((node.left, lvl+1))
            if node.right:
                queue.append((node.right, lvl+1))
        ans = []
        for k, v in store.items():
            ans.append(v[-1])
        return ans