class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        i = 1
        while i<len(s):
            if stack:
                prev = stack[-1]
                if ord(prev)-ord('a')==ord(s[i])-ord('A') or ord(prev)-ord('A')==ord(s[i])-ord('a'):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)