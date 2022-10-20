class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums)-1
        p = 0
        while p <= p2:
            if nums[p] == 0:
                nums[p0], nums[p] = nums[p], nums[p0]
                p0 += 1
                p += 1
            elif nums[p] == 1:
                p += 1
            else:
                nums[p2], nums[p] = nums[p], nums[p2]
                p2 -= 1