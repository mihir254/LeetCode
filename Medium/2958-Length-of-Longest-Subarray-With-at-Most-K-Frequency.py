from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        store = {}
        p1, p2 = 0, 0
        answer = 0
        while p2 < len(nums) and p1 < len(nums):
            if nums[p2] not in store:
                store[nums[p2]] = []
            store[nums[p2]].append(p2)
            if len(store[nums[p2]]) > k:
                firstIndex = store[nums[p2]][0]
                for i in range(p1, firstIndex+1):
                    store[nums[i]].pop(0)
                p1 = firstIndex + 1
            p2 += 1
            answer = max(answer, p2-p1)
        return answer