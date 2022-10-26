class Solution:
    def checkSubarraySum(self, nums, k):
        store = {0:-1}
        sumo = 0
        for i in range(len(nums)):
            sumo += nums[i]
            rem = sumo%k
            if rem not in store:
                store[rem] = i
            elif i-store[rem]>1:
                return True
        return False