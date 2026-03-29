class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def dfs(day, netProfit, lastValidState, currentState):
            print(day, netProfit, lastValidState, currentState)
            if day == n - 1:
                return max(netProfit, 0)
            
            if currentState == 'buy':
                # next state could be hold or sell
                netProfit = max(
                    dfs(
                        day + 1, 
                        netProfit + prices[day + 1],
                        'sell',
                        'sell'
                    ),

                    dfs(
                        day + 1,
                        netProfit,
                        'buy',
                        'hold'
                    )
                )
            
            elif currentState == 'sell':
                # next state can only be hold
                netProfit = dfs(
                    day + 1,
                    netProfit,
                    'sell',
                    'hold'

                )
            
            else: # this is the hold state
                if lastValidState == 'buy':
                    netProfit = max(
                        dfs(
                            day + 1,
                            netProfit,
                            lastValidState,
                            'hold'
                        ),

                        dfs(
                            day + 1,
                            netProfit + prices[day + 1],
                            'sell',
                            'sell'
                        )
                    )
                
                elif lastValidState == 'sell':
                    netProfit = max(
                        dfs(
                            day + 1,
                            netProfit - prices[day + 1],
                            'buy',
                            'buy'
                        ),

                        dfs(
                            day + 1,
                            netProfit,
                            lastValidState,
                            'hold'
                        )
                    )

            
            return netProfit
        
        maxProfit = 0

        for i in range(n):
            maxProfit = max(
                maxProfit,
                dfs(
                    i,
                    -prices[i],
                    'buy',
                    'buy'
                )
            )

        return maxProfit


































