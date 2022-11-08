class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = []
        # indices = []
        # for i in range(len(s)):
        #     if s[i] in "aeiouAEIOU":
        #         vowels.append(s[i])
        #         indices.append(i)
        # reverse_vowels = vowels[::-1]
        # s_list = [ch for ch in s]
        # for index in indices:
        #     letter = reverse_vowels.pop(0)
        #     s_list[index] = letter
        # return "".join(s_list)
        
        left, right = 0, len(s)-1
        vowels = set("aeiouAEIOU")
        s = list(s)
        while left <= right:
            while left <= right and s[left] not in vowels:
                left += 1
            while left <= right and s[right] not in vowels:
                right -= 1
            if left > right:
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)