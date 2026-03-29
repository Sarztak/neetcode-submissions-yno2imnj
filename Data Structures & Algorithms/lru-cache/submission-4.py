class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right = Node(0, 0)
        self.left = Node(0, 0)

        self.left.nxt = self.right
        self.right.prev = self.left


    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        node.nxt = nxt
        node.prev = prev

        prev.nxt = node
        nxt.prev = node

    
    def get(self, key: int) -> int:
        if key in self.cache:
            # remove is eager, whenever get or put is called
            self.remove(self.cache[key])

            # insertion depends on the situation, it is lazy
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.left.nxt
            self.remove(node)
            del self.cache[node.key]






