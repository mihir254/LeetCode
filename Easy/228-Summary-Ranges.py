class Solution:
    def summaryRanges(self, nums):
        result, ans = [], []
        for i in range(len(nums)):
            if not ans:
                ans.append(nums[i])
            elif ans[-1]+1 == nums[i]:
                    ans.append(nums[i])
            else:
                temp = ""
                if len(ans)==1:
                    result.append(str(ans[0]))
                else:
                    result.append(str(ans[0]) + "->" + str(ans[-1]))
                ans = []
                ans.append(nums[i])
        if ans:
            temp = ""
            if len(ans)==1:
                result.append(str(ans[0]))
            else:
                result.append(str(ans[0]) + "->" + str(ans[-1]))
        return result