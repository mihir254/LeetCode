from sortedcontainers import SortedDict
class StockPrice:

    def __init__(self):
        self.price_to_time = SortedDict()
        self.time_to_price = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_to_price:
            prev = self.time_to_price[timestamp]
            self.price_to_time[prev].remove(timestamp)
            if len(self.price_to_time[prev]) == 0:
                self.price_to_time.pop(prev)
        if price not in self.price_to_time:
            self.price_to_time[price] = set()
        self.time_to_price[timestamp] = price
        self.price_to_time[price].add(timestamp)

    def current(self) -> int:
        return self.time_to_price.items()[-1][1]

    def maximum(self) -> int:
        return self.price_to_time.items()[-1][0]

    def minimum(self) -> int:
        return self.price_to_time.items()[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()