class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 1
        hi = x
        while lo <= hi:
            mid = (lo + hi) // 2

            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x > mid ** 2:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return x

# this is good illustration of what binary search actually is
# there is a range and we take a guess at the answer such that it 
# is possible to element some of the region of the search space and then 
# to do this again and again until we find the answer.  