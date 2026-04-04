class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for k in range(1, i + 1):
                if k <= nums[i - k]: # this means the distance between i and i - k which is k <= what I can jump from nums[i - k]; this is the contraint of the problems
                    dp[i] = min(dp[i], dp[i - k] + 1)
        
        return dp[-1]


