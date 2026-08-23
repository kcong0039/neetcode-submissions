"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None
        dummy = Node(0)
        dummy.next = head
        prev = None
        nodes = {}
        while dummy.next != None:
            
            curr = Node(dummy.next.val)
            if prev:
                prev.next = curr
            nodes[dummy.next] = curr
            prev = curr
            dummy = dummy.next

        dummy2 = nodes[head]
        dummy3 = head
        while dummy2:
            dummy2.random = nodes[dummy3.random] if dummy3.random != None else None
            dummy2 = dummy2.next
            dummy3 = dummy3.next
        return nodes[head]
        



        