class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:
        visited = {start}
        queue = [[start, 0]]
        while queue:
            word, step = queue.pop(0)
            if word == end:
                 return step
            for ch in "ACGT":
                 for i in range(len(word)):
                    neighbour = word[:i] + ch + word[i+1:]
                    if neighbour not in visited and neighbour in bank:
                        queue.append([neighbour, step+1])
                        visited.add(neighbour)
        return -1