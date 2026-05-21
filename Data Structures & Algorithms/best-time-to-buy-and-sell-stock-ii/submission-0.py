class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This is probably the worst kind of problem because you can't solve it 
        by more understanding. There is just some bullshit trick to solve it. 
        Some neat observation that an armchair genius made in isolation and then later 
        constructed a problem to make people like me seem foolish. 
        This is the trick: 
        The point is that any trade from day i to day j gives the same profit as buying and selling every single day in between:
        prices[j] - prices[i] = (prices[i+1] - prices[i]) + (prices[i+2] - prices[i+1]) + ... + (prices[j] - prices[j-1])
        You can chain trades: buy day 0, sell day 2, buy day 3, sell day 5 etc. 
        Each trade telescopes into daily differences. 
        The full profit is just the sum of all positive daily differences across 
        all trades combined. The "hold at most one stock" constraint is 
        automatically satisfied because you're buying and selling on different days.
        you never need to hold two stocks simultaneously.
        """
        total_profit = 0
        for i in range(1, len(prices)):
            total_profit += max(0, prices[i] - prices[i - 1])
        
        return total_profit
