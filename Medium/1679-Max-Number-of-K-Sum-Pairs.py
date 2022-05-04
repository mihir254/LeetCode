class Solution:
    def maxOperations(self, nums, k: int) -> int:
        count, left, right = 0, 0, len(nums)-1
        nums.sort()
        
        while left < right:
            sumo = nums[left] + nums[right]
            if sumo < k:
                left += 1
            elif sumo > k:
                right -= 1
            else:
                nums.pop(left)
                right -= 1
                nums.pop(right)
                right -= 1
                count += 1
        
        return count