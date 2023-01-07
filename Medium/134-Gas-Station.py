class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        stations = len(gas)
        total, current = 0, 0
        start = 0
        for i in range(stations):
            total += gas[i] - cost[i]
            current += gas[i] - cost[i]
            if current < 0:
                current = 0
                start = i + 1
        return -1 if total < 0 else start