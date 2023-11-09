class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return t >= max(abs(sx-fx), abs(sy-fy)) if (sx!=fx or sy != fy) else t!=1