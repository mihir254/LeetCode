class Solution:
    def combine(self, n: int, k: int):
        answer = []
        for i in range(1, n+1):
            self.combination(i, [i], k, answer, n)
        return answer
    def combination(self, val, cur, k, answer, n):
        if len(cur) == k:
            answer.append(cur)
            return
        for i in range(val+1, n+1):
            self.combination(i, cur+[i], k, answer, n)