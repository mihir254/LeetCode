class Solution:
    def frequencySort(self, s: str) -> str:
        store = {}
        for ch in s:
            if ch not in store:
                store[ch] = 0
            store[ch] += 1
        final_s = ""
        for k,v in sorted(store.items(), key=lambda x: x[1], reverse=True):
            final_s += k*v
        return final_s