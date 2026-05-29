class StockSpanner:
    """
    The problem can be solved without using stack easily
    but what stack enables it using previously counted values.
    All I need to do is store the previous counts along with the 
    hightest value of the stock for that stock span. I don't 
    understand how the time complexity of this solution is O(n) and
    the per call amortized time complexity is O(1)
    """

    def __init__(self):
       self.stack = [] 

    def next(self, price: int) -> int:
        count = 0
        # for i in range(len(self.stack) - 1, -1, -1):
        #     if self.stack[i] > price:
        #         break
        #     count += 1
        # self.stack.append(price)
        while self.stack and self.stack[-1][1] <= price:
            count += self.stack[-1][0]
            self.stack.pop()
        self.stack.append((count + 1, price))

        return self.stack[-1][0]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)