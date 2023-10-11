from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Approach 1 - worst case Time complexity = O(n)

        # ind = -1
        # left, right = 0, len(nums)-1
        # ansLeft, ansRight = -1, -1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         ansLeft, ansRight = mid, mid
        #         while ansLeft > 0 and nums[ansLeft-1] == target:
        #             ansLeft -= 1
        #         while ansRight < len(nums)-1 and nums[ansRight+1] == target:
        #             ansRight += 1
        #         return [ansLeft, ansRight]
        #     if nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return [-1, -1]

        # Approach 2 - worst case Time complexity = O(logn)
        ansLeft = self.findBound(nums, target, "lower")
        if ansLeft == -1:
            return [-1, -1]
        ansRight = self.findBound(nums, target, "upper")
        return [ansLeft, ansRight]
    
    def findBound(self, arr, tgt, bound):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == tgt:
                if bound == "lower":
                    if mid == left or arr[mid-1] < tgt:
                        return mid
                    else:
                        right = mid-1
                else:
                    if mid == len(arr)-1 or arr[mid+1] > tgt:
                        return mid
                    else:
                        left = mid+1
            elif arr[mid] < tgt:
                left = mid + 1
            else:
                right = mid - 1
        return -1