class Solution:
    def swapNodes(self, head, k: int):
        count = 0
        temp = temp1 = temp2 = head
        while head:
            count += 1
            head = head.next
        b = count - k + 1
        front, back = 1, 1
        while front < k:
            temp1 = temp1.next
            front += 1
        while back < b:
            temp2 = temp2.next
            back += 1
        temp1.val, temp2.val = temp2.val, temp1.val
        return temp