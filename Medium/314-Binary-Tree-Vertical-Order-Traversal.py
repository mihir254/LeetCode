# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        queue, store = [(root, 0)], {}
        while queue:
            node, c = queue.pop(0)
            if c not in store:
                store[c] = []
            store[c].append(node.val)
            if node.left:
                queue.append((node.left, c-1))
            if node.right:
                queue.append((node.right, c+1))
        ans = []
        for k, v in sorted(store.items()):
            ans.append(v)
        return ans