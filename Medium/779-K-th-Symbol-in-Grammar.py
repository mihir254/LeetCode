class Solution:
    store = {0: "01", 1: "10"}
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        row = (k+1)//2
        offset = 1 if k%2==0 else 0
        return int(self.store[self.kthGrammar(n-1, row)][offset])