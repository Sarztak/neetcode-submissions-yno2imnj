class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        The logic for this problem is consider a window [i..j] now I have been asked 
        to find max(prices[j] - prices[i]) over the window such that 0 <= i < j < n 
        Now to solve this problem I need the maximum price that can be available in the future
        This can be done if I just walk from the end of the array and keep track of the maximum
        I first though I can use a list to keep track of each position but that is not needed because
        I just need the max over all the position seen so far from the right - that is over future days
        Once I know the max prices, the max profit for a  given day I purchase the coin is simple max_so_far - prices[i]
        Then all I need to do is to track the max_profit that I have seens so far for each day
        This does not seem like a window problem at all because just one index is needed to actually solve in
        But it is a window problem because of what is being asking is to consider some operation at the end of the window [i..j]
        Though since I just need the state at position i and j and nothing else in between I don't need to use 
        two indexes, just one running index is sufficient
        """
        n = len(prices)

        max_so_far = prices[-1]
        max_profit = 0

        for i in range(n - 2, -1, -1):
            max_profit = max(max_profit, max_so_far - prices[i])
            max_so_far = max(max_so_far, prices[i])
        
        return max_profit