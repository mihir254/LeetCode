class Solution:
    def letterCombinations(self, digits: str):
        if not digits or len(digits) == 0:
            return
        conv = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        self.recursion(digits, res, conv, "", 0)
        return res
    
    def recursion(self, quest, ans, mapping, current_string, current_index):
        if current_index == len(quest):
            ans.append(current_string)
            return
        letters = mapping[quest[current_index]]
        for letter in letters:
            self.recursion(quest, ans, mapping, current_string+letter, current_index+1)