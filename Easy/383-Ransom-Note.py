class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store1, store2 = {}, {}
        for letter in ransomNote:
            if letter not in store1:
                store1[letter] = 0
            store1[letter] += 1
        for letter in magazine:
            if letter not in store2:
                store2[letter] = 0
            store2[letter] += 1
        for k,v in store1.items():
            if k not in store2:
                return False
            if v > store2[k]:
                return False
        return True