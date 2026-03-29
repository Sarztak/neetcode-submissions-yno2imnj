class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        def dfs(arr, coins):
            n = len(arr)
            if n == 0:
                return coins
            if n == 1:
                return coins + arr[0]
            
            maxProd = -float('inf')

            for i in range(n):
                if i == 0:
                    maxProd = max(maxProd, dfs(arr[1:], coins + arr[0] * arr[1]))
                elif i == n - 1:
                    maxProd = max(maxProd, dfs(arr[:-1], coins + arr[-2] * arr[-1]))
                else:
                    maxProd = max(maxProd, dfs(arr[:i] + arr[i+1:], coins + arr[i - 1] * arr[i] * arr[i + 1]))
        
            return maxProd

        return dfs(nums, 0)        