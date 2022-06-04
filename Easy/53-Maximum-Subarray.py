class Solution:
    def maxSubArray(self, nums) -> int:
        # brute force
#         max_sum, prev_sum = nums[0], nums[0]
#         for num in nums[1:]:
#             print(prev_sum)
#             cur_sum = prev_sum + num
#             if num >= cur_sum:
#                 prev_sum = num
#             elif cur_sum >= prev_sum or cur_sum > 0:
#                 prev_sum = cur_sum
#             else:
#                 prev_sum = 0
#             max_sum = max(max_sum, prev_sum)
#         return max_sum
        # DP
        table = [0]*len(nums)
        res = nums[0]
        print(table)
        table[0] = nums[0]
        print(table)
        for i in range(1, len(nums)):
            table[i] = nums[i]+(table[i-1] if table[i-1] > 0 else 0)
            res = max(res, table[i])
        print(table)
        return res