# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        graph = {}
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val not in graph:
                graph[node.val] = []
            if node.right:
                graph[node.val].append(node.right.val)
                if node.right.val not in graph:
                    graph[node.right.val] = [node.val]
                queue.append(node.right)
            if node.left:
                graph[node.val].append(node.left.val)
                if node.left.val not in graph:
                    graph[node.left.val] = [node.val]
                queue.append(node.left)
        answer = []
        queue = [[target.val, 0]]
        visited = set()
        while queue:
            node, level = queue.pop(0)
            if level == k:
                answer.append(node)
            visited.add(node)
            neighbours = graph[node]
            if neighbours:
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append([neighbour, level+1])
        return answer