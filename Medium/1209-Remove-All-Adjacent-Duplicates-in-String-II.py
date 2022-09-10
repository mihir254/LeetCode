class Solution:
    def removeDuplicates(self, s, k) -> str:
        n = len(s)
        if k > n:
            return s
        i = 0
        stack = []
        while i < n:
            if stack:
                letter, count = stack.pop()
                if letter == s[i] and count == k-1:
                    i += 1
                    continue
                elif letter == s[i]:
                    stack.append((letter, count+1))
                else:
                    stack.append((letter, count))
                    stack.append((s[i], 1))
            else:
                stack.append((s[i], 1))
            i += 1
        string = ""
        while stack:
            letter, count = stack.pop()
            tempString = count*letter
            string = tempString + string
        return string