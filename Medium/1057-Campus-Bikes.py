from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # old answer
        # store_d, answer, ass_bike = {}, [-1]*len(workers), []
        # for i in range(len(workers)):
        #     for j in range(len(bikes)):
        #         if abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1]) not in store_d:
        #             store_d[abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])] = []
        #         store_d[abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])].append([i, j])
        # for k in sorted(store_d.keys()):
        #     for vals in store_d[k]:
        #         if answer[vals[0]] == -1 and vals[1] not in ass_bike:
        #             answer[vals[0]] = vals[1]
        #             ass_bike.append(vals[1])
        #     if -1 not in answer:
        #         return answer
        # return answer

        # new answer
        pairs = []
        for wi, w in enumerate(workers):
            for bi, b in enumerate(bikes):
                distance = self.findDistance(w, b)
                pairs.append([wi, bi, distance])
        pairs.sort(key=lambda x:[x[2], x[0], x[1]])
        workersDone, bikesDone = set(), set()
        answer = [-1]*len(workers)
        for pair in pairs:
            if pair[0] not in workersDone and pair[1] not in bikesDone:
                answer[pair[0]] = pair[1]
                workersDone.add(pair[0])
                bikesDone.add(pair[1])
        return answer

    def findDistance(self, worker, bike):
        wx, wy = worker
        bx, by = bike
        return abs(wx-bx) + abs(wy-by)