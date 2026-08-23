# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return
        ret = dummy = ListNode()
        fast = head
        slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        midpoint = slow.next
        slow.next = None
        prev, curr = None, midpoint
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        midpoint = prev
        print(head.val, midpoint.val)
        while head and midpoint:
            dummy.next = head
            head = head.next
            dummy = dummy.next
            dummy.next = midpoint
            midpoint = midpoint.next
            dummy = dummy.next
        dummy.next = head if head else midpoint
        
        

