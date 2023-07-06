class Solution:
    def __init__(self):
        self.ans = float('inf')
    def distributeCookies(self, cookies, k: int) -> int:
        if (len(cookies) == k):
            return max(cookies)
        self.recursion(0, [0]*k, cookies)
        return self.ans
    def recursion(self, i, score, cookies):
        if i == len(cookies):
            self.ans = min(self.ans, max(score))
            return
        if (max(score) >= self.ans):
            return
        for j in range(len(score)):
            score[j] += cookies[i]
            self.recursion(i+1, score, cookies)
            score[j] -= cookies[i]