from typing import List
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # houses = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             houses.append((i, j))
        # ans = {}
        # for hx, hy in houses:
        #     queue = [[(hx, hy), 0]]
        #     visited = set()
        #     while queue:
        #         node, dist = queue.pop(0)
        #         if node in visited:
        #             continue
        #         visited.add(node)
        #         if node not in ans:
        #             ans[node] = 0
        #         ans[node] += dist
        #         for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #             newX, newY = node[0]+dx, node[1]+dy
        #             if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) and ((newX, newY) not in visited):
        #                 queue.append([(newX, newY), dist+1])
        # res = -1
        # for k, v in ans.items():
        #     if res == -1:
        #         res = v
        #     else:
        #         res = min(res, v)
        # return res if res != -1 else 1
        # n, mx, my = len(houses), 0, 0
        # for hx, hy in houses:
        #     mx += hx
        #     my += hy
        # ax, ay = mx // n, my // n
        # ans = 0
        # for hx, hy in houses:
        #     ans += abs(ax-hx)+abs(ay-hy)
        # return ans
        r, c = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    r.append(i)
                    c.append(j)
        r.sort()
        c.sort()
        ax, ay = r[len(r)//2], c[len(c)//2]
        ans = 0
        for x in r:
            ans += abs(ax-x)
        for y in c:
            ans += abs(ay-y)
        return ans