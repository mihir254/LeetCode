class Solution:
    def removeDuplicates(self, nums: int) -> int:
        uni, dupli = 0, 0
        while dupli < len(nums):
            if nums[uni] == nums[dupli]:
                dupli += 1
            else:
                uni += 1
                nums[uni], nums[dupli] = nums[dupli], nums[uni]
                dupli += 1
        return uni+1