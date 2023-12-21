from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        s1, s2 = float('inf'), float('inf')
        for price in prices:
            if price < s1:
                s2 = s1
                s1 = price
            elif price < s2:
                s2 = price
        return money-(s1+s2) if s1+s2 <= money else money