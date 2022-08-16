class SparseVector:
    def __init__(self, nums):
        self.vec1 = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.vec1[i] = nums[i]

    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        for k,v in vec.vec1.items():
            if k in self.vec1:
                prod += v*self.vec1[k]
        return prod