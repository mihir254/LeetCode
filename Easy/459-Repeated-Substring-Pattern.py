class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 1
        while i < len(s)//2+1:
            subs = s[:i]
            if len(s)%len(subs)==0:
                if subs*(len(s)//len(subs)) == s:
                    return True
            i += 1
        return False