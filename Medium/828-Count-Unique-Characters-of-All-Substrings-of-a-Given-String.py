# from collections import Counter
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # store, ans = {}, 0
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         substr = s[i:j]
        #         if substr in store:
        #             ans += store[substr]
        #         else:
        #             uniques = 0
        #             counter = Counter(substr)
        #             for k, v in counter.items():
        #                 if v == 1:
        #                     uniques += 1
        #             store[substr] = uniques
        #             ans += uniques
        # return ans
        store = {}
        for i in range(len(s)):
            if s[i] not in store:
                store[s[i]] = [-1, len(s)]
            store[s[i]].insert(-1, i)
        ans = 0
        for k, v in store.items():
            for i in range(1, len(v)-1):
                ans += (v[i]-v[i-1])*(v[i+1]-v[i])
        st = "828. Count Unique Characters of All Substrings of a Given String"
        return ans