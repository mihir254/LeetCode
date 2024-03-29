from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        p1, p2 = 0, 0
        ind = []
        high = max(nums)
        answer = 0
        n = len(nums)
        while p1 < len(nums) and p2 < len(nums):
            p2 = max(p1, p2)
            if nums[p2] == high:
                if ind and ind[-1] == p2:
                    ind.pop()
                ind.append(p2)
            if len(ind) >= k:
                answer += (n - p2)
                if nums[p1] == high:
                    ind.pop(0)
                p1 += 1
                p2 -= 1
            p2 += 1
        return answer