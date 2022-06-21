class Solution:
    def insert(self, intervals, newInterval):
        f, l = 0, 0
        while f < len(intervals):
            if intervals[f][1] >= newInterval[0]:
                break
            else:
                f += 1
        if f == len(intervals):
            intervals.append(newInterval)
            return intervals
        l = f
        while l < len(intervals):
            if intervals[l][0] > newInterval[1]:
                break
            else:
                l += 1
        res = []
        for i in range(f):
            res.append(intervals[i])
        if l == f:
            res.append(newInterval)
        else:
            res.append([min(intervals[f][0], newInterval[0]), max(newInterval[1], intervals[l-1][1])])
        for i in range(l, len(intervals)):
            res.append(intervals[i])
        res.sort(key=lambda x:x[0])
        return res