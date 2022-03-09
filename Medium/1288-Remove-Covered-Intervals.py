class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        count, prev_end = 0, -1
        intervals.sort(key=lambda x:(x[0], -x[1]))
        for i in range(len(intervals)):
            if prev_end < intervals[i][1]:
                prev_end = intervals[i][1]
                count += 1
        return count