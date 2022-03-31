class Solution:
    def splitArray(self, nums, m: int) -> int:
        low, high, answer = max(nums), sum(nums), -1
        while low <= high:
            mid = (low+high)//2
            if self.checker(mid, m, nums):
                answer = mid
                high = mid-1
            else:
                low = mid+1
        return answer
    def checker(self, mid, m, nums):
        parts, check_sum = 0, 0
        for num in nums:
            check_sum += num
            if check_sum > mid:
                parts += 1
                check_sum = num
        parts+=1
        return parts<=m