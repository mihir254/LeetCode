# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = [], []
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        if len(num1) < len(num2):
            diff = len(num2) - len(num1)
            num1 = ['0']*diff + num1
        if len(num2) < len(num1):
            diff = len(num1) - len(num2)
            num2 = ['0']*diff + num2
        n1, n2 = int("".join(num1)), int("".join(num2))
        n3 = n1 + n2
        num3 = [i for i in str(n3)]
        l3 = ListNode()
        temp = l3
        for i in num3:
            temp.next = ListNode(i)
            temp = temp.next
        return l3.next