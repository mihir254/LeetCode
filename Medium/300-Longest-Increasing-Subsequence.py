class Solution:
    def lengthOfLIS(self, nums) -> int:
    #     res = 0
    #     for i in range(len(nums)):
    #         res = max(res, self.rec(nums, i, 1, i+1))
    #     return res
    # def rec(self, arr, prev, cur_len, cur_ind):
    #     if cur_ind >= len(arr):
    #         return cur_len
    #     include, notInclude = 0, 0
    #     if arr[cur_ind] > arr[prev]:
    #         include = self.rec(arr, cur_ind, cur_len+1, cur_ind+1)
    #     notInclude = self.rec(arr, prev, cur_len, cur_ind+1)
    #     return max(include, notInclude)
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)