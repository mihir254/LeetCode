class Solution:
    def findStrobogrammatic(self, n: int):
        ans = []
        store = {1:['0', '1', '8'], 2:['11', '69', '88', '96']}
        if n < 3:
            return store[n]
        cur = n
        while cur>0:
            if cur == n:
                for i in store[2]:
                    ans.append(i)
                store[2].append('00')
                cur -= 2
                continue
            if cur == 1:
                l = len(ans[0])//2
                temp = []
                for i in ans:
                    for j in store[1]:
                        temp.append(i[:l] + j + i[l:])
                ans = temp
                cur -= 2
                continue
            l = len(ans[0])//2
            temp = []
            for i in ans:
                for j in store[2]:
                    temp.append(i[:l] + j + i[l:])
            ans = temp
            cur -= 2
        return ans