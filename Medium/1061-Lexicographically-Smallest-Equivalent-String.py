class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent, group = {}, {}
        for i in range(len(s1)):
            if s1[i] not in parent and s2[i] not in parent:
                if ord(s1[i]) < ord(s2[i]):
                    parent[s1[i]] = s1[i]
                    parent[s2[i]] = s1[i]
                    group[s1[i]] = set([s1[i], s2[i]])
                else:
                    parent[s1[i]] = s2[i]
                    parent[s2[i]] = s2[i]
                    group[s2[i]] = set([s1[i], s2[i]])
            elif s1[i] not in parent:
                if ord(s1[i]) < ord(parent[s2[i]]):
                    original_parent = parent[s2[i]]
                    original_group = group[original_parent]
                    group.pop(original_parent, 'None')
                    group[s1[i]] = set([s1[i]])
                    parent[s1[i]] = s1[i]
                    for element in original_group:
                        parent[element] = s1[i]
                        group[s1[i]].add(element)
                else:
                    parent[s1[i]] = parent[s2[i]]
                    group[parent[s2[i]]].add(s1[i])
            elif s2[i] not in parent:
                if ord(s2[i]) < ord(parent[s1[i]]):
                    original_parent = parent[s1[i]]
                    original_group = group[original_parent]
                    group.pop(original_parent, 'None')
                    group[s2[i]] = set(s2[i])
                    parent[s2[i]] = s2[i]
                    for element in original_group:
                        parent[element] = s2[i]
                        group[s2[i]].add(element)
                else:
                    parent[s2[i]] = parent[s1[i]]
                    group[parent[s1[i]]].add(s2[i])
            else:
                if ord(parent[s1[i]]) < ord(parent[s2[i]]):
                    original_parent = parent[s2[i]]
                    original_group = group[original_parent]
                    for element in original_group:
                        parent[element] = parent[s1[i]]
                        group[parent[s1[i]]].add(element)
                    if parent[s1[i]] != parent[s2[i]]:
                        group.pop(original_parent, 'None')
                else:
                    original_parent = parent[s1[i]]
                    original_group = group[original_parent]
                    for element in original_group:
                        parent[element] = parent[s2[i]]
                        group[parent[s2[i]]].add(element)
                    if parent[s1[i]] != parent[s2[i]]:
                        group.pop(original_parent, 'None')
        answer = []
        for character in baseStr:
            if character in parent:
                answer.append(parent[character])
            else:
                answer.append(character)
        return "".join(answer)