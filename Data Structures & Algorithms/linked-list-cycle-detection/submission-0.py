# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = head
        h = head
        while True:
            if h == None or h.next == None:
                return False
            else:
                h = h.next.next
                t = t.next
                if h == t:
                    return True
            