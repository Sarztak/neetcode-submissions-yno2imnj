class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_price = prices[0]

        for price in prices:
            if buying_price > price:
                buying_price = price
            max_profit = max(max_profit, price - buying_price)
        
        return max_profit