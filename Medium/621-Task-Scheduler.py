from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        store = {}
        for task in tasks:
            if task not in store:
                store[task] = 0
            store[task] += 1
        q = [[k, v, 0] for k, v in store.items()]
        while q:
            q.sort(key=lambda x:(x[2], -x[1]))
            if q[0][2] > 0:
                time += 1
                for i in range(len(q)):
                    if q[i][2] > 0:
                        q[i][2] -= 1
                continue
            task, count, cd = q.pop(0)
            if count > 1:
                q.append([task, count-1, n])
            for i in range(len(q)):
                if q[i][0] != task and q[i][2] > 0:
                    q[i][2] -= 1
            time += 1
        return time