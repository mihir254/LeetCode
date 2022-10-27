class Solution:
    def findLength(self, nums1, nums2):
        x, y = len(nums1), len(nums2)
        dp = [[0]*(y+1) for _ in range(x+1)]
        ans = 0
        for i in range(1, x+1):
            for j in range(1, y+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        return ans