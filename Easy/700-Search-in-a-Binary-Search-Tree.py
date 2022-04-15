class Solution:
    def searchBST(self, root, val: int):
        while root:
            if root.val == val:
                return root
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
        return None