class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        m = (len(nums) - 1) // 2
        median = nums[m] if (len(nums) - 1) % 2 == 0 else sum(nums[m:m+2]) / 2
        return median
        