from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nums = deque()
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        nums.popleft()

        if nums:
            head.next = curr = ListNode(nums.pop())
        while nums:
            node_first = ListNode(nums.popleft())
            curr.next = node_first

            if nums:
                node_last  = ListNode(nums.pop())
                node_first.next = node_last
                curr = node_last

        