class Solution:
    def reverseWords(self, s: str) -> str:
        l = [w for w in s.strip().split()]
        return " ".join(l[::-1])