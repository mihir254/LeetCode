class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for ch in s:
            if ch in "aeiouAEIOU":
                vowels.append(ch)
        vowels.sort(key=lambda x:ord(x))
        t = ''
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                x = vowels.pop(0)
                t += x
            else:
                t += s[i]
        return t