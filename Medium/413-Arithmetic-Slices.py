class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        diff = []
        for i in range(len(nums)-1):
            diff.append(nums[i+1]-nums[i])
        streak, checker = 0, []
        for i in range(len(diff)-1):
            if diff[i+1]==diff[i]:
                streak += 1
                checker.append(streak)
            else:
                streak = 0
        return sum(checker)