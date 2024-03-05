import bisect

class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        ans = -1
        if n % 2 == 1:
            mid = n // 2
            ans = self.nums[mid]
        else:
            mid1, mid2 = (n // 2) - 1, n // 2
            ans = (self.nums[mid1] + self.nums[mid2]) / 2
        return ans

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()