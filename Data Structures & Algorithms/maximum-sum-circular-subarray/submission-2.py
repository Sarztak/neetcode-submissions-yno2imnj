class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_global = -float('inf')
        n = len(nums)

        # there is a better solution that runs in less time and 
        # it is based on the observation that those subarray that warp around can be computed by total - (elements that are not included)
        # but in case of total - (those that are not included) we minimize so that total - x is maximum
        # the other case is just the sum of normal subarray which does not warp around
        # so we compute the max and min of a normal subarray
        # the edge case is when all the elements are empty, in which case total - x will b zero which is not selecting any elements

        max_global = -float('inf')
        min_global = float('inf')
        change_min = 0
        change_max = 0
        for i in range(len(nums)):
            change_max = max(change_max + nums[i], nums[i])
            change_min = min(change_min + nums[i], nums[i])
            max_global = max(max_global, change_max)
            min_global = min(min_global, change_min)
        
        return max_global if max_global < 0 else max(max_global, sum(nums) - min_global)

