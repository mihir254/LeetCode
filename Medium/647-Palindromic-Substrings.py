class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.help(s, i, i)+self.help(s, i, i+1)
        return res
    def help(self, subs, l, r):
        ans = 0
        while l >= 0 and r < len(subs) and subs[l] == subs[r]:
            l -= 1
            r += 1
            ans += 1
        return ans