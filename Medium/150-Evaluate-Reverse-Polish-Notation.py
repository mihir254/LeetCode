class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                result = a + b
                stack.append(result)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                result = a - b
                stack.append(result)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                result = a * b
                stack.append(result)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                result = int(a/b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()