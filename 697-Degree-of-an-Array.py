class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        store = {}
        for i in range(len(nums)):
            if nums[i] in store:
                store[nums[i]][0] += 1
                store[nums[i]][2] = i
            else:
                store[nums[i]] = [1, i, i]
        maxi, mini = 0, 50000
        print(store)
        for k in store.keys():
            if store[k][0] > maxi:
                maxi = store[k][0]
                mini = store[k][2]-store[k][1]+1
            if store[k][0] == maxi:
                mini = min(mini, store[k][2]-store[k][1]+1)
        return mini