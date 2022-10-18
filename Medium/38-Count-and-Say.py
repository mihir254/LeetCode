class Solution:
    def countAndSay(self, n):
        s = "1"
        for _ in range(1, n):
            count = 1
            arr = []
            i = 1
            prev = s[0]
            while i < len(s):
                if s[i] == prev:
                    count += 1
                else:
                    arr.append([prev, count])
                    prev = s[i]
                    count = 1
                i += 1
            arr.append([prev, count])
            newS = ""
            for ele in arr:
                newS = newS + str(ele[1]) + ele[0]
            s = newS
        return s