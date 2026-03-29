# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def dfs(node, currMax):
            if not node:
                return
            if node.val >= currMax:
                count[0] += 1
                currMax = node.val
            
            dfs(node.left, currMax)
            dfs(node.right, currMax)
        
        dfs(root, -float('inf'))
        return count[0]