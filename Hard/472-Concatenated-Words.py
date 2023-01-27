class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        answer = set()
        store = set()
        for word in words:
            store.add(word)
        for word in words:
            self.helper(word, 0, 0, answer, store)
        return list(answer)
    def helper(self, word, index, found, answer, store):
        if index == len(word) and found > 1:
            answer.add(word)
            return
        for i in range(index+1, len(word)+1):
            word_formed = word[index:i]
            if word_formed in store:
                self.helper(word, i, found+1, answer, store)