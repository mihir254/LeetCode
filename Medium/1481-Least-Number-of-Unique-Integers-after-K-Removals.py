import heapq
from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        # arr = [[v,k] for k,v in counter.items()]
        # arr.sort(key=lambda x:x[0])
        # while k > 0:
        #     count, _ = arr.pop(0)
        #     if count > k:
        #         return len(arr)+1
        #     else:
        #         k -= count
        # return len(arr)
        heap = []
        for key,val in counter.items():
            heapq.heappush(heap, (val, key))
        while k > 0 and heap:
            count, number = heapq.heappop(heap)
            if count > k:
                heapq.heappush(heap, (count-k, number))
                k -= k
            else:
                k -= count
        return len(heap)