from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums.sort()
        # return (nums[-1]-1)*(nums[-2]-1)
        first, second = 0, 0
        for i in range(len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif nums[i] > second:
                second = nums[i]
        return (first-1)*(second-1)