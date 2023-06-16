class Solution:
    def productExceptSelf(self, nums):
        zeroes = 0
        pro = 1
        for num in  nums:
            if num == 0:
                zeroes += 1
            else:
                pro *= num
        if zeroes > 1:
            return [0]*len(nums)
        ans = []
        for num in nums:
            if num == 0:
                ans.append(pro)
            elif zeroes == 0:
                appended = pro // num
                ans.append(appended)
            else:
                ans.append(0)
        return ans