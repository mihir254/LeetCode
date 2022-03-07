class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 6
        dp = [0]*n
        dp[0], dp[1] = 1, 6
        for i in range(2, n):
            mult = (i+1)*2 - 1
            mul = (mult*(mult+1))//2
            dp[i] = (dp[i-1]*mul)%mod
        return dp[n-1]