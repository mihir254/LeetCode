from heapq import heapify, heappop, heappush


class Solution:
    def totalCost(self, costs, k: int, candidates: int) -> int:
        head, tail = costs[:candidates], costs[(max(candidates, len(costs) - candidates)):]
        head_next, tail_next = candidates, len(costs)-1-candidates
        heapify(head)
        heapify(tail)
        answer = 0
        for _ in range(k):
            if not tail or head and head[0] <= tail[0]:
                answer += heappop(head)
                if head_next <= tail_next:
                    heappush(head, costs[head_next])
                    head_next += 1
            else:
                answer += heappop(tail)
                if head_next <= tail_next:
                    heappush(tail, costs[tail_next])
                    tail_next -= 1
        return answer