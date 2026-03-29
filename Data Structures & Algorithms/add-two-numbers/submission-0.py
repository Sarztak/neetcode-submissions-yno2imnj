# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_num(head):
            n = ''
            while head:
                n = n + str(head.val)
                head = head.next
            return int(n[::-1]) if n != '' else 0
        s = list(str(get_num(l1) + get_num(l2)))
        dummy = curr = ListNode()
        for i in s[::-1]:
            curr.next = ListNode(int(i))
            curr = curr.next
        return dummy.next
        