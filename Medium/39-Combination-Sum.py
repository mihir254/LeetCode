class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.helper(candidates, 0, 0, [], target, result)
        return result
    def helper(self, nums, c_i, c_s, c_a, tgt, ans):
        if c_s == tgt:
            print(c_a)
            ans.append(c_a[:])
            return
        elif c_s > tgt:
            return
        for i in range(c_i, len(nums)):
            c_s += nums[i]
            c_a.append(nums[i])
            self.helper(nums, i, c_s, c_a, tgt, ans)
            c_a.pop()
            c_s -= nums[i]