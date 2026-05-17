from collections import defaultdict
class MyHashSet:

    def __init__(self):
       self.hash_set = defaultdict(int)

    def add(self, key: int) -> None:
        self.hash_set[key] += 1 # this is not needed though

    def remove(self, key: int) -> None:
        if key in self.hash_set:
            del self.hash_set[key]
        
    def contains(self, key: int) -> bool:
        return key in self.hash_set
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)