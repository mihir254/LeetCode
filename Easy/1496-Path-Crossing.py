class Solution:
    def isPathCrossing(self, path: str) -> bool:
        px, py = 0, 0
        hashset = set()
        hashset.add((0, 0))
        for direction in path:
            if direction == "N":
                py += 1
            elif direction == "S":
                py -= 1
            elif direction == "E":
                px += 1
            elif direction == "W":
                px -= 1
            if (px, py) in hashset:
                return True
            hashset.add((px, py))
        return False