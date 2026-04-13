class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        if lo == hi and target == nums[0]:
            return 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            print(lo, mid, hi)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # this means that all the number from index lo to mid are less than target because 
                # the array is sorted, therefore I can reduce the search space
                lo = mid + 1
            else:
                # this means nums[mid] > target so all the elements from index mid to hi are greater
                # the target since array is sorted, therefore I can reduce the search space
                hi = mid - 1
        
        return -1
                
        