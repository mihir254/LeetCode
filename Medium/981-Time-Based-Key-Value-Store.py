class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        all_occ = self.store[key]
        if timestamp < all_occ[0][1]:
            return ""
        l, r = 0, len(all_occ)-1
        nearest = -1
        while l <= r:
            m = (l+r)//2
            if all_occ[m][1] == timestamp:
                return all_occ[m][0]
            elif all_occ[m][1] < timestamp:
                nearest = max(nearest, m)
                l = m + 1
            else:
                r = m - 1
        return all_occ[nearest][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)