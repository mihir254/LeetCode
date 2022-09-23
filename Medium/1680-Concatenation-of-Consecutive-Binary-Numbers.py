class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modu = (10**9)+7
        conc = ""
        for i in range(1, n+1):
            conc += bin(i)[2:]
        res = int(conc, 2)
        return res%modu