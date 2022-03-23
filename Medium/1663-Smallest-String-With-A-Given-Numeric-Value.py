class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans, k, i = ['a']*n, k-n, n-1
        while k > 0:
            if k//26 > 0:
                ans[i] = 'z'
                k -= 25
                i -= 1
            else:
                ans[i] = chr(ord('a')+k)
                k = 0
        return "".join(ans)