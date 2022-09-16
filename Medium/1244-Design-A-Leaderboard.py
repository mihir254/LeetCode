class Leaderboard:

    def __init__(self):
        self.store = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.store:
            self.store[playerId] = 0
        self.store[playerId] += score

    def top(self, K: int) -> int:
        temp = []
        for k,v in self.store.items():
            temp.append(v)
        temp.sort(reverse=True)
        return sum(temp[:K])

    def reset(self, playerId: int) -> None:
        self.store[playerId] = 0