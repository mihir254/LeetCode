from collections import Counter
class Solution:
    def wordSubsets(self, words1, words2) -> List[str]:
        countB = Counter()
        for word in words2:
            countB |= Counter(word)
        return [a for a in words1 if not countB - Counter(a)]