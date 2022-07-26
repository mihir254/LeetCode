from collections import Counter
class Solution:
    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        letters = [i for i in counter.keys()]
        for i in range(len(letters)):
            for j in range(len(letters)):
                if i != j:
                    ans = 0
                    has_i, has_j = False, False
                    remain_i, remain_j = counter[letters[i]], counter[letters[j]]
                    for letter in s:
                        if letter!=letters[i] and letter!=letters[j]:
                            continue
                        if ans < 0 and remain_i != 0 and remain_j != 0:
                            ans = 0
                            has_i, has_j = False, False
                        if letter==letters[i]:
                            ans += 1
                            has_i = True
                            remain_i -= 1
                        elif letter==letters[j]:
                            ans -= 1
                            has_j = True
                            remain_j -= 1
                        if has_i and has_j:
                            res = max(res, abs(ans))
        return res