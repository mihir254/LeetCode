import collections
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += [b]
        route = []
        def visited(airport):
            while targets[airport]:
                visited(targets[airport].pop())
            route.append(airport)
        visited("JFK")
        return route[::-1]