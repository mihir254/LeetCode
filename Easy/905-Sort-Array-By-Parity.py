class Solution:
    def sortArrayByParity(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            while nums[left]%2 == 0 and left < right:
                left += 1
            while nums[right]%2 == 1 and left < right:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums