class Solution:
    def checkIfPangram(self, sentence):
        hashset = set()
        for letter in sentence:
            if letter not in hashset:
                hashset.add(letter)
            if len(hashset) == 26:
                return True
        return False