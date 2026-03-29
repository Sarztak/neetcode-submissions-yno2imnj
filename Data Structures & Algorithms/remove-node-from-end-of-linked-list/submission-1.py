# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        l = l - n - 1

        if l < 0:
            head = head.next
        else:
            curr = head
            while l:
                curr = curr.next
                l -= 1
            
            curr.next = curr.next.next

        return head
        