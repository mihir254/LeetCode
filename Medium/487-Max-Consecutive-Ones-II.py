from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # constant space for large input
        i, maxi = 0, 0
        last, prev = -1, -1
        while i < len(nums):
            if nums[i] == 0:
                if last != -1:
                    prev = last
                last = i
            i += 1
            maxi = max(maxi, i-(prev+1))
        return maxi
        
        # for smaller or fixed input, we can remember where we found the 0s and calculate prefix, suffix sum
        # pos = []
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         pos.append(i)
        # start = 0
        # maxi = 0
        # cur = 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         cur += 1
        #         maxi = max(maxi, cur)
        #     else:
        #         cur = 0
        # for i in range(len(pos)):
        #     if i < len(pos)-1:
        #         maxi = max(maxi, pos[i+1]-start)
        #     else:
        #         maxi = max(maxi, len(nums)-start)
        #     start = pos[i]+1
        # return maxi