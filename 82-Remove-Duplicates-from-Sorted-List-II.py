# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = ListNode()
        temp1 = temp
        temp.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val==head.next.val:
                    head = head.next
                head = head.next
                temp.next = head
            else:
                head = head.next
                temp = temp.next
        return temp1.next