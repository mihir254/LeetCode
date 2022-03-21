class Solution:
    def partitionLabels(self, s: str) -> int:
        store = {}
        for i in range(len(s)):
            if s[i] not in store:
                store[s[i]] = []
            store[s[i]].append(i)
        answer, s, e = [], -1, -1
        for key in store.keys():
            if store[key][0] > e:
                answer.append(e-s+1)
                s = store[key][0]
                e = store[key][-1]
            elif store[key][-1] > e:
                e = store[key][-1]
        answer.append(e-s+1)
        return answer[1:]