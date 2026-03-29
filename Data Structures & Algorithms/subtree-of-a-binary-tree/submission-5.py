# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            return dfs(node1.left, node2.left) and \
                    dfs(node1.right, node2.right)

        que = deque([root])

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node.val == subRoot.val:
                    if dfs(node, subRoot):
                        return True
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
        return False







