from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        store = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in store:
                store[groupSizes[i]] = [[]]
            if len(store[groupSizes[i]][-1]) == groupSizes[i]:
                store[groupSizes[i]].append([])
            store[groupSizes[i]][-1].append(i)
        answer = []
        for k,v in store.items():
            for arr in v:
                answer.append(arr)
        return answer