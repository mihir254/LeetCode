# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

import collections
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return None
        queue, hashmap = [root], collections.defaultdict(Node)
        while queue:
            node = queue.pop(0)
            hashmap[node].val = node.val
            for child in node.children:
                hashmap[child].val = child.val
                hashmap[node].children.append(hashmap[child])
                queue.append(child)
        return hashmap[root]