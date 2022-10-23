class Solution:
    def containsNearbyDuplicate(self, nums, k):
        store = {}
        for i in range(len(nums)):
            if nums[i] not in store:
                store[nums[i]] = []
            store[nums[i]].append(i)
        for key,v in store.items():
            if len(v) > 1:
                for i in range(1, len(v)):
                    if abs(v[i-1]-v[i]) <= k:
                        return True
        return False