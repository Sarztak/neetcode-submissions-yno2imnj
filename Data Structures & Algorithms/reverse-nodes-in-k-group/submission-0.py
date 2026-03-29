# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start):
            prev, curr = None, start
            while curr:
                p = curr.next
                curr.next = prev
                prev = curr
                curr = p
            
            return prev, start
        
        l = r = head
        prev = None
        n = 0
        head_list = []
        while r:
            while n < k and r:
                n += 1
                prev = r
                r = r.next
            
            if n == k:
                head_list.append(l)
                prev.next = None
                l = r
                n = 0

        reversed_head = []
        for h in head_list:
            reversed_head.append(reverse(h))
        
        for i in range(len(reversed_head) - 1):
            l1, r1 = reversed_head[i]
            l2, r2 = reversed_head[i + 1]
            r1.next = l2
        
        if n < k:
            s, e = reversed_head[-1]
            e.next = l
        return reversed_head[0][0]



