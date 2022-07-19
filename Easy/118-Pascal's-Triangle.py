class Solution:
    def generate(self, numRows: int):
        ans = []
        for i in range(1, numRows+1):
            arr = [0]*i
            arr[0] = 1
            arr[-1] = 1
            if i > 2:
                for j in range(1, i-1):
                    arr[j] = ans[i-2][j-1] + ans[i-2][j]
            ans.append(arr)
        return ans
        
        
        
# 1                    1                      [1]
# 2                1       1                  [1, 1]
# 3            1       2       1              [1, 2, 1]
# 4        1       3       3       1          [1, 3, 3, 1]
# 5    1       4       6       4       1      [1, 4, 6, 4, 1]