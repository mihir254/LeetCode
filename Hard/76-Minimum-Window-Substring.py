class Solution:
    def minWindow(self, s: str, t: str) -> str:
        store = {}
        for letter in t:
            if letter not in store:
                store[letter] = 0
            store[letter] += 1
        window = len(t)
        if len(s) < window:
            return ""
        start, end = 0, len(t)-1
        first_subArray = s[start:end+1]
        check = {}
        toFind = len(t)
        ans = ""
        for letter in first_subArray:
            if letter in store:
                if letter not in check:
                    check[letter] = 1
                    toFind -= 1
                else:
                    if store[letter] > check[letter]:
                        toFind -= 1
                    check[letter] += 1
        while start <= len(s) - window:
            if toFind == 0 or end == len(s)-1:
                if toFind == 0:
                    if ans == "":
                        ans = s[start:end+1]
                    else:
                        ans = ans if len(ans)<len(s[start:end+1]) else s[start:end+1]
                if s[start] in check:
                    check[s[start]] -= 1
                    if check[s[start]] < store[s[start]]:
                        toFind += 1
                start += 1
                continue
            end += 1
            if s[end] in store:
                if s[end] not in check:
                    check[s[end]] = 1
                    toFind -= 1
                else:
                    if store[s[end]] > check[s[end]]:
                        toFind -= 1
                    check[s[end]] += 1
        return ans
