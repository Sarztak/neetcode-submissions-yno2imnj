class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def multiply(nums):
            mul = 1
            for n in nums:
                mul *= n
            return mul
        output = []
        for i in range(len(nums)):
            a1 = nums[:i]
            a2 = nums[i+1:]
            output.append(multiply(a1) * multiply(a2))
        return output

        