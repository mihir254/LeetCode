from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if direction == 1:
                    return False
                direction = -1
            elif nums[i] < nums[i+1]:
                if direction == -1:
                    return False
                direction = 1
        return True