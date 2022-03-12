# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        hashmap, temp1, temp2 = {}, head, head
        while temp1:
            hashmap[temp1] = Node(temp1.val)
            temp1 = temp1.next
        while temp2:
            hashmap[temp2].next = None if not temp2.next else hashmap[temp2.next]
            hashmap[temp2].random = None if not temp2.random else hashmap[temp2.random]
            temp2 = temp2.next
        return hashmap[head]