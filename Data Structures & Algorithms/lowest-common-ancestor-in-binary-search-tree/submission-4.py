# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p.val, q.val = min(p.val, q.val), max(p.val, q.val)
        found = [None]
        def dfs(node):
            if node:
                if q.val < node.val:
                    dfs(node.left)
                if node.val < p.val:
                    dfs(node.right)
                
                if p.val <= node.val <= q.val:
                    found[0] = node
                    return 
            
        dfs(root)
        return found[0]
        