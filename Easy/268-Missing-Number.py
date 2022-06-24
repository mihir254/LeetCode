class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumo = 0
        for i in range(len(nums)+1):
            sumo ^= i
        for i in range(len(nums)):
            sumo ^= nums[i]
        return sumo