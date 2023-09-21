from typing import List
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftHigh = nums[0]
        rightLow = -1
        lows = [0]*len(nums)
        mini = float('inf')
        for i in range(len(nums)-1, -1, -1):
            mini = min(mini, nums[i])
            lows[i] = mini
        for i in range(1, len(nums)-1):
            if leftHigh <= lows[i]:
                return i
            leftHigh = max(leftHigh, nums[i])
        return len(nums)-1