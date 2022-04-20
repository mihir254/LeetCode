class Solution:
    left, middle, right, prev = None, None, None, None
    def recoverTree(self, root):
        self.helper(root)
        if not self.right:
            self.left.val, self.middle.val = self.middle.val, self.left.val
        else:
            self.left.val, self.right.val = self.right.val, self.left.val
    
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        
        if self.prev:
            if self.prev.val > root.val:
                if not self.left:
                    self.left = self.prev
                    self.middle = root
                else:
                    self.right = root
        self.prev = root
        
        self.helper(root.right)