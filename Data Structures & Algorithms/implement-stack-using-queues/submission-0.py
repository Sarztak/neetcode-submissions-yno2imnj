"""
This is an unseeming implementation; the push is always to the empty queue and then all elements fromt he 
non-empty queue are moved to the intially empty queue so that the most recent element is always in the front
This is O(n) in push but at least O(1) in pop operations
"""
class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        # if both are empty then start with queue1 else queue2
        if len(self.queue1) == 0:
            self.queue1.append(x)
            while len(self.queue2) > 0:
                self.queue1.append(self.queue2.pop(0))
        elif len(self.queue2) == 0:
            self.queue2.append(x)
            while len(self.queue1) > 0:
                self.queue2.append(self.queue1.pop(0))

    def pop(self) -> int:
        assert not self.empty(), "queue is empty; no element at the top"

        if len(self.queue1) > 0:
            return self.queue1.pop(0)
        else:
            return self.queue2.pop(0)

    def top(self) -> int:
        assert not self.empty(), "queue is empty; no element at the top"

        if len(self.queue1) > 0:
            return self.queue1[0]
        else:
            return self.queue2[0]

    def empty(self) -> bool:
        return len(self.queue1) == 0 and len(self.queue2) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()