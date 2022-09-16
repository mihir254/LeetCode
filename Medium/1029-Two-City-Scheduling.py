class Solution:
    def twoCitySchedCost(self, costs) -> int:
        AtoB = []
        cost = 0
        for a,b in costs:
            AtoB.append(b-a)
            cost += a
        AtoB.sort()
        for i in range(len(costs)//2):
            cost += AtoB[i]
        return cost