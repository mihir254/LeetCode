class MovingAverage:

    def __init__(self, size: int):
        self.window = size
        self.stream = []

    def next(self, val: int) -> float:
        self.stream.append(val)
        if len(self.stream) < self.window:
            return sum(self.stream)/len(self.stream)
        return sum(self.stream[-self.window:])/self.window