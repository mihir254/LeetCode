from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[0, heights[0]]]
        answer = 0
        for i in range(1, len(heights)):
            startIndex = i
            while stack and stack[-1][1] > heights[i]:
                ind, height = stack.pop()
                answer = max(answer, (i-ind)*height)
                startIndex = ind
            stack.append([startIndex, heights[i]])
        while stack:
            ind, height = stack.pop()
            answer = max(answer, (len(heights)-ind)*height)
        return answer