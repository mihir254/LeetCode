class Solution:
    def getAverages(self, nums, k):
        iterations = len(nums) - (2*k + 1) + 1
        if iterations <= 0:
            return [-1]*len(nums)
        answer = []
        sumo = sum(nums[:(2*k + 1)])
        for i in range(iterations-1):
            answer.append(sumo // (2*k + 1))
            sumo -= nums[i]
            sumo += nums[i+(2*k)+1]
        answer.append(sumo // (2*k + 1))
        return [-1]*k + answer + [-1]*k