class Solution:
    def longestConsecutive(self, nums) -> int:
        num_set = set(nums)
        count = 0
        for i in num_set:
            if i-1 not in num_set:
                counter = 1
                start = i
                while start+1 in num_set:
                    counter += 1
                    start += 1
                count = max(count, counter)
        return count