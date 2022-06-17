class Solution:
    def canJump(self, nums):
        cur, fin = 0, len(nums)-1
        if fin == 0:
            return True
        
        max_pos = 0
        
        for i in range(len(nums)):
            max_pos = max(max_pos, i+nums[i])
            print(i, max_pos)
            if i >= max_pos and i!=fin:
                return False
        
        return False if max_pos < fin else True