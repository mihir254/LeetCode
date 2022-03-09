# 1
class TwoSum:

    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        store = {}
        for num in self.nums:
            if num not in store:
                store[value-num] = num
            else:
                return True
        return False

# 2
class TwoSum:

    def __init__(self):
        self.store = {}

    def add(self, number: int) -> None:
        if number in self.store:
            self.store[number] += 1
        else:
            self.store[number] = 1

    def find(self, value: int) -> bool:
        for key in self.store.keys():
            diff = value - key
            if diff == key:
                if self.store[key] > 1:
                    return True
            elif diff in self.store.keys():
                return True
        return False
        
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)