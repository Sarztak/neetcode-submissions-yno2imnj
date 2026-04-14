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

        