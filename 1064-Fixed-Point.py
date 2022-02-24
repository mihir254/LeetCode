class Solution:
    def fixedPoint(self, arr) -> int:
        l, r = 0, len(arr)-1
        while l < r:
            m = (l+r)//2
            if arr[m] < m:
                l = m+1
            else:
                r = m
        if arr[l] == l:
            return l
        return -1