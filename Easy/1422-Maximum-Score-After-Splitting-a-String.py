class Solution:
    def maxScore(self, s: str) -> int:
        maxi = 0
        ones = s.count("1")
        zeroes = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zeroes += 1
            elif s[i] == '1':
                ones -= 1
            maxi = max(maxi, ones + zeroes)
        return maxi