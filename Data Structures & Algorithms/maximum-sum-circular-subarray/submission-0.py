class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_global = -float('inf')
        n = len(nums)
        for i in range(n):
            change = nums[i]
            max_global = max(max_global, change)
            for j in range(n - 1):
                next_num = nums[(i + j + 1) % n]
                change = max(change + next_num, next_num)
                max_global = max(max_global, change)
        
        return max_global