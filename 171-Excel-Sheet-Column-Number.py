class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, i, l = 0, 0, len(columnTitle)-1
        while i < l:
            ans += ((26**(l-i))*(ord(columnTitle[i])-ord("A")+1))
            i += 1
        ans += ord(columnTitle[i])-ord("A")+1
        return ans