class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         return self.helper(cardPoints, k)
    
#     def helper(self, arr, steps):
#         if steps <= 0:
#             return
#         if steps == 1:
#             return max(arr[0], arr[-1])
#         else:
#             return max(arr[0]+self.helper(arr[1:], steps-1), arr[-1]+self.helper(arr[:-1], steps-1))
    def maxScore(self, cardPoints, k):
        window = len(cardPoints) - k
        total_points = sum(cardPoints)
        window_sum = sum(cardPoints[:window])
        ans = total_points - window_sum
        for i in range(1, k+1):
            window_sum = window_sum + cardPoints[window+i-1] - cardPoints[i-1]
            ans = max(ans, total_points - window_sum)
        return ans