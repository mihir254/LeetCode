from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxi = -1
        store = {}
        for i in range(n):
            store[i] = set()
        for road in roads:
            city1, city2 = road
            store[city1].add(city2)
            store[city2].add(city1)
        for i in range(n-1):
            for j in range(i+1, n):
                pairScore = len(list(store[i])) + len(list(store[j]))
                if i in store[j]:
                    pairScore -= 1
                maxi = max(maxi, pairScore)
        return maxi