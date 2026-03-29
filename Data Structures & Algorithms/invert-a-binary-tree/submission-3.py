# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        que = deque([node])
        while que:
            node = que.popleft()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            que.extend([node.left, node.right])
        return root

        