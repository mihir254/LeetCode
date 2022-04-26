class Solution:
    def minCostConnectPoints(self, points) -> int:
        min_dist = []
        visited = set()
        cost = 0
        points_total = len(points)
        selected = 0
        visited.add(0)
        min_dist.append(0)
        for i in range(len(points)-1):
            min_dist.append(float('inf'))
        while len(visited) < points_total:
            for j in range(points_total):
                if j not in visited:
                    x1, y1, x2, y2 = points[selected][0], points[selected][1], points[j][0], points[j][1]
                    new_dist = self.manhattan(x1, y1, x2, y2)
                    if min_dist[j] > new_dist:
                        min_dist[j] = new_dist
            while True:
                not_visited = [i for i in range(points_total) if i not in visited]
                dist_not_visited = [min_dist[i] for i in not_visited]
                closest_dist = min(dist_not_visited)
                closest_point = min_dist.index(closest_dist)
                if closest_point not in visited:
                    cost += closest_dist
                    min_dist[closest_point] = 0
                    selected = closest_point
                    visited.add(closest_point)
                    break
        return cost
    def manhattan(self, x1, y1, x2, y2):
        return abs(x1-x2)+abs(y1-y2)