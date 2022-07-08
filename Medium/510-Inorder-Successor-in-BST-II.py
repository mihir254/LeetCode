class Solution:
    def inorderSuccessor(self, node):
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent:
            if node == node.parent.left:
                return node.parent
            node = node.parent
        return None