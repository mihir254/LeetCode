class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        p1, p2, store, res = 0, 0, {}, 1
        while p2 < len(s) and p1 < len(s):
            if s[p2] not in store:
                store[s[p2]] = [p2]
            else:
                store[s[p2]].append(p2)
                if store[s[p2]][-2] >= p1:
                    res = max(res, p2-p1)
                    print(p1, p2, p2-p1)
                    p1 = store[s[p2]][-2]+1
            p2 += 1
        res = max(res, p2-p1)
        return res