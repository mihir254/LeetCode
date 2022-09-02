class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.store = {}
        for i in range(1001):
            self.store[i] = ""

    def insert(self, idKey: int, value: str):
        ret = []
        self.store[idKey] = value
        while self.ptr < len(self.store):
            if self.store[self.ptr] != "":
                ret.append(self.store[self.ptr])
                self.ptr += 1
            else:
                return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)