from collections import Counter
class Solution:
    def minSetSize(self, arr) -> int:
        count = Counter(arr)
        cnt, dels, l = 0, 0, len(arr)
        for i, j in count.most_common():
            if dels >= l//2:
                return cnt
            dels += j
            cnt += 1
        return cnt