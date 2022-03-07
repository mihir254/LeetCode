class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==0:
            return 0
        prev = [poured]
        while query_row > 0:
            cur = []
            cur.append(max((prev[0]-1)/2, 0))
            for i in range(1, len(prev)):
                cur.append(max((prev[i-1]-1)/2, 0)+max((prev[i]-1)/2, 0))
            cur.append(max((prev[-1]-1)/2, 0))
            prev = cur
            query_row -= 1
        return min(prev[query_glass], 1)