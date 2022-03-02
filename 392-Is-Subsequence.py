class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (not s and t) or (not s and not t):
            return True
        if not t and s:
            return False
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
                if j >= len(s):
                    return True
                continue
        return True if j == len(s) else False