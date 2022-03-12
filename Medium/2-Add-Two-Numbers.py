# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n, c = ListNode(), 0
        n1 = n
        while l1 and l2:
            n1.next = ListNode()
            n1 = n1.next
            v = (l1.val + l2.val + c) % 10
            c = (l1.val + l2.val + c) // 10
            n1.val = v
            l1 = l1.next
            l2 = l2.next
        while l1:
            n1.next = ListNode()
            n1 = n1.next
            v = (l1.val + c) % 10
            c = (l1.val + c) // 10
            n1.val = v
            l1 = l1.next
        while l2:
            n1.next = ListNode()
            n1 = n1.next
            v = (l2.val + c) % 10
            c = (l2.val + c) // 10
            n1.val = v
            l2 = l2.next
        if c!=0:
            n1.next = ListNode()
            n1 = n1.next
            n1.val = c
        return n.next