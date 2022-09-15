class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ss = {}
        for c in s:
            if c not in ss:
                ss[c] = 0
            ss[c] += 1
        for c in t:
            if c in ss:
                ss[c] -= 1
        count = 0
        for k,v in ss.items():
            if v > 0:
                count += v
        return count