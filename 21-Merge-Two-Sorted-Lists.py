# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        head = ListNode()
        temp = head
        while list1 and list2:
            temp.next = ListNode()
            temp = temp.next
            if list1.val<list2.val:
                temp.val = list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next
        while list1:
            temp.next = ListNode()
            temp = temp.next
            temp.val = list1.val
            list1 = list1.next
        while list2:
            temp.next = ListNode()
            temp = temp.next
            temp.val = list2.val
            list2 = list2.next
        return head.next