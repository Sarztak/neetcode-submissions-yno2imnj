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
            rightSide = None
            for i in range(len(deck)):
                rightSide = deck.popleft()
                if rightSide.left:
                    deck.append(rightSide.left)
                if rightSide.right:
                    deck.append(rightSide.right)
            if rightSide:
                rightview.append(rightSide.val)
        return rightview
