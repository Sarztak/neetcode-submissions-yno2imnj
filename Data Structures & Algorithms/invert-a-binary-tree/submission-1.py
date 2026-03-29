# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if root.right:
                invert(root.right)
            if root.left:
                invert(root.left)
            t = root.left
            root.left = root.right
            root.right = t
        if root:
            invert(root)
        else:
            return None
        return root
    