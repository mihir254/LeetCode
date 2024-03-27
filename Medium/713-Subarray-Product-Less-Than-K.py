from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # answer = 0
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(i, len(nums)):
        #         product *= nums[j]
        #         if product < k:
        #             answer += 1
        #         else:
        #             break
        # return answer
        answer = 0
        p1, p2 = 0, 0
        product = 1
        while p2 < len(nums) and p1 < len(nums):
            p2 = max(p1, p2)
            while p2 < len(nums) and product*nums[p2] < k:
                product *= nums[p2]
                p2 += 1
            gap = p2-p1
            answer += gap*(gap+1)//2
            if p2 < len(nums):
                answer -= gap*(gap-1)//2
            product = max(product//nums[p1], 1)
            p1 += 1
        return answer