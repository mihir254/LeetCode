class Solution:
    def trap(self, height) -> int:
        if len(height) < 3:
            return 0
        water = 0
        leftPointer, rightPointer = 0, len(height)-1
        leftWall, rightWall = height[leftPointer], height[rightPointer]
        while leftPointer <= rightPointer:
            if height[leftPointer] > leftWall:
                leftWall = height[leftPointer]
            if height[rightPointer] > rightWall:
                rightWall = height[rightPointer]
            if leftWall <= rightWall:
                water += leftWall - height[leftPointer]
                leftPointer += 1
            else:
                water += rightWall - height[rightPointer]
                rightPointer -= 1
        return water