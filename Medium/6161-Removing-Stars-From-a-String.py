class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        arr = []
        while i < len(s):
            if s[i] != "*":
                arr.append(s[i])
                i += 1
                continue
            else:
                if arr:
                    arr.pop()
                i += 1
        return "".join(arr)