# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightview = []
        deck = deque()
        if root:
            deck.append(root)
        while deck:
            arr = []
            for i in range(len(deck)):
                x = deck.popleft()
                arr.append(x.val)
                if x.left:
                    deck.append(x.left)
                if x.right:
                    deck.append(x.right)
            rightview.append(arr[-1])
        return rightview
