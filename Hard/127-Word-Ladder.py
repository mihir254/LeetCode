from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff(word1, word2):
            if len(word1) != len(word2):
                return False
            i = 0
            dif = 0
            while i < len(word1):
                if word1[i] != word2[i]:
                    dif += 1
                if dif > 1:
                    return False
                i += 1
            return True
        queue = [[beginWord, 1]]
        wordSet = set(wordList)
        while queue:
            node, seqLen = queue.pop(0)
            if node == endWord:
                return seqLen
            for word in list(wordSet):
                if diff(word, node):
                    wordSet.remove(word)
                    queue.append([word, seqLen+1])
        return 0