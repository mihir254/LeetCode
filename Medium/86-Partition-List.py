class Solution:
    def partition(self, head, x):
        l1, l2 = ListNode(), ListNode()
        l3, l4 = l1, l2
        while head:
            if head.val < x:
                l1.next = ListNode(head.val)
                l1 = l1.next
            else:
                l2.next = ListNode(head.val)
                l2 = l2.next
            head = head.next
        l4 = l4.next
        l1.next = l4
        l3 = l3.next
        return l3