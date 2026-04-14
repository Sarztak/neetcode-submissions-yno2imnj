import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        def hours_required(k: int):
            k = max(1, k) # need to avoid division by zero error
            return sum(math.ceil(piles[i] / k) for i in range(len(piles))) 

        # the search space is 0 to max(piles) because if the rate is max(piles) then it is 
        # possible to finish eating all the piles in h hours and if the rate is zero
        # then it is not possible to finish anything at all 
        # here the condition is that if k * h < total_bananas then you can't finish so k <- k + 1
        # if (k - 1) * h < total_b <= k * h then the answer is k 
        # if k * h > total_b then k <- k - 1

        while lo <= hi:
            k = (lo + hi) // 2

            if hours_required(k) <= h < hours_required(k - 1):
                return k 
            elif h < hours_required(k):
                lo = k + 1
            else:
                hi = k - 1
        
        return 1
             
        