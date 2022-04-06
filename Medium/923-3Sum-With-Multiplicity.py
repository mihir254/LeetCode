class Solution:
    def threeSumMulti(self, arr, target: int) -> int:
        mod, tot = 10**9 + 7, 0
        check = [0]*101
        for i in arr:
            check[i] += 1
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k<0 or k>100:
                    continue
                if i == j and k == j:
                    tot += ((check[i]-2)*(check[i]-1)*check[i]/6)
                elif i == j and k != i:
                    tot += ((check[i]-1)*check[i]*check[k]/2)
                elif i<j and j<k:
                    tot += check[i]*check[j]*check[k]
        return int(tot%mod)