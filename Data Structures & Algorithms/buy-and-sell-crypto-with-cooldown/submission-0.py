class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        h = -prices[0]
        s = 0
        r = 0
        n = len(prices)
        maxProfit = 0

        for i in range(1, n):
            temp = r
            r = max(r, s)
            s = h + prices[i]
            h = max(h, temp - prices[i])
            maxProfit = max(maxProfit, h, r, s)

        return maxProfit
            
        