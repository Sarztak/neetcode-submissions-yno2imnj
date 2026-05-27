class FreqStack:

    def __init__(self):
        self.d = dict()
        self.b = [[]]

    def push(self, val: int) -> None:
        self.d[val] = self.d.get(val, 0) + 1
        if self.d[val] < len(self.b):
            self.b[self.d[val]].append(val)
        else:
            self.b.append([val])

    def pop(self) -> int:
        e = self.b[-1].pop()
        self.d[e] -= 1 
        if len(self.b[-1]) == 0:
            self.b.pop()
        return e
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()