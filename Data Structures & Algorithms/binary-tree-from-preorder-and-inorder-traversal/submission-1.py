# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0
        inDict = {val: i for i, val in enumerate(inorder)}
        def dfs(left, right):
            if left > right:
                return None
            
            val = preorder[self.pre_idx]
            node = TreeNode(val)
            idx = inDict[val]
            self.pre_idx += 1

            node.left = dfs(left, idx - 1)
            node.right = dfs(idx + 1, right)

            return node
        
        return dfs(0, len(preorder) - 1)