class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips, ones = 0, 0
        for digit in s:
            if digit == "0":
                flips += 1
            else:
                ones += 1
            flips = min(flips, ones)
        return flips