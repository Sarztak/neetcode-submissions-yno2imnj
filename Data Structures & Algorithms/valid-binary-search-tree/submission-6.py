# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            t1, t2 = True, True
            if node.left:
                t1 = left < node.left.val < node.val
            if node.right:
                t2 = node.val < node.right.val < right
            if not (t1 and t2):
                return False

            return t1 and t2 and dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        return dfs(root, -float('inf'), float('inf'))
        