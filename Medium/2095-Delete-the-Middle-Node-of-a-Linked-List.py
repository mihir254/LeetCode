# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head.next:
            return None
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        mid = length//2
        i = 0
        temp = head
        temp1 = temp
        while i < mid-1:
            i += 1
            temp = temp.next
        temp.next = temp.next.next
        return temp1