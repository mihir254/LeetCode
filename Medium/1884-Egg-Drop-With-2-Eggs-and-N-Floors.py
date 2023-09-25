class Solution:
    def twoEggDrop(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += 1
            n -= ans
        return ans