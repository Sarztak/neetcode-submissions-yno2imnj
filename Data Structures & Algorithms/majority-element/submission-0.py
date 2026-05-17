from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # there can be no more than floor(n / 2) + 1 elements
        # given that a majority element has to always exists
        # so the space required to solve this problem can be
        # fixed at the runtime itself
        # but even by any other method space won't exceed

        c = Counter(nums)
        n = len(nums)
        
        for k, v in c.items():
            if v >= math.floor(n / 2) + 1:
                return k
