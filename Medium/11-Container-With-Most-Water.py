class Solution:
    def maxArea(self, height) -> int:
        # Brute force - TLE
        # res = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         if height[i] > height[j]:
        #             if height[j]*(j-i) > res:
        #                 res = height[j]*(j-i)
        #         else:
        #             if height[i]*(j-i) > res:
        #                 res = height[i]*(j-i)
        # return res
        
        # 2 pointers better implementation
        res, left, right = 0, 0, len(height)-1
        while left < right:
            res = max (res, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res