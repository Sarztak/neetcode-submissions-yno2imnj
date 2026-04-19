class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binary_search(lo, hi, target):
            while lo <= hi:
                mid = (lo + hi) // 2

                if nums[mid] == target:
                    return True 
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False 

        n = len(nums)
        lo = 0
        hi = n - 1

        def find_min_index(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if lo == hi:
                    return lo
                elif hi == lo + 1:
                    # return the index that has minimum if they are not equal else smaller of the two indices
                    if nums[lo] <= nums[hi]:
                        return lo
                    else:
                        return hi
                elif nums[lo] == nums[mid] == nums[hi]:
                    lo = lo + 1
                elif nums[lo] < nums[mid] <= nums[hi]:
                    lo = mid
                elif nums[lo] <= nums[mid] < nums[hi]:
                    hi = mid
                elif nums[lo] < nums[mid] < nums[hi]:
                    return lo
                elif nums[lo] <= nums[mid] and nums[mid] > nums[hi]:
                    lo = mid 
                elif nums[mid] <= nums[hi] and nums[lo] > nums[mid]:
                    hi = mid

            return -1 
        
        min_index = find_min_index(lo, hi)

        assert min_index != -1, "min_index not found" 
        
        if min_index != -1:
            t1 = binary_search(min_index, n - 1, target)
            t2 = binary_search(0, min_index - 1, target)

            return t1 or t2
        else:
            return False


                    



















