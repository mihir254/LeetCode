from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        last = target[-1]
        pointer = 0
        answer = []
        i = 1
        while i < last+1:
            answer.append("Push")
            if target[pointer] == i:
                pointer += 1
            else:
                answer.append("Pop")
            i += 1
        return answer