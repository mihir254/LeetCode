class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l+r)//2
            if arr[m-1] < arr[m] and arr[m] > arr[m+1]:
                return m
            if arr[m-1] < arr[m] and arr[m] < arr[m+1]:
                l = m + 1
            elif arr[m-1] > arr[m] and arr[m] > arr[m+1]:
                r = m
        return l