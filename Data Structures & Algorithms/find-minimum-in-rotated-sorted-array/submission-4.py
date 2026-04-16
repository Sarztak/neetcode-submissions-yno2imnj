class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if lo == hi:
                return nums[lo]
            elif hi == lo + 1:
                return min(nums[lo], nums[hi])
            elif nums[lo] < nums[mid] < nums[hi]:
                return nums[lo]
            elif nums[lo] < nums[mid] and nums[mid] > nums[hi]:
                lo = mid
            elif nums[lo] > nums[mid] and nums[mid] < nums[hi]:
                hi = mid
        
        return -1 # solution failed, there is some condition that I didn't find