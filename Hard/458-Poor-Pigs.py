class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        possible_states = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(possible_states))