from typing import List
from collections import Counter
from math import ceil

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for k, v in Counter(nums).items():
            if v == 1:
                return -1
            operations += ceil(v / 3)
        return operations