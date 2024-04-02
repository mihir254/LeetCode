class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        p1, p2 = 0, 0
        answer = 0
        char1, char2 = ['', -1], ['', -1]
        while p2 < len(s):
            if char1[0] == s[p2]:
                char1[1] = p2
            elif char2[0] == s[p2]:
                char2[1] = p2
            elif char1[0] == '':
                char1 = [s[p2], p2]
            elif char2[0] == '':
                char2 = [s[p2], p2]
            else:
                if char1[1] < char2[1]:
                    p1 = char1[1] + 1
                    char1 = [s[p2], p2]
                else:
                    p1 = char2[1] + 1
                    char2 = [s[p2], p2]
            p2 += 1
            answer = max(answer, p2-p1)
        return answer