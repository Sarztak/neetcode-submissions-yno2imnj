class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [False] * n
        dp[0] = True # can always reach the first position because we start there LOL

        for i in range(1, n):
            for k in range(1, i + 1):
                dp[i] = dp[i] or (dp[i - k] and k <= nums[i - k])
        return dp[-1]
