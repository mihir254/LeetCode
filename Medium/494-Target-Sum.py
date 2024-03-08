from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        store = {}
        self.recursion(0, 0, nums, target, store)
        return store[(0, 0)]
    def recursion(self, val, i, nums, tgt, store):
        if i >= len(nums):
            return 1 if val == tgt else 0
        if (i, val) in store:
            return store[(i, val)]
        a = self.recursion(val+nums[i], i+1, nums, tgt, store)
        b = self.recursion(val-nums[i], i+1, nums, tgt, store)
        store[(i, val)] = a + b
        return a + b