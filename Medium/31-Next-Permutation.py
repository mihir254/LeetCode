class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            p1, p2 = len(nums)-1, len(nums)-2
            while p2 >= 0:
                if nums[p2] >= nums[p1]:
                    p2 -= 1
                    p1 -= 1
                else:
                    break
            if p2 < 0:
                nums[:] = nums[::-1]
            else:
                p1 = len(nums)-1
                while p1 > p2:
                    if nums[p1] <= nums[p2]:
                        p1 -= 1
                    else:
                        break
                nums[p2], nums[p1] = nums[p1], nums[p2]
                nums[:] = nums[:p2+1] + nums[p2+1:][::-1]