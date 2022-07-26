class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort(key=lambda x:x[0])
        rooms = [intervals[0][1]]
        for i in range(1, len(intervals)):
            found = False
            for j in range(len(rooms)):
                if rooms[j] <= intervals[i][0]:
                    rooms[j] = intervals[i][1]
                    found = True
                    break
            if not found:
                rooms.append(intervals[i][1])
        return len(rooms)