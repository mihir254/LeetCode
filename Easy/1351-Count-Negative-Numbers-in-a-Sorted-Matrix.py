# Binary Search => O(m.logn), O(1)

# class Solution:
#     def countNegatives(self, grid) -> int:
#         rows, cols = len(grid), len(grid[0])
#         count = 0
#         for row in range(rows):
#             firstNeg = self.binarySearch(grid[row])
#             if firstNeg != -1:
#                 count += len(grid[row]) - firstNeg
#         return count
    
#     def binarySearch(self, nums):
#         l, r = 0, len(nums)-1
#         while l <= r:
#             m = (r+l)//2
#             if nums[m] < 0 and (m == 0 or nums[m-1] >= 0):
#                 return m
#             if nums[m] >= 0:
#                 l = m+1
#             else:
#                 r = m-1
#         return -1


# Linear Traversal => O(m + n), O(1)

class Solution:
    def countNegatives(self, grid) -> int:
        count = 0
        n = len(grid[0])
        curNegIndex = n-1
        for i in range(len(grid)):
            while curNegIndex >= 0 and grid[i][curNegIndex] < 0:
                curNegIndex -= 1
            count += (n - (curNegIndex + 1))
        return count