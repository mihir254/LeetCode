class Solution:
    def combinationSum4(self, nums, target):
        res = 0
        store = {}
        
        def rec(remain):
            if remain == 0:
                return 1
            if remain in store:
                return store[remain]
            count = 0
            for num in nums:
                if remain-num >= 0:
                    count += rec(remain-num)
            store[remain] = count
            return count
        
        for i in nums:
            if target-i in store:
                res += store[target-i]
            else:
                res += rec(target-i)
        
        return res