from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total = 0
        temp = head
        extra = 0
        while temp:
            total += 1
            temp = temp.next
        if total < k:
            extra = k - total
        boxSize = total // k
        additional = total % k
        answer = []
        while head:
            thisBoxSize = boxSize
            if additional > 0:
                thisBoxSize += 1
                additional -= 1
            temp1 = head
            temp2 = temp1
            for _ in range(thisBoxSize-1):
                temp1 = temp1.next
            head = temp1.next
            temp1.next = None
            answer.append(temp2)
        if extra > 0:
            for _ in range(extra):
                answer.append(None)
        return answer