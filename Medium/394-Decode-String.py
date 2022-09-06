class Solution:
    def decodeString(self, s):
        stack = []
        num, st = 0, ''
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == "[":
                stack.append(st)
                stack.append(num)
                num = 0
                st = ''
            elif c == "]":
                mul = stack.pop()
                prev_st = stack.pop()
                st = prev_st + mul*st
                num = 0
            else:
                st += c
        return st