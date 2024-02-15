from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        nums.sort(reverse=True)
        for i in range(len(nums)):
            biggestSide = nums[i]
            remainingSum = totalSum - biggestSide
            if remainingSum > biggestSide:
                return totalSum
            totalSum -= biggestSide
        return -1