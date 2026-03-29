# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        inDict = {j:i for i, j in enumerate(inorder)}
        self.pos = 0
        def dfs(left, right):
            if left > right:
                return None
            val = preorder[self.pos]
            self.pos += 1
            node = TreeNode(val)
            idx = inDict[val]
            node.left = dfs(left, idx - 1)
            node.right = dfs(idx + 1, right)

            return node
        
        return dfs(0, n - 1)


        