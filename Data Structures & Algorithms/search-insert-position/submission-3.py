class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        mid = (lo + hi) // 2 # need to set this to be used later
        while lo <= hi: # condidtion for breaking is lo > hi
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # all element to left of mid are less
                lo = mid + 1
            else: # all element to the right of mid are greater
                hi = mid - 1
        
        # now based on mid the index can be decided
        # there was a fault in my understand, when target < nums[mid] then the answer is mid not mid - 1
        # I need to work out the cases on the paper and see if it agrees with what I wrote in code which I don't do
        # my understand is correct but I don't faithfully present that in code which is source of bugs 
        # do not depend on test cases to figure out the bugs, understand how to solve the problem 
        # for this problem I just rushed in without checking anything at all
        return mid + 1 if target > nums[mid] else mid # need to consider edge case


        