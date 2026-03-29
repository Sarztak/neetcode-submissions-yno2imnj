# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findDiameter(rr):
            if not rr : return 0, 0
            left_length, left_max = findDiameter(rr.left)
            right_length, right_max = findDiameter(rr.right)
            max_diameter = max(left_max, right_max, left_length + right_length)
            return max(left_length, right_length) + 1, max_diameter
        return findDiameter(root)[1]
        
        