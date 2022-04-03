class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            flag = 0
            if nums[-1] > nums[-2]:
                nums[-1], nums[-2] = nums[-2], nums[-1]
            else:
                p1, p2 = len(nums)-1, len(nums)-2
                while nums[p1] <= nums[p2]:
                    if p2 == 0 and nums[p1] <= nums[p2]:
                        nums[:] = nums[::-1]
                        flag = 1
                        break
                    p1-=1
                    p2-=1
                if flag == 0:
                    p1 = len(nums)-1
                    while nums[p1] <= nums[p2]:
                        p1 -= 1
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 = len(nums)-1
                    p2+=1
                    while p1>p2:
                        if nums[p1] < nums[p2]:
                            nums[p1], nums[p2] = nums[p2], nums[p1]
                        p1 -= 1
                        p2 += 1