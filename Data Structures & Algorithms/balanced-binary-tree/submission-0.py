# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def depth(r):
            if not r:
                return 0
            else:
                return max(depth(r.left), depth(r.right)) + 1
        return abs(depth(root.right) - depth(root.left)) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)
        