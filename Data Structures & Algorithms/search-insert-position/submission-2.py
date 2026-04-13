class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        mid = (lo + hi) // 2 # need to set this to be used later
        while lo <= hi: # condidtion for breaking is lo > hi
            mid = (lo + hi) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # all element to left of mid are less
                lo = mid + 1
            else: # all element to the right of mid are greater
                hi = mid - 1
        
        # now based on mid the index can be decided
        print(mid)
        return mid + 1 if target > nums[mid] else mid # need to consider edge case


        