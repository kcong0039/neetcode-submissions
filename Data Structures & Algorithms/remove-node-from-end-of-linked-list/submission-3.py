class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Reverse the linked list
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head = prev  # Head now points to the reversed list

        # Step 2: Delete the n-th node from the start of the reversed list
        dummy = ListNode(0, head)
        curr = dummy
        for _ in range(n - 1):
            if curr.next:
                curr = curr.next
        if curr.next:
            curr.next = curr.next.next

        # Step 3: Reverse the list again to restore original order
        prev, curr = None, dummy.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev