class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        arr.sort()
        prevDiff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            newDiff = arr[i] - arr[i-1]
            if newDiff != prevDiff:
                return False
        return True