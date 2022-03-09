# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        hashmap = {node: Node(node.val)}
        self.helper(node, hashmap)
        return hashmap[node]
    def helper(self, n, h):
        neighbours = n.neighbors
        for neighbour in neighbours:
            if neighbour not in h:
                h[neighbour] = Node(neighbour.val)
                self.helper(neighbour, h)
            h[n].neighbors.append(h[neighbour])