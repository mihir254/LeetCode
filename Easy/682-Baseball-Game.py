class Solution:
    def calPoints(self, ops) -> int:
        result = []
        for op in ops:
            if op == "C":
                result.pop()
            elif op == "+":
                one = result[-1]
                two = result[-2]
                result.append(one+two)
            elif op == "D":
                last = result[-1]
                result.append(last*2)
            else:
                result.append(int(op))
        return sum(result)