import math
class Solution:
    def minSpeedOnTime(self, dist, hour: float) -> int:
        l, r = 1, 10**9
        answer = -1
        while l <= r:
            m = (l+r)//2
            required = 0
            for i in range(len(dist)-1):
                required += math.ceil(dist[i] / m)
            required += dist[-1] / m
            if required <= hour:
                answer = m
                r = m - 1
            else:
                l = m + 1
        return answer