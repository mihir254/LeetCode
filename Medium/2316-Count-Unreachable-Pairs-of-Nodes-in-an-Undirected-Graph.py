class Solution:
    def countPairs(self, n: int, edges) -> int:
        parentOf, childrenOf = {}, {}
        for edge in edges:
            node1, node2 = edge
            if node1 not in parentOf and node2 not in parentOf:
                parentOf[node1] = node1
                parentOf[node2] = node1
                childrenOf[node1] = [node1, node2]
            elif node2 not in parentOf:
                parentOf[node2] = parentOf[node1]
                childrenOf[parentOf[node1]].append(node2)
            elif node1 not in parentOf:
                parentOf[node1] = parentOf[node2]
                childrenOf[parentOf[node2]].append(node1)
            else:
                parentOfNode1, parentOfNode2 = parentOf[node1], parentOf[node2]
                if parentOfNode1 != parentOfNode2:
                    childrenSet1, childrenSet2 = childrenOf[parentOfNode1], childrenOf[parentOfNode2]
                    if len(childrenSet1) >= len(childrenSet2):
                        for child in childrenSet2:
                            parentOf[child] = parentOfNode1
                            childrenOf[parentOfNode1].append(child)
                        childrenOf.pop(parentOfNode2, None)
                    else:
                        for child in childrenSet1:
                            parentOf[child] = parentOfNode2
                            childrenOf[parentOfNode2].append(child)
                        childrenOf.pop(parentOfNode1, None)
        for i in range(n):
            if i not in parentOf:
                parentOf[i] = i
                childrenOf[i] = [i]
        answer = 0
        remaining = n
        for k,v in childrenOf.items():
            if remaining <= 0:
                return answer
            answer += (remaining-len(v))*len(v)
            remaining -= len(v)
        return answer