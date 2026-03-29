class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res^n # the answer is if you xor all the number those that are duplicate will get cancelled
        return res
        