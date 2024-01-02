class Solution:
    def totalMoney(self, n: int) -> int:
        completeWeeks = n // 7
        sumOfPreviousWeeks = 0
        for x in range(completeWeeks):
            sumOfPreviousWeeks += 7*(x + 4)
        offsetDays = n % 7
        value = completeWeeks + 1
        res = sumOfPreviousWeeks
        for _ in range(offsetDays):
            res += value
            value += 1
        return res