class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # this is just the partitioning problem applied twice 

        i = 0
        n = len(nums)
        
        for j in range(n):
            if nums[j] == 0:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                i += 1
        
        k = i

        for j in range(i, n):
            if nums[j] == 1:
                t = nums[k]
                nums[k] = nums[j]
                nums[j] = t
                k += 1
