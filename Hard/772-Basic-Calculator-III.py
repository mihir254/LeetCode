class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        arr = []
        while i < len(s):
            if s[i].isdigit():
                number = 0
                while i < len(s) and s[i].isdigit():
                    number = number*10 + int(s[i])
                    i += 1
                arr.append(number)
            elif s[i] in "/*-+":
                arr.append(s[i])
                i += 1
            elif s[i] == "(":
                openCount = 1
                openBracketIndex = i
                i += 1
                while openCount != 0:
                    if s[i] == "(":
                        openCount += 1
                    elif s[i] == ")":
                        openCount -= 1
                    i += 1
                closeBracketIndex = i
                calculatedBracket = self.calculate(s[openBracketIndex+1:closeBracketIndex-1])
                arr.append(calculatedBracket)
        while "/" in arr or "*" in arr:
            print(arr)
            divIndex = -1
            if "/" in arr:
                divIndex = arr.index("/")
            mulIndex = -1
            if "*" in arr:
                mulIndex = arr.index("*")
            operandIndex = -1
            if divIndex == -1:
                operandIndex = mulIndex
            elif mulIndex == -1:
                operandIndex = divIndex
            else:
                operandIndex = min(mulIndex, divIndex)
            popIndex = operandIndex-1
            op1, operand, op2 = arr.pop(popIndex), arr.pop(popIndex), arr.pop(popIndex)
            result = 0
            if operand == "/":
                result = int(op1/op2)
            elif operand == "*":
                result = op1*op2
            arr.insert(popIndex, result)
        while len(arr) > 1:
            op1, operand, op2 = arr.pop(0), arr.pop(0), arr.pop(0)
            result = 0
            if operand == "+":
                result = op1+op2
            elif operand == "-":
                result = op1-op2
            arr.insert(0, result)
        return arr[0]