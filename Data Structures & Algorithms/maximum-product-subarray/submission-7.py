class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(float('inf'), -float('inf'))] * n # min, max
        dp[0] = (nums[0], nums[0])
        for i in range(1, n):
            max_so_far = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            min_so_far = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            dp[i] = (min_so_far, max_so_far)

        
        return max(dp[i][1] for i in range(n))