class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        for i in s:
            if i != "#":
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
        for i in t:
            if i != "#":
                stack2.append(i)
            else:
                if stack2:
                    stack2.pop()
        return True if "".join(stack1)=="".join(stack2) else False