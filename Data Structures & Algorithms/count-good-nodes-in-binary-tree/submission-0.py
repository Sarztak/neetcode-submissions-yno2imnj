# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(r, MAX):
            count = 0
            if not r:
                return 0
            if r.val >= MAX:
                count += 1
                MAX = r.val
            c1 = count_good_nodes(r.left, MAX)
            c2 = count_good_nodes(r.right, MAX)
            return count + c1 + c2
    
        return count_good_nodes(root, root.val)
        
        
        