class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        binary1 = bin(left)[2:]
        binary2 = bin(right)[2:]
        if len(binary1) != len(binary2) or left == 0 or right == 0:
            return 0
        diff = right - left
        pow = 0
        while diff >= 2**pow:
            pow += 1
        ans = 0
        for i in range(pow, len(binary1)):
            ans += 2**i
        return ans & left & right