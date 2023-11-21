from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # count = 0
        # visited = set()
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         num1, num2 = nums[i], nums[j]
        #         if (num1, num2) not in visited and (num2, num1) not in visited:
        #             if num1+int(str(num2)[::-1]) == int(str(num1)[::-1])+num2:
        #                 visited.add((i, j))
        #                 count += 1
        # return count
        store = {}
        for i in range(len(nums)):
            diff = nums[i]-int(str(nums[i])[::-1])
            if diff not in store:
                store[diff] = 0
            store[diff] += 1
        count = 0
        for k, v in store.items():
            count += (v*(v-1)//2)
        return count % ((10**9) + 7)