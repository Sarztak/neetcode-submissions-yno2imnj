"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        node_dict = {}
        while curr:
            node_dict[curr] = Node(curr.val)
            curr = curr.next
        
        for k, v in node_dict.items():
            v.random = node_dict.get(k.random, None)
            v.next = node_dict.get(k.next, None)
        
        return node_dict.get(head, None)