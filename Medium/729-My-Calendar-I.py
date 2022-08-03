class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        for x in self.arr:
            if max(x[0], start) < min(x[1], end):
                return False
        self.arr.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)