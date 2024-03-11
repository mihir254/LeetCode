import heapq

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        store = {}
        for i in range(len(order)):
            store[order[i]] = i
        # ans = []
        # for i in range(len(s)):
        #     char = s[i]
        #     if not ans or char not in store:
        #         ans.append(char)
        #     else:
        #         n = len(ans)
        #         while n >= 1:
        #             prev = ans[n-1]
        #             if prev not in store:
        #                 n -= 1
        #             else:
        #                 if store[prev] < store[char]:
        #                     ans.insert(n, char)
        #                     break
        #                 else:
        #                     n -= 1
        #         if n == 0:
        #             ans.insert(0, char)
        # return "".join(ans)
        heap = []
        for i in range(len(s)):
            char = s[i]
            if char in store:
                heapq.heappush(heap, (store[char], char))
            else:
                heapq.heappush(heap, (26, char))
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return "".join(ans)