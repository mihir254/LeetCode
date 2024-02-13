from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        invalid = 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    invalid += 1
        invalid += len(stack)
        ans = set()
        self.backtrack(s, invalid, ans, "", 0)
        return list(ans)

    def backtrack(self, s, n, ans, cur, start):
        if not s:
            if n == 0 and start == 0:
                ans.add(cur)
            return
        char = s[0]
        if char == "(":
            self.backtrack(s[1:], n, ans, cur+"(", start+1)
            if n > 0:
                self.backtrack(s[1:], n-1, ans, cur, start)
        elif char == ")":
            if start > 0:
                self.backtrack(s[1:], n, ans, cur+")", start-1)
            if n > 0:
                self.backtrack(s[1:], n-1, ans, cur, start)
        else:
            self.backtrack(s[1:], n, ans, cur+char, start)