class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        
        checker = [False] * (len(s)+1)
        checker[0] = True
        
        for i in range(len(s)):
            if checker[i]:
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        checker[j] = True
        return checker[-1]