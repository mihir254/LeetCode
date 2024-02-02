from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def createSequence(curLen, curStart):
            if curStart+curLen > 9:
                return
            numString = "".join(digits[curStart:curStart+curLen])
            num = int(numString)
            if num < low or num > high:
                return
            ans.append(num)


        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ans = []
        lowDigits = len(str(low))
        highDigits = len(str(high))
        for j in range(lowDigits, highDigits+1):
            for i in range(1, 9):
                createSequence(j, i-1)
        return ans