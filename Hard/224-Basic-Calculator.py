class Solution:
    def reCalculate(self, number1, sign, number2):
        if sign == "+":
            return number1 + number2
        else:
            return number1 - number2
    def calculate(self, s: str) -> int:
        s = "".join(s.strip().split(" "))
        cur_sign, cur_val, cur_num, stack = "+", 0, 0, []
        for ch in s:
            if ch == "-" or ch == "+":
                cur_val = self.reCalculate(cur_val, cur_sign, cur_num)
                cur_num = 0
                cur_sign = ch
            elif ch.isdigit():
                cur_num = cur_num*10 + int(ch)
            elif ch == "(":
                cur_val = self.reCalculate(cur_val, cur_sign, cur_num)
                cur_num = 0
                stack.append(cur_val)
                stack.append(cur_sign)
                cur_val = 0
                cur_sign = "+"
            elif ch == ")":
                cur_val = self.reCalculate(cur_val, cur_sign, cur_num)
                cur_num = 0
                sign = stack.pop()
                num = stack.pop()
                cur_val = self.reCalculate(num, sign, cur_val)
        cur_val = self.reCalculate(cur_val, cur_sign, cur_num)
        return cur_val