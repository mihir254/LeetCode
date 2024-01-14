from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = []
        for row in bank:
            count = 0
            for cell in row:
                if cell == '1':
                    count += 1
            if count > 0:
                lasers.append(count)
        if len(lasers) < 2:
            return 0
        answer = 0
        for i in range(1, len(lasers)):
            answer += lasers[i-1]*lasers[i]
        return answer