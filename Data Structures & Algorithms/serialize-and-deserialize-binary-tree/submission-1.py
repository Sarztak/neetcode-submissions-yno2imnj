# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = ''
        que = deque([root])
        while que:
            node = que.popleft()
            if not node:
                s += 'null,'
                continue
            s += f'{node.val},'
            que.append(node.left)
            que.append(node.right)
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        data = data.split(',')
        i = 1
        que = deque()
        root = TreeNode()
        if data[0] != 'null':
            root.val = int(data[0])
            que.append(root)
        else:
            return None

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if i < len(data):
                    if data[i] != 'null':
                        left = TreeNode(int(data[i]))
                        node.left = left
                        que.append(left)
                    i += 1
                if i < len(data):
                    if data[i] != 'null':
                        right = TreeNode(int(data[i]))
                        node.right = right
                        que.append(right)
                    i += 1
        return root








