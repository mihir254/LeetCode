from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        answer = 0
        p1, p2 = 0, 0
        addition = 0
        while p2 < len(nums) and p1 < len(nums):
            p2 = max(p1, p2)
            while p2 < len(nums) and (p2-p1+1)*(addition+nums[p2]) < k:
                addition += nums[p2]
                p2 += 1
            gap = p2-p1
            answer += gap*(gap+1)//2
            if p2 < len(nums):
                answer -= gap*(gap-1)//2
            addition = max(addition-nums[p1], 0)
            p1 += 1
        return answer