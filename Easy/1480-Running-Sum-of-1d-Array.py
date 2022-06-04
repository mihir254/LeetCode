class Solution:
    def runningSum(self, nums):
        res = [0]*len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = res[i-1] + nums[i]
        return res