from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(h):
            prev, curr = None, h
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        s = f = head
        
        while f and f.next:
            f = f.next.next
            s = s.next
        
        l2 = s.next
        s.next = None

        l2 = reverse(l2)
        curr = head

        while curr and l2:
            temp = curr.next
            curr.next = l2
            l2 = temp
            curr = curr.next

        