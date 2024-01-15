from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        store = {}
        for match in matches:
            w, l = match
            if l not in store:
                store[l] = 0
            if w not in store:
                store[w] = 0
            store[l] += 1
        zero, one = [], []
        for k, v in store.items():
            if v == 0:
                zero.append(k)
            elif v == 1:
                one.append(k)
        zero.sort()
        one.sort()
        return [zero, one]