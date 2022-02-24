class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ans = max(ans, self.helper(s, i, i), self.helper(s, i, i+1), key=len)
        return ans
    def helper(self, st, l, r):
        while l >= 0 and r < len(st) and st[l]==st[r]:
            l -= 1
            r += 1
        return st[l+1:r]