class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        prev1 = 0
        prev2 = nums[0]
        for i in range(1, len(nums)):
            cur = max(prev2, nums[i]+prev1)
            prev1 = prev2
            prev2 = cur
        return prev2