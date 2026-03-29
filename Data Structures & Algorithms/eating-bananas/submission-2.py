class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            # check fesibility
            hours = sum([(p + mid - 1) // mid for p in piles])
            if hours <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low