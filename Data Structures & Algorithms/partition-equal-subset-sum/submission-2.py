class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrSum = sum(nums)
        if arrSum % 2 != 0:
            return False
        
        target = arrSum // 2

        dp = [False]*(target + 1)
        dp[0] = True # we can always have a zero sum by an empty subset

        # dp[i] is True if we can create a sum of i using the elements of nums
        # so dp[target] would results from the previous sums if dp[target - num] is True
        # where num is a number in nums

        # I still don't understand why we need to fill it backwards

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num] # if i - num is possible so is i because we
                # will have two subset those that form i - num and one element num 

        return dp[target]















