class Solution:
    def checkValidString(self, s: str) -> bool:
        mini, maxi = 0, 0
        for char in s:
            if char == "(":
                mini += 1
            else:
                mini -= 1
            
            if char != ")":
                maxi += 1
            else:
                maxi -= 1
            
            if maxi < 0:
                break
            mini = max(mini, 0)
        return True if mini == 0 else False