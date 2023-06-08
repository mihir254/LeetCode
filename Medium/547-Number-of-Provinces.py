class Solution:
    def findCircleNum(self, isConnected) -> int:
        graph = {}
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    if i not in graph:
                        graph[i] = set()
                    graph[i].add(j)
                    if j not in graph:
                        graph[j] = set()
                    graph[j].add(i)
        parentToChild, childToParent = {}, {}
        for k,v in graph.items():
            for n in list(v):
                if k not in childToParent and n not in childToParent:
                    parentToChild[k] = set([k, n])
                    childToParent[k] = k
                    childToParent[n] = k
                elif k not in childToParent and n in childToParent:
                    parentOfn = childToParent[n]
                    parentToChild[parentOfn].add(k)
                    childToParent[k] = parentOfn
                elif n not in childToParent and k in childToParent:
                    parentOfk = childToParent[k]
                    parentToChild[parentOfk].add(n)
                    childToParent[n] = parentOfk
                else:
                    parentOfn, parentOfk = childToParent[n], childToParent[k]
                    if parentOfn != parentOfk:
                        lenN, lenK = len(list(parentToChild[parentOfn])), len(list(parentToChild[parentOfk]))
                        if lenK >= lenN:
                            for node in list(parentToChild[parentOfn]):
                                childToParent[node] = parentOfk
                                parentToChild[parentOfk].add(node)
                            parentToChild.pop(parentOfn, None)
                        else:
                            for node in list(parentToChild[parentOfk]):
                                childToParent[node] = parentOfn
                                parentToChild[parentOfn].add(node)
                            parentToChild.pop(parentOfk, None)
        count = 0
        for k,v in parentToChild.items():
            count += 1
        return count