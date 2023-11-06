import heapq
class SeatManager:

    def __init__(self, n: int):
        self.seats = [i+1 for i in range(n)]
        heapq.heapify(self.seats)
        self.reserved = set()

    def reserve(self) -> int:
        seat = heapq.heappop(self.seats)
        self.reserved.add(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        self.reserved.remove(seatNumber)
        heapq.heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)