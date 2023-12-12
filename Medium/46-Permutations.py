from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        hashset = []
        for i in range(len(nums)):
            self.helper([nums[i]], nums[:i]+nums[i+1:], hashset)
        return list(hashset)
    def helper(self, cur, arr, hashset):
        if not arr:
            hashset.append(cur)
            return
        for i in range(len(arr)):
            self.helper(cur+[arr[i]], arr[:i]+arr[i+1:], hashset)