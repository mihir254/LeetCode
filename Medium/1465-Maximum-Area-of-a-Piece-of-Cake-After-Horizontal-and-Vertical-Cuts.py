class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        high1, high2 = 0, 0
        modu = (10**9)+7
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        for i in range(1, len(horizontalCuts)):
            this_area = horizontalCuts[i] - horizontalCuts[i-1]
            high1 = max(high1, this_area)

        
        for j in range(1, len(verticalCuts)):
            this_area = verticalCuts[j] - verticalCuts[j-1]
            high2 = max(high2, this_area)
                
        
        return high1*high2%modu