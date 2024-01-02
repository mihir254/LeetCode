from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                sumo = img[i][j]
                neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                count = 1
                for dx, dy in neighbours:
                    if i+dx >= 0 and j+dy >= 0 and i+dx < len(img) and j+dy < len(img[0]):
                        sumo += img[i+dx][j+dy]
                        count += 1
                mat[i][j] = sumo // count
        return mat