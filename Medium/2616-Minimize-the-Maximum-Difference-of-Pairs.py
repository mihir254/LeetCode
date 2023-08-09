from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l, r = 0, nums[-1]-nums[0]
        while l <= r:
            m = (l+r) // 2
            if self.checker(m, nums) >= p:
                r = m - 1
            else:
                l = m + 1
        return l
    def checker(self, pivot, arr):
        i, count = 0, 0
        while i < len(arr)-1:
            if arr[i+1] - arr[i] <= pivot:
                count += 1
                i += 1
            i += 1
        return count