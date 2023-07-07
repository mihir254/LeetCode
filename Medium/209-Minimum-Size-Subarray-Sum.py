class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        runningSum = 0
        left, right = 0, 0
        mini = len(nums)+1
        while right < len(nums):
            runningSum += nums[right]
            if runningSum >= target:
                difference = runningSum - target
                while left <= right and difference > 0:
                    if difference >= nums[left]:
                        difference -= nums[left]
                        runningSum -= nums[left]
                        left += 1
                    else:
                        break
                mini = min(mini, right-left+1)
            right += 1
        return 0 if mini > len(nums) else mini