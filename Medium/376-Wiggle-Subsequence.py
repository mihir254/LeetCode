class Solution:
    def wiggleMaxLength(self, nums) -> int:
        prev_diff = 0
        count = 1
        
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 0 or (diff < 0 and prev_diff == '<') or (diff > 0 and prev_diff == '>'):
                continue
            else:
                count += 1
                prev_diff = '<' if diff < 0 else '>'
        
        return count