class StockSpanner:

    def __init__(self):
       self.stack = [] 

    def next(self, price: int) -> int:
        count = 0
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] > price:
                break
            count += 1
        self.stack.append(price)
        return count + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)