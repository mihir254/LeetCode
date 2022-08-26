class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        arr = [i for i in s]
        arr.sort()
        s = "".join(arr)
        for i in range(32):
            num = 2**i
            st = str(num)
            array = [j for j in st]
            array.sort()
            st = "".join(array)
            if s == st:
                return True
        return False