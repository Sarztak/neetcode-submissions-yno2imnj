class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('infinity')

    def push(self, val: int) -> None:
        self.stack.append(val)
        # self.minVal = min(self.min, val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
