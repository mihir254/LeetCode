class Solution:
    def groupAnagrams(self, strs):
        result, store = [], {}
        for s in strs:
            if "".join(sorted(s)) not in store:
                store["".join(sorted(s))] = []
            store["".join(sorted(s))].append(s)
        for v in store.values():
            result.append(v)
        return result