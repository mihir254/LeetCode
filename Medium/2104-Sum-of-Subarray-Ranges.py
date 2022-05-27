class Solution:
    def subArrayRanges(self, nums) -> int:
        ans, max_check, min_check = 0, 0, 0
        for i in range(len(nums)):
            max_check = nums[i]
            min_check = nums[i]
            for j in range(i+1, len(nums)):
                max_check = max(max_check, nums[j])
                min_check = min(min_check, nums[j])
                ans += max_check-min_check
        return ans