class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s)//2
        a, b = s[:half], s[half:]
        vowels1, vowels2 = 0, 0
        for ch in a:
            if ch in "AEIOUaeiou":
                vowels1 += 1
        for ch in b:
            if ch in "AEIOUaeiou":
                vowels2 += 1
        return vowels1 == vowels2