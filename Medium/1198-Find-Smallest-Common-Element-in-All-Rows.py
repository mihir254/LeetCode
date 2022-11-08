class Solution:
    # def smallestCommonElement(self, mat) -> int:
    #     s = set(mat[0])
    #     for row in mat[1:]:
    #         s = s.intersection(set(row))
    #     commons = list(s)
    #     return min(commons) if commons else -1
    
    def smallestCommonElement(self, mat) -> int:
        for num in mat[0]:
            flag = True
            for row in mat[1:]:
                if not self.binarySearch(num, row):
                    flag = False
                    break
            if flag:
                return num
        return -1
    
    def binarySearch(self, n, arr):
        if arr and n < arr[0]: return False
        if arr and n > arr[-1]: return False
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == n: return True
            elif arr[mid] < n: l = mid+1
            else: r = mid-1
        return False