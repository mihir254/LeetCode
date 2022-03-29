class Solution:
    def findDuplicate(self, nums) -> int:
        nums.sort()
        cur, pre = 0, 0
        for i in nums:
            if cur^i == pre:
                return i
            pre = cur
            cur ^= i