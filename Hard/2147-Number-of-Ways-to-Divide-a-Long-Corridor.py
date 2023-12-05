class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = 0
        spaces = 0
        totalSpaces = 0
        for obj in corridor:
            if obj == "S":
                if seats == 0:
                    seats += 1
                elif seats == 1:
                    seats += 1
                    spaces += 1
                else:
                    if totalSpaces == 0:
                        totalSpaces = spaces
                    else:
                        totalSpaces *= spaces
                    spaces = 0
                    seats = 1
            else:
                if seats == 2:
                    spaces += 1
        if seats == 1 or (seats == 0 and spaces == 0):
            return 0
        if totalSpaces == 0 and seats == 2:
            return 1
        return totalSpaces % (10**9 + 7)