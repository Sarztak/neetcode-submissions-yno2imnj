class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Taking help from the previous problem on finding the minimum 
        in a sorted and rotated array, if we can find the index of the
        mimimum element then the problem can be split into two binary 
        problem because array from 0 to i - 1 is sorted and i to n - 1
        is sorted where i is the index of the mimimum element. So we 
        can do the binary search two times. The overall time complexity would
        be 3 * log(n) which is still log(n)
        """
        n = len(nums)
        def binary_search(lo, hi, target):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            return -1 
        
        def find_minimum_index():
            lo = 0
            hi = n - 1

            while lo <= hi:
                mid = (lo + hi) // 2
                if lo == hi:
                    return lo
                elif hi == lo + 1:
                    # all numbers are uniques so condition 
                    # nums[hi] == nums[lo] won't arise if lo and hi are different
                    if nums[hi] > nums[lo]: 
                        return lo
                    else:
                        return hi
                elif nums[lo] < nums[mid] < nums[hi]:
                    return lo
                elif nums[lo] < nums[mid] and nums[mid] > nums[hi]:
                    lo = mid
                elif nums[mid] < nums[hi] and nums[mid] < nums[lo]:
                    hi = mid
            
            return -1 # should not happen

        min_index = find_minimum_index()

        if min_index != -1:
            # do regular binary search from 0 to min_index - 1
            # and from min_index to n - 1
            i1 = binary_search(0, min_index - 1, target)
            i2 = binary_search(min_index, n - 1, target)

            if i1 == -1 and i2 != -1:
                return i2
            elif i1 != -1 and i2 == -1:
                return i1
            elif i1 != -1 and i2 != -1:
                return i1
            else:
                return -1
        
        return -1


            
            




















