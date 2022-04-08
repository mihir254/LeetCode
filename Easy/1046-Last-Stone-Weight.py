class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) > 1:
            stones.sort()
            if stones[-2] == stones[-1]:
                stones.pop()
                stones.pop()
            else:
                stones[-2] = stones[-1]-stones[-2]
                stones.pop()
        if not stones:
            return 0
        else:
            return stones[0]