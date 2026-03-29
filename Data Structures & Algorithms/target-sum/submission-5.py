class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # if we can select element from nums such that they add up to s1
        # s1 + s2 = sum(nums); s1 - s2 = target
        s1 = (target + sum(nums)) // 2

        if sum(nums) < target or (target + sum(nums)) %2 != 0:
            return 0

        dp = [0]*(s1 + 1)
        dp[0] = 1

        for num in nums:
            for i in range(s1, num - 1 , -1):
                dp[i] += dp[i - num]
        
        return dp[s1]