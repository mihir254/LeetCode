class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        store = {1:1, 6:9, 8:8, 9:6, 0:0}
        while num:
            if len(num) == 1:
                return True if num[0] in "018" else False
            a = num[0]
            b = num[-1]
            num = num[1:-1]
            if int(a) in store and store[int(a)] == int(b):
                continue
            return False
        return True