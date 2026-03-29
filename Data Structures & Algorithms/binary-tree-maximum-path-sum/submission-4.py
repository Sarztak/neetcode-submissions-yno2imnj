# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -float('inf')
        def dfs(node):
            if not node:
                return 0
            # if not node.left and not node.right:
            #     return node.val
            
            left = dfs(node.left)
            right = dfs(node.right)
            S = max(left + node.val, right + node.val, node.val)
            self.maxSum = max(left + right + node.val, self.maxSum, S)
            return S
        
        dfs(root)

        return self.maxSum
        