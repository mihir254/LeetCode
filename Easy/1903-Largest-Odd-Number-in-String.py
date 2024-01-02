class Solution:
    def largestOddNumber(self, num: str) -> str:
        s = [x for x in num]
        while s:
            if int(s[-1]) % 2 == 1:
                return "".join(s)
            s.pop()
        return ""