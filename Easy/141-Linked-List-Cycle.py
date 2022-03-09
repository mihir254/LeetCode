# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #hashmap
    def hasCycle(self, head: ListNode) -> bool:
        store = {}
        while head:
            if head in store:
                return True
            store[head] = True
            head = head.next
        return False
    #Fast and slow pointers
    def hasCycle(self, head: ListNode) -> bool:
        tortoise, rabbit = head, head
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if tortoise == rabbit:
                return True
        return False