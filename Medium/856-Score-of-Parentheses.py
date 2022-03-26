class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack, count = [], 0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(s[i])
            else:
                stack.pop()
                if i > 0:
                    if s[i-1]=="(":
                        count += 2**len(stack)
        return count