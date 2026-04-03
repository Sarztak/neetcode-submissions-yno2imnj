class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global = -float('inf')
        change = 0
        for n in nums:
            change = max(n, change + n)
            max_global = max(max_global, change)
        
        return max_global
        