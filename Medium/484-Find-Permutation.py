class Solution:
    def findPermutation(self, s: str):
        result, cur, d = [1], 2, 0
        for i in range(len(s)):
            if s[i] == "I":
                result.append(cur)
                d = 0
            else:
                result.insert(i-d, cur)
                d += 1
            cur += 1
        return result