from typing import List
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        answer = []
        store = {}
        for num in nums:
            if num not in store:
                store[num] = 0
            store[num] += 1
            if len(answer) < store[num]:
                answer.append([])
            answer[store[num]-1].append(num)
        return answer