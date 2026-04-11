class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        # the solution is that keep on exapanding the array untiil the rumming sum becomes
        # greater than or equal to the target, and then shrink the array from the right just until 
        # doing so anymore would cause the running sum to be less that the target
        # keep track of the minimum length
        # the general idea seems to be that in such problems decided on i first and then compute length 
        # after all that do the update by 1 on j 


        min_len = n + 1
        i = j = 0
        running_sum = 0
        while j < n:
            running_sum += nums[j]
            if running_sum >= target:
                while not (running_sum - nums[i] < target):
                    running_sum -= nums[i]
                    i += 1
                
                # compute length
                min_len = min(min_len, j - i + 1)
            
            # in other cases when running_sum is less than target continue to expand 
            j += 1

        return min_len if min_len != n + 1 else 0
