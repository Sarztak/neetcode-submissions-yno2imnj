# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find(node, arr):
            if node.left:
                arr = find(node.left, arr)
            arr.append(node.val)
            if node.right:
                arr = find(node.right, arr)
            return arr
        arr = find(root, [])
        if len(arr) >= k:
            return arr[k-1]
        