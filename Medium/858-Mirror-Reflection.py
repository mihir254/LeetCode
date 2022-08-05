class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m, n = p, q
        while m%2==0 and n%2==0:
            m /= 2
            n /= 2
        if m%2==1 and n%2==0:
            return 0
        if m%2==1 and n%2==1:
            return 1
        if m%2==0 and n%2==1:
            return 2