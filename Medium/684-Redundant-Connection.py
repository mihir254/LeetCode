from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        children = {}
        for edge in edges:
            n1, n2 = edge
            if n1 not in parent and n2 not in parent:
                parent[n1] = n1
                parent[n2] = n1
                children[n1] = [n1, n2]
            elif n1 not in parent:
                parent[n1] = parent[n2]
                children[parent[n2]].append(n1)
            elif n2 not in parent:
                parent[n2] = parent[n1]
                children[parent[n1]].append(n2)
            else:
                if parent[n1] == parent[n2]:
                    return edge
                p1, p2 = parent[n1], parent[n2]
                c1, c2 = children[p1], children[p2]
                if len(c1) >= len(c2):
                    for child in children[p2]:
                        parent[child] = p1
                        children[p1].append(child)
                    children.pop(p2, None)
                else:
                    for child in children[p1]:
                        parent[child] = p2
                        children[p2].append(child)
                    children.pop(p1, None)
        return []