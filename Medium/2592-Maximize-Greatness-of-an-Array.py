from typing import List
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        store = {}
        for num in nums:
            if num not in store:
                store[num] = 0
            store[num] += 1
        xset = set(nums)
        x = sorted(list(xset), reverse=True)
        available = 0
        answer = 0
        while x:
            number = x.pop()
            canGive = store[number]
            toAnswer = min(available, canGive)
            answer += toAnswer
            available = available + canGive - toAnswer
        return answer