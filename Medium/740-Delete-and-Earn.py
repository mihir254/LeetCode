class Solution:
    def deleteAndEarn(self, nums: int) -> int:
        prev, cur, store = 0, 0, [0]*10001
        for num in nums:
            store[num] += num
        for num in store:
            prev, cur = cur, max(prev+num, cur)
        return cur