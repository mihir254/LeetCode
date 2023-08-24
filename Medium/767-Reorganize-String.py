from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        answer = ""
        prev = None
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            answer += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return answer