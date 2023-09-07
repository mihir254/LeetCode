from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []
        temp = head
        count = 0
        while temp:
            count += 1
            if count >= left and count <= right:
                stack.append(ListNode(temp.val))
            temp = temp.next

        temp1 = ListNode()
        temp2 = temp1
        counter = 0
        while head:
            counter += 1
            if counter < left:
                temp1.next = ListNode(head.val)
                temp1 = temp1.next
                head = head.next
            elif counter >= left and counter <= right:
                while stack:
                    popped = stack.pop()
                    temp1.next = popped
                    temp1 = temp1.next
                    head = head.next
                counter += (right-left+1)
            else:
                temp1.next = head
                break
        return temp2.next