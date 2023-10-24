from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer
        queue = [[root, 0]]
        while queue:
            node, level = queue.pop(0)
            if len(answer) == level:
                answer.append(node.val)
            else:
                answer[level] = max(answer[level], node.val)
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        return answer