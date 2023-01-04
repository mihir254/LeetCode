from collections import Counter
class Solution:
    def minimumRounds(self, tasks) -> int:
        tasks.sort()
        counter = Counter(tasks)
        answer = 0
        for key, value in counter.items():
            if value == 1:
                return -1
            # if value == 2 or value == 3:
            #     answer += 1
            # else:
            #     while value > 4:
            #         value -= 3
            #         answer += 1
            #     if value == 4:
            #         answer += 2
            #     elif value == 2 or value == 3:
            #         answer += 1
            if value % 3 == 0:
                answer += value//3
            else:
                answer += value//3 + 1
        return answer