from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            n = len(ans)
            for i in range(n):
                newOne = ans[i]+[num]
                newOne.sort()
                if newOne not in ans:
                    ans.append(newOne)
        return ans