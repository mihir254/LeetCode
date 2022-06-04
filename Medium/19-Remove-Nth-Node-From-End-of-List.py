# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        total = 0
        temp = head
        while temp:
            total += 1
            temp = temp.next
        temp1 = head
        i = 0
        if total-n-1 < 0:
            return head.next
        while i < total-n-1:
            i += 1
            temp1 = temp1.next
        temp1.next = temp1.next.next
        return head