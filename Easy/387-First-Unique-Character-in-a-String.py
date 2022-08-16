class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {}
        for i in range(len(s)):
            if s[i] not in store:
                store[s[i]] = i
            else:
                store[s[i]] = -1
        for k, v in store.items():
            if v != -1:
                return v
        return -1