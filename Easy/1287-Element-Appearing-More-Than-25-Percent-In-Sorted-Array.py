from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4
        prev = 'x'
        count = 0
        for i in range(len(arr)):
            if arr[i] == prev:
                count += 1
                if count > threshold:
                    return arr[i]
            else:
                prev = arr[i]
                count = 1
        return arr[-1]