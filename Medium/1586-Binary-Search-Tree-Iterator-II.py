class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.inorder = []
        self.pointer = -1
        self.push_next(root)
        
    def hasNext(self) -> bool:
        return self.stack or self.pointer < len(self.inorder)-1
    
    def next(self) -> int:
        nextPointer = self.pointer+1
        totalNodes = len(self.inorder)
        if nextPointer > totalNodes-1:            
            node = self.stack.pop()
            self.push_next(node.right)
            self.inorder.append(node)
        self.pointer += 1
        return self.inorder[self.pointer].val
        
    def hasPrev(self) -> bool:
        if self.pointer > 0 and self.pointer <= len(self.inorder)-1:
            return True
        return False

    def prev(self) -> int:
        self.pointer -= 1
        return self.inorder[self.pointer].val

    def push_next(self, node):
        while node:
            self.stack.append(node)
            node = node.left