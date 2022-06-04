class Solution:
    def search(self, nums, target) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid=(low+high)//2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        rot = low
        l, r = 0, len(nums)-1
        if target >= nums[rot] and target <= nums[r]:
            l = rot
        else:
            r = rot
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] <= target:
                l = m+1
            else:
                r = m-1
        return -1