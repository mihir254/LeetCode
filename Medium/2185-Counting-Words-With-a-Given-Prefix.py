class Solution:
    def prefixCount(self, words, pref: str) -> int:
        l, count = len(pref), 0
        for word in words:
            if len(word) >= l:
                if word[:l] == pref:
                    count += 1
        return count