from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            theirSum = numbers[l]+numbers[r]
            if theirSum == target:
                return [l+1, r+1]
            if theirSum > target:
                r -= 1
            else:
                l += 1
        return []