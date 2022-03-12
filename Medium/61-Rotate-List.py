# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        temp, l = head, 0
        while temp.next:
            l += 1
            temp = temp.next
        l += 1
        k = k % l
        if k == 0:
            return head
        temp.next = head
        temp = temp.next
        i = l - k
        for t in range(i):
            temp = temp.next
        for t in range(i-1):
            head = head.next
        head.next = None
        return temp