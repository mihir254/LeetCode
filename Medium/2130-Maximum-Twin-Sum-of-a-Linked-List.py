# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        maxi = 0
        stack = []
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        count = 0
        while head:
            if count <= (n//2)-1:
                stack.append(head.val)
            elif n%2 == 0:
                stack[-1] += head.val
                maxi = max(maxi, stack.pop())
            else:
                if count > n//2:
                    stack[-1] += head.val
                    maxi = max(maxi, stack.pop())
            count += 1
            head = head.next
        return maxi