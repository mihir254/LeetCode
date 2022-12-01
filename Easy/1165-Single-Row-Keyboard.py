class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        store = {}
        for index in range(len(keyboard)):
            store[keyboard[index]] = index
        score = 0
        current = 0
        for letter in word:
            score += abs(store[letter]-current)
            current = store[letter]
        return score