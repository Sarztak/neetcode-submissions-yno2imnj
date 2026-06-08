# the idea is to keep a separate stack in which to store the 
# minimum at each level that is min(val, currMin) and then pop
# from the minStack as well as the stack during the pop operation
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minElement = float('inf')
        

    def push(self, val: int) -> None:
        self.minElement = min(self.minElement, val)
        self.minStack.append(self.minElement)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

        # reset the minelement before the next comparision
        if self.minStack:
            self.minElement = self.minStack[-1]
        else:
            self.minElement = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
