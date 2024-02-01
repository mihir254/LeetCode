from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        if len(nums) % 3 != 0:
            return ans
        nums.sort()
        i = 0
        while i < len(nums)-2:
            if abs(nums[i] - nums[i+1]) <= k and abs(nums[i+1] - nums[i+2]) <= k and abs(nums[i] - nums[i+2]) <= k:
                ans.append(nums[i:i+3])
                i += 3
            else:
                return []
        return ans