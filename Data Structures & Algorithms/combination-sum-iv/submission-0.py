class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1 # there is one way to create target which is not to select anything

        for t in range(1, target + 1):
            for k in nums:
                if t - k >= 0:
                    dp[t] += dp[t - k]
        
        return dp[-1]

        