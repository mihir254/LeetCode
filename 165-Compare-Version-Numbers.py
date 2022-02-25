class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        if len(v2) > len(v1):
            for _ in range(len(v2)-len(v1)):
                v1.append(0)
        if len(v2) < len(v1):
            for _ in range(len(v1)-len(v2)):
                v2.append(0)
        v = max(len(v1), len(v2))
        for i in range(v):
            if v1[i] > v2[i]:
                return 1
            if v1[i] < v2[i]:
                return -1
        return 0