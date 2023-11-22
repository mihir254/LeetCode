from typing import List
# Store Tuple and Sort -> Time: O((m+n)log(m+n)), Space: O(m+n)
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                answer.append((i+j, i, nums[i][j]))
        answer.sort(key=lambda x:(x[0], -x[1]))
        return [x for (_, _, x) in answer]

# Arrange according to row, column sum in array or hashmap -> Time: O(m*n), Space: O(m+n)
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if len(answer) <= i+j:
                    answer.append([])
                answer[i+j].insert(0, nums[i][j])
        return [answer[x][y] for x in range(len(answer)) for y in range(len(answer[x]))]

# Look at it as a tree with root at (0,0) and then visit node, left, right (pre-order) -> Time: O(m+n), Space: O(m+n)
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = [[0, 0]]
        answer = []
        while queue:
            row, col = queue.pop(0)
            answer.append(nums[row][col])
            if col == 0 and row+1<len(nums):
                queue.append([row+1, col])
            if col+1<len(nums[row]):
                queue.append([row, col+1])
        return answer