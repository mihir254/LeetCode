class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        initSlope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) if (coordinates[1][0] - coordinates[0][0]) != 0 else float('inf')
        for i in range(2, len(coordinates)):
            newSlope = (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0]) if (coordinates[i][0] - coordinates[i-1][0]) != 0 else float('inf')
            if newSlope != initSlope:
                return False
        return True