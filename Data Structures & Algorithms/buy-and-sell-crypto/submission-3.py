class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        max_so_far = prices[-1]
        max_profit = 0

        for i in range(n - 2, -1, -1):
            max_profit = max(max_profit, max_so_far - prices[i])
            max_so_far = max(max_so_far, prices[i])
        
        return max_profit