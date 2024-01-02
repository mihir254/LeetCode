from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.helper(res, "", word)
        return res
    def helper(self, res, cur, word):
        if not word:
            res.append(cur)
            return
        self.helper(res, cur+word[0], word[1:])
        if cur != '':
            if cur[-1].isdigit():
                prev = int(cur[-1])
                prev += 1
                self.helper(res, cur[:-1]+str(prev), word[1:])
        if cur == '' or not cur[-1].isdigit():
            self.helper(res, cur+'1', word[1:])