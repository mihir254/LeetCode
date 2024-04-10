from typing import List
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        queue = [i for i in range(n)]
        answer = []
        while queue:
            x = queue.pop(0)
            answer.append(x)
            if queue:
                y = queue.pop(0)
                queue.append(y)
        res = [-1]*n
        for i in range(n):
            res[answer[i]] = deck[i]
        return res