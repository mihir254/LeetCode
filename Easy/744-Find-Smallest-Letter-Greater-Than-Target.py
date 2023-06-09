class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        targetNumber = ord(target)
        nums = [ord(x) for x in letters]
        index = self.bs(nums, targetNumber)
        if index == -1:
            return letters[0]
        return letters[index]
        
    def bs(self, nums, tgt):
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] > tgt:
                if m == 0 or nums[m-1] <= tgt:
                    return m
                else:
                    r = m - 1
            else:
                l = m + 1
        return -1