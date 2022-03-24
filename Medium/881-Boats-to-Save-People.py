class Solution:
    def numRescueBoats(self, people: int, limit: int) -> int:
        people.sort()
        count, checksum, l, r = 0, 0, 0, len(people)-1
        print(people)
        while l<=r:
            print(l, r)
            checksum = people[r]
            r -= 1
            if checksum+people[l] <= limit:
                l += 1
            count += 1
        return count