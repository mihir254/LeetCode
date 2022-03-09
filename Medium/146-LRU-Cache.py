from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.store = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.store.move_to_end(key)
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.move_to_end(key)
            self.store[key] = value
        self.store[key] = value
        if len(self.store) > self.capacity:
            self.store.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)