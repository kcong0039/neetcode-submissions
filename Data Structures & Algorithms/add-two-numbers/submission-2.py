# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        power = 0
        sum = 0
        ret = dummy = ListNode()
        while l1 or l2:
            if l1:
                sum += l1.val * 10**power
                l1 = l1.next
            if l2:
                sum += l2.val * 10**power
                l2 = l2.next
            power += 1
        if sum == 0:
            return ListNode()
        while sum != 0:
            dummy.next = ListNode(sum%10)
            dummy = dummy.next
            sum //= 10
        return ret.next


