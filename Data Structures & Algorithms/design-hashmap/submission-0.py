class MyHashMap:

    def __init__(self):
       self.keys = []

    def put(self, key: int, value: int) -> None:
        if key >= len(self.keys):
            # expand the list before inserting by that much
            # -1 is already there so that if key is not present that value
            # won't be over written and all the values are between 0 to 10K so
            # there is no conflict with -1
            # also extend doesn't return a new list
            self.keys.extend([-1] * (key - len(self.keys) + 1))
        self.keys[key] = value # zero based

    def get(self, key: int) -> int:
        if key >= len(self.keys):
            return -1
        else:
            return self.keys[key]

    def remove(self, key: int) -> None:
        if key >= len(self.keys):
            return None # do nothing 
        else:
            self.keys[key] = -1 # remove the key by inserting -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)