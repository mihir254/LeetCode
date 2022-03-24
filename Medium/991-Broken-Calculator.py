class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        count = 0
        while y > x:
            if y%2 != 0:
                y += 1
            else:
                y //= 2
            count += 1
        return count+x-y