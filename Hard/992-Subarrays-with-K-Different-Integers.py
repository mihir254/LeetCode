from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        answer1, answer2 = 0, 0
        p1, p2 = 0, 0
        store = {}
        while p2 < len(nums) and p1 < len(nums):
            p2 = max(p1, p2)
            if nums[p2] not in store:
                store[nums[p2]] = 0
            store[nums[p2]] += 1
            if len(store.keys()) > k:
                while p1 < len(nums) and len(store.keys()) > k:
                    answer1 += p2 - p1
                    store[nums[p1]] -= 1
                    if store[nums[p1]] == 0:
                        store.pop(nums[p1], None)
                    p1 += 1
            p2 += 1
        answer1 += ((p2-p1) * (p2-p1+1) // 2)
        p1, p2 = 0, 0
        store = {}
        while p2 < len(nums) and p1 < len(nums):
            p2 = max(p1, p2)
            if nums[p2] not in store:
                store[nums[p2]] = 0
            store[nums[p2]] += 1
            if len(store.keys()) > k-1:
                while p1 < len(nums) and len(store.keys()) > k-1:
                    answer2 += p2 - p1
                    store[nums[p1]] -= 1
                    if store[nums[p1]] == 0:
                        store.pop(nums[p1], None)
                    p1 += 1
            p2 += 1
        answer2 += ((p2-p1) * (p2-p1+1) // 2)
        return answer1 - answer2