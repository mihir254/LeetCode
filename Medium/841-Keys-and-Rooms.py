class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        visited = set()
        n = len(rooms)
        self.dfs(visited, 0, rooms)
        return len(visited) == n
    def dfs(self, visit, room, rooms):
        visit.add(room)
        keys = rooms[room]
        for key in keys:
            if key not in visit:
                self.dfs(visit, key, rooms)