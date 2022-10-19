class Solution:
    def topKFrequent(self, words, k):
        store = {}
        for word in words:
            store[word] = store.get(word, 0) + 1
        l = [[key, val] for key, val in store.items()]
        l.sort(key = lambda x: (-x[1], x[0]))
        return [l[i][0] for i in range(k)]