class StockSpanner:
    def __init__(self):
        self.array = []

    def next(self, price: int) -> int:
        count = 1
        while self.array and self.array[-1][0] <= price:
            count += self.array.pop()[1]
        self.array.append([price, count])
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)