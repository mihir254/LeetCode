from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur, cnt = nums[0], 1
        i = 1
        while i < len(nums):
            if nums[i] == "_":
                return i
            if nums[i] == cur:
                cnt += 1
                if cnt > 2:
                    nums.pop(i)
                    nums.append("_")
                    cnt -= 1
                else:
                    i += 1
            else:
                cur = nums[i]
                cnt = 1
                i += 1
        return len(nums)