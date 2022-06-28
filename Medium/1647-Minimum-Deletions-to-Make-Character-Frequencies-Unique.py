class Solution:
    def minDeletions(self, s: str) -> int:
        store = {}
        for i in s:
            if i not in store:
                store[i] = 0
            store[i] += 1
        ans, freqs = 0, set()
        for i in store.keys():
            while store[i] > 0 and store[i] in freqs:
                store[i] -= 1
                ans += 1
            freqs.add(store[i])
        return ans