class Solution:
    def earliestAcq(self, logs, n: int) -> int:
        store = {}
        leader = {}
        logs.sort(key=lambda x:x[0])
        print(logs)
        for log in logs:
            time, person1, person2 = log[0], log[1], log[2]
            if person1 not in store and person2 not in store:
                store[person1] = person1
                store[person2] = person1
                leader[person1] = set({person1, person2})
                if len(leader[person1]) == n:
                    return time
            elif person1 in store and person2 not in store:
                store[person2] = store[person1]
                leader[store[person1]].add(person2)
                if len(leader[store[person1]]) == n:
                    return time
            elif person1 not in store and person2 in store:
                store[person1] = store[person2]
                leader[store[person2]].add(person1)
                if len(leader[store[person2]]) == n:
                    return time
            else:
                if store[person1] == store[person2]:
                    continue
                len1 = len(leader[store[person1]])
                len2 = len(leader[store[person2]])
                if len2 < len1:
                    to_change = list(leader[store[person2]])
                    leader[store[person1]].update(leader[store[person2]])
                    leader[store[person2]].clear()
                    for person in to_change:
                        store[person] = store[person1]
                    if len(leader[store[person1]]) == n:
                        return time
                else:
                    to_change = list(leader[store[person1]])
                    leader[store[person2]].update(leader[store[person1]])
                    leader[store[person1]].clear()
                    for person in to_change:
                        store[person] = store[person2]
                    if len(leader[store[person2]]) == n:
                        return time
        return -1