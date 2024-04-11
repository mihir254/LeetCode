class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for x in num:
            while stack and stack[-1] > x and k > 0:
                stack.pop()
                k -= 1
            stack.append(x)
        while k > 0 and stack:
            stack.pop()
            k -= 1
        return "".join([str(x) for x in stack]).lstrip("0") or "0"