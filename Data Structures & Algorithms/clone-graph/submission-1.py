"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        adjDict = {}

        def dfs(node):
            if node.val in adjDict:
                return adjDict[node.val]

            newNode = Node()
            newNode.val = node.val
            adjDict[newNode.val] = newNode
            for n in node.neighbors:
                n = dfs(n)
                newNode.neighbors.append(n)

            return newNode

        return dfs(node)

