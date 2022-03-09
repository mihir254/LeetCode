from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        return (sum((c1-c2).values())) + (sum((c2-c1).values()))