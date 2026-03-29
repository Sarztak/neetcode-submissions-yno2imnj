# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        que = deque([node])
        depth = 0
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if not node:
                    continue
                que.extend([node.left, node.right])
            depth += 1

        return depth - 1
        