class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        rows, cols = len(text1)+1, len(text2)+1
        for i in range(rows):
            dp.append([])
            for j in range(cols):
                dp[-1].append(0)
        for i in range(1, rows):
            for j in range(1, cols):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]