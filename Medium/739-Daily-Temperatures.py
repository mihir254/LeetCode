from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                x = stack.pop()
                answer[x[1]] = i - x[1]
            stack.append([temperatures[i], i])
        return answer