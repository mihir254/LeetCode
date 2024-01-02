from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cols = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(cols) <= j:
                    cols.append([])
                cols[j].append(mat[i][j])
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(cols[j]) == 1:
                    res += 1
        return res