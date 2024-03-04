import bisect
from typing import List
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1, a2 = [nums[0]], [nums[1]]
        as1, as2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            l1, l2 = len(a1), len(a2)
            num = nums[i]
            b1, b2 = bisect.bisect_right(as1, num), bisect.bisect_right(as2, num)
            if l1-b1 > l2-b2:
                a1.append(num)
                bisect.insort_right(as1, num)
            elif l1-b1 < l2-b2:
                a2.append(num)
                bisect.insort_right(as2, num)
            else:
                if l1 < l2:
                    a1.append(num)
                    bisect.insort_right(as1, num)
                elif l1 > l2:
                    a2.append(num)
                    bisect.insort_right(as2, num)
                else:
                    a1.append(num)
                    bisect.insort_right(as1, num)
        return a1+a2