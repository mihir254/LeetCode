from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_ind = []
        b_ind = []
        i = 0
        while i < (len(s)-len(a)+1):
            if s[i:i+len(a)] == a:
                a_ind.append(i)
                i += len(a)
            else:
                i += 1
        i = 0
        while i < (len(s)-len(b)+1):
            if s[i:i+len(b)] == b:
                b_ind.append(i)
                i += len(b)
            else:
                i += 1
        ans = []
        i, j = 0, 0
        while i < len(a_ind) and j < len(b_ind):
            if abs(a_ind[i]-b_ind[j]) <= k:
                ans.append(a_ind[i])
                i += 1
            elif a_ind[i] > b_ind[j]:
                j += 1
            else:
                i += 1
        return ans