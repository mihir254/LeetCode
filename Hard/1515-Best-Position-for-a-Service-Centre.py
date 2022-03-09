import math
class Solution:
    def getMinDistSum(self, positions: int) -> float:
        sum_x, sum_y = 0, 0
        for i in positions:
            sum_x += i[0]
            sum_y += i[1]
        mean_x = sum_x/len(positions)
        mean_y = sum_y/len(positions)
        euc_dist = 0
        for i in positions:
            euc_dist += math.sqrt((mean_x-i[0])**2 + (mean_y-i[1])**2)
        acc = 100
        while acc > 1e-6:
            trial = True
            for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                xx = mean_x + acc*dx
                yy = mean_y + acc*dy
                dd = 0
                for i in positions:
                    dd += math.sqrt((xx-i[0])**2 + (yy-i[1])**2)
                if dd < euc_dist:
                    euc_dist = dd
                    mean_x, mean_y = xx, yy
                    trial = False
                    break
            if trial:
                acc /= 2
        return euc_dist