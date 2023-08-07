class Solution:
    def searchMatrix(self, matrix, target):
        top, bottom = 0, len(matrix)-1
        mainRow = -1
        while top <= bottom:
            center = (top+bottom) // 2
            if matrix[center][0] == target:
                return True
            if matrix[center][0] < target:
                if matrix[center][-1] == target:
                    return True
                if matrix[center][-1] > target:
                    mainRow = center
                    break
                else:
                    top = center + 1
            elif matrix[center][0] > target:
                bottom = center - 1
        searchArea = matrix[mainRow]
        print(matrix[mainRow])
        left, right = 0, len(matrix[mainRow]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mainRow][mid] == target:
                return True
            if matrix[mainRow][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False