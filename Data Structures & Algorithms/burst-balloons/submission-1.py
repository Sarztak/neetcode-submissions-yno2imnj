class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Create a DP table
        dp = [[0] * n for _ in range(n)]
        
        # Fill the DP table
        for length in range(2, n):  # length of the subarray
            for left in range(n - length):  # left boundary
                right = left + length  # right boundary
                for i in range(left + 1, right):  # the last balloon to burst
                    coins = nums[left] * nums[i] * nums[right]
                    dp[left][right] = max(dp[left][right], dp[left][i] + dp[i][right] + coins)
        
        return dp[0][n - 1]
        