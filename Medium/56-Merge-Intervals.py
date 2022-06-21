class Solution:
    def merge(self, intervals):
        l = sorted(intervals, key = lambda x:(x[0], x[1]))
        res = []
        for i in range(len(l)):
            low, high = l[i][0], l[i][1]
            if res and low <= res[-1][1]:
                res[-1][1] = max(res[-1][1], high)
            else:
                res.append([low, high])
        return res