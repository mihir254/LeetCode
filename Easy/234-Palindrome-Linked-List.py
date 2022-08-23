# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
        mid = l//2
        temp1 = head
        stack = []
        while mid > 0:
            mid -= 1
            stack.append(temp1.val)
            temp1 = temp1.next
        if l%2==1:
            temp1=temp1.next
        while temp1:
            if stack:
                x = stack.pop()
                if x != temp1.val:
                    return False
            else:
                return False
            temp1 = temp1.next
        return True