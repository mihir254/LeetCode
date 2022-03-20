class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        store_d, answer, ass_bike = {}, [-1]*len(workers), []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                if abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1]) not in store_d:
                    store_d[abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])] = []
                store_d[abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])].append([i, j])
        for k in sorted(store_d.keys()):
            for vals in store_d[k]:
                if answer[vals[0]] == -1 and vals[1] not in ass_bike:
                    answer[vals[0]] = vals[1]
                    ass_bike.append(vals[1])
            if -1 not in answer:
                return answer
        return answer