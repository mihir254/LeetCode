from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s1, s2, l1, l2 = float('inf'), float('inf'), -1, -1
        for num in nums:
            if num < s1:
                s2 = s1
                s1 = num
            elif num < s2:
                s2 = num
            if num > l1:
                l2 = l1
                l1 = num
            elif num > l2:
                l2 = num
        return (l1*l2)-(s1*s2)