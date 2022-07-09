class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        total = 0
        while truckSize > 0 and boxTypes:
            if boxTypes[0][0] < truckSize:
                truckSize -= boxTypes[0][0]
                total += boxTypes[0][0]*boxTypes[0][1]
                boxTypes.pop(0)
            else:
                total += truckSize*boxTypes[0][1]
                truckSize -= truckSize
        return total