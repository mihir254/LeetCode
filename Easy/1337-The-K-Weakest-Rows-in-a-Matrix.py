class Solution:
    def kWeakestRows(self, mat, k):
        store = {}
        for i in range(len(mat[0])+1):
            store[i] = []
        for i in range(len(mat)):
            s = sum(mat[i])
            store[s].append(i)
        count, ans = 0, []
        for key in store.keys():
            if len(store[key]) > 0:
                for i in store[key]:
                    ans.append(i)
                    count += 1
                    if count == k:
                        return ans