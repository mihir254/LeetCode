class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.push_next(root)
    def next(self) -> int:
        node = self.stack.pop()
        self.push_next(node.right)
        return node.val
    def hasNext(self) -> bool:
        return self.stack
    def push_next(self, node):
        while node:
            self.stack.append(node)
            node = node.left