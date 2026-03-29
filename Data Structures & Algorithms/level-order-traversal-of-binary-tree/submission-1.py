# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        listNode = []
        if not root:
            return []
    
        que = deque([root])

        while que:
            t = []
            for _ in range(len(que)):
                node = que.popleft()
                if node:
                    t.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if t:
                listNode.append(t)
    
        return listNode

        