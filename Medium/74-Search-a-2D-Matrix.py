class Solution:
    def searchMatrix(self, matrix, target):
        row = 0
        while row < len(matrix)-1:
            if matrix[row][-1] >= target:
                break
            row += 1
        arr = matrix[row]
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if target == arr[mid]:
                return True
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False