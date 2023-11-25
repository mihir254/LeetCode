from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        sums = [total]
        for i in range(1, len(nums)):
            decreasedSum = sums[i-1] - nums[i-1]
            sums.append(decreasedSum)
        result = []
        prev = 0
        for i in range(len(nums)):
            if i == 0:
                ans = sums[i] - nums[i]*(len(nums)-i)
            else:
                ans = sums[i] - nums[i]*(len(nums)-i) + prev+(nums[i]-nums[i-1])*i
                prev += (nums[i]-nums[i-1])*i
            result.append(ans)
        return result