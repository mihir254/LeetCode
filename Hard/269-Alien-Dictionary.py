from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        uniq = set("".join(words))
        child = {}
        parents = {}
        for x in list(uniq):
            child[x] = set()
            parents[x] = 0
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            n = min(len(w1), len(w2))
            found = False
            for j in range(n):
                if w1[j] != w2[j]:
                    found = True
                    if w2[j] not in child[w1[j]]:
                        child[w1[j]].add(w2[j])
                        parents[w2[j]] += 1
                    break
            if not found and len(w2) < len(w1):
                return ""
        ans = []
        queue = [k for k,v in parents.items() if v == 0]
        while queue:
            node = queue.pop(0)
            ans.append(node)
            for x in child[node]:
                parents[x] -= 1
                if parents[x] == 0:
                    queue.append(x)
        if len(ans) != len(list(uniq)):
            return ""
        return ''.join(ans)