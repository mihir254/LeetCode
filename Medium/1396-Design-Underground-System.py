class UndergroundSystem:

    def __init__(self):
        self.store1, self.store2 = {}, {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.store1[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkedInAt = self.store1[id]
        if (startStation, stationName) not in self.store2:
            self.store2[(startStation, stationName)] = [0, 0]
        self.store2[(startStation, stationName)][0] += t - checkedInAt
        self.store2[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.store2[(startStation, endStation)][0]/self.store2[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)