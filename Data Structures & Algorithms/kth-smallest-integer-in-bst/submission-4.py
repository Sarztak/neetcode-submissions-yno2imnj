# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if not node or len(arr) == k:
                return
            if not node.left and not node.right:
                arr.append(node.val)
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        return arr[k - 1]
        