from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode(0)
        l = cur
        cur.next = head
        store = {}
        preSum = 0
        while cur:
            preSum += cur.val
            if preSum not in store:
                store[preSum] = cur
            else:
                prev = store[preSum]
                tempSum = preSum
                temp = prev.next
                while temp != cur:
                    tempSum += temp.val
                    store.pop(tempSum, None)
                    temp = temp.next
                prev.next = cur.next
            cur = cur.next
        return l.next