from collections import Counter
class Solution:
    def majorityElement(self, nums) -> int:
        counter = Counter(nums)
        return counter.most_common()[0][0]