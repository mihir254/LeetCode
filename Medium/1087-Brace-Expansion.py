class Solution:
    def expand(self, s):
        ans, l, i = [""], len(s), 0
        while i < l:
            if s[i] == "{":
                j = i+1
                while not s[j] == "}":
                    j += 1
                temp = s[i+1:j].split(",")
                ans *= len(temp)
                u = 0
                while u < len(ans):
                    for k in temp:
                        te = len(ans)//len(temp)
                        for _ in range(te):
                            ans[u] += k
                            u += 1
                i = j
            elif s[i] == "}":
                i += 1
                continue
            else:
                for p in range(len(ans)):
                    ans[p] += s[i]
                i += 1
        ans.sort()
        return ans