class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        positions = {}
        for i, character in enumerate(s):
            if character not in positions:
                positions[character] = [i, i]
            else:
                positions[character][1] = i
        answer = 0
        for k,v in positions.items():
            if v[1]-v[0] > 0:
                subs = s[v[0]+1:v[1]]
                answer += len(list(set(subs)))
        return answer