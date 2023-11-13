from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[position[i], speed[i]] for i in range(len(position))]
        arr.sort(reverse=True, key=lambda x:x[0])
        stack = []
        for i in range(len(arr)):
            time = (target-arr[i][0])/arr[i][1]
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)