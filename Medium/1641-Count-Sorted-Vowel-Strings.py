class Solution:
    result = 0
    def countVowelStrings(self, n: int) -> int:
        vowels = {0:"a", 1:"e", 2:"i", 3:"o", 4:"u"}
        self.combinationGenerator(vowels, 0, 0, n)
        return self.result
    def combinationGenerator(self, vowels, current_index, current_letter, length):
        if current_index == length:
            self.result += 1
            return
        for i in range(current_letter, 5):
            self.combinationGenerator(vowels, current_index+1, i, length)