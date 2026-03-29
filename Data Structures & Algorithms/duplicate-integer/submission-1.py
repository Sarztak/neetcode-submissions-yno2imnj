from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicates = defaultdict(int)
        for num in nums:
            hasDuplicates[num] += 1
        for key, value in hasDuplicates.items():
            if value > 1:
                return True
        return False

         