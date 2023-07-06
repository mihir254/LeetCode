class Solution:
    def longestSubarray(self, nums) -> int:
        arr = []
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == 0:
                if count != 0:
                    arr.append(count)
                    count = 0
                arr.append(0)
            else:
                count += 1
            i += 1
        if count != 0:
            arr.append(count)
        if len(arr) == 1:
            return arr[0]-1 if arr[0] > 0 else arr[0]
        maxi = 0
        for i in range(len(arr)):
            prev, nxt = 0, 0
            if i-1 >= 0:
                prev = arr[i-1]
            if i+1 < len(arr):
                nxt = arr[i+1]
            maxi = max(maxi, prev+nxt)
        return maxi