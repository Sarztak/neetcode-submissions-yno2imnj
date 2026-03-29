class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res  = [[]]
        for i in nums:
            res += [subset + [i] for subset in res]
        return res