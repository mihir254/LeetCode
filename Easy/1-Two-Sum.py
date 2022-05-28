class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if nums[i] not in store:
                store[target-nums[i]] = i
            else:
                return [i, store[nums[i]]]