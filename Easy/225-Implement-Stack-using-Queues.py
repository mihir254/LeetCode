class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        x = self.q1.pop()
        self.q1 = self.q2
        self.q2 = []
        return x

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return False if len(self.q1)>0 else True