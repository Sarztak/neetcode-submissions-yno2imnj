# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def foo(self, node):
        if not node:
            return [-float('infinity'), 0]
        
        [leftMax, leftPath] = self.foo(node.left)
        [rightMax, rightPath] = self.foo(node.right)

        nodePath = node.val + max(leftPath, rightPath, 0)
        nodeMax = max(leftMax, rightMax, node.val + max(leftPath, 0) + max(rightPath, 0))
        return [nodeMax, nodePath]

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _max, _ = self.foo(root)
        return _max
