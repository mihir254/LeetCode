class Solution:
    def minCost(self, nums, cost) -> int:
        def costFunction(num):
            sumo = 0
            for k,v in list(zip(nums, cost)):
                diff = abs(k-num)
                if diff != 0:
                    sumo += diff*v
            return sumo
        l, r = min(nums), max(nums)
        answer = 0
        while l < r:
            m = (r+l)//2
            cost1, cost2 = costFunction(m), costFunction(m+1)
            answer = min(cost1, cost2)
            if cost1 <= cost2:
                r = m
            else:
                l = m + 1
        return answer