class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set([ch for ch in s])
        longest = 0
        for i, ch in enumerate(list(chars)):
            start, end = 0, 0
            parasites = []
            while end < len(s):
                if s[end] != ch:
                    parasites.append(end)
                    if len(parasites) > k:
                        start = parasites.pop(0)+1
                end += 1
                longest = max(longest, end-start)
        return longest