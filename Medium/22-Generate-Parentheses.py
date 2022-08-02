class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper(ans, 1, n-1, n, "(")
        return ans
    def helper(self, res, opened, canOpen, n, cur):
        if len(cur) == n*2:
            res.append(cur)
            return
        if canOpen > 0:
            self.helper(res, opened+1, canOpen-1, n, cur+"(")
            if opened > 0:
                self.helper(res, opened-1, canOpen, n, cur+")")
        else:
            cur += ")"*(opened)
            res.append(cur)
            return