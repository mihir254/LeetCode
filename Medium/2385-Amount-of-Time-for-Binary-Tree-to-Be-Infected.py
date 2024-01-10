from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        store = {}
        self.convert(root, store)
        queue = [[start, 0]]
        visited = set()
        maxi = 0
        while queue:
            node, ht = queue.pop(0)
            visited.add(node)
            maxi = max(maxi, ht)
            neighbours = store.get(node)
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append([neighbour, ht+1])
        return maxi

    def convert(self, node, store):
        if not node:
            return
        if node.val not in store:
            store[node.val] = []
        if node.left:
            store[node.val].append(node.left.val)
            if node.left.val not in store:
                store[node.left.val] = []
            store[node.left.val].append(node.val)
            self.convert(node.left, store)
        if node.right:
            store[node.val].append(node.right.val)
            if node.right.val not in store:
                store[node.right.val] = []
            store[node.right.val].append(node.val)
            self.convert(node.right, store)