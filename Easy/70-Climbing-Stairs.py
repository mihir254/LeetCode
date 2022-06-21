class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {0:0, 1:1, 2:2}
        self.helper(n, mem)
        return mem[n]
    def helper(self, n, mem):
        if n not in mem:
            mem[n] = self.helper(n-1, mem)+self.helper(n-2, mem)
        return mem[n]