# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.curr_max = -float('inf')
        def dfs(node):
            if not node:
                return 0
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            self.curr_max = max(self.curr_max, left_max + node.val + right_max)
            return node.val + max(left_max, right_max)
        dfs(root)
        return self.curr_max
        