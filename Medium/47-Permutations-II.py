class Solution:
    def permuteUnique(self, nums):
        res, n = [], len(nums)
        nums.sort()
        self.recursion(nums, n, [], res)
        return res
    def recursion(self, arr, length, cur, ans):
        if len(cur) == length:
            ans.append(cur)
            return
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            pivot = arr[i]
            remaining = arr[:i] + arr[i+1:]
            self.recursion(remaining, length, [pivot]+cur, ans)