# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret = dummy = ListNode()
        while not all(x is None for x in lists):
            minNode = None
            minVal = None
            minIndex = None
            for i in range(len(lists)):
                curr = lists[i]
                if curr != None:
                    if minNode == None or curr.val < minVal:
                        minVal = curr.val
                        minNode = curr
                        minIndex = i
            if minNode != None:
                dummy.next = minNode
                dummy = dummy.next
            if minIndex != None:
                lists[minIndex] = lists[minIndex].next
        return ret.next
