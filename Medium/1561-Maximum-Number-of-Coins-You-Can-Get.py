from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        answer = 0
        while piles:
            piles.pop()
            answer += piles.pop()
            piles.pop(0)
        return answer