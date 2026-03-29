# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = -9999
        while head:
            if head.val == dummy:
                return True
            head.val = dummy
            head = head.next
        return False