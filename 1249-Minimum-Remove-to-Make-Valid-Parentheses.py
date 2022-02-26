class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, removal = [], []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack:
                    removal.append(i)
                else:
                    stack.pop()
        to_remove = set(removal).union(set(stack))
        ans = []
        for i in range(len(s)):
            if i not in to_remove:
                ans.append(s[i])
        return "".join(ans)