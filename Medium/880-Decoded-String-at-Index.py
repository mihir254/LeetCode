class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total = 0
        for i in range(len(s)):
            if s[i].isdigit():
                total *= int(s[i])
            else:
                total += 1
            if k <= total:
                break
        for j in range(i, -1, -1):
            letter = s[j]
            if letter.isdigit():
                total /= int(letter)
                k %= total
            else:
                if k == total or k == 0:
                    return letter
                total -= 1
        return ""