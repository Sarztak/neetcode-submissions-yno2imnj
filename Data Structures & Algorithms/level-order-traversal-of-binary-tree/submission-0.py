# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deck = deque()
        res = []
        if root:
            deck.append(root)

        while deck:
            l = []
            
            for i in range(len(deck)):
                x = deck.popleft()
                l.append(x.val)

                if x.left:
                    deck.append(x.left)
                if x.right:
                    deck.append(x.right)
            res.append(l)

        return res


        