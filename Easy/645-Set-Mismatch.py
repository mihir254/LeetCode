class Solution:
    def findErrorNums(self, nums):
        rep = sum(nums) - sum(set(nums))
        sumo = (len(nums)*(len(nums)+1))//2
        miss = sumo - (sum(nums) - rep)
        return [rep, miss]