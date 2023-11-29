from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # res = None
    # first = True
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     count = 0
    #     temp = head
    #     newHead = head
    #     prevTail = None
    #     while temp:
    #         count += 1
    #         if count == k:
    #             tempHead = temp.next
    #             temp.next = None
    #             reversedListHead, reveresedListTail = self.reverseList(newHead)
    #             if prevTail:
    #                 prevTail.next = reversedListHead
    #             prevTail = reveresedListTail
    #             reveresedListTail.next = tempHead
    #             newHead = tempHead
    #             temp = tempHead
    #             count = 0
    #         else:
    #             temp = temp.next
    #     return self.res
    # def reverseList(self, head):
    #     if not head:
    #         return None
    #     prev = None
    #     while head:
    #         temp = head.next
    #         head.next = prev
    #         prev = head
    #         head = temp
    #     temp = prev
    #     if self.first:
    #         self.res = prev
    #         self.first = False
    #     while temp.next:
    #         temp = temp.next
    #     return [prev, temp]
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = dummy = ListNode(0)
        temp = l = r = head
        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                dummy.next, dummy, l = pre, l, r
            else:
                return res.next