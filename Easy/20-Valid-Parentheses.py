class Solution:
    def isValid(self, s: str) -> bool:
        stack, store = [], {'}':'{', ']':'[', ')':'('}
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                j = stack.pop()
                if store[i] != j:
                    return False
        return True if not stack else False