class Solution:
    def findSubsequences(self, nums):
        answer = []
        store = set()
        self.helper(nums, 0, answer, [], store)
        return answer
    def helper(self, nums, start, answer, current, store):
        if start >= len(nums):
            if len(current) > 1 and tuple(current) not in store:
                store.add(tuple(current))
                answer.append(current)
            return
        if current:
            prev = current[-1]
            if nums[start] >= prev:
                self.helper(nums, start+1, answer, current+[nums[start]], store)
        else:
            self.helper(nums, start+1, answer, current+[nums[start]], store)
        self.helper(nums, start+1, answer, current, store)